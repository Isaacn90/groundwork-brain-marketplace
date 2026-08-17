# Groundwork Brain

Five skills for working in an AI Brain folder. They are folder-agnostic: each one
resolves the brain root by finding `brain.config.json`, then follows the layout
described in that brain's `CLAUDE.md`. The same plugin works on every client brain.

| Skill | What it does |
|---|---|
| `brain-prime` | Catches Claude up at the start of a session without reading the whole wiki. |
| `brain-ingest` | Files whatever is waiting in `_sources/` as `wiki_status: pending`. |
| `brain-wrapup` | Saves what a session worked out, so tomorrow starts knowing it. |
| `brain-health` | Checks the brain over and writes up anything that needs a human. |
| `brain-digest` | Drafts a short "here is what changed" note. Drafts it. Never sends it. |

## Install

Claude desktop app: **Customize** -> **Plugins** -> **Personal plugins** -> **+** ->
**Add marketplace** -> **Add from a repository** -> `https://github.com/Isaacn90/GroundWorkAI`
then install **groundwork-brain**.

Claude Code:

```
/plugin marketplace add https://github.com/Isaacn90/GroundWorkAI.git
/plugin install groundwork-brain@groundwork-ai
```

## Safety

Every skill inherits the safety rules in the brain's own `CLAUDE.md`: draft only,
never send, never move money, never take an irreversible action. `brain-digest`
drafts the weekly note and never sends it, including on a scheduled run.

The two scheduled tasks that ship with a brain (`Update my brain`, `Weekly check`)
deliberately do not call these skills. They spell out every step themselves so the
brain keeps maintaining itself whether or not this plugin is installed.
