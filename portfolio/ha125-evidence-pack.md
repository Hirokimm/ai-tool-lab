# HA125 — marketplace-ready evidence pack

> Demonstration material only. This does **not** assert eligibility, prior client work, or employment experience. It contains no employer, shipboard, customer, credential, or private information.

## 30-second reviewer summary
I can demonstrate a bounded generative-AI workflow in which source material is sanitized first, AI output is constrained against unsupported facts, a human review gate is mandatory, and accepted changes are managed with Git branches, commits, diffs, and reversible rollback.

Primary sample: [`ha125-ai-git-workflow-demo.md`](./ha125-ai-git-workflow-demo.md)

## Evidence map

| Requested capability | Evidence in sample | Verifiable behavior |
|---|---|---|
| Generative-AI efficiency | Structured prompt turns sanitized notes into summary, open questions, and checklist | Output contract is explicit and bounded |
| Hallucination control | Prompt forbids unsupported facts and marks uncertainty with `VERIFY:` | Reviewer can compare every claim with source input |
| Human-in-the-loop | Human verification is required before merge | Unsupported additions are rejected before release |
| Git operation | Short-lived branch → commit → diff review → merge | `git diff --check` and `git diff main...HEAD` are shown |
| Safe rollback | Revert is specified instead of silently rewriting history | `git revert <commit>` provides a reversible path |
| Information hygiene | Sanitization occurs before AI use | Secrets, PII, employer/client and proprietary data are excluded |

## Minimal fulfilment SOP
1. Receive the task objective and explicitly permitted source material.
2. Remove or replace sensitive identifiers before any AI processing.
3. Define the output schema and acceptance criteria before prompting.
4. Generate a bounded draft; unsupported claims must be marked for verification.
5. Human-review the draft against the permitted source material.
6. Put the reviewed change on a task-specific Git branch.
7. Run `git diff --check`, inspect the complete diff, then commit with a descriptive message.
8. Deliver the reviewed artifact plus unresolved questions; merge only through the agreed review process.
9. If a released change is defective, use a traceable revert rather than hiding history.

## Evidence that can be supplied without private data
- Public Git commit history for this demonstration repository
- The sanitized workflow sample linked above
- A task-specific diff produced from fictional or buyer-provided non-confidential material
- A concise change log stating input scope, review performed, unresolved items, and rollback point

## Scope boundary
This package demonstrates process competence only. Any factual eligibility requirements for HA125 must be confirmed separately by the human applicant before submission. No application has been submitted by this artifact.
