# groundwork-brain-marketplace

Groundwork AI's public Claude Code plugin marketplace. `.claude-plugin/marketplace.json`
lists three plugins under `plugins/`: `groundwork-brain` (run an AI Brain folder),
`groundwork-toolkit` (everyday skills and agents) and `groundwork-build` (builds
a client brain, removed at handover).

## Where it runs

Public. Install in Claude Code with `/plugin marketplace add Isaacn90/groundwork-brain-marketplace`.

## Tickets

Feature requests and bugs are GitHub Issues on this repo. A ticket filed with
the Feature or Bug form is built by Claude in Actions
(`.github/workflows/claude-ticket.yml`) and arrives as a PR filled from
`.github/pull_request_template.md`. Comment `@claude ...` on the PR for changes.
The owner's `approve` comment runs `.github/workflows/claude-ship.yml`, which
merges once CI is green. Approving a ticket merges it, and it's live for anyone who updates the marketplace.

More detail for Claude sessions is in `CLAUDE.md`.
