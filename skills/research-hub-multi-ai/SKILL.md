---
name: research-hub-multi-ai
description: Write .coord/multi_ai_plan.md for a user-requested workflow involving two or more available AI delegates. Use only when the user explicitly requests delegation or multi-agent coordination. Verify each delegate actually exists before naming it; do not require this router for a single-agent task and do not claim execution from a plan alone.
---

# Research Hub Multi-AI Router

Create a coordination artifact only when the user explicitly requests two or more delegates. The plan separates independent work, dependencies, evidence, and reconciliation; it does not execute the tasks by itself.

## Prerequisites

- Confirm the current host permits delegation and list the actually callable agents or model CLIs.
- Run `research-hub doctor` only if a planned task will invoke the research-hub CLI.
- Do not name unavailable leaf skills, tools, models, or commands.
- If only one agent is needed, skip this skill and run that task directly.

Astra, Sol, Luna, Codex, Gemini, or another delegate must be assigned by demonstrated capability and current availability, not stereotypes or untested performance claims. Keep critical safety and verification instructions in every task brief regardless of model.

## Output

Write `.coord/multi_ai_plan.md` and one brief per task. Use `references/multi_ai_plan_template.md` for the schema. Each task needs:

- stable ID and exact deliverable;
- assigned available delegate;
- dependency list;
- allowed files and prohibited actions;
- observable success criteria and verification command;
- failure artifact or status;
- reconciliation owner.

If an active plan exists, preserve it and write a new plan-specific filename unless the user explicitly asked to update it.

## Planning rules

- Use at least two genuinely independent or sequentially necessary tasks; do not create ceremony by splitting one small task.
- Avoid concurrent writes to the same files.
- Give weaker or faster delegates enough local context and explicit checks; do not delete rules merely because one stronger model may infer them.
- Keep credentials, destructive actions, publishing, and external messages under the same authorization limits as the parent request.
- A delegate result is evidence to reconcile, not automatic acceptance.

## Completion and failure

Planning completes only when every named delegate and command was checked, all brief paths exist, and success criteria can be evaluated. Execution completes only after the reconciler verifies each result against the plan. If a delegate is missing or fails, mark that task blocked or reassign it explicitly; never silently claim the overall goal is complete.
