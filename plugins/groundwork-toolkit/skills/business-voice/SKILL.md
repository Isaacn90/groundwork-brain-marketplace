---
name: business-voice
description: Learn and apply a business's own writing voice and tone, so drafts sound like the business, not generic. Use when the user asks "does this sound like us", "write this in our voice", "how do we usually talk to customers", wants a voice or tone guide, or when drafting anything (emails, posts, ads, website copy) where matching an established house style matters.
---

# Business Voice

Figure out how this specific business talks, then write to match it. A voice guide beats guessing every time.

## Step 1: check for an AI Brain

Look for a folder containing `brain.config.json` with a `wiki/topics/` directory next to it, either in the current working folder or a parent of it. That's an AI Brain: a knowledge base built for this business.

If one exists:
1. Search `wiki/topics/` for an existing voice or tone page. Look for titles or filenames containing "voice", "tone", "communication", or "style".
2. If found, read it and use it as the source of truth. Don't re-derive voice from scratch when a guide already exists.
3. If none exists, go to Step 2, then offer to save what you learn (see Step 3).

If no AI Brain is present, just do Step 2 in this conversation and stop there.

## Step 2: infer voice from real writing

Ask for, or work from, actual samples of the business's own writing: past emails, website copy, social posts, texts to customers. The more real samples, the better. Don't invent a voice from a brand name or a guess at their industry.

From the samples, note:
- **Formality**: Do they use contractions? Slang? Full sentences or fragments?
- **Sentence length**: Short and punchy, or longer and explanatory?
- **What they lead with**: The price? The benefit? A greeting?
- **Words they use and avoid**: Do they say "customers" or "clients"? Formal terms or plain ones?
- **Warmth**: Friendly and personal, or brisk and businesslike?
- **What's missing**: Corporate phrases they'd never say. Jargon that doesn't fit how they actually talk.

Summarize this in a few plain sentences, not a checklist longer than the samples themselves.

## Step 3: offer to save it (brain present only)

If working inside an AI Brain and no voice page existed, offer to save the findings as a new wiki page. Follow that brain's own `CLAUDE.md` for the exact format, but the pattern is consistently:
- A page under `wiki/topics/` with frontmatter (`type`, `title`, `description`, `resource`, `tags`, `timestamp`) followed by the guide in plain sentences.
- Only do this if the user agrees. It's their business record, not a scratch note.

## Rules

- Never invent voice traits without either a saved guide or real samples to point to.
- If samples conflict (formal on the website, casual in texts), say so and ask which context applies, or note both.
- Don't write into a client's brain with another business's facts, or vice versa. This skill only touches the brain it's already running inside.
- A voice guide describes how they already write. It's not a style to aspire to.
