# Groundwork Build

One skill, `brain-build`, used once. It turns a business's documents, website
and sent emails into a working AI Brain, asking the questions in conversation
and driving the Groundwork engine behind them.

This is a **delivery tool, not part of running a brain**. Everything the owner
needs afterwards is in `groundwork-brain`. Install this for the build session,
then remove it: an owner should never be left holding a skill for a job that is
already finished.

| Skill | What it does |
|---|---|
| `brain-build` | Builds a business a brain from scratch: intake, voice capture, documents, sensitivity triage, local processing, the handover pack, and the walkthrough. |

## Requires

The Groundwork engine on the machine running the build, found at `$AIBRAIN_HOME`
or `~/dev/GroundWorkAI/AiBrainFramework/installer`. Without it the skill says so
and stops rather than half-building anything.

## Install

Claude Code:

```
/plugin marketplace add https://github.com/Isaacn90/groundwork-brain-marketplace
/plugin install groundwork-build@groundwork-ai
```

## After handover

```
/plugin uninstall groundwork-build@groundwork-ai
```

Leave `groundwork-brain` installed. That is the one the owner uses every day.

## Safety

The build never sends anything, never moves money, and never handles a
credential: it needs no API key, no password and no token. Anything the owner
marks sensitive is compiled by a model on their own machine and is never read by
the build session.
