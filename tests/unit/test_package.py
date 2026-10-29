"""Package-level facts that the seal and the install depend on."""

import re
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_pyproject_version_matches_version_file_tag():
    # pyproject.toml says to keep its version in step with the tag in
    # VERSION, which is what the seal records.
    with open(ROOT / 'pyproject.toml', 'rb') as f:
        pyproject_version = tomllib.load(f)['project']['version']
    lines = [line for line in (ROOT / 'VERSION').read_text().splitlines()
             if line.strip() and not line.startswith('#')]
    tag = lines[0].split()[0]
    assert re.fullmatch(r'v\d+\.\d+\.\d+', tag)
    assert tag == f'v{pyproject_version}'


def test_console_script_points_at_runner_main():
    with open(ROOT / 'pyproject.toml', 'rb') as f:
        scripts = tomllib.load(f)['project']['scripts']
    module_name, _, attr = scripts['ap1-run'].partition(':')
    import importlib
    module = importlib.import_module(module_name)
    assert callable(getattr(module, attr))
