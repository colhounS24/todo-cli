#!/usr/bin/env bash
# Build and upload to PyPI locally. Requires environment variable PYPI_API_TOKEN set.
set -euo pipefail
python -m pip install --upgrade build twine
python -m build
if [ -z "${PYPI_API_TOKEN:-}" ]; then
  echo "Set PYPI_API_TOKEN environment variable first (create token at https://pypi.org/manage/account/)."
  exit 1
fi
python -m twine upload dist/* -u __token__ -p "$PYPI_API_TOKEN"
