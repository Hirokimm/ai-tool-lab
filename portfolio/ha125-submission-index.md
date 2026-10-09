# HA125 — Submission Evidence Index

> Demonstration package only. This page does **not** claim eligibility, prior client work, employment experience, or an application to HA125. All examples are synthetic/sanitized and contain no employer, shipboard, client, or private information.

## Purpose

A single reviewer entry point for the HA125 demonstration package. It reduces review friction by mapping each relevant capability to a concrete artifact and a bounded verification path.

## 60-second review path

1. **AI + Git workflow demo** — inspect the end-to-end workflow: sanitized input → AI draft → human review → branch/commit/diff → merge/revert.
   - `ha125-ai-git-workflow-demo.md`
2. **Verification cases** — inspect explicit pass/fail tests for unsupported facts, missing owners/deadlines, no-action inputs, preservation of explicit information, and prompt-injection-like source text.
   - `ha125-verification-cases.md`
3. **Fulfilment starter kit** — inspect the bounded intake, baseline, information-hygiene, delivery, acceptance, measurement, and rollback process.
   - `ha125-fulfilment-starter-kit.md`
4. **Bounded trial protocol** — inspect a small first engagement that can be evaluated before broader access or scope is granted.
   - `ha125-bounded-trial-protocol.md`
5. **Evidence pack** — inspect the capability-to-evidence mapping.
   - `ha125-evidence-pack.md`

## Capability → evidence

| Capability to evaluate | Evidence | What to verify |
|---|---|---|
| Generative-AI workflow design | AI + Git workflow demo | Inputs are sanitized; AI output is treated as a draft; human review is explicit |
| Hallucination / unsupported-fact control | Verification cases | Pass/fail cases reject invented owners, dates, actions, or unsupported claims |
| Git-safe change management | AI + Git workflow demo | Branch/commit/diff/check/revert path is explicit |
| Reversible delivery | Fulfilment starter kit + bounded trial | Acceptance and rollback gates exist before broader deployment |
| Measurement discipline | Fulfilment starter kit | Baseline and observed results are separated from estimates |
| Information hygiene | All artifacts | Synthetic/sanitized inputs only; no confidential operational data |

## Suggested reviewer acceptance gate

The demonstration is suitable to proceed to a bounded trial only if the reviewer can answer **yes** to all of these:

- Can the proposed workflow be tested without production credentials or confidential data?
- Is every AI-produced factual claim reviewable against an allowed source?
- Can the change be inspected as a Git diff before acceptance?
- Is rollback defined before deployment or handoff?
- Are observed measurements distinguished from estimates?

If any answer is **no**, stop and narrow the scope before proceeding.

## Scope boundary

This package demonstrates a method and review discipline. It intentionally does not assert that the author satisfies any platform-specific eligibility condition. Eligibility and application status must be confirmed separately by the human account holder before any submission.
