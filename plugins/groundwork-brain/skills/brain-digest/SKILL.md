---
name: brain-digest
description: Draft a short Monday-morning summary of what changed in the AI Brain and what needs the owner's attention. Use when the user asks for a digest, a weekly summary, or a catch-up email, or on a scheduled weekly run.
---

# Weekly digest

A five-line read that tells the owner what their brain learned last week and
what is waiting on them.

## Which brain

Every path below is relative to the brain root, the folder holding
`brain.config.json`: the current directory or nearest parent that has one,
otherwise the brain path named in your `CLAUDE.md`. If neither exists, say so
and stop. One digest covers one brain, named at the top, so a week's changes are
never reported under the wrong business.

## Steps

1. Read the entries at the end of `wiki/log.md` covering the last seven days.
   Do not read the whole file.
2. Read `NEEDS-YOUR-EYES.md` at the brain root if it exists.
3. Count documents still waiting: files in `_sources/` whose **frontmatter**
   field `wiki_status` is `pending`, plus any file loose in `inbox/` other than
   `README.txt` and `_processed/`. Read the frontmatter at the top of the file;
   do not just search for the text `wiki_status: pending`, because a source
   that documents how ingestion works contains that line as an example and is
   not itself waiting. Counting those reports a backlog that does not exist,
   every week, until the owner stops believing the number.
4. Write the digest to `exports/digest-YYYY-MM-DD.md` and show it in the reply.

## Format

```
Your brain, week ending [date]

What it learned
- [one line per meaningful change, plain language, at most five]

What needs you
- [one line per open question from NEEDS-YOUR-EYES.md, at most three]

Waiting to be filed
- [count] documents waiting to be filed, or "nothing waiting"
```

## Rules

- Write in the owner's own tone of voice if the brain has a page for it.
- Plain language. No jargon, no file paths, no page names the owner would not
  recognise. They should be able to read it on a phone in thirty seconds.
- If nothing changed last week, say that in one line. Do not pad it.
- This is a draft. Never send it, never email it, never post it. The owner
  sends. This is a hard line and it does not bend for a scheduled run.
