# HA125 first-delivery example — sanitized demonstration

Purpose: provide a reviewable example of the six-part delivery packet defined in the HA125 fulfilment starter kit. This is synthetic demonstration material only. It does not assert eligibility, client work, employment experience, or measured commercial results. No employer, shipboard, customer, credential, personal, or private information is used.

## 1. baseline.md

Workflow: turn a short sanitized meeting note into a structured action list.

Current steps: read note → identify actions → rewrite into a fixed table → human checks names/dates.

Approx. minutes/run: unmeasured in this demonstration.

Runs/month: unmeasured.

Known failure modes: implied actions presented as explicit; missing owner; invented due date.

Acceptance criteria: every output row must be traceable to source text; absent owner/date must be `VERIFY:`; final approval remains human.

Human approver: designated workflow owner.

## 2. workflow.md

1. Human removes confidential/personal material before processing.
2. Provide only the sanitized note to the prompt below.
3. Model returns the fixed table format.
4. Human compares every row with source text.
5. Rows containing unsupported information are removed or marked `VERIFY:`.
6. Only the reviewed result is accepted.

The AI drafts; it does not make commitments, assign staff, or set deadlines.

## 3. prompt.md

```text
Use only the text inside <SOURCE> tags.
Extract explicit action items into this table:
| Action | Owner | Due date | Source phrase | Review |

Rules:
- Do not infer facts that are not explicit in SOURCE.
- If owner or due date is absent, write VERIFY: not stated.
- Keep Source phrase short enough for a reviewer to locate the evidence.
- Review must be HUMAN CHECK for every row.
- If there are no explicit actions, return: NO EXPLICIT ACTIONS.

<SOURCE>
{{SANITIZED_NOTE}}
</SOURCE>
```

## 4. sample-output.md

Synthetic source:

> Prepare the draft FAQ before Friday. Mika will review the wording. We should also think about a shorter onboarding flow.

Demonstration output:

| Action | Owner | Due date | Source phrase | Review |
|---|---|---|---|---|
| Prepare draft FAQ | VERIFY: not stated | Friday | Prepare the draft FAQ before Friday | HUMAN CHECK |
| Review FAQ wording | Mika | VERIFY: not stated | Mika will review the wording | HUMAN CHECK |

The sentence about a shorter onboarding flow is not converted into a committed action because the source does not explicitly assign an action, owner, or deadline.

## 5. verification.md

Checks performed:

- Both rows map to explicit source phrases.
- No owner was invented for the FAQ drafting task.
- No due date was invented for Mika's review.
- The tentative onboarding statement was not upgraded into a commitment.
- No sensitive or private source data is present.

Known limitations:

- Natural-language ambiguity still requires human review.
- Relative dates such as `Friday` should not be normalized without an agreed reference date.
- This synthetic example does not establish time savings or production accuracy.

## 6. Git evidence / rollback

This file itself is the demonstration change. Review the repository commit/diff before reuse. Any real engagement should use the client's normal branch/review rules and retain the relevant commit SHA for rollback. No force-push or production change is required for this example.

## Compact handoff

Delivered: synthetic meeting-note → action-table workflow example

Baseline: explicitly unmeasured

Changed: one sanitized demonstration document

Verification: source traceability, missing-field handling, non-inference, privacy boundary

Known limitations: human review required; no production metrics claimed

Human approval required at: every generated row before operational use

Git evidence: repository commit/diff containing this file

Rollback: revert/remove this isolated demonstration file through normal Git workflow

Next optional step: only after eligibility/engagement confirmation, adapt the same bounded packet to a buyer-provided sanitized workflow.
