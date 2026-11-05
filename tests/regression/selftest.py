"""Direct tests of the regression harness's own checking code.

Standard library only (unittest), so it runs without pytest:

    python tests/regression/selftest.py

The scenarios exercise these checks end to end; the tests here pin their
rules with known answers, so a broken oracle cannot pass by agreeing with
a broken runner.
"""

import ast
import contextlib
import hashlib
import io
import json
import os
import shutil
import subprocess
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

import check_source_files  # noqa: E402
import driver  # noqa: E402  (snapshot() only; main() is not run)
import hard_checks  # noqa: E402
import hash_oracle  # noqa: E402
import run_regression  # noqa: E402
from mock_endpoint import MockEndpoint  # noqa: E402


class CanonicalHash(unittest.TestCase):

    def test_known_answer_with_decimal_and_unicode(self):
        # The vector tests/regression/verify_hashes.py checks on three
        # platforms (hashes.yml); its digest is that script's EXPECTED_DIGEST,
        # the value hash_digest.txt held while it was committed.
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

    def test_verify_hashes_pins_the_same_digest(self):
        # Parsed, not imported: importing the script would import the runner.
        path = os.path.join(HERE, 'verify_hashes.py')
        with open(path, encoding='utf-8') as f:
            tree = ast.parse(f.read(), path)
        pins = [ast.literal_eval(node.value) for node in tree.body
                if isinstance(node, ast.Assign)
                and [getattr(t, 'id', None) for t in node.targets]
                == ['EXPECTED_DIGEST']]
        self.assertEqual(pins, [
            '831709b2231846ed20fd63ff0bc0764d73cee50db271f733e6a2f1c377c7cff3'])

    def test_float_is_refused(self):
        with self.assertRaises(hash_oracle.HashCheckError):
            hash_oracle.canonical_hash({'a': [1.5]})

    def test_non_string_key_is_refused(self):
        # json.dumps would quietly write {"0.5":"x"}.
        for obj in ({'a': {0.5: 'x'}}, {1: 'x'}, [{None: 1}]):
            with self.assertRaises(hash_oracle.HashCheckError):
                hash_oracle.canonical_hash(obj)
        self.assertIn('float key 0.5', hash_oracle.canonical_refusal(
            {'extension': {0.5: 'x'}}))


class VersionFile(unittest.TestCase):

    def setUp(self):
        self.root = tempfile.mkdtemp(prefix='ap1-oracle-')

    def tearDown(self):
        shutil.rmtree(self.root)

    def write(self, text):
        with open(os.path.join(self.root, 'VERSION'), 'w') as f:
            f.write(text)

    def test_first_line_that_is_not_a_comment(self):
        self.write('# header\n\n  v1.3.1 e0d9ec9  extra\nv9 ffff\n')
        self.assertEqual(hash_oracle.version_file_fields(self.root),
                         ('v1.3.1', 'e0d9ec9'))

    def test_fallbacks(self):
        self.assertEqual(hash_oracle.version_file_fields(self.root),
                         ('unknown', 'unknown'))
        self.write('v1.3.1\n')
        self.assertEqual(hash_oracle.version_file_fields(self.root),
                         ('v1.3.1', 'unknown'))


class Timestamp(unittest.TestCase):

    def test_must_fall_within_the_run(self):
        import time
        now = time.time()
        from datetime import datetime, timezone
        inside = datetime.fromtimestamp(now, timezone.utc).isoformat()
        self.assertEqual(hash_oracle._check_timestamp(inside, (now, now)), [])
        self.assertIn('outside the run', hash_oracle._check_timestamp(
            '2000-01-01T00:00:00+00:00', (now, now))[0])
        self.assertIn('not a valid date', hash_oracle._check_timestamp(
            '2026-13-40T25:00:00+00:00', (now, now))[0])
        self.assertIn('not ISO 8601', hash_oracle._check_timestamp(
            '2026-11-02T10:00:00+01:00', (now, now))[0])


