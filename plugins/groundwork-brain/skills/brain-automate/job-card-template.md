---
name: [job-name-in-kebab-case]
description: One sentence. What job does this do, and how often?
doc_type: job-card
owner: [client-business-slug]
rung: 1 | 2 | 3
status: draft | running | paused
updated: YYYY-MM-DD
---

# [Job name]

## 1. The job

What you do now, in one sentence, and how often you do it.

> Example: "Every Saturday I write the week ahead post for the academy group.
> Takes about half an hour."

How long it takes you now: [minutes]
How often: [daily | weekly | monthly | when X happens]

## 2. What stays the same

The facts that are true every time you do this. Do not write them out here.
Name the page in the wiki that already holds them, and if no page holds them
yet, that is the first thing to fix.

- [wiki/topics/some-page.md] — what it gives this job
- [a data file, if the facts are a list or a table]

If this section is empty, the job is not ready. A job with no standing facts
is a job the brain cannot help with, because it would have to be told
everything every time.

## 3. What changes

The smallest thing you have to say each time you run this.

**The three-line test.** If you cannot write what changes in three lines, the
job is still a judgment call and automating it will make it worse. Break it
into a smaller job and come back.

> Example:
> - Warkworth cancelled Friday
> - Feature the Womens session
> - I am in Brisbane with the U16s, 2am start

How it reaches the brain: [a message | a voice note | a file dropped in inbox/
| nothing, it runs on the standing facts alone]

## 4. What lands

What gets made, and where it turns up.

- Output: [a draft | an image | a file | rows in a sheet | a page in the wiki]
- Lands in: [a folder | an email to yourself | the brain's exports/]
- Format that matters: [anything that has to be exact every time goes here]

## 5. Who checks it

A person, named, for anything that leaves the business.

- Checked by: [name]
- Before: [posting | sending | filing]

Nothing on a job card sends, posts, publishes, pays, or deletes. The job makes
the thing and puts it where you will see it. You are the one who sends it.
That is not a limitation to work around later. It is the design.

## 6. When it breaks

How you find out, and what happens in the meantime.

- If it cannot run: [it says so where? ]
- If it runs on stale facts: [what tells you? ]
- Safe to miss a run? [yes | no, and why]

Design it so a missed run costs nothing. The next run should pick up everything
the missed one would have done, because it works from what is on disk rather
than from what happened since last time.

---

## How it runs

Pick the lowest rung that does the job.

**Rung 1 — you ask for it.** A skill. You say the job's name, it runs, you read
the output. No schedule, nothing running in the background, nothing to break.
Start here. Most jobs never need to leave.

**Rung 2 — it arrives.** The same thing on a timer, as a scheduled task. Move
up when you keep forgetting to ask, or when it needs to be waiting for you at a
particular time.

**Rung 3 — it arrives, exact.** A scheduled task plus a small script, for the
part of the output that has to be identical every time: an image, a spreadsheet,
a file another system reads. The script does the exact part. The brain does the
part that needs judgment. Only go here when "close enough" is not enough.

Chosen rung: [1 | 2 | 3]
Why: [one line]

## Build notes

[Filled in once it is built: where the files are, what the scheduled task
prompt says, anything the next person needs to know.]
