---
name: ai-native-startup-founder-playbook
description: Use when evaluating, validating, building, launching, or scaling an AI-native startup. Guides agents through stage diagnosis, evidence gaps, adversarial validation, MVP scope control, launch readiness, and scale readiness.
version: 1.1.0
author: Xiang Li
license: MIT
homepage: https://github.com/xiang-lee/ai-native-startup-founder-playbook
repository: https://github.com/xiang-lee/ai-native-startup-founder-playbook
keywords:
  - ai startup
  - founder
  - product validation
  - customer discovery
  - mvp
  - product-market fit
  - launch readiness
  - startup coach
compatibility:
  - tool-neutral
  - markdown
  - agent-skill
metadata:
  tags: [startup, ai-native, founder, validation, customer-discovery, product-market-fit, mvp, launch, scale, agent-workflow]
---

# AI-Native Startup Founder Playbook

A tool-neutral agent skill for founders building with AI.

This skill is a synthesized workflow, not a summary or copy of any source document. It is designed to help an agent act as a rigorous founder coach: diagnose the current startup stage, identify missing evidence, challenge assumptions, control MVP scope, and produce a concrete next sprint plan.

## Core Principle

AI has reduced the cost of building. That makes judgment more important, not less.

The founder's bottleneck is no longer only “Can we build this?” but:

- Is the problem real?
- Is the user specific?
- Is the solution validated?
- Is traction real or vanity?
- Is the company ready to grow without the founder becoming the bottleneck?

Use AI agents for research, coding, documentation, workflow automation, and critique. Keep founder judgment for problem selection, tradeoffs, positioning, trust, and final decisions.

## AI Tool Surface Selection

Use the right AI mode for the job. The model matters, but the surrounding context, tools, and permissions matter more.

- **Conversational mode:** quick critique, rewrites, founder thinking partner, premortems, scenario analysis.
- **Workspace / cowork mode:** research across files and systems, interview synthesis, market maps, recurring reports, CRM/documentation workflows.
- **Coding / agentic development mode:** code generation, tests, refactors, security scans, architecture audits, API/webhook/SDK integration work.

Do not give a coding agent broad implementation tasks until the current stage has enough evidence and a written scope.

---

## When to Use

Use this skill when the user asks to:

- Evaluate whether a startup idea is worth building
- Turn a vague idea into a testable problem hypothesis
- Design customer discovery interviews
- Analyze user interviews or feedback
- Define MVP scope and prevent scope creep
- Build a founder-friendly execution plan for an AI-native startup
- Review launch readiness, founder bottlenecks, or operational gaps
- Assess product-market fit signals
- Think through scaling, enterprise readiness, workflow lock-in, or moat narrative

Do not use this skill for:

- Generic motivational startup advice
- Pure pitch-deck polishing
- Pure code implementation without product-stage context
- Brainstorming features before the problem has been validated

---

## Stage Map

### Stage 1: Idea — prove the problem deserves to exist

**Core question:** Is this a real, specific, frequent, painful problem for an identifiable user?

**Work to do:**

- Convert the idea into a testable problem hypothesis
- Define the exact user, buyer, workflow, frequency, and current workaround
- Research competitors, indirect alternatives, and failed attempts
- Design non-leading customer discovery interviews
- Search for disconfirming evidence

**Exit criteria:**

- You can name who has the problem, when it happens, how painful it is, and what they currently do about it
- The proposed solution addresses the problem discovered through validation, not just the founder’s original assumption
- There is enough qualitative evidence to justify building an MVP

**Risks:**

- Treating a prototype as validation
- Asking leading questions
- Mistaking founder conviction for evidence
- Building before understanding the user’s current workflow

#### Customer Discovery Protocol

For Idea-stage work, do not ask whether people like the idea. Test real past behavior.

Define:

- Interview target profile: job title, company type, team structure, seniority, painful workflow proximity, and where this person can be reached.
- Persona separation: daily user, economic buyer, influencer, blocker, admin/implementer, procurement or compliance gatekeeper.
- Question audit: remove leading questions, remove future-facing “would you use this?” questions, prefer “tell me about the last time...” prompts, and add probes for vague answers.
- Synthesis cadence: after every five interviews, summarize supporting evidence, challenging evidence, surprising findings, segment differences, and what the founder may be over-interpreting.

#### Optional bridge: lightweight prototype

After problem validation but before committing to an MVP, build only the single core interaction required to test the solution concept. Use it with five people from the validated target profile.

The prototype is not validation by itself. It is a conversation instrument to test whether the proposed solution matches the validated problem, whether users understand the value quickly, and which solution assumptions fail under real interaction.

