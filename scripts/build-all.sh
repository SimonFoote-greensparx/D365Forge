#!/usr/bin/env bash
# Regenerate every generated file, then run every check: bash scripts/build-all.sh
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/build-bundles.py
python3 scripts/build-port.py
python3 scripts/build-sources.py
python3 scripts/build-readme.py
python3 scripts/build-site.py
python3 scripts/build-cowork.py
bash scripts/check-all.sh
