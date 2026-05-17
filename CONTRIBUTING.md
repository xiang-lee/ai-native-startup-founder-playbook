# Contributing

Contributions are welcome if they make the skill more useful, more rigorous, or easier to apply.

## Good contributions

- Better customer discovery protocols
- Sharper PMF diagnostics
- More realistic examples
- Stage-specific security/compliance checks
- Founder bottleneck and operating-system templates
- Workflow lock-in and moat audit improvements
- Tool-neutral installation notes for different agent systems

## Avoid

- Vendor-specific lock-in unless clearly marked as optional
- Generic motivational startup advice
- Long copied excerpts from proprietary documents
- Prompts that encourage premature building or fake certainty
- Advice that replaces qualified legal, financial, security, or compliance review

## Style

- Be concrete.
- Prefer checklists, schemas, and decision gates over essays.
- Distinguish evidence from assumptions.
- Add adversarial checks by default.
- Keep the skill tool-neutral.

## Validation

Run:

```bash
python3 scripts/validate_skill.py
```

Before opening a PR, make sure the script passes and examples still match the skill's output contract.
