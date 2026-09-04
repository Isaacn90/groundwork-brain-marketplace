---
name: brain-health
description: Check an AI Brain for gaps, contradictions, and stuck documents, then report what needs a human. Use when the user says check my brain, health check, is my brain ok, or on a scheduled weekly run.
---

# Health check

Find what is broken or unanswered in this brain and put the human-shaped part
in front of the owner.

## Which brain

Every path below is relative to the brain root, the folder holding
`brain.config.json`: the current directory or nearest parent that has one,
otherwise the brain path named in your `CLAUDE.md`. If neither exists, say so
and stop. Check one brain per run and name it in the report, so a finding is
never attributed to the wrong business.

## Where the pages live

A standard brain keeps its topic pages in `wiki/topics/`, its catalog in
`wiki/index.md`, and its history in `wiki/log.md`, and this skill says so
throughout. Some brains are older than that layout and keep topic folders at
the root with a differently named catalog and log. `CLAUDE.md` is the authority:
if it describes a different layout, follow it and read the three names below as
"the topic pages", "the catalog", and "the log".

## Steps

Work through each check and record what you find:

1. **Environment.** `brain.config.json` parses as valid JSON. `wiki/topics/`,
   `_sources/`, and `inbox/` exist. `schema_version` in `brain.config.json` is
   present and equals `1`. A missing or older `schema_version` is a finding,
   not a failure: say that this brain predates the current schema and needs a
   migration.
2. **Stuck documents.** Files in `_sources/` still marked `wiki_status: pending`
   from more than a week ago, or marked `failed` or `needs-review` at all.
3. **Disconnected pages.** Count links **between pages in `wiki/topics/` only**.
   `wiki/index.md` links to every page, so counting it means this check can
   never fire and the wiki silently rots into a star with the index at the
   centre. Report three numbers: pages with no outbound link, pages with no
   inbound link, and pages with neither. A page with neither is isolated and is
   the real problem. If more than about one page in ten is isolated, say so as
   a finding in its own right: it means pages are being written without being
   connected to the courses, clients, platforms and techniques they name.
4. **Broken links.** Relative markdown links pointing at files that do not exist.
5. **Missing frontmatter.** Pages with no `type` field, or with a `description`
   that is empty or is just the top of the page body copied out. Descriptions
   are what `wiki/index.md` shows, so a bad one costs the reader twice.
6. **Near-duplicates.** Two pages covering the same thing under different names.
   Read both before calling it: a version, a stage, or a client name in the
   title usually means two different things, and a pair that already links to
   each other under `## Related` has been checked. Report the rest.
7. **Stale pages.** Pages whose `timestamp` is older than the `stale_days`
   value in `brain.config.json`, on subjects that change (prices, staff,
   services), not on subjects that do not.
8. **Placeholders.** Any remaining `[FILL IN]`, `[needs confirming]`, or
   `TODO` markers in pages the owner is meant to rely on.
9. **Contradictions.** Two pages stating incompatible facts. Read the pages,
   do not guess from titles.
10. **Credentials.** Passwords, PINs, licence keys, and account numbers sitting
   in the wiki. They came from the owner's own documents, so nothing has
   leaked, but everything in a connected folder is readable while Claude works.
   List them and leave the decision to the owner. Never delete one, and never
   quote the value into `NEEDS-YOUR-EYES.md`: name the page instead.

## Output

Two files:

- `_reports/health-YYYY-MM-DD.md`: the full findings, one section per check,
  with file paths. This is the record.
- `NEEDS-YOUR-EYES.md` at the brain root: only the items a human must answer,
  rewritten as plain questions. One line each, no jargon, newest at the top.
  If a previous version exists, keep any item still unresolved and drop the
  ones now fixed.

Also refresh `hot.md` at the brain root: rewrite its last-updated date and its
one-line status (`Nothing needs you.` or `N things need your eyes. See
NEEDS-YOUR-EYES.md`) from what you just wrote to `NEEDS-YOUR-EYES.md`. Leave
the page counts and `## This week` alone; ingest and wrap-up keep those.

Then reply with a two-line summary: how many findings, and the single most
important one.

## Rules

- Fail loud. If a check could not run, say which one and why. Never report
  "all clear" for a check you did not complete. An empty result and a failed
  result are different things and must read differently.
- Report only. Do not fix contradictions, delete pages, or merge duplicates
  without being asked. Suggest the fix and wait.
