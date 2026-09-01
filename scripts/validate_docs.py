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

UNTRANSLATED_PROSE = {
    "adapter": "适配器",
    "capture": "采集",
    "commit": "提交",
    "contract": "契约",
    "fallback": "后备路径",
    "lineage": "证据链",
    "no-op": "无变更",
    "package": "软件包",
    "provider": "模型提供方",
    "recall": "召回",
    "smoke": "冒烟测试",
    "stale": "过期",
}
UPSTREAM_ROOT = ROOT.parent / "powercontext"

errors: list[str] = []


def strip_non_prose(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"<Visibility\b.*?</Visibility>", "", text, flags=re.DOTALL)
    text = re.sub(r"`[^`\n]+`", "", text)
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("工作契约（Work Contract）", "工作契约")
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

ledger_path = ROOT / "scripts" / "page_fact_ledger.tsv"
if not ledger_path.exists():
    errors.append("page fact ledger is missing: scripts/page_fact_ledger.tsv")
else:
    ledger_pages = {
        line.split("\t", 1)[0]
        for line in ledger_path.read_text().splitlines()[1:]
        if line.strip()
    }
    expected_pages = {str(path) for path in zh_files}
    if ledger_pages != expected_pages:
        errors.append(
            f"page fact ledger differs from locale tree: missing={sorted(expected_pages-ledger_pages)}, "
            f"extra={sorted(ledger_pages-expected_pages)}"
        )

for rel in sorted(zh_files & en_files):
    zh = (ROOT / "zh" / rel).read_text()
    en = (ROOT / "en" / rel).read_text()
    zh_code = re.findall(r"```[^\n]*\n(.*?)```", zh, flags=re.DOTALL)
    en_code = re.findall(r"```[^\n]*\n(.*?)```", en, flags=re.DOTALL)
    if zh_code != en_code:
        errors.append(f"bilingual fenced code differs: {rel}")

    prose = strip_non_prose(zh)
    for match in re.finditer(r"合同|\b[Cc]ontract(?:s)?\b", prose):
        line = prose.count("\n", 0, match.start()) + 1
        errors.append(f"contract should be 契约 in Chinese prose: zh/{rel}:{line}")
    for term, replacement in UNTRANSLATED_PROSE.items():
        for match in re.finditer(rf"(?i)(?<![\w-]){re.escape(term)}(?![\w-])", prose):
            line = prose.count("\n", 0, match.start()) + 1
            errors.append(f"translate {term} as {replacement} in Chinese prose: zh/{rel}:{line}")
    reader_text = re.sub(r"```.*?```|`[^`\n]+`", "", zh, flags=re.DOTALL)
    first_work_contract = reader_text.find("工作契约")
    if first_work_contract >= 0 and not reader_text.startswith("工作契约（Work Contract）", first_work_contract):
        line = reader_text.count("\n", 0, first_work_contract) + 1
        errors.append(f"first Work Contract use needs 工作契约（Work Contract）: zh/{rel}:{line}")

for path in list((ROOT / "zh").rglob("*.mdx")) + list((ROOT / "en").rglob("*.mdx")):
    text = path.read_text()
    if re.search(r"^(<<<<<<<|=======|>>>>>>>)", text, flags=re.MULTILINE):
        errors.append(f"merge conflict marker: {path.relative_to(ROOT)}")
    for target in re.findall(r'href=["\'](/(?:zh|en)/[^"\']+)', text) + re.findall(r"\]\((/(?:zh|en)/[^)]+)\)", text):
        destination = ROOT / f"{target.rstrip('/').lstrip('/')}.mdx"
        if not destination.exists():
            errors.append(f"broken internal link: {path.relative_to(ROOT)} -> {target}")

if UPSTREAM_ROOT.exists():
    import subprocess

    actual_upstream_sha = subprocess.run(
        ["git", "-C", str(UPSTREAM_ROOT), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    if actual_upstream_sha != EXPECTED_UPSTREAM_SHA:
        errors.append(
            f"upstream fact baseline is stale: expected {EXPECTED_UPSTREAM_SHA}, current {actual_upstream_sha}"
        )

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

commit_refs = set(re.findall(r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])", navigated_text))
if commit_refs != {EXPECTED_UPSTREAM_SHA}:
    errors.append(
        f"tutorial commit pins differ from upstream fact baseline: found={sorted(commit_refs)}, "
        f"expected={[EXPECTED_UPSTREAM_SHA]}"
    )

if errors:
    print("Documentation policy validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Documentation policy validation passed for {len(zh_files)} bilingual page pairs.")
print(f"Upstream fact baseline: {EXPECTED_UPSTREAM_SHA}")
