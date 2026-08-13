#!/usr/bin/env python3
"""List cloud NotebookLM notebooks and visible source titles.

This intentionally reads only NotebookLM page content through the authenticated
browser context. It does not inspect or print cookies, tokens, or browser state.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

from patchright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).parent))

from auth_manager import AuthManager
from browser_utils import BrowserFactory
from config import DATA_DIR


HOME_URL = "https://notebooklm.google.com"
OUTPUT_FILE = DATA_DIR / "cloud_inventory.json"


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "")).strip()


def extract_notebooks(page) -> list[dict[str, str]]:
    anchors = page.evaluate(
        """() => Array.from(document.querySelectorAll('a[href]')).map((a) => ({
            href: a.href || '',
            text: (a.innerText || a.textContent || '').trim(),
            aria: a.getAttribute('aria-label') || '',
            title: a.getAttribute('title') || ''
        }))"""
    )

    notebooks: dict[str, dict[str, str]] = {}
    for anchor in anchors:
        href = anchor.get("href", "")
        if "notebooklm.google.com/notebook/" not in href:
            continue
        url = href.split("?")[0].rstrip("/")
        text_parts = [
            normalize_space(anchor.get("text", "")),
            normalize_space(anchor.get("aria", "")),
            normalize_space(anchor.get("title", "")),
        ]
        name = next((part for part in text_parts if part), "Untitled Notebook")
        notebooks[url] = {"name": name, "url": url}

    return list(notebooks.values())


def visible_source_candidates(page) -> list[str]:
    values = page.evaluate(
        """() => {
            const selectors = [
                '[data-testid*="source" i]',
                '[class*="source" i]',
                '[aria-label*="source" i]',
                '[aria-label*="來源"]',
                'mat-list-item',
                'li',
                'button'
            ];
            const nodes = new Set();
            for (const selector of selectors) {
                for (const node of document.querySelectorAll(selector)) {
                    const rect = node.getBoundingClientRect();
                    if (rect.width > 0 && rect.height > 0) nodes.add(node);
                }
            }
            return Array.from(nodes).map((node) => ({
                text: (node.innerText || node.textContent || '').trim(),
                aria: node.getAttribute('aria-label') || '',
                title: node.getAttribute('title') || ''
            }));
        }"""
    )

    blocked = {
        "add source",
        "sources",
        "source",
        "新增來源",
        "來源",
        "studio",
        "chat",
        "notes",
        "筆記",
        "notebook guide",
        "settings",
        "share",
    }
    seen: set[str] = set()
    results: list[str] = []
    for item in values:
        for raw in (item.get("text", ""), item.get("aria", ""), item.get("title", "")):
            text = normalize_space(raw)
            key = text.casefold()
            if not text or key in blocked or key in seen:
                continue
            if len(text) < 2 or len(text) > 180:
                continue
            if "NotebookLM" in text and len(text) < 30:
                continue
            seen.add(key)
            results.append(text)

    return results[:80]


def page_debug(page) -> dict[str, Any]:
    return {
        "url": page.url,
        "title": page.title(),
        "body_preview": normalize_space(page.inner_text("body") if page.query_selector("body") else "")[:1200],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Inventory cloud NotebookLM notebooks.")
    parser.add_argument("--show-browser", action="store_true", help="Show browser while scanning.")
    parser.add_argument("--with-sources", action="store_true", help="Open each notebook and collect visible source titles.")
    parser.add_argument("--limit", type=int, default=30, help="Maximum notebooks to inspect for sources.")
    parser.add_argument("--output", default=str(OUTPUT_FILE), help="JSON output path.")
    args = parser.parse_args()

    auth = AuthManager()
    if not auth.is_authenticated():
        print("Not authenticated. Run: python scripts/run.py auth_manager.py setup")
        return 2

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    output_path = Path(args.output)

    playwright = None
    context = None
    try:
        playwright = sync_playwright().start()
        context = BrowserFactory.launch_persistent_context(playwright, headless=not args.show_browser)
        page = context.new_page()
        page.goto(HOME_URL, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(6000)

        if "accounts.google.com" in page.url:
            print("Authentication required. Run: python scripts/run.py auth_manager.py setup")
            return 2

        notebooks = extract_notebooks(page)
        inventory: dict[str, Any] = {
            "scanned_at": datetime.now().isoformat(),
            "home": page_debug(page),
            "notebooks": notebooks,
        }

        if args.with_sources and notebooks:
            for index, notebook in enumerate(notebooks[: args.limit], start=1):
                print(f"[{index}/{min(len(notebooks), args.limit)}] {notebook['name']}")
                try:
                    page.goto(notebook["url"], wait_until="domcontentloaded", timeout=60000)
                    page.wait_for_timeout(7000)
                    notebook["page_title"] = page.title()
                    notebook["sources"] = visible_source_candidates(page)
                except Exception as exc:
                    notebook["source_error"] = str(exc)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2), encoding="utf-8")

        print(f"Found {len(notebooks)} cloud notebooks.")
        print(f"Wrote {output_path}")
        if not notebooks:
            print("Page debug preview:")
            print(inventory["home"]["body_preview"])
        else:
            for notebook in notebooks[:20]:
                source_count = len(notebook.get("sources", []))
                suffix = f" ({source_count} visible sources)" if "sources" in notebook else ""
                print(f"- {notebook['name']}: {notebook['url']}{suffix}")

        return 0

    finally:
        if context:
            context.close()
        if playwright:
            playwright.stop()


if __name__ == "__main__":
    raise SystemExit(main())
