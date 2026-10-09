# HA125 — Delivery Receipt Template

> Demonstration/fulfilment artifact only. This template does **not** claim eligibility, prior client work, employment experience, or an application to HA125. Use only sanitized/client-approved information. Do not include employer, shipboard, private, credential, or unrelated confidential data.

## Purpose

A one-page receipt for a bounded generative-AI efficiency task managed with Git. It makes completion, review, acceptance, measurement, and rollback auditable without requiring a long handoff conversation.

## Delivery receipt

**Task ID:** `[client/project]-[YYYYMMDD]-[short-name]`  
**Scope agreed:** `[one bounded workflow/change]`  
**Out of scope:** `[explicit exclusions]`  
**Input classification:** `synthetic / public / client-approved sanitized`  
**Production credentials used:** `No` unless separately authorized by the client.

### 1. Baseline

- Previous process: `[brief description]`
- Baseline measure: `[e.g. minutes/item, steps/item, error count]`
- Measurement source: `[observed / client-provided]`
- Sample size: `[n]`

Never present an estimate as an observed result.

### 2. Change delivered

- AI-assisted step: `[what AI drafts/classifies/extracts]`
- Human-review gate: `[what must be checked before acceptance]`
- Files changed: `[paths]`
- Branch: `[branch]`
- Commit: `[commit SHA]`
- Diff reviewed: `Yes / No`
- Automated/manual checks: `[checks and result]`

### 3. Safety / factuality check

- Unsupported owners, dates, actions or facts introduced: `Yes / No`
- Allowed-source verification completed: `Yes / No / N/A`
- Prompt-injection-like source text treated as data, not instructions: `Yes / No / N/A`
- Confidential/private information added to repository: `Yes / No`

Any unsafe `Yes` above blocks acceptance until corrected.

### 4. Result

- Post-change measure: `[observed value]`
- Sample size: `[n]`
- Observed delta: `[baseline → result]`
- Known limitations: `[limitations]`
- Estimate/hypothesis, if any: `[clearly labelled; optional]`

### 5. Acceptance gate

Reviewer checks:

- [ ] Scope matches the agreed bounded task.
- [ ] Git diff is understandable and limited to the intended change.
- [ ] AI-produced factual content has passed the required human/source review.
- [ ] No prohibited/confidential information is present.
- [ ] Measurement is reproducible from the stated sample/source.
- [ ] Rollback path is known.

**Decision:** `ACCEPT / REQUEST CHANGES / REJECT`  
**Reviewer note:** `[optional]`  
**Accepted version/commit:** `[SHA or N/A]`

### 6. Rollback

- Rollback trigger: `[failure condition]`
- Rollback method: `[revert commit / restore prior file / disable workflow]`
- Known irreversible side effects: `None / [describe before execution]`

## Minimal handoff rule

A task is not marked complete merely because an AI output or code change exists. Completion requires: bounded scope, reviewable diff/artifact, checks recorded, observed-vs-estimated results separated, acceptance decision captured, and a rollback path where applicable.
