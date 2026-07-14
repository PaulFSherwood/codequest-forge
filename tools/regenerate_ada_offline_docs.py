#!/usr/bin/env python3
"""Regenerate offline Markdown/CSV from data/ada_quests.json after manual quest edits."""
from __future__ import annotations
import csv, json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
source = root / "data" / "ada_quests.json"
docs = root / "docs"
docs.mkdir(parents=True, exist_ok=True)
doc = json.loads(source.read_text(encoding="utf-8"))
quests = doc["quests"]
lines = ["# Ada Project Mastery Path", "", f"Projects: **{doc['project_count']}**", f"Chapters: **{doc['chapter_count']}**", f"Quests: **{len(quests)}**", ""]
for project in doc["projects"]:
    lines += [f"## {project['name']}", "", project["goal"], "", f"Workspace: `{project['workspace']}`", ""]
    for chapter in project["chapters"]:
        lines.append(f"- **{chapter['name']}** — {chapter['deliverable']}")
    lines.append("")
lines += ["# Complete Quest List", ""]
for quest in quests:
    lines += [f"## {quest['quest_id']} — {quest['title']}", "", quest["prompt"], "", f"Workspace: `{quest['workspace']}`", "", "Completion checks:", ""]
    lines += [f"- {item}" for item in quest["acceptance"]]
    lines.append("")
(docs / "ADA_PROJECT_PATH.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
with (docs / "ADA_PROJECT_QUESTS.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.writer(handle)
    writer.writerow(["sequence","quest_id","project","chapter","kind","title","workspace","prompt","verification"])
    for q in quests:
        writer.writerow([q["sequence"],q["quest_id"],q["project_name"],q["chapter_name"],q["kind"],q["title"],q["workspace"],q["prompt"],q["verification"]])
print(f"Regenerated docs for {len(quests)} quests.")
