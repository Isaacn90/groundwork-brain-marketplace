---
name: brain-wrapup
description: Save what this session learned into the AI Brain before it is lost. Use when the user says wrap up, we are done, save this, or at the end of any session that produced a new fact, decision, or correction about the business.
---

# Wrap up

Conversation is disposable. The wiki is not. This closes a session by moving
anything durable out of the chat and into the brain.

## Which brain

Every path below is relative to the brain root, the folder holding
`brain.config.json`: the current directory or nearest parent that has one,
otherwise the brain path named in your `CLAUDE.md`. If neither exists, say so
and stop. This skill writes, so getting it wrong puts one business's facts in
another's brain. Never guess, and if the session touched a different business
than the brain you resolved, write nothing and say why.

## Where the pages live

A standard brain keeps its topic pages in `wiki/topics/`, its catalog in
`wiki/index.md`, and its history in `wiki/log.md`, and this skill says so
throughout. Some brains are older than that layout and keep topic folders at
the root with a differently named catalog and log. `CLAUDE.md` is the authority:
if it describes a different layout, follow it and read the three names below as
"the topic pages", "the catalog", and "the log".

## Steps

1. Read `CLAUDE.md` for this brain's schema.
2. Look back over this session and pick out only the durable things:
   - A new client, supplier, product, or price.
   - A decision that was made, and why.
   - A preference about how work should be done.
   - A correction to something the brain believed.
   - A fact the user stated that is not yet written down anywhere.

   Ignore anything that was one-off: a draft, a question answered from
   existing pages, formatting, or chit-chat.
3. For each durable item, file it into the right page in `wiki/topics/`,
   following the schema. Create the page if it does not exist. Where it
   corrects an existing statement, state the current fact and note that it
   supersedes the old one.
4. Append one line to `wiki/log.md`: the date and what changed, in plain
   language the owner would understand a year from now.
5. If something about the business changed in a way that affects every future
   session, for example the tone of voice, a hard rule, or what the business
   sells, update `CLAUDE.md` itself as well.
6. If the session surfaced something you could not resolve, add it to
   `NEEDS-YOUR-EYES.md` at the brain root as a one-line question for the owner.

## Output

A short list of what you filed and where. If nothing durable came up, say
exactly that in one line. An empty wrap-up is a valid result, but only say it
after you have actually looked.

## Rules

- Never invent a fact to make a page look complete. If you are unsure whether
  something was decided, write it as a question in `NEEDS-YOUR-EYES.md`
  instead of writing it as fact.
- Never delete a fact. Supersede it and note the change.
- Do not rewrite pages you did not need to touch.
