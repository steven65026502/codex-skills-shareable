# Maintainer Profile Format

Recommended root file name:

```text
.github-maintainer.yml
```

Recommended fields:

```yaml
default_branch: main
push_policy: direct-to-main-after-user-confirmation

protected_paths:
  - metadata.txt
  - __init__.py

docs:
  readme: README.md
  changelog: CHANGELOG.md
  docs_index: docs/README.md
  issue_ledger: docs/project/PROJECT_ISSUE_LEDGER.md
  file_guide: docs/project/REPOSITORY_FILE_GUIDE.md

generated_do_not_commit:
  - "*.h5"
  - "*.nc"
  - "*.dump"
  - "*.log"
  - "tmp*/"

cleanup_safe:
  - "__pycache__/"
  - "logs/"
  - "tmp*/"
  - "*.log"

verify:
  - "git diff --check"
```

Guidance:

- Keep project-specific facts in the profile, not in the generic skill.
- Use `protected_paths` for framework entry files that should not be moved casually.
- Use `generated_do_not_commit` for source-control hygiene.
- Use `cleanup_safe` only for files that can be regenerated or are clearly temporary.
- Use `verify` for cheap checks that should run before committing.
