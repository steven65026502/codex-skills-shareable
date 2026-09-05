---
name: ui-ux-pro-max
description: Search the bundled UI/UX knowledge base for evidence-based style, color, typography, accessibility, chart, and stack-specific implementation guidance. Use when a web or mobile design decision or UI audit benefits from structured recommendations. Do not use for ordinary code changes that need no design judgment.
license: MIT
metadata:
  source_repository: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
  source_commit: f3ac195224eac1eb0dfe1a3059c2a6add78ffbe3
---

# UI/UX Pro Max

Use the bundled search tool as a decision aid. It supplies structured options and implementation guidance; project requirements, existing design systems, accessibility needs, and user instructions remain authoritative.

## Use when

- choosing a visual direction, palette, type pairing, chart, or interaction pattern;
- reviewing a web or mobile interface for UX or accessibility issues;
- requesting stack-specific implementation guidance;
- generating a project design-system recommendation on explicit request.

Do not invoke it for a routine code change with no design decision. Use `frontend-skill` for art direction, `ui-styling` for shadcn/Tailwind implementation, and `design-system` for token architecture.

## Search

From this skill directory:

```powershell
python -X utf8 scripts/search.py "fintech dashboard" --domain product --max-results 5
python -X utf8 scripts/search.py "keyboard focus dialog" --domain ux --json
python -X utf8 scripts/search.py "data table" --stack react --max-results 5
```

Use `--help` to inspect the installed options. Prefer one focused query first; expand domains only when the first result is insufficient.

For an explicitly requested design-system recommendation:

```powershell
python -X utf8 scripts/search.py "healthcare portal" --design-system --project-name "Portal" --format markdown
```

Do not use `--persist` unless the user asked to write design-system files. When persisting, pass `--output-dir` as the verified project root and inspect existing files before using `--force`.

The full upstream workflow and domain catalogue are preserved in `references/full-guide.md`.

## Applying results

1. State the product context, audience, platform, stack, and constraints.
2. Search only the relevant domain or stack.
3. Reconcile results with the repository's existing tokens and components.
4. Implement only the requested scope.
5. Verify responsive behavior, keyboard/focus behavior, contrast, and critical states in proportion to the change.

Search results are guidance, not proof that a design is usable. Avoid quoting database counts as quality claims.

## Completion and failure

- Report the query or domain used when recommendations materially influenced the output.
- For code changes, run the project's own tests plus targeted UI checks.
- If the script, data, Python, or requested stack is unavailable, report the missing prerequisite and continue only with clearly labeled general guidance.
- Do not claim accessibility, visual fidelity, or performance improvements without the corresponding check.
