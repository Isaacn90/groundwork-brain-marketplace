---
name: brain-prime
description: Orient yourself in an AI Brain folder at the start of a session. Use when a session begins in a brain folder, or when the user says prime, get up to speed, catch me up, or what has been happening.
---

# Prime

Get oriented in this brain without reading it end to end. Large brains hold
thousands of pages; loading everything wastes the session before it starts.

## Which brain

Every path in this skill is relative to the brain root, the folder holding
`brain.config.json`. Resolve it in this order, and name the one you used:

1. The current directory, or the nearest parent directory, that holds
   `brain.config.json`.
2. Otherwise, the brain path named in your `CLAUDE.md`.

If neither exists, say so and stop. Never guess a folder. On a machine holding
more than one brain, a guess files one business's facts into another's.

## Where the pages live

A standard brain keeps its topic pages in `wiki/topics/`, its catalog in
`wiki/index.md`, and its history in `wiki/log.md`, and this skill says so
throughout. Some brains are older than that layout and keep topic folders at
the root with a differently named catalog and log. `CLAUDE.md` is the authority:
if it describes a different layout, follow it and read the three names below as
"the topic pages", "the catalog", and "the log".

## Steps

1. Resolve the brain root as above and confirm `CLAUDE.md` sits beside
   `brain.config.json` in it.
2. Read `CLAUDE.md`. It is the schema and the safety rules for this brain.
3. Read only the most recent entries at the end of `wiki/log.md`, not the
   whole file, to see what changed lately.
4. Count the pages in `wiki/topics/` to gauge scope.
5. Count the files in `_sources/` whose frontmatter says `wiki_status: pending`.
   These are documents waiting to be filed.
6. Check whether `NEEDS-YOUR-EYES.md` exists at the root. If it does, read it.

## Output

Four short lines, no preamble:

- What this brain knows most about, from the recent log and the topic names.
- What changed recently.
- How many documents are waiting to be filed, if any, and an offer to run
  `brain-ingest` now.
- Anything in `NEEDS-YOUR-EYES.md` that is still open.

## Rules

- Never read `wiki/index.md` or `wiki/log.md` from top to bottom.
- If a file you expect is missing, say which one and what it means. Never
  report a clean start when you could not check.
