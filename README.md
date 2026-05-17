# AI-Native Startup Founder Playbook

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Version](https://img.shields.io/badge/version-1.1.0-blue)
![Skill](https://img.shields.io/badge/agent%20skill-tool--neutral-purple)

A public, tool-neutral agent skill for founders building AI-native startups.

Use this skill when you want an AI agent to act less like a hype-driven brainstorming partner and more like a disciplined startup operating partner.

Repo: https://github.com/xiang-lee/ai-native-startup-founder-playbook

## Why this exists

AI makes building cheaper. That does **not** make startup judgment cheaper.

The dangerous failure mode for AI-native founders is no longer “I cannot build it.” It is:

- building before validating the problem
- mistaking prototypes for evidence
- adding features because agents make them cheap
- treating early attention as product-market fit
- scaling before the founder has built repeatable systems

This skill turns those risks into a structured workflow an agent can run.

## Best for

- solo founders
- AI-native builders
- early-stage startup teams
- agents helping with product strategy, validation, MVP planning, launch readiness, and scale readiness

## Not for

- generic startup motivation
- pitch-deck cosmetics
- premature feature brainstorming
- replacing founder judgment

## What the skill covers

- Idea validation and problem hypothesis sharpening
- Customer discovery design and interview synthesis
- TAM/SAM/SOM, buyer landscape, and market timing analysis
- Competitive, indirect alternative, and failed-product research
- MVP scope control and feature admission criteria
- Durable AI coding context: `CLAUDE.md`, architecture context, session logs
- PMF signal review, including retention, referral, Sean Ellis-style tests, effort tests, and false-PMF checks
- Security and compliance review by stage
- Launch readiness and founder bottleneck audits
- Workflow automation and one-week founder absence tests
- Scale readiness, enterprise procurement readiness, workflow lock-in, data flywheels, proprietary context, and moat narrative

## Installation

Clone the repo:

```bash
git clone https://github.com/xiang-lee/ai-native-startup-founder-playbook.git
```

Then copy `SKILL.md` into your agent skill, prompt, or instruction system.

You can also paste the contents of `SKILL.md` directly into any AI system that supports reusable instructions, such as:

- Claude Projects / Claude Code-style skills
- Cursor rules or project instructions
- ChatGPT Projects / custom GPT instructions
- Hermes Agent skills
- OpenCode / Codex / other coding-agent instruction files

The skill is intentionally tool-neutral. It does not assume a specific model or vendor.

## Quickstart

Paste this into your agent:

```text
Use the AI-Native Startup Founder Playbook skill.

Startup idea:
Target user:
Current evidence:
Constraints:
Desired output:
```

Example:

```text
Use the AI-Native Startup Founder Playbook skill.

Startup idea: AI assistant that reconciles employee expense reports against accounting software.
Target user: Finance managers at mid-market companies.
Current evidence: Founder has talked to two finance managers informally. No paid users. No prototype.
Constraints: Must avoid handling sensitive finance data until we understand trust and integration requirements.
Desired output: Stage diagnosis, customer discovery plan, adversarial critique, and a 2-week sprint plan.
```

## Expected output

A good run should produce:

- Stage diagnosis: Idea / MVP / Launch / Scale
- Assumptions and unknowns when the input is incomplete
- Supporting evidence and missing evidence
- Strongest adversarial argument
- Current-stage exit criteria
- Kill / pivot criteria
- 1–2 week sprint plan with concrete targets
- For Idea-stage B2B workflows: problem hypothesis, discovery plan, buyer/user distinction, TAM/SAM/SOM assumptions, and trust/data/procurement checks
- For MVP-stage workflows: MVP scope, non-goals, metrics framework, AI coding context, security checklist, and PMF diagnostic
- For Launch-stage workflows: founder bottleneck inventory, one-week absence test, operating-system gaps, and security/compliance workstream
- For Scale-stage workflows: workflow lock-in audit, enterprise readiness gaps, proprietary context audit, data flywheel, and moat narrative
- Suggested durable context assets, such as:
  - `problem_hypothesis.md`
  - `customer_discovery_plan.md`
  - `interview_synthesis.md`
  - `mvp_scope.md`
  - `CLAUDE.md` or `architecture_context.md`
  - `metrics_framework.md`
  - `security_review.md`
  - `founder_bottleneck_map.md`
  - `workflow_lockin_audit.md`
  - `moat_narrative.md`

## Examples

See:

- [`examples/idea_validation_example.md`](examples/idea_validation_example.md)
- [`examples/mvp_pmf_diagnostic_example.md`](examples/mvp_pmf_diagnostic_example.md)

## Design principles

- Evidence over enthusiasm
- Validation before construction
- Scope discipline over feature accumulation
- Founder judgment over agent autopilot
- Durable context assets over one-off chat
- Adversarial review by default

## Validation

This repo includes a lightweight contract check:

```bash
python3 scripts/validate_skill.py
```

It verifies that `SKILL.md` contains frontmatter and the core sections needed for the skill to be usable.

## Note on sources

This is a synthesized, tool-neutral workflow inspired by current AI-native startup practices and founder playbooks. It is not a copy of any proprietary document and intentionally avoids vendor-specific assumptions.

## License

MIT