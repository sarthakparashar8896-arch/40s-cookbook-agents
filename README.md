# The 40's Cookbook — AI Agentic Team

This folder contains your AI employees, configured as Claude Code sub-agents.

## What you have

```
40s-cookbook/
├── BRAND_FOUNDATION.md       ← Single source of truth. All agents read this.
├── README.md                  ← This file
└── .claude/
    └── agents/
        ├── brand-strategist.md
        ├── market-researcher.md
        ├── gtm-strategist.md
        ├── supplier-scout.md
        └── content-writer.md
```

## How to use the team

After installing Claude Code (see setup guide), open a terminal in this folder and run:

```
claude
```

This starts the main Claude Code session — your "team lead." From here you can delegate work to any agent.

### Two ways to invoke an agent

**1. Explicit invocation (recommended when starting out):**

> Use the brand-strategist agent to give me 5 alternative tagline options that don't use the word "table."

> Use the market-researcher to do a deep-dive on Naagin's pricing, packaging, and social engagement on Instagram.

> Use the supplier-scout to build a shortlist of 10 contract manufacturers for pickle production in North India.

**2. Automatic invocation:**

If your prompt clearly matches an agent's `description` field, Claude Code will route it automatically. Example:

> I need a list of glass jar suppliers in Delhi NCR.

Claude Code will see this matches `supplier-scout` and dispatch automatically.

### Running multiple agents in parallel

You can ask the main session to run multiple agents at once:

> Run the market-researcher and the gtm-strategist in parallel:
> - Market-researcher: pull pricing benchmarks for the top 8 Indian pickle brands.
> - GTM-strategist: based on those benchmarks, recommend our launch price band.

Each agent runs in its own context window, so they don't pollute each other.

### Useful commands inside Claude Code

- `/agents` — Open the agents management UI. Create, edit, view all agents.
- `/clear` — Clear the current conversation if context gets cluttered.
- `claude agents` (from the terminal, before starting Claude) — List all configured agents.

## Updating an agent

Two ways:

1. **Edit the markdown file directly** in `.claude/agents/<agent>.md`, save, then restart the Claude Code session.
2. **Use `/agents` inside Claude Code** to edit through a UI. Changes are live immediately.

## Adding a new agent

Either:
1. Create a new `.md` file in `.claude/agents/` following the same format as the existing agents.
2. Or run `/agents` inside Claude Code and select "Create new agent."

## Important notes

- **Agents read `BRAND_FOUNDATION.md`** at the project root. If you update brand details (name, tagline, audience, etc.), update that file. All agents will pick up the change automatically.
- **Each agent has its own context window.** They don't share findings unless you (the orchestrator) pass them.
- **Token usage scales with agents.** Running 3 agents in parallel uses ~3x the tokens of a single session. Worth it for time savings on big tasks.
- **Agents can use web search and write files.** They can pull live data from the internet and save reports into your project folder.

## Suggested first tasks

1. **Market researcher:** Build a competitor pricing table for Mother's Recipe, Priya, Patanjali, Naagin, and 4 others. Output to `research/competitor-pricing.md`.
2. **Supplier scout:** Find 10 FSSAI-compliant pickle contract manufacturers in North India. Output to `suppliers/contract-manufacturers.md`.
3. **GTM strategist:** Build a 90-day launch calendar with specific weekly milestones. Output to `gtm/90-day-plan.md`.
4. **Brand strategist:** Refine the flavor variant naming — give 3 alternative naming systems for the launch flavors.
5. **Content writer:** Draft the website "About" page using the Madhu and Banaras story.

## When to come back here vs. a regular Claude chat

| Use Claude Code agents when | Use a regular Claude chat when |
|---|---|
| You need parallel work across multiple specialists | One quick question or brainstorm |
| The work needs to be saved as files in a project | Conversational thinking with no deliverable |
| You want consistent voice via dedicated system prompts | One-off creative riffing |
| The task involves web research, sourcing, or analysis | Image generation or visual artifacts |
