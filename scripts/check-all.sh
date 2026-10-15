#!/usr/bin/env bash
# Every check CI runs, runnable locally: bash scripts/check-all.sh
# CI calls this same file, so the two cannot drift.
set -uo pipefail
cd "$(dirname "$0")/.."
fail=0
run() {
  printf '\n\033[1m%s\033[0m\n' "$1"; shift
  if "$@"; then :; else fail=1; printf '  FAILED\n'; fi
}
run "Skill frontmatter and sections are valid"   python3 scripts/validate-skills.py
run "Skill references resolve"                   python3 scripts/check-skill-refs.py
run "Every skill has trigger tests"              python3 scripts/check-triggers.py
run "UK English spelling"                        python3 scripts/check-uk-english.py
run "No third-party licence text"                python3 scripts/check-provenance.py
run "Surface map is coherent"                    python3 scripts/check-surfaces.py
run "Source catalogue is valid"                  python3 scripts/check-sources.py
run "Role data and templates are consistent"     python3 scripts/check-data.py
run "Sample profiles validate"                   python3 scripts/check-profiles.py
run "Manifests and department READMEs current"   python3 scripts/build-port.py --check
run "Skill source files current"                 python3 scripts/build-sources.py --check
run "README current"                             python3 scripts/build-readme.py --check
run "Website catalogue current"                  python3 scripts/build-site.py --check
run "Editions emit and validate"                 python3 scripts/build-edition.py --all --verify
run "Manifests parse" python3 -c "
import json,glob,sys
bad=[]
for f in ['.claude-plugin/marketplace.json','.agents/plugins/marketplace.json']+glob.glob('plugins/*/.claude-plugin/plugin.json')+glob.glob('plugins/*/.codex-plugin/plugin.json'):
    try: json.load(open(f))
    except Exception as e: bad.append(f'{f}: {e}')
for b in bad: print(' ',b)
print(f'manifests: {len(bad)} problems')
sys.exit(1 if bad else 0)
"
printf '\n'
if [ "$fail" -eq 0 ]; then printf '\033[32mAll checks passed.\033[0m\n'; else printf '\033[31mChecks failed.\033[0m\n'; fi
exit "$fail"
