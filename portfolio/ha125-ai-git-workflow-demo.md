# AI-assisted Git workflow — sanitized demonstration

Purpose: demonstrate a small, auditable workflow for using generative AI while keeping human review and Git rollback in the loop. This sample uses no employer, client, shipboard, or private information.

## Scenario
A fictional support team repeatedly turns rough meeting notes into a short operating checklist. The goal is to reduce drafting time without allowing AI output to bypass review.

## Workflow
1. **Input** — place only sanitized notes in `input/notes.md`; remove names, credentials, customer data, and confidential facts.
2. **AI draft** — ask an AI tool to return: `summary`, `open_questions`, and `checklist`. Require it to mark uncertain statements instead of inventing facts.
3. **Human review gate** — verify every factual claim against the input; reject unsupported additions; check that no sensitive data appears.
4. **Version control** — create a short-lived branch (`docs/<topic>`), commit the reviewed change with a descriptive message, and review the diff before merge.
5. **Release** — merge only the reviewed artifact. If a defect is found, revert the merge/commit rather than editing production history silently.

## Example prompt
```text
Transform the sanitized notes below into:
1. a 5-line maximum summary,
2. a list of unresolved questions,
3. a numbered operating checklist.
Do not add facts that are absent from the notes. Prefix uncertain items with "VERIFY:".
Return Markdown only.
```

## Example Git sequence
```bash
git switch -c docs/example-checklist
# review the AI-produced Markdown manually
git diff --check
git add docs/example-checklist.md
git commit -m "docs: add reviewed example checklist"
git diff main...HEAD
# merge only after human review
```

## Review checklist
- [ ] No secrets, credentials, personal data, employer/client data, or proprietary source material
- [ ] Every factual statement is supported by the sanitized input
- [ ] `VERIFY:` items are resolved or deliberately retained as open questions
- [ ] `git diff --check` passes
- [ ] Diff is reviewed before merge
- [ ] Rollback path is known (`git revert <commit>`)

## What this demonstrates
- Generative-AI use for bounded documentation/operations work
- Human verification instead of blind acceptance of AI output
- Basic branch/commit/diff/revert Git workflow
- A reversible operating rule suitable for team documentation

This is a deliberately small demonstration asset, not a claim of prior client work or employment experience.
