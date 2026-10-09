# HA125 fulfilment starter kit — sanitized demonstration

Purpose: shorten time from a hypothetical contract start to a safe first deliverable for a remote generative-AI efficiency + Git engagement. This is a demonstration artifact only; it does not assert eligibility, prior client work, or employment experience. It contains no employer, shipboard, client, credential, or private information.

## 1. Intake — first 15 minutes
Collect only the minimum information needed for one bounded workflow:

- Current task name and desired outcome
- Sanitized example input and expected output
- Current manual steps and approximate frequency
- Definition of a correct result
- Data that must never be sent to an AI service
- Existing repository/branch/review conventions
- Person responsible for final human approval

Do not request credentials, production secrets, personal data, confidential customer data, or proprietary source material for a demonstration.

## 2. Baseline record
Before changing anything, record:

```text
Workflow:
Current steps:
Approx. minutes/run:
Runs/month:
Known failure modes:
Acceptance criteria:
Human approver:
```

The baseline is descriptive, not a promise of savings.

## 3. Smallest safe AI intervention
Choose one reversible drafting/classification/transformation step. Keep deterministic business decisions and final approval with a human.

Prompt requirements:

- State the permitted source material.
- Prohibit unsupported facts.
- Require uncertain items to be marked `VERIFY:`.
- Specify an exact output format.
- Do not include secrets or personal/confidential information.

## 4. Git-safe change path

```bash
git switch -c experiment/<short-topic>
# add only sanitized demonstration/config/documentation changes
git diff --check
git add <reviewed-files>
git commit -m "experiment: add reviewed AI workflow"
git diff main...HEAD
```

No force-push, history rewriting, direct production modification, or merge without the repository owner's normal review process.

Rollback: use the team's established process; for a simple merged commit where appropriate, retain the commit SHA so the change can be reverted cleanly.

## 5. First-delivery evidence packet
A first bounded delivery should contain:

1. `baseline.md` — sanitized before-state and acceptance criteria
2. `workflow.md` — proposed bounded workflow and human-review gate
3. `prompt.md` — reviewed prompt/template with uncertainty handling
4. `sample-output.md` — sanitized example output
5. `verification.md` — checks performed, unresolved `VERIFY:` items, and known limitations
6. Git commit/diff reference — auditable change history

## 6. Acceptance gate
Do not call the workflow complete unless:

- [ ] Output matches the agreed format
- [ ] Unsupported factual additions are absent
- [ ] Uncertainty is explicitly surfaced
- [ ] Sensitive/private data is absent
- [ ] Human approver can reproduce the review steps
- [ ] Git diff is readable and scoped
- [ ] Rollback path is documented
- [ ] Any claimed time saving is measured against the recorded baseline rather than estimated as fact

## 7. Compact handoff template

```text
Delivered: <bounded workflow/change>
Baseline: <measured or explicitly unmeasured>
Changed: <files/process step>
Verification: <checks performed>
Known limitations: <items>
Human approval required at: <gate>
Git evidence: <branch/commit/diff>
Rollback: <documented method>
Next optional step: <one reversible improvement>
```

## What this demonstrates

- A concrete intake-to-delivery path for AI-assisted efficiency work
- Safe handling boundaries before AI use
- Human verification and explicit uncertainty handling
- Basic Git branch/commit/diff/rollback discipline
- Measurement that distinguishes observed results from assumptions

Related sanitized demonstration: `portfolio/ha125-ai-git-workflow-demo.md`.
