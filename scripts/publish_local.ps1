#!/usr/bin/env pwsh
# Build and upload to PyPI locally. Requires environment variable `PYPI_API_TOKEN` set.
python -m pip install --upgrade build twine
python -m build
if (-not $Env:PYPI_API_TOKEN) {
  Write-Error "Set PYPI_API_TOKEN environment variable first (create token at https://pypi.org/manage/account/)."
  exit 1
}
python -m twine upload dist/* -u __token__ -p $Env:PYPI_API_TOKEN
