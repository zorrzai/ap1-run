"""A pytest plugin for tests/conformance/test_marks.py: at the end of
collection it writes every collected test's finding, proposal and xfail
marks to the JSON file named by $AP1_MARKS_DUMP. Loaded only by that test,
in a subprocess (-p marks_plugin)."""

import json
import os


def pytest_collection_modifyitems(session, config, items):
    path = os.environ.get('AP1_MARKS_DUMP')
    if not path:
        return
    out = []
    for item in items:
        out.append({
            'nodeid': item.nodeid,
            'finding': [list(m.args) for m in item.iter_markers('finding')],
            'proposal': [{'args': list(m.args), 'kwargs': dict(m.kwargs)}
                         for m in item.iter_markers('proposal')],
            'provisional': [{'args': list(m.args), 'kwargs': dict(m.kwargs)}
                            for m in item.iter_markers('provisional')],
            'strict_xfail': any(m.kwargs.get('strict')
                                for m in item.iter_markers('xfail')),
        })
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(out, f)
