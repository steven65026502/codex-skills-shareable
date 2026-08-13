# Prompt for the recipient's Codex

Copy the text below into Codex on the recipient's computer:

```text
I received a sanitized Codex Agent Skills bundle for Windows. Locate the extracted bundle or ask me for its path, then read README.md, THIRD_PARTY_NOTICE.md, inventory/SKILLS.md, inventory/VALIDATION.md, and mcp/config.example.toml.

First inspect the current environment and preserve all existing data. Do not overwrite existing skills or ~/.codex/config.toml. Run installers/install-skills.ps1 with -WhatIf, show me the resolved source and target, then install only after the preview is safe. The default target is %USERPROFILE%\.agents\skills.

After installation, verify that 41 skill directories are present and that issue-ledger, github-maintainer, and obsidian-github-backup each contain SKILL.md. Restart Codex if needed and verify with /skills.

Treat MCP and plugins as a separate stage. Do not copy placeholders into live configuration as if they were credentials. Back up any existing ~/.codex/config.toml before merging selected MCP sections. Ask me locally for my own Obsidian vault path, API key, base URL, GitHub owner/repository, and OAuth sign-ins. Never print secrets in chat or command output.

Do not install plugin-cache copies. Reinstall Cowart, GitHub, Gmail, Canva, and OpenAI Templates from their supported plugin sources when I request them. Report what succeeded, what was skipped because it already existed, and what still needs my login or credentials.
```
