#!/usr/bin/env python3
"""BM25 search over a brain's wiki/topics/ and _sources/ markdown pages.

Stdlib only, no pip installs (this runs on client machines).

Usage:
    python3 search.py index <brain-root>
    python3 search.py query <brain-root> "<query>" [-n N]
"""

import argparse
import json
import math
import re
import sys
from pathlib import Path

K1 = 1.5
B = 0.75
FRONTMATTER_WEIGHT = 3
INDEX_REL_PATH = "_reports/.search-index.json"

TOKEN_RE = re.compile(r"[a-z0-9]+")


def tokenize(text):
    return TOKEN_RE.findall(text.lower())


def parse_frontmatter(text):
    """Return (title, description, body). Tolerates missing/malformed frontmatter."""
    if not text.startswith("---"):
        return "", "", text
    end = text.find("\n---", 3)
    if end == -1:
        return "", "", text
    header = text[3:end]
    body = text[end + 4 :]
    title = description = ""
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key == "title":
            title = value
        elif key == "description":
            description = value
    return title, description, body


def collect_docs(brain_root):
    paths = []
    for sub in ("wiki/topics", "_sources"):
        d = brain_root / sub
        if d.is_dir():
            paths.extend(sorted(d.rglob("*.md")))
    docs = []
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        title, description, body = parse_frontmatter(text)
        tokens = (
            tokenize(title) * FRONTMATTER_WEIGHT
            + tokenize(description) * FRONTMATTER_WEIGHT
            + tokenize(body)
        )
        if not tokens:
            continue
        tf = {}
        for tok in tokens:
            tf[tok] = tf.get(tok, 0) + 1
        docs.append(
            {
                "path": str(path.resolve()),
                "title": title or path.stem,
                "description": description,
                "tf": tf,
                "len": len(tokens),
            }
        )
    return docs


def build_index(brain_root):
    docs = collect_docs(brain_root)
    df = {}
    for doc in docs:
        for term in doc["tf"]:
            df[term] = df.get(term, 0) + 1
    n = len(docs)
    avgdl = sum(doc["len"] for doc in docs) / n if n else 0.0
    index = {"n": n, "avgdl": avgdl, "df": df, "docs": docs}
    index_path = brain_root / INDEX_REL_PATH
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(json.dumps(index), encoding="utf-8")
    return index


def newest_topic_mtime(brain_root):
    topics = brain_root / "wiki" / "topics"
    if not topics.is_dir():
        return 0.0
    mtimes = [p.stat().st_mtime for p in topics.rglob("*.md")]
    return max(mtimes) if mtimes else 0.0


def load_index(brain_root):
    index_path = brain_root / INDEX_REL_PATH
    if not index_path.exists() or index_path.stat().st_mtime < newest_topic_mtime(brain_root):
        return build_index(brain_root)
    return json.loads(index_path.read_text(encoding="utf-8"))


def score_docs(index, query):
    terms = tokenize(query)
    n = index["n"]
    avgdl = index["avgdl"] or 1.0
    df = index["df"]
    scored = []
    for doc in index["docs"]:
        tf = doc["tf"]
        dl = doc["len"]
        score = 0.0
        for term in terms:
            f = tf.get(term, 0)
            if f == 0:
                continue
            term_df = df.get(term, 0)
            idf = math.log((n - term_df + 0.5) / (term_df + 0.5) + 1)
            denom = f + K1 * (1 - B + B * dl / avgdl)
            score += idf * (f * (K1 + 1)) / denom
        if score > 0:
            scored.append((score, doc))
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return scored


def cmd_index(args):
    brain_root = Path(args.brain_root)
    if not brain_root.is_dir():
        print(f"error: brain root not found: {brain_root}", file=sys.stderr)
        sys.exit(1)
    index = build_index(brain_root)
    print(f"indexed {index['n']} pages -> {brain_root / INDEX_REL_PATH}")


def cmd_query(args):
    brain_root = Path(args.brain_root)
    if not brain_root.is_dir():
        print(f"error: brain root not found: {brain_root}", file=sys.stderr)
        sys.exit(1)
    index = load_index(brain_root)
    results = score_docs(index, args.query)[: args.num]
    for score, doc in results:
        print(f"{score:.4f}\t{doc['path']}\t{doc['title']}\t{doc['description']}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_index = sub.add_parser("index", help="build the BM25 index for a brain")
    p_index.add_argument("brain_root")
    p_index.set_defaults(func=cmd_index)

    p_query = sub.add_parser("query", help="search the brain")
    p_query.add_argument("brain_root")
    p_query.add_argument("query")
    p_query.add_argument("-n", "--num", type=int, default=8)
    p_query.set_defaults(func=cmd_query)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
