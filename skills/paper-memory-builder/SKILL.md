---
name: paper-memory-builder
description: Convert the user's manuscript draft, figures, and available Zotero metadata into .paper/claims.yml and .paper/figures.yml for later writing and audit work. Use when the user explicitly asks to build paper memory or extract claims. Do not edit the manuscript, invent missing evidence, or use this for cited-paper cluster summaries.
---

# paper-memory-builder

Bridge between research-hub and `academic-writing-skills`. Reads a
manuscript draft (Word, LaTeX, Markdown, Obsidian paper folder) plus the
figures it references, and writes structured `.paper/claims.yml` +
`.paper/figures.yml` so the writing skill can reason about the paper
without parsing the manuscript on every call.

This skill **does not edit the manuscript itself**. That's the writing
skill's job. We just produce the memory layer it consumes.

## When to use

Trigger phrases:

- "Build paper memory for this manuscript."
- "Extract claims, figures, and evidence from this paper folder."
- "Prepare reusable memory for writing and revision."
- "I'm starting a rebuttal — give me the claims layer first."

Not for:

- Writing the rebuttal itself — `academic-writing-skills`.
- Building the orientation memo — `research-project-orienter`.
- Comparing papers — `literature-triage-matrix`.
- Verifying a NotebookLM brief — `notebooklm-brief-verifier`.

## Inputs

In priority order:

1. **`.paper/` existing files** — if `claims.yml` already exists, parse
   it; this run should refresh, not replace human edits.
2. **The manuscript file** — usually one of:
   - `paper/manuscript.docx` / `manuscript.tex` / `manuscript.md`
   - Obsidian paper note under `raw/<paper-cluster>/manuscript.md`
   - Word/LaTeX in a sibling repo specified by the user
3. **Figure files** under `figures/` or `outputs/figures/` — read
   filenames + captions; don't OCR images.
4. **`.research/project_manifest.yml`** — for project context (research
   question, datasets, current_stage). Use to anchor claims in the
   project's overall question.
5. **`.research/literature_matrix.md`** — for citation key lookup if the
   manuscript references "Smith 2024" but you need to disambiguate.

## Outputs

Write to `<project-root>/.paper/`:

- `claims.yml` — every paper-level claim, with evidence pointers + status. Schema: `references/yaml-schemas.md`.
- `figures.yml` — every figure inventory, with key numbers + supported claims. Schema: `references/yaml-schemas.md`.
- `revision_history.yml` — append-only log of revision rounds. Schema + append-vs-overwrite rules: `references/revision_history_schema.md`.

Do **not** touch `journal_format.md`, `reviewer_comments.md`, or `style_overrides.md` — those belong to `academic-writing-skills`.

## Token-saving behavior

- Read manuscript ONCE per session, extract claims + figures, then
  reference `.paper/*.yml` in subsequent writing turns.
- Pass-through claim text exactly as in the manuscript; do not rephrase.
  The writing skill will polish later.
- For figures, read just the caption + filename; don't OCR or describe
  visual content.
- After running, hand off cleanly: tell the user "claims.yml and
  figures.yml ready. Load `academic-writing-skills` next for any
  writing/revision/audit pass."

## Output format for the user

```
[paper-memory-builder]
  Read manuscript: paper/manuscript.docx (8 pages, 12 figures)
  Wrote: .paper/claims.yml (9 claims; 2 marked at risk)
  Wrote: .paper/figures.yml (12 figures; 8 mapped to claims, 4 are context)
  Suggested next: load academic-writing-skills for revision/audit passes.
```

## What NOT to do

- Don't edit the manuscript file. Read-only.
- Don't paraphrase claim text. Copy exactly from the manuscript.
- Don't fabricate figures or claims that aren't in the source.
- Don't write to `.paper/journal_format.md`, `reviewer_comments.md`, or
  `style_overrides.md`. Those are owned by `academic-writing-skills`.
- Don't write to `.research/` — that's the workspace layer, not the
  paper layer.
- Don't extract claims from cited works — only from THIS paper.

## Completion and failure handling

Before completion, parse every YAML output and validate it against `references/yaml-schemas.md` and `references/revision_history_schema.md`. Claim and figure IDs must be unique; evidence and figure paths must either exist or be explicitly marked unresolved. Compare the manuscript's figure references with `figures.yml` and report count mismatches. Preserve existing human-edited records by stable ID and inspect the diff to confirm that the manuscript and `.research/` were not changed.

If the manuscript cannot be read, a schema is missing, YAML is invalid, or source attribution is ambiguous, do not publish partial files as complete. Leave prior valid files in place, write no invented placeholders, and report the exact source or record that blocked completion. If only one output validates, keep it as a labeled partial artifact only when doing so cannot overwrite a previous valid file.

## See also

- `references/yaml-schemas.md` — `.paper/claims.yml` and `.paper/figures.yml` schemas
- `references/revision_history_schema.md` — `.paper/revision_history.yml` schema + append-only audit-trail rules
