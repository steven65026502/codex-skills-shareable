#!/usr/bin/env python3
"""Print a lightweight GitHub maintenance hygiene report for a repository."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
from pathlib import Path


SECRET_RE = re.compile(
    r"(password|passwd|secret|token|api[_-]?key|private[_-]?key|PGPASSWORD)",
    re.IGNORECASE,
)


def run_git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return result.stdout.strip()


def staged_files(repo: Path) -> list[str]:
    output = run_git(repo, "diff", "--cached", "--name-only")
    return [line for line in output.splitlines() if line.strip()]


def file_size(repo: Path, rel: str) -> int:
    path = repo / rel
    try:
        return path.stat().st_size
    except OSError:
        return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Repository root.")
    parser.add_argument(
        "--large-mb",
        type=float,
        default=5.0,
        help="Warn for staged files larger than this many MB.",
    )
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    print(f"Repository: {repo}")
    print(f"Branch: {run_git(repo, 'branch', '--show-current') or '(detached)'}")
    print("")

    print("Status:")
    print(run_git(repo, "status", "-sb") or "(clean)")
    print("")

    staged = staged_files(repo)
    if staged:
        print("Staged files:")
        for rel in staged:
            size_mb = file_size(repo, rel) / (1024 * 1024)
            marker = "  LARGE" if size_mb > args.large_mb else ""
            print(f"- {rel} ({size_mb:.2f} MB){marker}")
        print("")

        print("Potential staged secret-related paths:")
        hits = [rel for rel in staged if SECRET_RE.search(rel)]
        if hits:
            for rel in hits:
                print(f"- {rel}")
        else:
            print("(none by path scan)")
        print("")
    else:
        print("Staged files: none")
        print("")

    ignored = run_git(repo, "status", "--short", "--ignored", "-uall")
    ignored_lines = [line for line in ignored.splitlines() if line.startswith("!! ")]
    print(f"Ignored/untracked ignored entries: {len(ignored_lines)}")
    for line in ignored_lines[:30]:
        print(line)
    if len(ignored_lines) > 30:
        print(f"... {len(ignored_lines) - 30} more")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
