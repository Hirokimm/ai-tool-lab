# HA125 — Pre-work Sanitization Gate

> Demonstration/process asset only. This does **not** assert eligibility, employment history, client work, or an application to any marketplace job.

## Purpose

A reusable gate to prevent confidential, employer, shipboard, client, credential, or personally identifying information from entering an AI-assisted workflow or public Git history.

## Gate: run before AI processing or `git add`

### 1. Source permission
- [ ] I am authorized to use the source material for this task.
- [ ] The task does not require employer/shipboard/private information.
- [ ] If permission is uncertain, STOP and request a synthetic or explicitly approved substitute.

### 2. Remove direct identifiers
Replace with neutral tokens before processing:
- Person names → `[PERSON_A]`
- Company/client names → `[ORG_A]`
- Email/phone/address/account IDs → `[CONTACT_OR_ID]`
- Internal project/system names → `[PROJECT_A]`
- Exact operational locations/assets → `[LOCATION_A]` / `[ASSET_A]`

### 3. Remove secrets and access material
Do not place in prompts, examples, commits, issues, or logs:
- passwords / API keys / tokens
- cookies / session data
- private URLs containing credentials
- private keys / certificates
- `.env` contents

If any appears, STOP. Revoke/rotate through the authorized owner where applicable; do not merely redact a committed secret and assume it is safe.

### 4. Remove sensitive operational context
- [ ] No proprietary procedures, internal incidents, non-public performance data, private correspondence, customer records, or confidential technical/operational details.
- [ ] Dates, quantities, filenames, screenshots and metadata cannot reconstruct the sensitive source.

### 5. Synthetic substitution
When demonstrating capability, prefer a fabricated example that preserves only the workflow shape.

Example safe input:

```text
Meeting: Project Atlas weekly sync
Decision: use CSV import for the pilot.
Action: [PERSON_A] drafts validation rules by Friday.
Open question: retention period requires owner confirmation.
```

### 6. Pre-commit check
Before `git add`:

```bash
git status --short
git diff -- . ':!*.lock'
```

Check filenames and diff for identifiers/secrets as well as file contents. Then stage only intended files:

```bash
git add -- <explicit-path>
git diff --cached --check
git diff --cached
```

### 7. Release decision
PASS only when all are true:
- authorized source or synthetic source;
- no secrets;
- no employer/shipboard/client/private information;
- no unnecessary identifiers;
- staged diff manually reviewed;
- output can be understood without reconstructing the original sensitive material.

Otherwise: **DO NOT PROCESS / DO NOT COMMIT / DO NOT PUBLISH.**

## Minimal audit receipt

```text
Source class: synthetic / explicitly approved
Direct identifiers removed: yes/no
Secrets detected: yes/no
Operational/private context removed: yes/no
Staged diff reviewed: yes/no
Gate result: PASS/STOP
Reviewer: __________
Date: __________
```

This gate is intentionally conservative and reversible: rejected material remains outside the AI/Git workflow rather than being cleaned up after publication.
