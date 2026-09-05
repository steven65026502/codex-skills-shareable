---
name: paper-summarize
description: Fill per-paper Key Findings, Methodology, and Relevance sections in both Obsidian Markdown and Zotero notes after research-hub ingest. Use only for an existing configured cluster when the user requests per-paper summaries. Verify the CLI, model delegate, source abstract, and both write targets first; stop and report partial failures without claiming atomic success.
---

# Paper Summarize

Fill the existing per-paper summary sections created by research-hub. This is for cited papers in an existing cluster, not the user's manuscript and not a cluster-level brief.

## Prerequisites

Before any processing:

1. Run `research-hub doctor`.
2. Verify the requested cluster exists under the configured vault.
3. Verify the chosen `claude`, `codex`, or `gemini` CLI is callable if the installed research-hub version requires one.
4. Confirm each target note has a source abstract and, for dual writes, a Zotero item key.
5. Start with a dry run; `--apply` is required for writes.

If the CLI or configuration is absent, stop. Do not reconstruct research-hub's private cache or claim MCP tools that are not available.

## Scope

For each paper, produce only:

- `Key Findings`: three to five abstract-supported bullets;
- `Methodology`: one concise abstract-supported statement;
- `Relevance`: one or two sentences tied to the cluster topic.

Preserve existing anchors and unrelated note content. If the abstract is empty or too thin, mark the field `[PDF needed]` rather than inferring from the title or metadata.

## Commands

Inspect the installed command help before relying on flags:

```powershell
research-hub summarize --help
research-hub summarize --cluster <slug>
research-hub summarize --cluster <slug> --llm-cli codex --apply
```

Use `--no-zotero` or `--no-obsidian` only when the user explicitly accepts a one-sided update. The exact available flags and test locations belong to the installed research-hub version, not this standalone skill.

## Write contract

1. Validate the model response as structured data before any write.
2. Reject unknown paper slugs, empty required fields, and claims not traceable to the abstract.
3. Treat the Markdown and Zotero update as one transaction per paper.
4. After both writes, read both records back and confirm the anchors and sections match.
5. If the Zotero write fails, restore that paper's prior Markdown.
6. On any partial synchronization failure, stop the remaining batch and report papers already verified, rolled back, and not attempted. Do not blindly retry.

## Completion and failure

A paper counts as complete only when both requested targets are read back and match. A dry run is not an applied update. Report the cluster, model CLI, item counts, skipped papers, rollback results, and whether the run was dry or applied.

When a compatible research-hub source checkout is available, run its current summarize tests and targeted live dry run. Do not claim a fixed test count or bundled test coverage from this skill: those test files are not included here.
