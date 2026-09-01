#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_UPSTREAM_SHA = "3e629eb163ba0ddf2935ce3b3fbaced0f9371977"
ALLOWED_STATUSES = {
    "Supported",
    "Preview",
    "Unsupported",
    "Not validated",
    "Host-gated",
    "Version-gated",
}

errors: list[str] = []


def strip_non_prose(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"<Visibility\b.*?</Visibility>", "", text, flags=re.DOTALL)
    text = re.sub(r"`[^`\n]+`", "", text)
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    return text


config = json.loads((ROOT / "docs.json").read_text())
zh_files = {p.relative_to(ROOT / "zh") for p in (ROOT / "zh").rglob("*.mdx")}
en_files = {p.relative_to(ROOT / "en") for p in (ROOT / "en").rglob("*.mdx")}
if zh_files != en_files:
    errors.append(f"locale trees differ: only zh={sorted(zh_files-en_files)}, only en={sorted(en_files-zh_files)}")

pages: list[str] = []
for language in config["navigation"]["languages"]:
    for tab in language["tabs"]:
        for group in tab["pages"]:
            pages.extend(group["pages"])
for page in pages:
    if not (ROOT / f"{page}.mdx").exists():
        errors.append(f"navigation target missing: {page}.mdx")

for rel in sorted(zh_files & en_files):
    zh = (ROOT / "zh" / rel).read_text()
    en = (ROOT / "en" / rel).read_text()
    zh_code = re.findall(r"```[^\n]*\n(.*?)```", zh, flags=re.DOTALL)
    en_code = re.findall(r"```[^\n]*\n(.*?)```", en, flags=re.DOTALL)
    if zh_code != en_code:
        errors.append(f"bilingual fenced code differs: {rel}")

    prose = strip_non_prose(zh)
    for match in re.finditer(r"\b[Cc]ontract(?:s)?\b", prose):
        line = prose.count("\n", 0, match.start()) + 1
        errors.append(f"bare Contract in Chinese prose: zh/{rel}:{line}")

for path in list((ROOT / "zh").rglob("*.mdx")) + list((ROOT / "en").rglob("*.mdx")):
    text = path.read_text()
    if re.search(r"^(<<<<<<<|=======|>>>>>>>)", text, flags=re.MULTILINE):
        errors.append(f"merge conflict marker: {path.relative_to(ROOT)}")
    for target in re.findall(r'href=["\'](/(?:zh|en)/[^"\']+)', text) + re.findall(r"\]\((/(?:zh|en)/[^)]+)\)", text):
        destination = ROOT / f"{target.rstrip('/').lstrip('/')}.mdx"
        if not destination.exists():
            errors.append(f"broken internal link: {path.relative_to(ROOT)} -> {target}")

all_text = "\n".join(p.read_text() for p in list((ROOT / "zh").rglob("*.mdx")) + list((ROOT / "en").rglob("*.mdx")))
for status in re.findall(r"\b(?:Supported|Preview|Unsupported|Not validated|Host-gated|Version-gated)\b", all_text):
    if status not in ALLOWED_STATUSES:
        errors.append(f"unknown maturity status: {status}")

navigated_text = "\n".join((ROOT / f"{page}.mdx").read_text() for page in pages)
agent_plugin_pages = {
    "en/common-agents/agent-plugin",
    "zh/common-agents/agent-plugin",
}
for page in agent_plugin_pages:
    if page not in pages:
        errors.append(f"Agent Plugin is missing from navigation: {page}")
if re.search(r"(?:powercontext\s+)?(?:setup|doctor)\s+agent-plugin\b", navigated_text):
    errors.append("Agent Plugin is incorrectly documented as having setup or doctor commands")

if errors:
    print("Documentation policy validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Documentation policy validation passed for {len(zh_files)} bilingual page pairs.")
print(f"Upstream fact baseline: {EXPECTED_UPSTREAM_SHA}")
