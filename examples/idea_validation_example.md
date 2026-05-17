# Example: Idea Validation

## Input

```text
Use the AI-Native Startup Founder Playbook skill.

Startup idea: AI assistant that reconciles employee expense reports against accounting software.
Target user: Finance managers at mid-market companies.
Current evidence: Founder has talked to two finance managers informally. No paid users. No prototype.
Constraints: Must avoid handling sensitive finance data until we understand trust and integration requirements.
Desired output: Stage diagnosis, customer discovery plan, adversarial critique, and a 2-week sprint plan.
```

## Expected Agent Output Shape

```markdown
## Assumptions and Unknowns

- Assumptions I am making:
  - The target user is a finance/AP manager responsible for reviewing expense submissions.
  - The buyer may be a CFO, controller, or finance operations lead, not necessarily the daily user.
- Unknowns that materially affect the answer:
  - Which systems of record are involved: Concur, Expensify, Ramp, Brex, NetSuite, QuickBooks, Xero, spreadsheets, or custom workflows.
  - Whether reconciliation pain is frequent enough and expensive enough to justify a new tool.
  - Whether data-access, procurement, or audit requirements block adoption.
- Clarifying questions to answer during the sprint, not before it:
  - What was the last painful reconciliation incident?
  - How many hours did it consume?
  - What error, delay, or audit risk resulted?
```

```markdown
## Stage Diagnosis

- Current stage: Idea
- Why:
  - Supporting evidence: two informal conversations suggest possible pain.
  - Missing evidence: no structured interviews, no quantified workflow cost, no buyer validation, no proof that current tools fail in a repeatable way.
  - Counter-evidence / risk: incumbents may already solve most of the problem; users may complain but buyers may not fund another finance tool.
- Things not to do yet:
  - Do not build production integrations.
  - Do not handle sensitive financial data.
  - Do not design a multi-system automation roadmap.
- Exit criteria for next stage:
  - At least 8–12 structured interviews across daily users, buyers, and adjacent stakeholders.
  - Evidence that the problem is frequent, costly, and poorly solved by current workflows.
  - A specific segment where the pain is acute enough to test a lightweight prototype.
```

```markdown
## Problem Hypothesis

- Target user: Finance or AP managers at 100–1,000 employee companies.
- Buyer / budget owner: CFO, controller, or finance operations lead.
- Workflow moment: weekly/monthly review of employee expense submissions before reimbursement, close, or audit.
- Frequency: likely weekly during reimbursement cycles and intense near month-end close.
- Pain / cost: manual reconciliation, missing receipts, policy mismatch, duplicate spend, delayed reimbursements, audit risk.
- Current workaround: spreadsheets, manual review inside expense tools, emails/Slack reminders, ERP exports.
- Why now: finance teams are under pressure to do more with fewer people, while AI and integrations make partial automation more feasible.
```

```markdown
## Discovery Plan

- Interview targets:
  - 5 finance/AP managers who personally review expenses.
  - 3 controllers/CFOs who own budget and risk.
  - 2 IT/security/procurement stakeholders who approve finance-data integrations.
- Non-leading questions:
  - Tell me about the last time an expense report caused extra reconciliation work.
  - What systems did you open during that process?
  - How long did it take from first review to resolution?
  - What made the current tool insufficient?
  - What happens if this work is delayed or wrong?
  - Who cares about this problem besides you?
  - What have you tried to reduce the workload?
  - What would make a new tool impossible to approve?
  - What data would you never allow an AI tool to access?
  - If this disappeared tomorrow, what metric would improve?
- Evidence to capture:
  - Time spent per week/month.
  - Error or exception rate.
  - Number of systems touched.
  - Buyer urgency and budget path.
  - Trust and audit requirements.
- Disconfirming evidence to seek:
  - Existing tools already solve it.
  - Pain is annoying but too small to buy.
  - Integration/security burden is larger than the workflow cost.
```

```markdown
## Next Sprint Plan

### North Star Question
Do mid-market finance teams have a frequent, costly reconciliation workflow that current tools fail to solve, and is there a viable trust/procurement path for an AI-assisted solution?

### Workstreams

1. Discovery / Research
   - Tasks: recruit 8–12 interviews across user, buyer, and gatekeeper personas.
   - Output: `customer_discovery_plan.md`, interview notes, synthesis after every five interviews.
   - Done when: at least 8 interviews completed with quantified workflow examples.

2. Build / Prototype
   - Tasks: create a non-production clickable walkthrough or concierge workflow using mock data only.
   - Output: `problem_hypothesis.md`, prototype storyboard, data-access assumptions.
   - Done when: five validated target users react to the core workflow.

3. Measurement / Ops
   - Tasks: define activation and evidence thresholds before building.
   - Output: `metrics_framework.md`, trust/procurement checklist.
   - Done when: go / narrow / kill decision criteria are explicit.

### Kill / Pivot Criteria

- Kill if most users spend less than one hour per month on this or current tools solve it well.
- Narrow if pain exists only in a specific system pair, e.g. Expensify → NetSuite.
- Do not build production software until trust/data/procurement constraints are understood.
```