---

### Stage 2: MVP — prove the solution creates value

**Core question:** Does a specific group of users use, return to, pay for, or recommend the product?

**Work to do:**

- Define the one core loop of the MVP
- Explicitly list what the MVP will not include
- Define what evidence would justify adding features
- Build only the smallest product needed to test the validated problem
- Create a measurement framework before launch
- Run a first-pass security and data exposure review
- Iterate toward evidence, not completeness

**Exit criteria:**

- Real product-market-fit signals exist: retention, repeated use, revenue, referral, strong pull from a specific segment, or Sean Ellis-style “very disappointed” responses from active users
- The product begins to pull users back without heroic founder intervention
- The signal persists across multiple iteration cycles, not just the launch spike
- The founder can explain who retains, why they retain, and what behavior predicts retention

**Risks:**

- Scope creep because AI makes features cheap to add
- Agentic technical debt caused by missing architecture/context files
- False PMF from friends, hype, press, or founder-assisted usage
- Security and privacy issues hidden behind working code

---

### Stage 3: Launch — prove growth can become repeatable

**Core question:** Can the product and company handle real growth without the founder becoming the bottleneck?

**Work to do:**

- Audit technical debt, reliability, security, monitoring, and compliance gaps
- Explain acquisition channels, conversion, CAC/LTV, and payback assumptions
- Identify founder bottlenecks in support, sales, product, engineering, and reporting
- Build lightweight operating systems: specs, sprint cadence, bug triage, weekly metrics
- Automate recurring workflows where possible

**Exit criteria:**

- Growth comes from explainable, repeatable channels
- The product can withstand real production usage
- Important operational workflows happen because systems exist, not because the founder remembers them

**Risks:**

- The founder stays in every loop and becomes the constraint
- MVP technical debt starts collecting interest
- Security, compliance, and procurement needs appear after they are already urgent
- Expansion into new markets before the original market is truly understood

---

### Stage 4: Scale — prove the company can compound

**Core question:** Can the company keep growing when the founder is no longer personally running day-to-day operations?

**Work to do:**

- Convert founder knowledge into documents, playbooks, skills, evals, and operating rules
- Convert domain expertise into proprietary context: industry edge cases, regulatory gotchas, customer workflows, jargon, decision rules, and reasons generic solutions fail
- Build enterprise-grade support, SLAs, documentation, incident response, and compliance posture
- Create repeatable GTM motions: segmentation, messaging, sales playbooks, partner/analyst narrative
- Turn product usage into a data/product improvement flywheel
- Deepen workflow lock-in through integrations, automation, and operational dependency
- Build a moat narrative supported by evidence

**Exit criteria:**

- Growth, governance, compliance, financial controls, support, and product defensibility can survive external scrutiny
- There is a clear explanation for why competitors cannot easily copy or replace the product
- The company can plausibly move toward sustained profitability, acquisition readiness, or IPO readiness

**Risks:**

- The company has a product but no operating system
- GTM still depends on founder hustle
- “Moat” is a slogan rather than a data, workflow, integration, or trust advantage
- Automation replaces judgment in places where judgment is still required

---

## Required AI Coding Context

Before building an MVP, create a durable project context file such as `CLAUDE.md`, `AGENTS.md`, or an equivalent agent-readable architecture context.

It should include:

- Product: core user, core problem, core product loop, explicit non-goals.
- Architecture: chosen stack, architectural principles, dependencies to prefer, dependencies to avoid, expected scale for the next six months, and MVP tradeoffs accepted for speed.
- Security constraints: data handled, authentication model, secrets handling, PII/sensitive data boundaries, audit expectations.
- Session protocol: start each coding session by reading scope and context; state the specific task and constraints; do not add features outside the scope document; end each session by logging decisions, assumptions, and files changed.

## Security and Compliance by Stage

### MVP security minimum

Before real users touch the product, review authentication/session handling, authorization boundaries, secrets management, data exposure in API responses, input validation/injection risks, dependency vulnerabilities, PII or sensitive data handling, and logs that might leak sensitive data.

### Launch security/compliance workstream

Before production growth, prioritize remediation from the MVP review, add monitoring and alerting, define access management, identify relevant compliance frameworks such as SOC 2, GDPR, HIPAA, PCI, or industry-specific requirements, and maintain compliance documentation as part of the development cycle.

### Scale enterprise readiness

Before enterprise or institutional scrutiny, prepare incident response, SLA definitions, support escalation paths, security-questionnaire answers, data retention/deletion policies, vendor/procurement documentation, and independent review when risk warrants it.

