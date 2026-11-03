"""Direct tests of the regression harness's own checking code.

Standard library only (unittest), so it runs without pytest:

    python tests/regression/selftest.py

The scenarios exercise these checks end to end; the tests here pin their
rules with known answers, so a broken oracle cannot pass by agreeing with
a broken runner.
"""

import hashlib
import json
import os
import shutil
import sys
import tempfile
import types
import unittest
import urllib.error
import urllib.request
from decimal import Decimal

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'fixtures'))

import driver  # noqa: E402  (snapshot() only; main() is not run)
import hard_checks  # noqa: E402
import hash_oracle  # noqa: E402
from mock_endpoint import MockEndpoint  # noqa: E402


class CanonicalHash(unittest.TestCase):

    def test_known_answer_with_decimal_and_unicode(self):
        # The vector verify_hashes.py checks on three platforms; its digest
        # is the committed hash_digest.txt.
        obj = {
            'z_last': 'should sort last',
            'a_first': 'should sort first',
            'decimal_value': Decimal('274.1375'),
            'nested': {'inner_b': Decimal('777.4125'),
                       'inner_a': [Decimal('15.20'), Decimal('3109.65')]},
            'empty_list': [],
            'unicode': '−',
        }
        self.assertEqual(
            hash_oracle.canonical_json(obj),
            '{"a_first":"should sort first","decimal_value":"274.1375",'
            '"empty_list":[],"nested":{"inner_a":["15.20","3109.65"],'
            '"inner_b":"777.4125"},"unicode":"−",'
            '"z_last":"should sort last"}')
        self.assertEqual(
            hash_oracle.canonical_hash(obj),
            '831709b2231846ed20fd63ff0bc0764d73cee50db271f733e6a2f1c377c7cff3')

    def test_float_is_refused(self):
        with self.assertRaises(hash_oracle.HashCheckError):
            hash_oracle.canonical_hash({'a': [1.5]})


class Snapshot(unittest.TestCase):

    def test_round_trip_keeps_types(self):
        value = {'d': Decimal('0.010'), 'b': True, 'i': 1, 's': 'x’',
                 'n': None, 'l': [Decimal('1'), ('t',)], 'f': 0.5}
        back = hash_oracle.from_snapshot(driver.snapshot(value))
        self.assertEqual(back, {'d': Decimal('0.010'), 'b': True, 'i': 1,
                                's': 'x’', 'n': None,
                                'l': [Decimal('1'), ['t']], 'f': 0.5})
        self.assertIs(type(back['d']), Decimal)
        self.assertIs(type(back['b']), bool)
        self.assertEqual(str(back['d']), '0.010')

    def test_unknown_type_is_refused(self):
        with self.assertRaises(hash_oracle.HashCheckError):
            hash_oracle.from_snapshot(driver.snapshot({'p': object()}))

    def test_strict_equal_tells_true_from_one(self):
        self.assertFalse(hash_oracle._strict_equal(True, 1))
        self.assertFalse(hash_oracle._strict_equal([1], [1.0]))
        self.assertTrue(hash_oracle._strict_equal({'a': [True]},
                                                  {'a': [True]}))


class SourceHash(unittest.TestCase):

    def setUp(self):
        self.root = tempfile.mkdtemp(prefix='ap1-oracle-')
        files = {
            'b.py': b'B',
            'a.py': b'A',
            'pkg/c.py': b'C',
            'pkg/data.txt': b'not hashed',
            'output/run.py': b'excluded',
            'output_x.py': b'excluded',
            'review_output_1/r.py': b'excluded',
            '__pycache__/m.py': b'excluded',
        }
        for rel, data in files.items():
            path = os.path.join(self.root, *rel.split('/'))
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'wb') as f:
                f.write(data)

    def tearDown(self):
        shutil.rmtree(self.root)

    def test_files_and_known_answer(self):
        self.assertEqual(
            [p.replace(os.sep, '/')
             for p in hash_oracle.source_hash_files(self.root)],
            ['a.py', 'b.py', 'pkg/c.py'])
        want = hashlib.sha256(
            b'a.py\x00A\x00b.py\x00B\x00pkg/c.py\x00C\x00').hexdigest()
        self.assertEqual(hash_oracle.runner_source_hash(self.root), want)


