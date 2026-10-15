#!/usr/bin/env python3
"""Check that every source URL still resolves. Run weekly by .github/workflows/links.yml, not on every push,
because a publisher being briefly down is not a reason to fail an unrelated change."""
import sys, urllib.request
from _common import sources, finish

problems = []
items = sources()
for s in items:
    req = urllib.request.Request(s["url"], headers={"User-Agent": "dynamics-365-ce-roster-link-check"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            if r.status >= 400:
                problems.append(f"{s['id']}: HTTP {r.status} {s['url']}")
    except Exception as e:  # noqa: BLE001 - report every failure the same way
        problems.append(f"{s['id']}: {e.__class__.__name__} {s['url']}")
finish("source links", problems, len(items))
