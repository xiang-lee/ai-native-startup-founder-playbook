# AI-Native Startup Founder Playbook

A public, tool-neutral agent skill for founders building AI-native startups.

It helps an AI agent act as a rigorous founder coach: diagnose startup stage, find evidence gaps, challenge assumptions, control MVP scope, and produce a concrete 1–2 week sprint plan.

## Why this exists

AI makes building cheaper. That does **not** make startup judgment cheaper.

The dangerous failure mode for AI-native founders is no longer “I cannot build it.” It is:

- building before validating the problem
- mistaking prototypes for evidence
- adding features because agents make them cheap
- treating early attention as product-market fit
- scaling before the founder has built repeatable systems

This skill turns those risks into a structured workflow an agent can run.

## What the skill covers

- Idea validation
- Customer discovery
- Competitive and adversarial research
- MVP scope control
- PMF signal review
- Launch readiness
- Founder bottleneck audit
- Scale readiness, workflow lock-in, and moat narrative

## How to use

Copy `SKILL.md` into any agent system that supports skills, prompts, or reusable instructions.

Then ask your agent something like:

```text
Use the AI-Native Startup Founder Playbook skill to evaluate this idea:

<Idea / target user / current evidence / constraints>
```

Or:

```text
Use this skill to diagnose what stage my startup is in and produce a 2-week sprint plan.
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
- For Idea-stage B2B workflows: problem hypothesis, discovery plan, buyer/user distinction, and trust/data/procurement checks
- Suggested durable context assets, such as:
  - `problem_hypothesis.md`
  - `customer_discovery_plan.md`
  - `mvp_scope.md`
  - `metrics_framework.md`
  - `founder_bottleneck_map.md`
  - `moat_narrative.md`

## Design principles

- Evidence over enthusiasm
- Validation before construction
- Scope discipline over feature accumulation
- Founder judgment over agent autopilot
- Durable context assets over one-off chat
- Adversarial review by default

## Note on sources

This is a synthesized, tool-neutral workflow inspired by current AI-native startup practices and founder playbooks. It is not a copy of any proprietary document and intentionally avoids vendor-specific assumptions.

## License

MIT