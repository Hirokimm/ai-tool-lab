# AI Workflow Demo — Sanitized Portfolio Sample

Purpose: demonstrate a reproducible generative-AI work-efficiency workflow without employer, shipboard, client, or private information.

## Scenario
A fictional small online shop receives a mixed inbox of product questions, delivery questions, refund requests, and irrelevant messages. The operator needs a fast, auditable triage workflow.

## Workflow
1. Intake: copy only non-sensitive message text into a local working set.
2. Classify with a fixed schema: `category`, `urgency`, `needs_human`, `draft_reply`, `reason`.
3. Require the model to return structured JSON and forbid invented order facts, dates, prices, or policies.
4. Validate output: reject malformed JSON; route any uncertain or refund/payment case to human review.
5. Generate a concise reply draft only for low-risk FAQ cases.
6. Record input ID, model result, validation result, and final human decision for later evaluation.

## Example prompt contract
```text
Classify the customer message using only the supplied text and policy excerpt.
Return JSON with: category, urgency, needs_human, draft_reply, reason.
Never invent order status, delivery dates, prices, refunds, or policy terms.
If required information is missing, set needs_human=true.
```

## Example input
```text
Message ID: demo-003
Message: "Can I change the delivery address after ordering?"
Policy excerpt: "Address changes require staff confirmation before dispatch."
```

## Expected output
```json
{
  "category": "delivery_change",
  "urgency": "normal",
  "needs_human": true,
  "draft_reply": "Address changes require staff confirmation before dispatch. I’ll route this for confirmation.",
  "reason": "The policy explicitly requires staff confirmation."
}
```

## Git-based operating pattern
- Keep prompts, schemas, and test cases as version-controlled text files.
- Make one scoped change per branch.
- Review the diff before merge.
- Add regression cases whenever a failure mode is found.
- Keep secrets, personal data, production exports, and employer/client material out of the repository.

## Evaluation
A small test set can measure: schema-valid rate, correct escalation rate, unsupported-claim rate, and human edit rate. A change is accepted only when it does not increase unsupported claims and does not reduce required escalation.

## What this demonstrates
Prompt specification, structured-output design, hallucination controls, human-in-the-loop routing, measurable evaluation, and a Git-friendly improvement loop. The scenario and all sample data are fictional.