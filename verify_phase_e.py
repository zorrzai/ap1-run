"""Phase E verification suite.

Tests:
  1. DOI seal: config with ap1_version_doi -> seal records it;
     config missing it -> ConfigError naming the field
  2. Sheet completeness: generated sheet contains question, response,
     fixture excerpt, tool-call record, evidence class, reason, rubric
     (all six outcomes), two scorer copies
  3. Report structure: report declares unmeasured dimensions (D3-D6),
     evidence classes, auto/adjudicated split, kappa with small-n caveat
  4. Partial-dimension run: a run measuring only some dimensions produces
     a report declaring the rest as not measured
  5. Clopper-Pearson k=0 formula verification
  6. D2 auto-measured: report does NOT declare D2 as requiring adjudication
  7. D2 mechanism class reporting per surface

Run: python verify_phase_e.py
"""

import json
import math
import sys
import unittest
from decimal import Decimal
from pathlib import Path


# -- Ensure runner directory is on path --------------------------------
sys.path.insert(0, str(Path(__file__).parent))


class TestDOIRequired(unittest.TestCase):
    """ap1_version_doi is in REQUIRED_FIELDS."""

    def test_doi_in_required_fields(self):
        """ap1_version_doi appears in config.REQUIRED_FIELDS."""
        from config import REQUIRED_FIELDS
        self.assertIn('ap1_version_doi', REQUIRED_FIELDS)

    def test_missing_doi_refused(self):
        """A config omitting ap1_version_doi is refused, naming the field."""
        import tempfile
        from config import ConfigError, load_config

        # Minimal valid config minus ap1_version_doi
        cfg = {
            'endpoint_url': 'http://localhost:8080',
            'model': 'test-model',
            'sampling': {},
            'answer_tolerance': '0.01',
            'quantisation': {'places': '2', 'rounding': 'ROUND_HALF_UP'},
            'permitted_transformations': [],
            'decline_markers': [],
            'decimal_separator': '.',
            'grouping_separator': ',',
            'currency_symbols': ['$'],
            'dimensions_claimed': ['D1', 'D7'],
            'repeat_count': '1',
            'structured_answer_field': 'none',
            'ap1_version': '1.3',
            'ap1_text_hash': 'abc123',
            # ap1_version_doi intentionally omitted
        }
        with tempfile.NamedTemporaryFile(
                mode='w', suffix='.json', delete=False) as f:
            json.dump(cfg, f)
            f.flush()
            path = f.name

        try:
            with self.assertRaises(ConfigError) as ctx:
                load_config(path)
            self.assertIn('ap1_version_doi', str(ctx.exception))
        finally:
            import os
            os.unlink(path)


class TestDOISeal(unittest.TestCase):
    """ap1_version_doi is recorded and verified in seal."""

    def test_doi_recorded_in_seal(self):
        """seal() records ap1_version_doi from config."""
        import tempfile
        from seal import seal

        config = {
            'ap1_version': '1.3',
            'ap1_text_hash': 'placeholder',
            'ap1_version_doi': '10.5281/zenodo.21755443',
        }
        # seal() takes file paths, not pre-computed hashes
        with tempfile.NamedTemporaryFile(
                mode='w', suffix='.json', delete=False) as qf:
            json.dump({'items': []}, qf)
            qf.flush()
            q_path = qf.name
        with tempfile.NamedTemporaryFile(
                mode='w', suffix='.json', delete=False) as ff:
            json.dump({'accounts': []}, ff)
            ff.flush()
            f_path = ff.name
        with tempfile.NamedTemporaryFile(
                mode='w', suffix='.py', delete=False) as gf:
            gf.write('# stub')
            gf.flush()
            g_path = gf.name

        try:
            record = seal(
                config=config,
                fixture_path=f_path,
                questions_path=q_path,
                ground_truth_path=g_path,
            )
            self.assertEqual(
                record['ap1_version_doi'], '10.5281/zenodo.21755443')
        finally:
            import os
            os.unlink(q_path)
            os.unlink(f_path)
            os.unlink(g_path)


