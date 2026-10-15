# Security

This repository holds skills, templates and scripts, not a running service. The realistic risks are a script that
does something unexpected on a contributor's machine, or organisation data accidentally committed.

- **Organisation data.** Never commit a real organisation profile or generated pack. `input/` and `output/` are
  git-ignored for that reason. If you find personal or confidential data in the history, report it privately so it can
  be removed.
- **Scripts.** The scripts read and write files inside the repository only, and `check-links.py` makes outbound requests
  to the URLs in `sources/`. Report anything else.

Report a security concern privately to the maintainers listed in `AUTHORS.md` rather than in a public issue.
