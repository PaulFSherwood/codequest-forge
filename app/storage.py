from __future__ import annotations

import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "seed.json"
INSTANCE_DIR = ROOT / "instance"
DB_FILE = INSTANCE_DIR / "codequest_forge.db"


def load_seed() -> dict[str, Any]:
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def connect() -> sqlite3.Connection:
    INSTANCE_DIR.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quest_id TEXT NOT NULL,
            github_url TEXT NOT NULL,
            screenshot_url TEXT,
            release_tag TEXT,
            console_output TEXT,
            notes TEXT,
            status TEXT NOT NULL DEFAULT 'Pending Review',
            created_at TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS quest_overrides (
            quest_id TEXT PRIMARY KEY,
            status TEXT NOT NULL,
            progress INTEGER NOT NULL,
            updated_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    return conn


def get_submissions() -> list[dict[str, Any]]:
    with connect() as conn:
        rows = conn.execute(
            "SELECT * FROM submissions ORDER BY created_at DESC, id DESC"
        ).fetchall()
    return [dict(row) for row in rows]


def get_latest_submission_by_quest() -> dict[str, dict[str, Any]]:
    latest: dict[str, dict[str, Any]] = {}
    for item in get_submissions():
        latest.setdefault(item["quest_id"], item)
    return latest


def add_submission(
    quest_id: str,
    github_url: str,
    screenshot_url: str | None,
    release_tag: str | None,
    console_output: str | None,
    notes: str | None,
) -> None:
    now = datetime.now().isoformat(timespec="seconds")
    with connect() as conn:
        conn.execute(
            """
            INSERT INTO submissions
            (quest_id, github_url, screenshot_url, release_tag, console_output, notes, status, created_at)
            VALUES (?, ?, ?, ?, ?, ?, 'Pending Review', ?)
            """,
            (quest_id, github_url, screenshot_url, release_tag, console_output, notes, now),
        )
        conn.execute(
            """
            INSERT INTO quest_overrides (quest_id, status, progress, updated_at)
            VALUES (?, 'Pending Review', 90, ?)
            ON CONFLICT(quest_id) DO UPDATE SET
                status=excluded.status,
                progress=excluded.progress,
                updated_at=excluded.updated_at
            """,
            (quest_id, now),
        )
        conn.commit()


def get_quest_overrides() -> dict[str, dict[str, Any]]:
    with connect() as conn:
        rows = conn.execute("SELECT * FROM quest_overrides").fetchall()
    return {row["quest_id"]: dict(row) for row in rows}


def state() -> dict[str, Any]:
    seed = load_seed()
    overrides = get_quest_overrides()
    latest_subs = get_latest_submission_by_quest()

    quests = []
    for quest in seed["quests"]:
        q = dict(quest)
        if q["id"] in overrides:
            q["status"] = overrides[q["id"]]["status"]
            q["progress"] = overrides[q["id"]]["progress"]
        if q["id"] in latest_subs:
            q["submission"] = latest_subs[q["id"]]
        quests.append(q)
    seed["quests"] = quests
    seed["submissions"] = get_submissions()
    return seed


def find_quest(quest_id: str) -> dict[str, Any] | None:
    for quest in state()["quests"]:
        if quest["id"] == quest_id:
            return quest
    return None


def reset_local_progress() -> None:
    with connect() as conn:
        conn.execute("DELETE FROM submissions")
        conn.execute("DELETE FROM quest_overrides")
        conn.commit()
