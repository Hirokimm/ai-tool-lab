# Delivery Partner Runbook — ¥49,000 Automation Pilot

This is the reusable operating contract for an approved implementation partner delivering one bounded Automation Pilot. It is designed to make fulfillment transferable without exposing buyer secrets or creating open-ended support obligations.

## Commercial unit

Buyer-facing pilot price: **¥49,000 fixed**.

Partner compensation is **not automatic** and must be agreed in writing for the specific job before any work begins. This page does not promise work, payment, volume, exclusivity, or reimbursement.

## What one pilot means

One pilot = one clearly defined repetitive digital workflow, one measurable before/after metric, one safe test dataset, one acceptance check, and one correction pass for defects inside the agreed scope.

Do not expand scope informally. New workflows, new integrations, production deployment, ongoing maintenance, extra revisions, or materially changed requirements require a separate agreement.

## Handoff packet required before work starts

A delivery partner should receive only the minimum safe packet needed to build the pilot:

1. generic workflow description;
2. runs per month;
3. current minutes per run;
4. target minutes per run;
5. testable output specification;
6. synthetic, public, or explicitly non-confidential test inputs;
7. acceptance criterion;
8. agreed delivery format and deadline;
9. written commercial terms for that specific job.

If any required item is missing, do not improvise against private or production systems. Return the missing-item list instead.

## Delivery sequence

1. Reproduce the manual baseline using the safe test example.
2. Build the smallest automation that satisfies the agreed output specification.
3. Keep configuration portable and dependencies documented.
4. Run the agreed acceptance check.
5. Deliver the runnable automation/configuration plus a short operating note.
6. If the delivered result fails the agreed criterion because of an in-scope defect, perform one correction pass.
7. Record the before/after result using the agreed metric.

## Definition of done

A pilot is complete when all of the following are true:

- the agreed safe test input can be processed;
- the agreed output is produced;
- the acceptance criterion can be checked by the buyer;
- the runnable artifact/configuration has been handed over;
- a short operating note states how to run it and any material limitations;
- the before/after metric has been recorded;
- any one included in-scope defect correction has been completed or is not needed.

## Hard safety boundary

Do not request, receive, store, copy, or publish passwords, API keys, production credentials, personal data, employer/customer confidential information, proprietary documents, private URLs, or regulated/high-risk decision data through public GitHub surfaces.

Do not use employer systems, customer systems, vessel/operational information, or other third-party confidential material. Do not perform unauthorized access, scraping, circumvention, or production changes.

If a real deployment later requires sensitive access, that is outside this public pilot workflow and requires a separate private agreement and appropriate controls.

## IP and reuse boundary

Do not assume ownership of buyer-provided material. Do not publish buyer-specific inputs or outputs. Generic implementation patterns, checklists, and non-confidential reusable components may only be reused where doing so does not disclose buyer information or violate an agreed term.

## Escalate instead of guessing

Stop the job and request a scope decision if:

- requirements conflict with the agreed acceptance criterion;
- the workflow needs sensitive/production access;
- a new paid service or other cash spend is required;
- the requested change adds another workflow/integration;
- legal, privacy, security, employment, or reputational risk becomes material;
- the acceptance criterion cannot be tested with the agreed safe data.

## Partner application

Implementation partners can introduce themselves through the public partner intake:

https://github.com/Hirokimm/ai-tool-lab/issues/10

Do not post confidential client information there. Actual assignment and compensation require a separate case-specific agreement before work starts.
