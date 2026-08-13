---
name: obsidian-github-backup
description: Back up a local Obsidian vault to a private GitHub repository with safety checks. Use when the user asks to upload, sync, commit, push, or back up Obsidian notes or a vault to GitHub, especially when the backup must stay private and avoid committing API keys, private keys, local REST credentials, or other secrets.
---

# Obsidian GitHub Backup

Use this skill to back up an Obsidian vault to GitHub as a private repository.

## Required Inputs

- Vault path: obtain the actual path from the user; never guess a username or vault name.
- GitHub repository: require `owner/repository` from the user.
- Branch: default to `main` unless the existing repository uses another branch.
- Required privacy: private.
- Known sensitive file to exclude: `.obsidian/plugins/obsidian-local-rest-api/data.json`.

## Workflow

1. Inspect the vault.
   - Confirm the vault path exists.
   - Check total file count and size.
   - Check whether the vault already has `.git/`.

2. Protect secrets before staging.
   - Ensure `.gitignore` excludes `.obsidian/plugins/obsidian-local-rest-api/data.json`.
   - Do not remove the local file; just prevent it from being tracked.
   - Scan staged contents for private-key patterns before commit.

3. Confirm GitHub privacy.
   - Use Git Credential Manager when available.
   - Create the backup repo if missing.
   - If the repo exists but is public, switch it to private before pushing.

4. Commit and push.
   - Use `main`.
   - Commit only when there are changes.
   - Use a precise commit message such as `Back up Obsidian vault YYYY-MM-DD HH:mm`.

5. Report clearly.
   - Repo full name and visibility.
   - Commit SHA or "no changes".
   - Files tracked and excluded.
   - Any warnings, especially files intentionally excluded.

## Recommended Command

Run the bundled script with explicit vault and repository parameters:

```powershell
$script = Join-Path $env:USERPROFILE ".agents\skills\obsidian-github-backup\scripts\backup_obsidian_to_github.ps1"
powershell -ExecutionPolicy Bypass -File $script `
  -VaultPath "<FULL_PATH_TO_VAULT>" `
  -RepositoryFullName "<OWNER>/<PRIVATE_REPOSITORY>"
```

Do not run the script while placeholders remain. Confirm both resolved values with the user first.

## Policy Notes

Read `references/default-policy.md` if you need the exact include/exclude policy or need to explain why a file was excluded.
