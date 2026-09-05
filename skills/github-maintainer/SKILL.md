---
name: github-maintainer
description: Maintain GitHub repositories with an industry-style workflow. Use when Codex is asked to organize a repository, clean GitHub structure, update README/CHANGELOG/docs, apply a project-specific maintainer profile, inspect git status before committing, avoid committing secrets or large generated files, write professional commit messages, push confirmed changes, or prepare repository handoff documentation.
---

# GitHub Maintainer

Use this skill for repository maintenance work where the goal is a clean, explainable GitHub history rather than only making code changes.

## Choose the smallest path

- Quick edit: for one README link, typo, badge, or small metadata change, read the target file plus applicable project instructions, inspect `git status -sb`, make the edit, run `git diff --check`, and verify only affected links. Do not require the full maintenance workflow.
- Full maintenance: use the workflow below for repository reorganization, broad documentation changes, cleanup, release preparation, or handoff work.
- Audit only: inspect and report; do not edit, delete, commit, push, or open a PR unless the user requested those actions.

## Core Workflow

1. Read project context.
   - Start with `README.md`, `CHANGELOG.md`, `docs/README.md`, and any maintainer profile such as `.github-maintainer.yml`.
   - If a project has `docs/project/REPOSITORY_FILE_GUIDE.md`, use it as the file-responsibility map.
   - If a project has `docs/project/PROJECT_ISSUE_LEDGER.md`, update it for meaningful decisions and verification.

2. Inspect repository state before editing.
   - Run `git status -sb`.
   - Run `git branch --show-current`.
   - Run `git ls-files` or `rg --files` when reviewing structure.
   - Preview ignored/untracked clutter with `git status --short --ignored -uall` or `git clean -ndX`; do not blindly clean source-like files.

3. Apply the project profile.
   - If `.github-maintainer.yml` exists, follow its branch, protected paths, documentation paths, generated-file rules, and verification commands.
   - If no profile exists, infer a conservative profile from README, docs, `.gitignore`, and repository layout.

4. Keep repository structure boring and predictable.
   - Keep runtime entry files where the framework expects them.
   - Move explanatory material into `docs/`.
   - Move dependency lists into `requirements/` or the ecosystem-standard location.
   - Move operational scripts into `scripts/` unless the framework requires them elsewhere.
   - Do not move files just to make the tree look neat if that breaks local tooling.

5. Update documentation with impact, not just file names.
   - Update `README.md` when project purpose, entry points, setup, or reader flow changes.
   - Update `CHANGELOG.md` for user-visible or collaborator-visible changes.
   - Update `docs/README.md` when documentation navigation changes.
   - Update project guides when file responsibilities, API contracts, deployment steps, or data contracts change.

6. Verify before commit.
   - Run relevant compile/tests from the profile.
   - Run `git diff --check`.
   - For Markdown navigation changes, verify relative links exist.
   - For cleanup, verify `git status -sb` and report what was deleted or intentionally kept.

7. Commit professionally.
   - Use an imperative subject line, e.g. `Organize repository documentation structure`.
   - Body should say what changed, why, and the impact/scope.
   - Avoid vague subjects like `update files`, `fix`, or `cleanup`.

8. Push only according to user/project policy.
   - Prefer the default branch only when the user or profile explicitly says direct updates are expected.
   - Otherwise use a branch/PR workflow.

## Cleanup Rules

Treat these as usually safe to delete after workspace-bound path verification:

- `__pycache__/`, `.pytest_cache/`, build caches.
- `*.log`, error logs, temporary command output.
- `tmp*`, `tmp_*`, preview images, generated reports.
- Large demo datasets when they are ignored and not part of source control.

Do not automatically delete these without clear evidence:

- Source-like scripts, even when ignored.
- Research pipeline files.
- Hand-authored notes or thesis documents.
- Local handoff bundles unless the user confirms they exist elsewhere.
- Any file outside the current workspace.

On Windows, before recursive deletion, resolve absolute paths and confirm they remain inside the intended workspace. Use PowerShell `Remove-Item -LiteralPath` rather than string-built shell deletion.

## Project Profile

Prefer a root `.github-maintainer.yml` for project-specific policy. See `references/profile-format.md` for the expected fields.

If the profile conflicts with a direct user instruction, follow the newest user instruction, then update the profile or notes only when the change is meant to persist.

## Optional Helper

Use `scripts/check_repo_hygiene.py` when a quick repository hygiene report is useful. It prints the current branch, status, ignored/untracked summary, staged large files, and possible staged secret patterns.