---

## Workflow

### Phase 0: Establish the boundary

First extract or ask for:

- Startup name or one-line description
- Current stage, if known: Idea / MVP / Launch / Scale / Unknown
- Target user and buyer
- Current evidence: interviews, usage data, revenue, retention, waitlist, code, demos, customer feedback, sales calls
- Desired output: stage diagnosis, validation plan, MVP scope, launch plan, scale plan, investor narrative, or sprint plan

If enough information is present to infer a default, proceed with explicit assumptions instead of blocking on clarification. If the stage is unclear, diagnose it before producing a roadmap.

For every run, include a short **Assumptions and Unknowns** section before recommendations:

```markdown
## Assumptions and Unknowns
- Assumptions I am making:
- Unknowns that materially affect the answer:
- Clarifying questions to answer during the sprint, not before it:
```

---

### Phase 1: Stage diagnosis

Output:

```markdown
## Stage Diagnosis

- Current stage: <Idea | MVP | Launch | Scale>
- Why:
  - Supporting evidence:
  - Missing evidence:
  - Counter-evidence / risk:
- Things not to do yet:
- Exit criteria for next stage:
```

Diagnosis rules:

- No real user/problem evidence → Idea
- Prototype but no retention, payment, repeated use, or referral → MVP
- Early revenue but growth is not repeatable and operations are founder-driven → Launch
- Repeatable GTM, reliability pressure, compliance pressure, enterprise procurement, or governance needs → Launch / Scale
- Cross-market expansion, enterprise readiness, auditability, and moat defense → Scale

---

### Phase 2: Evidence gap analysis

List the evidence required for the current stage.

**Idea gaps:**

- Exact user profile: role, context, workflow, frequency
- Buyer, budget owner, influencer, and approver; note when these are different people
- Last real occurrence of the problem
- Current workaround and cost of workaround
- Why existing alternatives fail
- Behavioral willingness-to-pay signals: time, data, budget, introduction, manual workaround
- Data access and trust constraints: sensitive data, permissions, integrations, auditability, and compliance blockers
- Market sizing: TAM / SAM / SOM estimate, assumptions behind each number, weakest assumption, and whether the market is expanding, consolidating, or mature
- Buyer landscape: economic buyer, daily user, technical evaluator, influencer, blocker, procurement/compliance gatekeeper
- Market timing: regulatory trends, technology shifts, demographic or workflow changes, and 24-month tailwinds/headwinds

**MVP gaps:**

- Activation definition
- Retention interval
- Core loop completion rate
- Revenue, referral, or repeat-use signal
- False PMF indicators
- Feature admission criteria
- PMF test design: Sean Ellis survey among active users, % “very disappointed” without the product, effort test, false positives such as signups without activation or revenue without retention, and whether signal holds across multiple iteration cycles

**Launch gaps:**

- Acquisition channel evidence
- Unit economics assumptions
- Production reliability and security posture
- Technical debt priority
- Founder bottleneck inventory
- Candidate workflows for automation or delegation

**Scale gaps:**

- Enterprise support, documentation, SLA, compliance
- Repeatable GTM motion
- Data/product flywheel
- Workflow lock-in and integration depth
- Proprietary context depth: what domain knowledge exists only in the founder's head, which edge cases are encoded into product/tests/prompts/workflows, and which expert workflows have become reusable skills or playbooks
- Evidence-backed moat narrative

---

### Phase 3: Agent perspectives

Use three perspectives. If subagents are available, run them in parallel. If not, perform the perspectives sequentially in one report.

#### 1. Research Agent

Focus: market size, TAM/SAM/SOM assumptions, competitors, indirect alternatives, failed products, user language, buyer landscape, procurement path, and market timing.

Must answer:

```markdown
- Hypothesis tested:
- Evidence found:
- Strongest supporting evidence:
- Strongest opposing evidence:
- Biggest uncertainty:
- TAM / SAM / SOM estimate and weakest assumptions:
- Buyer landscape: user, buyer, influencer, blocker, procurement gatekeeper:
- Market timing: key tailwinds and headwinds:
- Recommended next experiment:
```

Research quality rule: distinguish public desk research from customer evidence. Do not present TAM, trend data, competitor claims, or review snippets as validation unless they are tied to user behavior or customer conversations.

#### 2. Adversarial Agent

Focus: why this may fail.

Must answer:

```markdown
- Why the founder might be wrong:
- What evidence would kill this idea:
- What users might say but not do:
- Which competitor or workaround is underestimated:
- What would make this a bad business even if the product works:
```