class ReplayComparison(unittest.TestCase):

    def test_equal(self):
        self.assertIsNone(hard_checks.first_difference(
            {'a': [1, {'b': True}]}, {'a': [1, {'b': True}]}))

    def test_type_aware(self):
        self.assertIn('bool True', hard_checks.first_difference(
            {'a': True}, {'a': 1}))
        self.assertIn('int 1', hard_checks.first_difference(
            {'a': 1}, {'a': 1.0}))

    def test_names_the_path(self):
        self.assertTrue(hard_checks.first_difference(
            {'a': [0, {'b': 'x'}]}, {'a': [0, {'b': 'y'}]}
        ).startswith('$.a[1].b: '))
        self.assertIn('missing from the replay',
                      hard_checks.first_difference({'k': 1}, {}))
        self.assertIn('2 entries in the published run, 1',
                      hard_checks.first_difference([1, 2], [1]))


class MockTransportContract(unittest.TestCase):

    KEY = 'sk-selftest'

    def setUp(self):
        self.mock = MockEndpoint(
            questions={'items': [{'id': 'Q01', 'text': 'What?'}]},
            system_prompts={'S': 'base'}, api_key=self.KEY,
            responses={'Q01/*/*': [{'say': 'It is $1.00.'}]}).start()
        self.base = self.mock.url.rsplit('/v1/', 1)[0]

    def tearDown(self):
        self.mock.stop()

    def post(self, path='/v1/chat/completions', auth='Bearer sk-selftest'):
        body = json.dumps({'messages': [
            {'role': 'system', 'content': 'S'},
            {'role': 'user', 'content': 'Question: What?'}]}).encode()
        req = urllib.request.Request(self.base + path, data=body,
                                     method='POST')
        req.add_header('Content-Type', 'application/json')
        if auth is not None:
            req.add_header('Authorization', auth)
        try:
            with urllib.request.urlopen(req, timeout=10) as r:
                return r.status, json.loads(r.read())
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read())

    def test_valid_request_is_served_and_logged(self):
        status, body = self.post()
        self.assertEqual(status, 200)
        self.assertEqual(body['choices'][0]['message']['content'],
                         'It is $1.00.')
        self.assertEqual(self.mock.violations, [])
        self.assertEqual([e['repeat'] for e in self.mock.log], [1])

    def test_refusals_do_not_advance_the_script(self):
        self.assertEqual(self.post(auth=None)[0], 401)
        self.assertEqual(self.post(auth='Bearer wrong')[0], 401)
        self.assertEqual(self.post(auth='sk-selftest')[0], 401)
        self.assertEqual(self.post(path='/v1/completions')[0], 404)
        self.assertEqual(self.mock.log, [])
        self.assertEqual(self.mock.violations, [
            {'kind': 'credential', 'path': '/v1/chat/completions'},
            {'kind': 'credential', 'path': '/v1/chat/completions'},
            {'kind': 'credential', 'path': '/v1/chat/completions'},
            {'kind': 'path', 'path': '/v1/completions'}])
        # The first valid request is still repeat 1.
        self.assertEqual(self.post()[0], 200)
        self.assertEqual([e['repeat'] for e in self.mock.log], [1])

    def test_violations_never_record_header_names_or_values(self):
        self.post(auth='Bearer leaked-secret')
        self.assertNotIn('leaked-secret', json.dumps(self.mock.violations))
        self.assertEqual(sorted(self.mock.violations[0]), ['kind', 'path'])

    def test_harness_fails_a_run_with_a_violation(self):
        result_dir = tempfile.mkdtemp(prefix='ap1-selftest-')
        try:
            path = os.path.join(result_dir, 'transport_violations.json')
            with self.assertRaises(hard_checks.HardCheckError):
                hard_checks.check_transport(result_dir)   # not recorded
            with open(path, 'w') as f:
                json.dump([{'kind': 'path', 'path': '/x'}], f)
            with self.assertRaises(hard_checks.HardCheckError):
                hard_checks.check_transport(result_dir)
            with open(path, 'w') as f:
                json.dump([], f)
            hard_checks.check_transport(result_dir)
        finally:
            shutil.rmtree(result_dir)


class Independence(unittest.TestCase):

    def test_a_runner_module_in_the_process_fails(self):
        sys.modules['seal'] = types.ModuleType('seal')
        try:
            with self.assertRaises(hash_oracle.HashCheckError) as cm:
                hash_oracle.check_independent()
            self.assertIn('seal', str(cm.exception))
        finally:
            del sys.modules['seal']

    def test_clean_process_passes(self):
        hash_oracle.check_independent()


if __name__ == '__main__':
    unittest.main()
