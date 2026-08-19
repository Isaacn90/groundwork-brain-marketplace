# Groundwork Toolkit

Five skills and three agents for the everyday work a business actually asks for.
Unlike `groundwork-brain`, none of these need a brain folder to be useful, though
`business-voice` uses one when it finds one.

| Skill | What it does |
|---|---|
| `web-design` | Designs anything visual and makes it look professionally made: a page, a flyer, a logo, a social image, a deck. |
| `writing-polish` | Turns writing that reads as machine-written into writing that reads as a person's. |
| `business-voice` | Learns how this business actually talks, from its own brain where there is one, and writes to match. |
| `idea-check` | An honest read on a new idea, before money or weeks go into it. |
| `complex-task` | A steady way through a big multi-part job: plan it, work it in parts, keep the thread. |

None of them need a `/`. They switch on from a plain-English ask.

| Agent | For |
|---|---|
| `deep-planner` | Planning genuinely hard multi-part work before anything gets produced. Pins a model only max plans have, so pro sessions do the same work in the main conversation. |
| `worker` | Executing one well-specified part of a larger job to done. |
| `bulk-helper` | Mechanical work at volume: summarising, repetitive edits, reformatting. |

## Install

Claude desktop app: **Customize** -> **Plugins** -> **Personal plugins** -> **+** ->
**Add marketplace** -> **Add from a repository** ->
`https://github.com/Isaacn90/groundwork-brain-marketplace`
then install **groundwork-toolkit**.

Claude Code:

```
/plugin marketplace add https://github.com/Isaacn90/groundwork-brain-marketplace
/plugin install groundwork-toolkit@groundwork-ai
```

## Safety

These inherit the safety rules of whatever brain they are used in: draft only,
never send, never move money, never take an irreversible action. Where there is
no brain, the same rules still apply.

`skills/web-design/` includes data from Next Level Builder, used under the MIT
licence in that folder.
