---
name: brain-automate
description: Turn a recurring manual job into a working automation on this brain. Use when the owner says automate this, I do this every week, can you make this happen automatically, I keep writing the same thing, set this up to run on its own, or names a repeating job and asks whether the brain can take it over.
---

# Build an automation

The owner has a job they do over and over. Your work is to turn it into
something that runs, without handing them a form to fill in or a diagram to
read. They describe the job in their own words. You do everything else.

The method is the Job Card Framework: six questions, then the lowest rung of a
three-rung ladder that does the job. Read `docs/automation-framework.md` if it
is in reach. If it is not, everything you need is below.

**Read the brain before you ask anything.** This is the whole difference between
this and a generic automation tool. Most of the six answers are already written
down in the wiki. Turning up with four of six already filled in is what makes
this feel like their own system rather than a setup wizard.

## Step 1: find the job

Search `wiki/topics/` for the job they named. Recurring jobs leave traces: a
page describing the task, past examples of the output, a line in a client page
saying they do this weekly.

Then say back what you think the job is, in one sentence, and how often you
think they do it. Getting this wrong is cheap to fix now and expensive later.

If you find nothing, ask them to describe one recent time they did it, start to
finish. One real example beats any amount of describing the general case.

## Step 2: check it is worth building

Two gates. Both are fast, and failing either is a real result worth saying out
loud rather than a reason to press on.

**The five-times rule.** Have they done this at least five times? If not, they
do not yet know what stays the same, and neither do you. Say so, and offer to
come back after they have.

**The three-line test.** Write down what changes each time they run it. If you
cannot get it into three lines, the job is a judgment call, not a routine.
Automating it will produce confident nonsense. Split it into a smaller job and
test that instead.

Do not soften a failed gate. A job that should not be automated is the most
useful thing you can tell them today.

## Step 3: fill the six fields

Work these out from the brain first, and ask only what is genuinely missing.
Ask in plain language, one question at a time, never as a numbered list.

1. **The job** — what they do now, how often, how long it takes them.
2. **What stays the same** — the facts true every run. **Name the wiki page
   that holds them. Never copy the facts onto the card.** Two copies drift, and
   the drift is silent. If no page holds them, that is the real first job:
   file them into the wiki, then come back.
3. **What changes** — the smallest thing they must say each time, and how it
   reaches the brain: a message, a voice note, a file in `inbox/`, or nothing
   at all if the standing facts carry the whole job.
4. **What lands** — what gets made and where it turns up. Push for specifics.
   "A post" is not an answer. "A PNG 1600x900 and a caption in a text file,
   in a dated folder" is.
5. **Who checks it** — a named person, before it goes anywhere.
6. **When it breaks** — how they find out, and whether a missed run is safe.

## Step 4: pick the rung

Pick the **lowest** rung that does the job, and say why in one line. Every rung
up adds something that can break.

- **Rung 1, they ask for it.** A skill. Nothing scheduled, nothing running in
  the background, nothing that can fail quietly. Default here. A job run eleven
  times by hand is a job they actually understand.
- **Rung 2, it arrives.** A scheduled task on a timer. Move up only when they
  keep forgetting to ask, or it must be waiting at a set time. Write the task
  prompt so it spells the work out in full rather than naming a skill, because
  a scheduled task cannot rely on a skill being installed.
- **Rung 3, it arrives exact.** Scheduled task plus a small script, for output
  that must be byte-identical every time: an image, a spreadsheet, a file
  another system parses. Script does the exact part, you do the judgment part.
  This is the first rung with real code, and real code needs maintaining. Say
  that out loud before building it.

Owners often ask for rung 3 when rung 1 would do. Build rung 1, show them, and
let the next fortnight decide. Nobody regrets that order.

## Step 5: build it

Create `automations/<job-name>/` in the brain folder:

```
automations/<job-name>/
  job-card.md      the six answers
  data/            standing facts, only if they are a list or table
  code/            code, only at rung 3
  runs/            dated output
```

Use `job-card-template.md`, next to this file, for the card.

**Never name that folder `build/`.** The git-policy ignore baseline excludes
`build/` everywhere, so an automation built there is untracked, invisible to the
session-end commit, and gone the first time the folder is tidied. `code/` is the
convention for that reason.

Anything at rung 3 must be **runnable by them without you**: one command, no
arguments, sensible defaults, and it says what it did. If running it needs a
paragraph of instructions, it is not finished.

**Catch-up safety, at every rung.** The job's queue is what sits on disk, never
"what happened since last time". A job working from a timestamp breaks for good
the first time the laptop is asleep when it should have run. A job working from
a folder just picks everything up next time.

## Step 6: prove it

Run it on a real example from their own work, not a made-up one, and put the
output next to what they produced by hand last time.

This is the step that gets skipped and it is the one that matters. An
automation nobody has seen produce a correct result is a guess. If the output
is not as good as theirs, say so plainly and either fix it or drop the rung.

Then fill in the build notes at the bottom of the card: where the files are,
what the scheduled task prompt says, what the next person needs to know.

## Step 7: file it

Append a line to `wiki/log.md`. If the job produced a durable fact about the
business, file that into the right `wiki/topics/` page too. If building it
turned up a question only they can answer, add it to `NEEDS-YOUR-EYES.md`.

## Rules

- **Nothing sends.** No email, post, message, or comment to anyone outside the
  business. Jobs draft, the owner sends. If a job seems to need to send, the
  job is drawn wrong: redraw it to stop one step short.
- Nothing moves money, changes anyone's pay, role, or access, deletes anything,
  or commits the business to anything legal.
- Never write a credential into a job card, a script, or any file. Credentials
  go through `gw creds setup`. Write the schema freely: which keys the job
  needs, what they are for, where to get one.
- Never copy a fact onto a job card that already lives in the wiki. Point at it.
- Never build a job they did not raise themselves. If it did not come up
  unprompted, it is not a pain, and it will not get used.
- Fail loud. If a step could not run, say what and why. Never report a clean
  build when it was not one.