For B2B or regulated workflows, explicitly test procurement, security review, integration complexity, incumbent distribution, and the risk that the user wants relief but the buyer will not fund it.

#### 3. Build/Ops Agent

Focus: translating validated decisions into scope, systems, specs, metrics, security checks, and automation.

Must answer:

```markdown
- Minimal next artifact to build:
- What not to build yet:
- Required context files:
- Metrics to instrument:
- Security/data/compliance checks:
- Operations that can be automated:
```

If the startup is in the Idea stage, the minimal build artifact should usually be a discovery asset, clickable demo, concierge workflow, or data-access test — not production software. State what must be learned before writing production code.

---

### Phase 4: Next sprint plan

Always produce a 1–2 week sprint, not a vague six-month roadmap.

```markdown
## Next Sprint Plan

### North Star Question
The one question this sprint must answer:

### Workstreams

1. Discovery / Research
   - Tasks:
   - Output:
   - Done when:

2. Build / Prototype
   - Tasks:
   - Output:
   - Done when:

3. Measurement / Ops
   - Tasks:
   - Output:
   - Done when:

### Kill / Pivot Criteria
Stop, narrow, or return to the previous stage if:
- ...

### Do Not Do Yet
- ...
```

The sprint plan must include concrete targets, not only task categories. For Idea-stage work, specify:

- Number and profile of customer interviews, usually 8–12 across user, buyer, and adjacent stakeholder personas
- Recruiting channels and minimum response target
- Interview script deliverable
- Competitor/alternative review deliverable
- Decision threshold for moving to prototype, narrowing the segment, or killing the idea

---

### Phase 5: Create reusable context assets

Each run should produce at least one asset future agents can reuse.

Recommended artifacts:

- Idea: `problem_hypothesis.md`, `customer_discovery_plan.md`, `interview_synthesis.md`
- MVP: `mvp_scope.md`, `CLAUDE.md` or `architecture_context.md`, `session_log.md`, `metrics_framework.md`, `security_review.md`
- Launch: `tech_debt_audit.md`, `founder_bottleneck_map.md`, `product_ops_system.md`
- Scale: `enterprise_readiness_gap.md`, `gtm_playbook.md`, `moat_narrative.md`, `workflow_lockin_audit.md`

Recommended location inside a project:

```text
contexts/startup_playbooks/<startup_name>/<artifact>.md
```

When writing in chat rather than editing a repository, still name the exact artifact(s) that should be created and provide a compact outline for each. Do not merely say “create assets.”

---

## Stage-Specific Output Requirements

These requirements prevent generic advice. Include the relevant items for the diagnosed stage.

### Idea-stage required outputs

```markdown
## Problem Hypothesis
- Target user:
- Buyer / budget owner:
- Workflow moment:
- Frequency:
- Pain / cost:
- Current workaround:
- Why now:

## Riskiest Assumptions
1. ...

## Discovery Plan
- Interview targets:
- Non-leading questions:
- Evidence to capture:
- Disconfirming evidence to seek:

## Exit Criteria Before MVP
- Build only if:
- Narrow / pivot if:
- Kill if:
```

### B2B workflow and finance-data addendum

For products touching finance, legal, HR, health, security, or other sensitive workflows, add:

```markdown
## Trust, Data, and Procurement Checks
- Systems of record involved:
- Data required to test the workflow:
- Permission/security concerns:
- Auditability requirements:
- Integration dependency risk:
- Procurement path and likely objections:
```

---

## Prompt Templates

### Idea: sharpen the hypothesis

```text
You are a rigorous AI-native startup founder coach. Turn the following idea into a testable problem hypothesis.

Input:
- Idea:
- Target user:
- Current evidence:

Output:
1. The most specific problem hypothesis: who, workflow, frequency, pain, current workaround
2. Five riskiest assumptions
3. Strongest argument that this is not worth building
4. A customer discovery plan: exact personas to interview, where to find them, separate question sets for user/buyer/influencer if needed, ten non-leading questions focused on past behavior, follow-up probes for vague answers, and a synthesis template to run after every five interviews
5. Exit criteria before building an MVP
```

### MVP: lock the scope

```text
Define an AI-native MVP scope from the validated problem below.

Input:
- Validated problem:
- Target user:
- Core use case:
- Constraints: time, technical, data, compliance, budget

Output:
1. The single core product loop
2. Must-have features
3. Explicitly excluded features
4. Evidence required to admit a new feature
5. Architecture/context decisions to document
6. Pre-launch security checklist
7. Activation, retention, and false-PMF metrics
```

