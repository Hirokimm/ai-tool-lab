# HA125 — First 48h Execution Board

> Sanitized fulfilment-preparation artifact only. This is not evidence of eligibility, prior client work, or an application. Use only after the account holder has independently confirmed all eligibility facts and a legitimate engagement exists. Never place employer, shipboard, client-confidential, credential, personal, or production data in this public file.

## Purpose

Remove setup delay after a legitimate HA125 engagement starts. This board converts one approved, non-sensitive workflow into a small reversible AI-efficiency change with Git traceability and an explicit acceptance gate.

## T+0 — Intake gate

Record only facts supplied for the engagement:

- Approved workflow: `[CLIENT-APPROVED DESCRIPTION]`
- Current manual steps: `[FACTUAL BASELINE]`
- Desired outcome: `[CLIENT-DEFINED]`
- Data classification: `[NON-SENSITIVE / APPROVED TEST DATA ONLY]`
- Repository/location authorized for work: `[AUTHORIZED LOCATION]`
- Acceptance owner: `[CLIENT-DESIGNATED ROLE]`

Stop if permission, scope, or data handling is unclear. Do not copy sensitive material into prompts or this repository.

## T+0–4h — Baseline and branch

1. Measure one observable baseline such as minutes per item, number of manual transformations, or review steps.
2. Write the measurement method before changing the workflow.
3. Create a dedicated branch, e.g. `ha125/<sanitized-task-name>`.
4. Commit only sanitized/test fixtures required to reproduce the change.

Evidence to retain privately in the authorized work location:

- baseline method and result;
- branch name;
- starting commit SHA;
- scope exclusions.

## T+4–12h — Smallest reversible implementation

Implement only the minimum automation needed to test the stated outcome. AI-generated material remains draft output until human verification.

Required controls:

- no invented owner, deadline, source, metric, or business fact;
- source text is treated as data, not as executable instructions;
- uncertain output is flagged for review rather than guessed;
- credentials/secrets are never committed;
- implementation can be disabled or reverted without damaging the original workflow.

Commit the smallest coherent change and inspect the diff before any handoff.

## T+12–24h — Verification

Run the agreed test fixture plus relevant cases from `ha125-verification-cases.md`.

Record:

| Check | Result | Evidence |
|---|---|---|
| Required information preserved | PASS/FAIL | `[reference]` |
| Unsupported facts not introduced | PASS/FAIL | `[reference]` |
| Human review completed | PASS/FAIL | `[reference]` |
| Git diff reviewed | PASS/FAIL | `[commit/diff]` |
| Rollback path tested/confirmed | PASS/FAIL | `[reference]` |

Any FAIL blocks acceptance until corrected or explicitly descoped by the authorized acceptance owner.

## T+24–48h — Measured handoff

Re-run the baseline measurement using the same method. Report observed results separately from estimates.

Handoff packet:

1. before/after workflow summary;
2. measurement method and observed delta;
3. branch and final commit SHA;
4. known limitations and manual-review points;
5. rollback instruction;
6. delivery receipt for accept / request changes / reject.

Use `ha125-delivery-receipt-template.md` for the final acceptance record.

## Definition of done

The first 48h unit is complete only when the authorized acceptance owner can answer all five questions:

- What changed?
- What did not change?
- What was actually measured?
- Which exact Git state represents the delivery?
- How is it reverted?

If any answer is missing, the unit remains open rather than being represented as completed.