class Report(unittest.TestCase):

    def test_only_identified_fields_are_seal_references(self):
        # A 64-hex config value (a valid decline marker) is not a hash.
        config = {'decline_markers': ['a' * 64], 'answer_tolerance': '0.01'}
        record = {'config_hash': hash_oracle.canonical_hash(config),
                  'seal_hash': 'b' * 64, 'verification_keys': []}
        report = '\n'.join(
            ['## 1. Pre-Registration Record', '', '| Field | Value |',
             '|---|---|']
            + [f'| `{k}` | `{v}` |' for k, v in sorted(record.items())]
            + ['', '## 2. Resolved Configuration', '', '```json',
               json.dumps(config, indent=2, sort_keys=True), '```', '',
               '## 3. Results', 'quoted: ' + 'c' * 64])
        self.assertEqual(hash_oracle.check_report(report, record), [])
        wrong = report.replace('b' * 64, 'd' * 64)
        self.assertIn('report §1 seal_hash',
                      hash_oracle.check_report(wrong, record)[0])


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

    def test_a_tuple_is_a_sequence_not_text(self):
        self.assertEqual(driver.snapshot(()), ['list', []])
        self.assertEqual(hash_oracle.from_snapshot(driver.snapshot(('k',))),
                         ['k'])

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



class NothingRunIsNotAPass(unittest.TestCase):
    """REORG-1: the harness exits non-zero when it runs no scenario."""

    def test_no_scenarios(self):
        empty = tempfile.mkdtemp(prefix='ap1-no-scenarios-')
        saved, run_regression.SCENARIOS = run_regression.SCENARIOS, empty
        try:
            with contextlib.redirect_stdout(io.StringIO()), \
                    contextlib.redirect_stderr(io.StringIO()) as err:
                code = run_regression.main([])
        finally:
            run_regression.SCENARIOS = saved
            shutil.rmtree(empty)
        self.assertNotEqual(code, 0)
        self.assertIn('nothing was checked', err.getvalue())

    def test_zero_runs(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as cm:
                run_regression.main(['--runs', '0'])
        self.assertNotEqual(cm.exception.code, 0)

class SourceFileList(unittest.TestCase):
    """check_source_files.py takes its list from the oracle's rule."""

    def test_a_rule_change_shows_in_the_list(self):
        # A rule change git ls-files with the excluded prefixes cannot see:
        # the oracle stops hashing __init__.py files.
        rule = hash_oracle.source_hash_files

        def narrower(base_dir):
            return [p for p in rule(base_dir)
                    if os.path.basename(p) != '__init__.py']
        with open(check_source_files.LIST, encoding='utf-8') as f:
            pinned = f.read().splitlines()
        hash_oracle.source_hash_files = narrower
        try:
            listed = check_source_files.tracked_source_files()
        finally:
            hash_oracle.source_hash_files = rule
        self.assertEqual(
            sorted(set(pinned) - set(listed)),
            sorted(p for p in pinned if p.endswith('/__init__.py')))
        self.assertTrue(set(listed) < set(pinned))

    def test_untracked_files_are_named_not_listed(self):
        root = tempfile.mkdtemp(prefix='ap1-source-list-')
        try:
            files = {'a.py': 'tracked', 'pkg/b.py': 'tracked',
                     'output/c.py': 'tracked', 'scratch.py': 'untracked',
                     'notes.txt': 'tracked'}
            for rel in files:
                path = os.path.join(root, *rel.split('/'))
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, 'w') as f:
                    f.write('x = 1\n')
            env = check_source_files.git_env()
            subprocess.run(['git', 'init', '-q', root], check=True, env=env)
            subprocess.run(['git', '-C', root, 'add', '--']
                           + [r for r, kind in files.items()
                              if kind == 'tracked'], check=True, env=env)
            repo, check_source_files.REPO = check_source_files.REPO, root
            err = io.StringIO()
            try:
                with contextlib.redirect_stderr(err):
                    listed = check_source_files.tracked_source_files()
            finally:
                check_source_files.REPO = repo
            self.assertEqual(listed, ['a.py', 'pkg/b.py'])
            self.assertIn('1 untracked file(s)', err.getvalue())
            self.assertIn('scratch.py', err.getvalue())
        finally:
            shutil.rmtree(root)

