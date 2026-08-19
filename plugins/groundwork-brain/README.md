# Groundwork Brain

Eight skills for working in an AI Brain folder. They are folder-agnostic: each one
resolves the brain root by finding `brain.config.json`, then follows the layout
described in that brain's `CLAUDE.md`. The same plugin works on every client brain.

| Skill | What it does |
|---|---|
| `brain-prime` | Catches Claude up at the start of a session without reading the whole wiki. |
| `brain-ingest` | Files whatever is waiting in `_sources/` as `wiki_status: pending`. |
| `brain-wrapup` | Saves what a session worked out, so tomorrow starts knowing it. |
| `brain-health` | Checks the brain over and writes up anything that needs a human. |
| `brain-digest` | Drafts a short "here is what changed" note. Drafts it. Never sends it. |
| `client-review` | Works through the feedback a client left on their preview site. |
| `brain-automate` | Turns a recurring manual job into a working automation, via the Job Card Framework. |
| `brain-steward` | Gus the Groundskeeper's weekly walk: checks no rule has been broken and nothing was left running unattended, then pins what he found to `steward/noticeboard.html`. |

## Install

Claude desktop app: **Customize** -> **Plugins** -> **Personal plugins** -> **+** ->
**Add marketplace** -> **Add from a repository** ->
`https://github.com/Isaacn90/groundwork-brain-marketplace`
then install **groundwork-brain**.

Claude Code:

```
/plugin marketplace add https://github.com/Isaacn90/groundwork-brain-marketplace
/plugin install groundwork-brain@groundwork-ai
```

## Safety

Every skill inherits the safety rules in the brain's own `CLAUDE.md` and
`safety-constitution.md`: draft only, never send, never move money, never take an
irreversible action. `brain-digest` drafts the weekly note and never sends it,
including on a scheduled run. `brain-steward` reports and routes and never
repairs, and may never edit the constitution it checks.

The scheduled tasks that ship with a brain (`Update my brain`, `Weekly check`,
`Gus's weekly walk`) deliberately do not call these skills. They spell out every
step themselves so the brain keeps maintaining itself whether or not this plugin
is installed.