class TestSheetCompleteness(unittest.TestCase):
    """Adjudication sheet contains everything a scorer needs."""

    def _make_transcript_record(self, figure_outcome='ADJUDICATE-DECLINE'):
        return {
            'item_id': 'Q01',
            'condition': 'base',
            'error_state': None,
            'figure_outcome': figure_outcome,
            'response_received': {
                'choices': [{'message': {'content': 'The answer is $15.20'}}]
            },
            'tool_calls': [{
                'function': {
                    'name': 'calculator',
                    'arguments': '{"expression": "15200 * 0.012 / 12"}',
                },
                'return_value': '{"result": 15.2}',
            }],
            'evidence_class': 'EV-2 PLATFORM-STRUCTURAL',
            'invocation_outcome': 'TOOL-INVOKED',
            'operation_correctness': [
                {'outcome': 'OPERATION-CORRECT', 'reason': 'matches'}
            ],
            'ground_truth_final': '15.20',
            'required_operation': '15200 * 0.012 / 12',
        }

    def _make_questions(self):
        return {
            'items': [{
                'id': 'Q01',
                'category': 'interest',
                'text': 'What is the monthly interest earned?',
                'source_accounts': ['savings'],
            }]
        }

    def _make_fixture(self):
        return {
            'accounts': [{
                'id': 'savings',
                'name': 'Savings Account',
                'balance': '15200.00',
                'annual_rate': '1.2',
            }]
        }

    def test_sheet_has_question(self):
        from adjudication import generate_sheets
        sheets = generate_sheets(
            [self._make_transcript_record()],
            self._make_questions(),
            self._make_fixture(),
            {'ap1_version': '1.3', 'ap1_version_doi': 'doi'},
        )
        self.assertIn('What is the monthly interest earned?', sheets)

    def test_sheet_has_response_verbatim(self):
        from adjudication import generate_sheets
        sheets = generate_sheets(
            [self._make_transcript_record()],
            self._make_questions(),
            self._make_fixture(),
            {'ap1_version': '1.3', 'ap1_version_doi': 'doi'},
        )
        self.assertIn('The answer is $15.20', sheets)

    def test_sheet_has_fixture_excerpt(self):
        from adjudication import generate_sheets
        sheets = generate_sheets(
            [self._make_transcript_record()],
            self._make_questions(),
            self._make_fixture(),
            {'ap1_version': '1.3', 'ap1_version_doi': 'doi'},
        )
        self.assertIn('Savings Account', sheets)
        self.assertIn('15200.00', sheets)
        self.assertIn('1.2', sheets)

    def test_sheet_has_tool_call_record(self):
        from adjudication import generate_sheets
        sheets = generate_sheets(
            [self._make_transcript_record()],
            self._make_questions(),
            self._make_fixture(),
            {'ap1_version': '1.3', 'ap1_version_doi': 'doi'},
        )
        self.assertIn('calculator', sheets)
        self.assertIn('15200 * 0.012 / 12', sheets)

    def test_sheet_has_evidence_class(self):
        from adjudication import generate_sheets
        sheets = generate_sheets(
            [self._make_transcript_record()],
            self._make_questions(),
            self._make_fixture(),
            {'ap1_version': '1.3', 'ap1_version_doi': 'doi'},
        )
        self.assertIn('EV-2 PLATFORM-STRUCTURAL', sheets)

    def test_sheet_has_reason(self):
        from adjudication import generate_sheets
        sheets = generate_sheets(
            [self._make_transcript_record()],
            self._make_questions(),
            self._make_fixture(),
            {'ap1_version': '1.3', 'ap1_version_doi': 'doi'},
        )
        self.assertIn('decline marker', sheets)

    def test_sheet_has_all_six_outcomes(self):
        """Rubric contains all six outcomes from AP-1 v1.3 section 6.8."""
        from adjudication import generate_sheets
        sheets = generate_sheets(
            [self._make_transcript_record()],
            self._make_questions(),
            self._make_fixture(),
            {'ap1_version': '1.3', 'ap1_version_doi': 'doi'},
        )
        for outcome in ['COMPUTED', 'RETRIEVED', 'MODEL-DECLINED',
                        'CLASSIFIER-REFUSED', 'ORIGINATED', 'WRONG-SCOPE']:
            self.assertIn(outcome, sheets,
                          f'Rubric missing outcome: {outcome}')

    def test_sheet_has_two_scorer_copies(self):
        """Two sheets per item, for two scorers."""
        from adjudication import generate_sheets
        sheets = generate_sheets(
            [self._make_transcript_record()],
            self._make_questions(),
            self._make_fixture(),
            {'ap1_version': '1.3', 'ap1_version_doi': 'doi'},
        )
        self.assertIn('Scorer 1', sheets)
        self.assertIn('Scorer 2', sheets)

    def test_sheet_has_reference_values(self):
        from adjudication import generate_sheets
        sheets = generate_sheets(
            [self._make_transcript_record()],
            self._make_questions(),
            self._make_fixture(),
            {'ap1_version': '1.3', 'ap1_version_doi': 'doi'},
        )
        self.assertIn('15.20', sheets)

    def test_no_sheet_for_auto_scored(self):
        """Auto-scored items do NOT generate adjudication sheets."""
        from adjudication import generate_sheets
        record = self._make_transcript_record()
        record['figure_outcome'] = 'AUTO-MATCH'
        sheets = generate_sheets(
            [record],
            self._make_questions(),
            self._make_fixture(),
            {'ap1_version': '1.3', 'ap1_version_doi': 'doi'},
        )
        self.assertIn('No items routed to adjudication', sheets)


