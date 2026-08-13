# Obsidian Backup Policy

## Include

- Markdown notes.
- Attachments such as images, PDFs, PPTX, HTML exports, and project assets.
- Obsidian configuration files that do not contain credentials.
- Project folders and source notes inside the vault.

## Exclude

- `.git/`
- `.obsidian/plugins/obsidian-local-rest-api/data.json`
- `Thumbs.db`
- `Desktop.ini`
- `.DS_Store`
- `.trash/`
- `*.tmp`
- `*.temp`

## Why Local REST API Data Is Excluded

The Obsidian Local REST API `data.json` file can contain:

- API key
- certificate
- RSA private key

Do not commit it even to a private GitHub repository. The local plugin can regenerate or manage this file locally.

## Privacy

The target GitHub repository must be private. If the repo cannot be verified as private, stop and report the blocker.
