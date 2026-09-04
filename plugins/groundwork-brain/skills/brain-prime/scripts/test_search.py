#!/usr/bin/env python3
"""Self-check for search.py. Plain python3, no framework.

Builds a tiny corpus in a temp dir, indexes it, queries it, and asserts
the obviously-relevant page ranks first.
"""

import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).parent / "search.py"

PAGES = {
    "wiki/topics/pricing.md": """---
type: concept
title: Pricing Model
description: How Groundwork AI prices brain builder engagements
---

# Pricing Model

Groundwork AI charges a flat fee for a brain builder engagement, billed in
two installments.
""",
    "wiki/topics/color-palette.md": """---
type: concept
title: Brand Color Palette
description: The hex values used across Groundwork AI marketing material
---

# Brand Color Palette

Primary blue, secondary grey, accent orange. Used in decks and the website.
""",
    "wiki/topics/onboarding.md": """---
type: process
title: Client Onboarding Steps
description: What happens after a client signs, before the kickoff call
---

# Client Onboarding Steps

Send the welcome email, schedule the kickoff call, set up the shared folder.
""",
}


def main():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for rel, content in PAGES.items():
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

        index_proc = subprocess.run(
            [sys.executable, str(SCRIPT), "index", str(root)],
            capture_output=True, text=True,
        )
        assert index_proc.returncode == 0, f"index failed: {index_proc.stderr}"
        assert (root / "_reports" / ".search-index.json").exists(), "index file not written"

        query_proc = subprocess.run(
            [sys.executable, str(SCRIPT), "query", str(root), "pricing brain builder"],
            capture_output=True, text=True,
        )
        assert query_proc.returncode == 0, f"query failed: {query_proc.stderr}"
        lines = [l for l in query_proc.stdout.strip().splitlines() if l]
        assert lines, "no results returned"

        top_path = lines[0].split("\t")[1]
        assert top_path.endswith("pricing.md"), f"expected pricing.md first, got: {lines[0]}"

        # Rebuild-on-stale check: query alone with no prior index should still work.
        with tempfile.TemporaryDirectory() as tmp2:
            root2 = Path(tmp2)
            for rel, content in PAGES.items():
                path = root2 / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            fresh_query = subprocess.run(
                [sys.executable, str(SCRIPT), "query", str(root2), "onboarding kickoff call"],
                capture_output=True, text=True,
            )
            assert fresh_query.returncode == 0, f"fresh query failed: {fresh_query.stderr}"
            fresh_lines = [l for l in fresh_query.stdout.strip().splitlines() if l]
            assert fresh_lines, "no results on auto-build"
            assert fresh_lines[0].split("\t")[1].endswith("onboarding.md"), (
                f"expected onboarding.md first, got: {fresh_lines[0]}"
            )

        print("OK: pricing query ranked pricing.md first")
        print("OK: auto-build-on-missing-index ranked onboarding.md first")


if __name__ == "__main__":
    main()