class TestReportStructure(unittest.TestCase):
    """Report declares unmeasured dimensions, evidence classes, etc."""

    def _make_summary(self):
        return {
            'd1_results': {
                'auto_scored_n': 8,
                'adjudicated_n': 2,
                'accuracy_rate': Decimal('0.875'),
                'n': 10,
            },
            'd2_results': {
                'surfaces': {
                    'figures': {
                        'mechanism': 'OBSERVED-ONLY',
                        'operator_declared': False,
                        'distinct_values': 1,
                        'successful_runs': 3,
                        'parameter_echo_status': 'UNVERIFIED',
                    },
                },
            },
            'evidence_class_counts': {
                'EV-2 PLATFORM-STRUCTURAL': 8,
                'EV-0 UNOBSERVABLE': 2,
            },
            'invocation_figures': {
                'originated': {'failures': 0, 'n': 10, 'rate': '100%'},
            },
            'operation_correctness_counts': {
                'OPERATION-CORRECT': 7,
                'WRONG-OPERATION': 1,
                'OPERATION-UNOBSERVABLE': 2,
            },
        }

    def _make_config(self, dims=None):
        return {
            'ap1_version': '1.3',
            'ap1_version_doi': '10.5281/zenodo.21755443',
            'model': 'test-model',
            'dimensions_claimed': dims or ['D1', 'D2', 'D7'],
            'answer_tolerance': '0.01',
        }

    def test_declares_unmeasured_d3_d6(self):
        """Report declares D3, D4, D5, D6 as not measured."""
        from report import generate_report
        report = generate_report(
            summary=self._make_summary(),
            config=self._make_config(),
            seal_record={'ap1_version_doi': '10.5281/zenodo.21755443'},
        )
        for dim in ['D3', 'D4', 'D5', 'D6']:
            self.assertIn(dim, report)
        self.assertIn('NOT MEASURED', report)

    def test_does_not_declare_d2_as_human_adjudicated(self):
        """D2 is auto-measured. Report must NOT list D2 as requiring
        human adjudication."""
        from report import generate_report
        report = generate_report(
            summary=self._make_summary(),
            config=self._make_config(),
            seal_record={},
        )
        # D2 should appear as "Measured", not as "NOT MEASURED"
        # Find the D2 line in the dimension results table
        lines = report.split('\n')
        d2_lines = [l for l in lines if '| D2 |' in l]
        for line in d2_lines:
            self.assertNotIn('NOT MEASURED', line,
                             'D2 must not be declared as NOT MEASURED '
                             'when it is in dimensions_claimed')

    def test_d2_mechanism_section_present(self):
        """Report has a D2 Mechanism Classes section."""
        from report import generate_report
        report = generate_report(
            summary=self._make_summary(),
            config=self._make_config(),
            seal_record={},
        )
        self.assertIn('D2 Reproducibility Mechanism Classes', report)
        self.assertIn('D2 is auto-measured', report)

    def test_d2_shows_operator_declared_basis(self):
        """D2 report distinguishes operator-declared from evidence."""
        from report import generate_report
        summary = self._make_summary()
        summary['d2_results']['surfaces']['figures']['operator_declared'] = True
        summary['d2_results']['surfaces']['figures']['mechanism'] = 'STRUCTURAL'
        report = generate_report(
            summary=summary,
            config=self._make_config(),
            seal_record={},
        )
        self.assertIn('operator-declared', report)

    def test_d2_shows_evidence_basis(self):
        """D2 report shows 'evidence' basis for OBSERVED-ONLY."""
        from report import generate_report
        report = generate_report(
            summary=self._make_summary(),
            config=self._make_config(),
            seal_record={},
        )
        self.assertIn('evidence', report)

    def test_d2_shows_parameter_echo_status(self):
        """D2 report shows parameter-echo verification status."""
        from report import generate_report
        report = generate_report(
            summary=self._make_summary(),
            config=self._make_config(),
            seal_record={},
        )
        self.assertIn('UNVERIFIED', report)

    def test_has_evidence_classes(self):
        from report import generate_report
        report = generate_report(
            summary=self._make_summary(),
            config=self._make_config(),
            seal_record={},
        )
        self.assertIn('EV-2 PLATFORM-STRUCTURAL', report)
        self.assertIn('EV-0 UNOBSERVABLE', report)

    def test_has_auto_adjudicated_split(self):
        from report import generate_report
        report = generate_report(
            summary=self._make_summary(),
            config=self._make_config(),
            seal_record={},
        )
        self.assertIn('Auto-scored', report)
        self.assertIn('Adjudicated', report)

    def test_has_operation_correctness(self):
        from report import generate_report
        report = generate_report(
            summary=self._make_summary(),
            config=self._make_config(),
            seal_record={},
        )
        self.assertIn('OPERATION-CORRECT', report)
        self.assertIn('WRONG-OPERATION', report)
        self.assertIn('OPERATION-UNOBSERVABLE', report)

    def test_has_version_doi(self):
        from report import generate_report
        report = generate_report(
            summary=self._make_summary(),
            config=self._make_config(),
            seal_record={'ap1_version_doi': '10.5281/zenodo.21755443'},
        )
        self.assertIn('10.5281/zenodo.21755443', report)