class PublishedSourceHash(unittest.TestCase):
    """The oracle's source-hash rule, on the code of the September runs,
    gives the runner_source_hash their seals record (docs/REPRODUCING.md).

    The tree is the tag's blobs as stored, written out byte for byte: at
    the tag, .py files are stored as they were on disk when the runs were
    sealed (-text, mixed CRLF and LF), and reading the blobs directly keeps
    a checkout's line-ending conversion out of it. Needs the tag in the
    clone (CI checks out with full history).

    What this pins: the byte reading (the tag has CRLF and LF files), the
    path encoding, the NUL framing and the sort, over a nearly flat tree
    (44 .py files at the top, 7 in ap1_inspect/, 2 in example/; no tests/,
    src/ or tools/). It cannot see a rule change that only affects deeper
    or other directories, such as no longer hashing tests/: which files
    are in scope is pinned by check_source_files.py."""

    TAG = 'e7-quantise-fix'
    # docs/REPRODUCING.md, and report.md section 1 of both September runs.
    PUBLISHED = ('da0739eb396e65468d33adb7953aa828fdde9bee6ec1c78e56c83c345'
                 'defd795')
    RUNS = ('run_e_mini', 'run_f_sol')

    def setUp(self):
        self.root = tempfile.mkdtemp(prefix='ap1-oracle-tag-')

    def tearDown(self):
        shutil.rmtree(self.root)

    def git(self, *args, stdin=None):
        # The clone this file is in, whatever GIT_DIR a caller has set.
        repo = os.path.dirname(os.path.dirname(HERE))
        return subprocess.run(['git', '-C', repo, *args], input=stdin,
                              capture_output=True, check=True,
                              env=check_source_files.git_env()).stdout

    def write_tag_tree(self):
        try:
            listing = self.git('ls-tree', '-r', '-z', self.TAG + '^{tree}')
        except (OSError, subprocess.CalledProcessError) as e:
            # Fails rather than skips: a skip would let a CI checkout
            # without tags pass this check silently.
            self.fail(
                f'cannot read the tag {self.TAG} from this clone '
                f'({getattr(e, "stderr", None) or e!r}). This test needs '
                f'git and the tag: a shallow clone, a clone without tags, '
                f'or a copy without .git does not have it. Run '
                f'"git fetch --tags" (CI checks out with fetch-depth: 0). '
                f'It fails rather than skips so that a missing tag cannot '
                f'pass silently.')
        entries = []
        for entry in listing.split(b'\0'):
            if entry:
                meta, path = entry.split(b'\t', 1)
                mode, kind, sha = meta.split()
                self.assertEqual((kind, mode in (b'100644', b'100755')),
                                 (b'blob', True), path)
                entries.append((path.decode('utf-8'), sha))
        out = self.git('cat-file', '--batch',
                       stdin=b''.join(sha + b'\n' for _, sha in entries))
        pos = 0
        for rel, sha in entries:
            header_end = out.index(b'\n', pos)
            got_sha, kind, size = out[pos:header_end].split()
            self.assertEqual((got_sha, kind), (sha, b'blob'))
            start = header_end + 1
            data = out[start:start + int(size)]
            pos = start + int(size) + 1
            path = os.path.join(self.root, *rel.split('/'))
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'wb') as f:
                f.write(data)
        return entries

    def test_the_published_value_is_the_sealed_one(self):
        repo = os.path.dirname(os.path.dirname(HERE))
        for run in self.RUNS:
            with open(os.path.join(repo, 'output', run, 'report.md'),
                      encoding='utf-8') as f:
                rows = [line.strip() for line in f
                        if line.startswith('| `runner_source_hash` |')]
            self.assertEqual(
                rows, [f'| `runner_source_hash` | `{self.PUBLISHED}` |'], run)

    def test_rule_recomputes_the_published_hash_from_the_tag(self):
        self.write_tag_tree()
        self.assertEqual(hash_oracle.runner_source_hash(self.root),
                         self.PUBLISHED)

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


