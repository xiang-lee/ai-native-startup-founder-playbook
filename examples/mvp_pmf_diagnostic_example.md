# Example: MVP PMF Diagnostic

## Input

```text
Use the AI-Native Startup Founder Playbook skill to diagnose PMF signal quality.

Product: AI meeting follow-up assistant for customer success managers.
Current stage: MVP.
Activation data: 120 signups, 70 connected calendar, 42 generated first follow-up.
Retention data: 9 weekly active users after 4 weeks.
Revenue: 3 paid teams, all founder-sold.
Referral: no organic referrals yet.
User feedback: users like summaries but often edit heavily before sending.
Founder intervention: founder manually reminds users to try it after calls.
Sean Ellis survey: not run yet.
Desired output: PMF signal review, false-positive risks, and next sprint plan.
```

## Expected Agent Output Shape

```markdown
## Stage Diagnosis

- Current stage: MVP
- Why:
  - Supporting evidence: users are activating and a few teams paid.
  - Missing evidence: weak retention, no organic referrals, no Sean Ellis survey, high founder intervention.
  - Counter-evidence / risk: revenue may reflect founder sales rather than product pull.
- Things not to do yet:
  - Do not scale GTM.
  - Do not hire sales.
  - Do not add broad CRM integrations until the retained segment is understood.
- Exit criteria for Launch:
  - Retention improves in a specific segment.
  - Usage occurs without founder reminders.
  - Users would be very disappointed if the product disappeared or show equivalent behavioral pull.
```

```markdown
## PMF Signal Quality

1. Strongest evidence for PMF
   - Some users complete activation and three teams paid.
   - The workflow is tied to a recurring job: customer follow-up.

2. Strongest evidence against PMF
   - Only 9 of 120 signups are weekly active after 4 weeks.
   - Users edit heavily, suggesting the generated output may not meet trust or quality requirements.
   - Founder reminders are still needed.

3. False-positive risks
   - Signup without retained usage.
   - Founder-sold revenue without repeat pull.
   - Positive feedback on summaries without sending behavior.

4. Product pull vs founder push
   - Current signal is mostly founder-pushed.
   - Need to test whether users return after meetings without reminders.

5. Segment that may be most retained
   - Unknown. Segment retention should be split by customer size, meeting volume, CRM usage, and role seniority.

6. Next experiment
   - Narrow to CSMs with 10+ customer calls/week.
   - Improve follow-up quality for one meeting type.
   - Measure weekly repeated use and send-without-heavy-edit rate.
```

```markdown
## Next Sprint Plan

### North Star Question
Can a narrow segment of CSMs repeatedly send AI-generated follow-ups without founder reminders and without heavy edits?

### Workstreams

1. Discovery / Research
   - Tasks: interview all 9 retained users and 10 churned activated users.
   - Output: retained-vs-churned synthesis.
   - Done when: top 3 retention drivers and top 3 quality blockers are identified.

2. Build / Prototype
   - Tasks: improve one high-frequency follow-up workflow, not the entire product.
   - Output: updated prompt/template/eval for one meeting type.
   - Done when: 10 users test the improved workflow.

3. Measurement / Ops
   - Tasks: instrument edit rate, send rate, repeat usage, and no-reminder return rate.
   - Output: `metrics_framework.md` and weekly PMF review.
   - Done when: the team can distinguish product pull from founder push.

### Kill / Pivot Criteria

- Kill or pivot if retained users still rewrite most output after two focused improvement cycles.
- Narrow if one segment shows materially stronger repeat usage.
- Continue only if users return without founder reminders.
```
