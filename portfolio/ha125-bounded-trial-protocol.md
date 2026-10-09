# HA125 — bounded paid-trial protocol

> Demonstration material only. This does **not** assert HA125 eligibility, prior client work, employment experience, or application status. No employer, shipboard, customer, credential, or private information is used.

## Purpose
Provide a ready-to-run first-task protocol so a buyer can evaluate generative-AI efficiency and Git discipline on a small, reversible unit of work before broader ongoing work.

## Trial unit
**One permitted, non-confidential workflow → one reviewed improvement → one Git-traceable delivery.**

Default boundary:
- Input: one buyer-approved sample or synthetic sample.
- Change surface: one workflow/document/script-sized unit agreed before work begins.
- AI use: only on material explicitly permitted for AI processing.
- Delivery: one branch/diff or equivalent reviewable artifact, plus a short handoff note.
- Expansion: none unless separately agreed after acceptance.

## Intake gate
Before processing anything, record:
1. Desired outcome.
2. Current manual steps or current artifact.
3. Explicitly permitted input data.
4. Data that must not be sent to an AI system.
5. Required output format.
6. Acceptance criterion: what observable result counts as done?
7. Repository/review convention, if Git is involved.

If permission for a data class is unclear, exclude it rather than infer permission.

## Execution path
1. **Sanitize** — remove credentials, personal identifiers, confidential business data, and unrelated context.
2. **Baseline** — record the current steps and a simple measurable baseline where available (for example, manual steps or elapsed handling time). Do not invent a baseline.
3. **Constrain** — define the output schema and instruct the model not to add unsupported facts; uncertain items are flagged for verification.
4. **Generate** — produce only the bounded trial output.
5. **Verify** — compare factual claims and required fields against the permitted source.
6. **Git-review** — place accepted changes on a task branch; inspect the full diff and run `git diff --check` where applicable.
7. **Deliver** — provide the reviewed artifact/diff, verification result, unresolved items, and rollback point.
8. **Measure** — report only observed before/after values. If no reliable measurement exists, state `not measured`.

## Acceptance record
Use this compact receipt for the first delivery:

```text
Objective:
Permitted input scope:
Excluded/sanitized data:
Delivered artifact:
Verification performed:
Observed result:
Unresolved items:
Git branch/commit or review reference:
Rollback point:
Buyer acceptance: pending / accepted / revision requested
```

## Failure / rollback rule
- Unsupported factual additions: reject before delivery.
- Requirement ambiguity: mark unresolved; do not silently choose a business rule.
- Defective committed change: use a traceable revert rather than rewriting history.
- Sensitive data discovered mid-task: stop processing that material, remove it from the working set, and request a sanitized/approved replacement through the marketplace workflow.

## What this removes
The buyer does not need to design a first evaluation task from scratch. A small evaluation can start with explicit data boundaries, acceptance criteria, review evidence, and rollback from the first unit of work.

## Related public evidence
- [`ha125-ai-git-workflow-demo.md`](./ha125-ai-git-workflow-demo.md)
- [`ha125-evidence-pack.md`](./ha125-evidence-pack.md)
- [`ha125-fulfilment-starter-kit.md`](./ha125-fulfilment-starter-kit.md)
- [`ha125-verification-cases.md`](./ha125-verification-cases.md)