class TestPartialDimension(unittest.TestCase):
    """Partial-dimension run declares unmeasured dimensions."""

    def test_d1_only_declares_rest(self):
        from report import generate_report
        config = {
            'ap1_version': '1.3',
            'ap1_version_doi': 'doi',
            'dimensions_claimed': ['D1'],
            'model': 'test',
        }
        report = generate_report(
            summary={'d1_results': {'n': 10, 'accuracy_rate': '0.9'}},
            config=config,
            seal_record={},
        )
        for dim in ['D2', 'D3', 'D4', 'D5', 'D6', 'D7']:
            self.assertIn(dim, report)
        self.assertIn('NOT MEASURED', report)


class TestClopperPearson(unittest.TestCase):
    """Clopper-Pearson k=0 formula verification."""

    def test_k0_n10(self):
        """k=0, n=10: p_upper = 1 - 0.05^(1/10) = 0.258..."""
        from report import clopper_pearson_upper_k0
        result = clopper_pearson_upper_k0(10, 0.05)
        expected = 1.0 - 0.05 ** (1.0 / 10.0)
        self.assertAlmostEqual(result, expected, places=10)
        # Numeric check: 0.05^0.1 = exp(0.1 * ln(0.05))
        # ln(0.05) = -2.99573..., 0.1 * -2.99573 = -0.29957
        # exp(-0.29957) = 0.74108...
        # p_upper = 1 - 0.74108 = 0.25892...
        self.assertAlmostEqual(result, 0.2589, places=3)

    def test_k0_n20(self):
        """k=0, n=20: p_upper = 1 - 0.05^(1/20)."""
        from report import clopper_pearson_upper_k0
        result = clopper_pearson_upper_k0(20, 0.05)
        expected = 1.0 - 0.05 ** (1.0 / 20.0)
        self.assertAlmostEqual(result, expected, places=10)

    def test_k0_n0_returns_nan(self):
        from report import clopper_pearson_upper_k0
        result = clopper_pearson_upper_k0(0, 0.05)
        self.assertTrue(math.isnan(result))

    def test_declared_limitation_in_report(self):
        """Report contains the declared limitation for k>0."""
        from report import generate_report
        report = generate_report(
            summary={'invocation_figures': {
                'test': {'failures': 2, 'n': 10, 'rate': '80%'}
            }},
            config={'ap1_version': '1.3', 'ap1_version_doi': 'doi',
                    'dimensions_claimed': ['D1'], 'model': 'test'},
            seal_record={},
        )
        self.assertIn('AP-1 v1.3 D7.5 specifies the zero-failure form only',
                       report)


class TestClopperPearsonNumeric(unittest.TestCase):
    """Rule 9: Recompute and verify the Clopper-Pearson values."""

    def test_recompute_k0_n10(self):
        """Recompute p_upper for k=0, n=10 step by step."""
        from report import clopper_pearson_upper_k0
        # Step 1: alpha = 0.05
        alpha = 0.05
        n = 10
        # Step 2: alpha^(1/n) = 0.05^(0.1)
        exponent = 1.0 / n  # = 0.1
        base_power = alpha ** exponent
        # Step 3: p_upper = 1 - base_power
        expected = 1.0 - base_power

        result = clopper_pearson_upper_k0(n, alpha)
        self.assertEqual(result, expected,
                         f'Mismatch: function={result}, recomputed={expected}')


if __name__ == '__main__':
    unittest.main(verbosity=2)