class ReplayExpectedDifferences(unittest.TestCase):

    def rows(self, **fields):
        row = {'item_id': 'Q01', 'condition': 'base', 'repeat': 1,
               'transcription_outcome': 'TRANSCRIBED-EXACT'}
        row.update(fields)
        return {'seal_hash': 'x', 'all_results': [row]}

    def expected(self, moves=None, new_fields=(), new_keys=()):
        return {'moves': moves or {}, 'new_execution_fields': list(new_fields),
                'new_top_level_keys': list(new_keys)}

    def diff(self, published, replayed, expected):
        return hard_checks.replay_differences(published, replayed, expected)

    def test_identical_passes(self):
        self.assertEqual(self.diff(self.rows(), self.rows(), self.expected()), [])

    def test_unlisted_move_fails(self):
        found = self.diff(self.rows(), self.rows(
            transcription_outcome='TRANSCRIBED-ALTERED'), self.expected())
        self.assertEqual(len(found), 1)
        self.assertIn('(Q01/base/r1).transcription_outcome', found[0])

    def test_listed_move_passes(self):
        moves = {'Q01/base/r1': {'transcription_outcome': [
            'TRANSCRIBED-EXACT', 'TRANSCRIBED-ALTERED']}}
        self.assertEqual(self.diff(self.rows(), self.rows(
            transcription_outcome='TRANSCRIBED-ALTERED'),
            self.expected(moves)), [])

    def test_listed_move_to_another_value_fails(self):
        moves = {'Q01/base/r1': {'transcription_outcome': [
            'TRANSCRIBED-EXACT', 'TRANSCRIBED-ALTERED']}}
        found = self.diff(self.rows(), self.rows(
            transcription_outcome='UNOBSERVABLE'), self.expected(moves))
        self.assertEqual(len(found), 1)
        self.assertIn('listed move', found[0])

    def test_listed_move_that_does_not_happen_fails(self):
        moves = {'Q01/base/r1': {'transcription_outcome': [
            'TRANSCRIBED-EXACT', 'TRANSCRIBED-ALTERED']}}
        found = self.diff(self.rows(), self.rows(), self.expected(moves))
        self.assertEqual(len(found), 1)
        moves = {'Q02/base/r1': {'transcription_outcome': ['a', 'b']}}
        found = self.diff(self.rows(), self.rows(), self.expected(moves))
        self.assertIn('matches no execution', found[0])

    def test_new_field_must_be_listed(self):
        self.assertEqual(len(self.diff(self.rows(), self.rows(new=1),
                                       self.expected())), 1)
        self.assertEqual(self.diff(self.rows(), self.rows(new=1),
                                   self.expected(new_fields=['new'])), [])
        self.assertEqual(len(self.diff(self.rows(new=1), self.rows(),
                                       self.expected(new_fields=['new']))), 1)

    def test_new_top_level_key_must_be_listed(self):
        rep = self.rows()
        rep['extra'] = []
        self.assertEqual(len(self.diff(self.rows(), rep, self.expected())), 1)
        rep = self.rows()
        rep['extra'] = []
        self.assertEqual(self.diff(self.rows(), rep,
                                   self.expected(new_keys=['extra'])), [])

    def test_seal_hash_and_order(self):
        self.assertEqual(self.diff(self.rows(), dict(self.rows(), seal_hash='y'),
                                   self.expected()), [])
        found = self.diff(self.rows(), self.rows(repeat=2), self.expected())
        self.assertIn('Q01/base/r1 in the published run', found[0])

    def test_the_committed_list_parses(self):
        for run in ('output/run_e_mini', 'output/run_f_sol'):
            listed = hard_checks.load_replay_expected(run)
            for key, fields in listed['moves'].items():
                self.assertRegex(key, r'^Q\d\d/[a-z_]+/r\d+$')
                for move in fields.values():
                    self.assertEqual(len(move), 2)
                    self.assertNotEqual(move[0], move[1])


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

    def request(self, method, data=None):
        req = urllib.request.Request(
            self.base + '/v1/chat/completions', data=data, method=method)
        req.add_header('Authorization', 'Bearer sk-selftest')
        try:
            with urllib.request.urlopen(req, timeout=10) as r:
                return r.status
        except urllib.error.HTTPError as e:
            e.read()
            return e.code

    def test_other_methods_are_refused_and_recorded(self):
        methods = ['GET', 'HEAD', 'PUT', 'DELETE', 'PATCH', 'OPTIONS',
                   'TRACE', 'BREW']
        for m in methods:
            data = b'{}' if m in ('PUT', 'PATCH') else None
            self.assertEqual(self.request(m, data), 405, m)
        self.assertEqual(self.mock.log, [])
        self.assertEqual(self.mock.violations, [
            {'kind': 'method', 'method': m, 'path': '/v1/chat/completions'}
            for m in methods])
        # The first valid POST is still repeat 1.
        self.assertEqual(self.post()[0], 200)
        self.assertEqual([e['repeat'] for e in self.mock.log], [1])

    def test_harness_fails_a_run_with_a_method_violation(self):
        self.request('GET')
        result_dir = tempfile.mkdtemp(prefix='ap1-selftest-')
        try:
            with open(os.path.join(result_dir, 'transport_violations.json'),
                      'w') as f:
                json.dump(self.mock.violations, f)
            with self.assertRaisesRegex(hard_checks.HardCheckError,
                                        r'method \(GET /v1/chat'):
                hard_checks.check_transport(result_dir)
        finally:
            shutil.rmtree(result_dir)

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
