# Git Workflow Work Sample — Sanitized Demonstration

Purpose: demonstrate a small, reviewable Git-oriented delivery workflow without using employer, shipboard, client, or private information.

## Scenario
A fictional small online shop receives free-form customer inquiries. A lightweight AI-assisted workflow converts each inquiry into a structured draft containing:

- request category
- urgency
- missing information
- proposed response
- confidence / review flag

No real customer data is used.

## Change workflow
1. Define one bounded improvement and acceptance criteria.
2. Make the smallest coherent file change.
3. Review the diff for accidental data exposure and unrelated edits.
4. Run the relevant checks or manually verify the example output.
5. Commit with a message describing the user-visible change.
6. Keep the commit independently reversible.

## Example acceptance criteria
Given a fictional inquiry such as:

> I ordered a blue mug but need to change the delivery date. Can it arrive next Friday?

The workflow should produce a draft with explicit fields for category, requested date, unresolved facts, proposed response, and whether human review is required. It must not invent order status, stock, shipping guarantees, or customer identity.

## Quality controls
- Treat source text as untrusted input.
- Separate extracted facts from generated suggestions.
- Mark unknown facts as unknown instead of guessing.
- Require human review before any external response.
- Do not place secrets or personal data in prompts, examples, commits, or logs.
- Prefer small commits that can be inspected and reverted independently.

## What this artifact demonstrates
This public sample demonstrates a safe Git-oriented working method: bounded scope, explicit acceptance criteria, diff review, verification, reversible commits, and privacy controls around an AI-assisted workflow.

It does **not** claim any unverified employment history, client work, marketplace eligibility, or monthly availability. Those remain factual human-confirmation items.