### MVP: diagnose PMF signal quality

```text
Use this after launch or after several product iterations.

Input:
- Activation data:
- Retention data:
- Revenue:
- Referral:
- User feedback:
- Founder interventions required to keep users active:
- Sean Ellis survey results, if available:

Output:
1. Strongest evidence for PMF
2. Strongest evidence against PMF
3. False-positive risks
4. Whether usage is pulled by the product or pushed by founder effort
5. Segment that appears most strongly retained
6. Next experiment to confirm, narrow, pivot, or return to Idea stage
```

### MVP: pivot diagnostic

```text
Use after three or more iteration cycles without meaningful movement toward PMF benchmarks.

Input:
- Original problem hypothesis:
- Current segment:
- Retention data:
- Activation data:
- User feedback:
- Product changes tried:
- Messaging changes tried:

Output:
1. Is any segment responding materially better than the rest?
2. Is the gap a positioning problem, onboarding problem, product problem, or problem-selection problem?
3. What would have to be true for the current product to reach PMF?
4. Is that scenario realistic given the evidence?
5. Recommendation: continue, narrow segment, reposition, rebuild, or return to Idea stage
```

### Launch: audit founder bottlenecks

```text
Audit launch readiness with a focus on founder bottlenecks.

Input:
- Product and user scale:
- Growth channels:
- Founder’s recurring weekly tasks:
- Support/sales/product/engineering workflows:

Output:
1. Founder bottleneck inventory: recurring tasks, decisions waiting on founder, approvals routed through founder, support answers only founder knows, sales/customer-success steps only founder can perform, and reports or rituals that only happen when founder remembers
2. One-week absence test: which workflows stall if the founder is unavailable, why they stall, and what context/automation/delegation/escalation path is missing
3. Categorization: automate / delegate / document / keep founder-owned
4. Founder-only work to protect: product narrative, strategic tradeoffs, enterprise relationship moments, board/investor relationships, high-stakes hiring or partnership decisions
5. Production security, reliability, and compliance gaps
6. Five highest-ROI system-building actions for the next two weeks
7. Markets, features, or channels not to expand into yet
```

### Scale: review moat and auditability

```text
Review this company from the perspective of a scale-stage investor, enterprise buyer, or acquirer.

Input:
- Product:
- User behavior data:
- Integrations and workflows:
- GTM status:
- Support/compliance/documentation:

Output:
1. Ten questions external reviewers will ask
2. Whether the data flywheel is real and what evidence is missing
3. Workflow lock-in audit by customer segment: integrations, automations, team workflows, APIs/webhooks/SDK usage, switching cost, and next lock-in deepening opportunity
4. Enterprise readiness gaps
5. Proprietary context audit: domain edge cases, regulatory gotchas, reusable expert workflows, and eval/test coverage
6. One-page moat narrative draft
```

---

## Workflow Lock-in Audit Template

For each key customer or segment, document:

- Core workflows running through the product
- Integrations connected
- Automations built on top of the product
- Teams trained on the workflow
- Customer-specific prompts, templates, or operating procedures
- APIs, webhooks, or SDK usage
- Estimated switching cost: low = replaceable tool; medium = workflow disruption; high = operational migration project
- Next integration or automation that would deepen lock-in

---

## Quality Checklist

A good output must:

- Identify the current startup stage
- Separate evidence, assumptions, and founder conviction
- Include an adversarial section
- Define exit criteria and kill/pivot criteria
- Produce a concrete 1–2 week sprint plan
- Identify at least one reusable context asset
- Avoid encouraging premature building, premature scaling, or premature hiring
- Include basic security, privacy, data, and compliance checks where relevant
- State uncertainty instead of pretending the agent knows what it does not know

---

## Common Pitfalls

### Pitfall: treating a prototype as validation

A prototype is a learning instrument. Validation comes from user behavior, retention, payment, referral, or costly commitment.

### Pitfall: letting AI research confirm the founder’s bias

Always run an adversarial pass. Search for failed companies, stronger competitors, procurement blockers, and reasons users may not care.

### Pitfall: adding features because AI makes them cheap

Cheap features can still create expensive complexity. New features need evidence.

### Pitfall: coding without context files

Agentic coding drifts without durable project context. Maintain product scope, architecture principles, decision logs, and security constraints.

### Pitfall: mistaking early traction for PMF

Watch retention, repeated usage, revenue, referral, and what happens when the founder stops manually pushing users through the product.

### Pitfall: scaling a product before building a company

At scale, support, documentation, compliance, GTM, finance, governance, and operational reliability become product requirements.