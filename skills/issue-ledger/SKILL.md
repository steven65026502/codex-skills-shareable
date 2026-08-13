---
name: issue-ledger
description: Maintain a layered issue ledger for coding, research, debugging, or project work. Use when the user asks Codex to record, organize, inspect, update, or summarize problems, solved items, unresolved issues, blockers, risks, evidence, decisions, verification results, or next steps across a project or repeated sessions.
---

# Issue Ledger

Maintain a project-local problem ledger that can be inspected from broad overview down to evidence-level detail.

## Core Idea

Use a layered structure:

1. **Layer 0: Snapshot** - one-screen current state.
2. **Layer 1: Index** - grouped issue list by status and area.
3. **Layer 2: Issue Cards** - stable IDs with symptoms, impact, owner/context, and next action.
4. **Layer 3: Evidence Trail** - commands, files, queries, logs, screenshots, or user confirmations that justify the status.
5. **Layer 4: Decision And Verification Log** - what changed, why it changed, and how it was checked.

The goal is not to write a diary. The goal is to make future retrieval easy: start from the snapshot, find an issue ID, then drill into evidence and decisions.

## File Location

Prefer a project-local file named:

```text
PROJECT_ISSUE_LEDGER.md
```

If the project already has a status, TODO, issue log, or project notes file, update that existing file instead of creating a duplicate. If no project workspace exists, ask where to store the ledger.

## Issue IDs

Assign stable IDs using an area prefix plus a three-digit number:

```text
DB-001
UI-001
PIPE-001
TEST-001
DOC-001
PERF-001
```

Choose prefixes from the project context. Reuse an existing issue ID when the new finding is the same underlying issue. Create a new ID only when the cause, affected area, or required action is materially different.

## Status Values

Use exactly these status values:

- `open`: known problem, not fixed yet.
- `in-progress`: actively being investigated or changed.
- `resolved`: fixed or confirmed no longer a problem.
- `blocked`: cannot proceed without missing input, permission, data, service, or decision.
- `watch`: not urgent, but worth monitoring.

Never mark an issue `resolved` without evidence such as a passing test, successful command, successful query, code inspection, screenshot, or explicit user confirmation.

## Update Workflow

When using this skill:

1. Find or create the ledger file.
2. Read the Snapshot and Index first.
3. Search for related issue IDs before creating new ones.
4. Add new findings as issue cards with clear evidence.
5. Move statuses only when the evidence supports the change.
6. Add a short entry to the Decision And Verification Log after meaningful progress.
7. In the final response, mention only the important ledger changes and unresolved next steps.

For coding tasks, update the ledger after investigation and again after verification if the issue status changed.

## Ledger Template

Use this structure when creating a new ledger:

```markdown
# Project Issue Ledger

Last updated: YYYY-MM-DD HH:mm TZ

## Layer 0: Snapshot

- Current focus:
- Open issues:
- In progress:
- Recently resolved:
- Main blocker:
- Recommended next step:

## Layer 1: Issue Index

| ID | Status | Area | Title | Last Evidence | Next Step |
| --- | --- | --- | --- | --- | --- |
| DB-001 | open | Database | Example issue | Query confirmed ... | Update SQL ... |

## Layer 2: Issue Cards

### DB-001 - Example Issue Title

- Status: open
- Area: Database
- First seen: YYYY-MM-DD
- Last updated: YYYY-MM-DD HH:mm TZ
- Symptom:
- Impact:
- Likely cause:
- Next action:

#### Evidence Trail

- YYYY-MM-DD HH:mm TZ - Observation, command, file reference, query result, or user confirmation.

#### Decision And Verification

- YYYY-MM-DD HH:mm TZ - Decision made, change applied, or verification result.

## Layer 3: Cross-Cutting Notes

- Assumptions:
- Risks:
- External dependencies:

## Layer 4: Session Change Log

- YYYY-MM-DD HH:mm TZ - Added DB-001, confirmed schema, left SQL ordering open.
```

## Retrieval Behavior

When the user asks "what problems do we still have?", "which ones are solved?", "database part?", "continue from last time", or similar:

1. Read Layer 0 and Layer 1.
2. Open only the relevant issue cards from Layer 2.
3. Report the current state in this order:
   - active focus
   - unresolved issues
   - resolved issues relevant to the request
   - blockers
   - recommended next action

Do not dump the entire ledger unless the user asks for the full file.

## Writing Style

Keep entries concise and evidence-based. Prefer specific references over vague notes:

- Good: `src/data_loader.py load_records() filters by date but not timestamp.`
- Good: `Database query returned multiple time slots for each forecast lead.`
- Avoid: `Database has problems.`

Use the user's language for titles and notes when practical. Preserve technical identifiers exactly.
