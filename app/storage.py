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
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS book_progress (
            book_id TEXT PRIMARY KEY,
            show_done INTEGER NOT NULL DEFAULT 0,
            guide_done INTEGER NOT NULL DEFAULT 0,
            test_done INTEGER NOT NULL DEFAULT 0,
            help_uses INTEGER NOT NULL DEFAULT 0,
            updated_at TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS dev_state (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
        """
    )
    conn.commit()
    return conn


def level_from_xp(xp: int) -> tuple[int, int, int]:
    """Return (level, current_level_start_xp, next_level_xp)."""
    thresholds = [0]
    cumulative = 0
    for level in range(1, 101):
        # Early levels are quick, then the curve gets heavier like old-school MMO leveling.
        # Tuned so the v0.4 quest campaign can carry a player toward level 100.
        need = int(300 + (level ** 1.6) * 6)
        cumulative += need
        thresholds.append(cumulative)
    current = 1
    for i, threshold in enumerate(thresholds):
        if xp >= threshold:
            current = max(1, min(i + 1, 100))
    start = thresholds[current - 1] if current - 1 < len(thresholds) else thresholds[-2]
    nxt = thresholds[current] if current < len(thresholds) else thresholds[-1]
    return current, start, nxt




def xp_for_level(level: int) -> int:
    """Return total XP required to stand at the beginning of a level."""
    level = max(1, min(int(level), 100))
    total = 0
    for current_level in range(1, level):
        total += int(300 + (current_level ** 1.6) * 6)
    return total


def get_dev_state() -> dict[str, Any]:
    with connect() as conn:
        rows = conn.execute("SELECT key, value FROM dev_state").fetchall()
    values = {row["key"]: row["value"] for row in rows}
    return {
        "xp_adjustment": int(values.get("xp_adjustment", "0") or 0),
    }


def set_dev_value(key: str, value: str | int) -> None:
    with connect() as conn:
        conn.execute(
            """
            INSERT INTO dev_state (key, value)
            VALUES (?, ?)
            ON CONFLICT(key) DO UPDATE SET value=excluded.value
            """,
            (key, str(value)),
        )
        conn.commit()


def adjust_dev_xp(delta: int) -> None:
    current = get_dev_state()["xp_adjustment"]
    set_dev_value("xp_adjustment", current + int(delta))


def set_dev_total_xp(total_xp: int) -> None:
    raw_quests = load_seed().get("quests", [])
    overrides = get_quest_overrides()
    completed_ids = {qid for qid, row in overrides.items() if row["status"] == "Completed"}
    completed_xp = sum(q.get("xp", 0) for q in raw_quests if q["id"] in completed_ids)
    set_dev_value("xp_adjustment", int(total_xp) - completed_xp)


def set_dev_level(level: int) -> None:
    set_dev_total_xp(xp_for_level(level))


def clear_dev_state() -> None:
    with connect() as conn:
        conn.execute("DELETE FROM dev_state")
        conn.commit()

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


def mark_quest_complete(quest_id: str) -> None:
    now = datetime.now().isoformat(timespec="seconds")
    with connect() as conn:
        conn.execute(
            """
            INSERT INTO quest_overrides (quest_id, status, progress, updated_at)
            VALUES (?, 'Completed', 100, ?)
            ON CONFLICT(quest_id) DO UPDATE SET
                status=excluded.status,
                progress=excluded.progress,
                updated_at=excluded.updated_at
            """,
            (quest_id, now),
        )
        conn.commit()


def clear_quest_override(quest_id: str) -> None:
    with connect() as conn:
        conn.execute("DELETE FROM quest_overrides WHERE quest_id = ?", (quest_id,))
        conn.commit()


def get_quest_overrides() -> dict[str, dict[str, Any]]:
    with connect() as conn:
        rows = conn.execute("SELECT * FROM quest_overrides").fetchall()
    return {row["quest_id"]: dict(row) for row in rows}


def get_book_progress() -> dict[str, dict[str, Any]]:
    with connect() as conn:
        rows = conn.execute("SELECT * FROM book_progress").fetchall()
    return {row["book_id"]: dict(row) for row in rows}


def mark_book_stage(book_id: str, stage: str) -> None:
    if stage not in {"show", "guide", "test"}:
        raise ValueError("stage must be show, guide, or test")
    now = datetime.now().isoformat(timespec="seconds")
    column = {"show": "show_done", "guide": "guide_done", "test": "test_done"}[stage]
    with connect() as conn:
        conn.execute(
            """
            INSERT INTO book_progress (book_id, updated_at)
            VALUES (?, ?)
            ON CONFLICT(book_id) DO UPDATE SET updated_at=excluded.updated_at
            """,
            (book_id, now),
        )
        conn.execute(
            f"UPDATE book_progress SET {column}=1, updated_at=? WHERE book_id=?",
            (now, book_id),
        )
        conn.commit()


def clear_book_progress(book_id: str) -> None:
    with connect() as conn:
        conn.execute("DELETE FROM book_progress WHERE book_id = ?", (book_id,))
        conn.commit()


def use_book_help(book_id: str) -> None:
    now = datetime.now().isoformat(timespec="seconds")
    with connect() as conn:
        conn.execute(
            """
            INSERT INTO book_progress (book_id, help_uses, updated_at)
            VALUES (?, 1, ?)
            ON CONFLICT(book_id) DO UPDATE SET
                help_uses=help_uses + 1,
                updated_at=excluded.updated_at
            """,
            (book_id, now),
        )
        conn.commit()


def _title_for_level(titles: list[dict[str, Any]], level: int) -> tuple[str, str, int]:
    current = titles[0]
    next_title = titles[-1]
    for item in titles:
        if level >= item["level"]:
            current = item
        elif item["level"] > level:
            next_title = item
            break
    return current["title"], next_title["title"], next_title["level"]


def _quest_status(quest: dict[str, Any], completed_ids: set[str], overrides: dict[str, dict[str, Any]], visible_level: int) -> tuple[str, int]:
    qid = quest["id"]
    if qid in overrides:
        status = overrides[qid]["status"]
        progress = int(overrides[qid]["progress"])
        if status == "Completed":
            return "Completed", 100
        return status, progress

    prereqs = set(quest.get("prereq_ids", []))
    if prereqs.issubset(completed_ids):
        return "Available", 0

    # Show nearby locked quests but keep distant regions mysterious.
    if quest.get("always_visible") or quest.get("recommended_level", 1) <= visible_level + 4:
        return "Locked", 0
    if completed_ids.intersection(prereqs):
        return "Locked", 0
    return "Hidden", 0


def state() -> dict[str, Any]:
    seed = load_seed()
    overrides = get_quest_overrides()
    book_progress = get_book_progress()
    latest_subs = get_latest_submission_by_quest()

    raw_quests = [dict(q) for q in seed["quests"]]
    completed_ids = {qid for qid, row in overrides.items() if row["status"] == "Completed"}
    earned_xp = sum(q.get("xp", 0) for q in raw_quests if q["id"] in completed_ids)
    dev = get_dev_state()
    completed_xp = max(0, earned_xp + int(dev.get("xp_adjustment", 0)))
    level, level_start, level_next_total = level_from_xp(completed_xp)

    title, next_title, next_title_level = _title_for_level(seed["titles"], level)
    profile = dict(seed["profile"])
    profile["level"] = level
    profile["xp"] = completed_xp - level_start
    profile["xp_total"] = completed_xp
    profile["xp_next"] = max(1, level_next_total - level_start)
    profile["earned_xp_total"] = earned_xp
    profile["dev_xp_adjustment"] = int(dev.get("xp_adjustment", 0))
    profile["current_title"] = title
    profile["next_title"] = next_title
    profile["next_title_level"] = next_title_level

    quests = []
    for quest in raw_quests:
        status, progress = _quest_status(quest, completed_ids, overrides, level)
        quest["status"] = status
        quest["progress"] = progress
        if quest["id"] in latest_subs:
            quest["submission"] = latest_subs[quest["id"]]
        quests.append(quest)
    seed["quests"] = quests
    seed["next_quest"] = (
        next((q for q in quests if q["status"] in {"Pending Review", "In Progress", "Available"}), None)
        or next((q for q in quests if q["status"] == "Locked"), None)
        or next((q for q in reversed(quests) if q["status"] == "Completed"), None)
    )

    # Gear unlocks from completed quests.
    completed_reward_gear = {q.get("reward_gear") for q in raw_quests if q["id"] in completed_ids and q.get("reward_gear")}
    gear = []
    for item in seed.get("gear", []):
        g = dict(item)
        if g["name"] in completed_reward_gear:
            g["locked"] = False
            g["equipped"] = True
        gear.append(g)
    seed["gear"] = gear

    # Dynamic class progress from completed quests by class_ids.
    classes = []
    for cls in seed.get("classes", []):
        c = dict(cls)
        cxp = sum(q.get("xp", 0) for q in raw_quests if q["id"] in completed_ids and c["id"] in q.get("class_ids", []))
        clevel, cstart, cnext = level_from_xp(cxp)
        c["level"] = clevel
        c["xp"] = cxp - cstart
        c["xp_total"] = cxp
        c["xp_next"] = max(1, cnext - cstart)
        classes.append(c)
    seed["classes"] = classes

    # Skill progress from tag/class completion. Kept simple: percent of related quests completed, capped.
    skills = []
    for skill in seed.get("skills", []):
        tags = set(skill.get("tags", []))
        related = [q for q in raw_quests if tags.intersection(set(q.get("tags", [])))]
        done = [q for q in related if q["id"] in completed_ids]
        value = int(100 * len(done) / len(related)) if related else 0
        sk = dict(skill)
        sk["value"] = value
        skills.append(sk)
    seed["skills"] = skills

    # Class skill progress mirrors skills but keeps old mini-card shape.
    class_skills = []
    for skill in seed.get("class_skills", []):
        tags = set(skill.get("tags", []))
        related = [q for q in raw_quests if tags.intersection(set(q.get("tags", [])))]
        done = [q for q in related if q["id"] in completed_ids]
        value = int(100 * len(done) / len(related)) if related else 0
        cs = dict(skill)
        cs["value"] = value
        cs["level"] = max(1, value // 10)
        class_skills.append(cs)
    seed["class_skills"] = class_skills

    # Dynamic zone reveal. A zone is known when any quest in that zone is not Hidden.
    zones = []
    current_zone_set = False
    for zone in seed.get("zones", []):
        z = dict(zone)
        zquests = [q for q in quests if q.get("zone") == z["name"]]
        if not zquests:
            z["status"] = "Hidden"
            z["progress"] = 0
        else:
            known = [q for q in zquests if q["status"] != "Hidden"]
            done = [q for q in zquests if q["status"] == "Completed"]
            avail = [q for q in zquests if q["status"] in {"Available", "Pending Review"}]
            if not known:
                z["status"] = "Hidden"
            elif len(done) == len(zquests):
                z["status"] = "Completed"
            elif avail and not current_zone_set:
                z["status"] = "Current"
                current_zone_set = True
                profile["current_zone"] = z["name"]
            else:
                z["status"] = "Locked"
            z["progress"] = int(100 * len(done) / len(zquests))
        zones.append(z)
    current_zone = next((z for z in zones if z.get("status") == "Current"), None)
    if current_zone is None:
        known_zones = [z for z in zones if z.get("status") != "Hidden"]
        current_zone = (
            next((z for z in reversed(known_zones) if z.get("status") == "Completed"), None)
            or next((z for z in reversed(known_zones)), None)
            or (zones[0] if zones else {"name": "No Zone", "summary": "No zone data found.", "range": "?"})
        )
        profile["current_zone"] = current_zone.get("name", "No Zone")
    seed["current_zone"] = current_zone
    seed["zones"] = zones
    seed["profile"] = profile
    seed["dev"] = dev

    activity = list(seed.get("activity", []))
    if completed_ids:
        latest_completed = next((q for q in reversed(raw_quests) if q["id"] in completed_ids), None)
        if latest_completed:
            activity.insert(0, {"icon": "✅", "kind": "Completed", "text": latest_completed["name"], "reward": f'{latest_completed.get("xp",0)} XP', "when": "local save"})
    seed["activity"] = activity[:8]

    # Books of Knowledge use the old training rhythm:
    # Show Me -> Guide Me -> Test Me. Books can also depend on mastered earlier books.
    books = []
    mastered_book_ids = {bid for bid, row in book_progress.items() if int(row.get("test_done", 0)) == 1}
    for book in seed.get("books", []):
        b = dict(book)
        quest_prereqs = set(b.get("prereq_quest_ids", []))
        book_prereqs = set(b.get("prereq_book_ids", []))
        progress = dict(book_progress.get(b["id"], {}))
        show_done = bool(progress.get("show_done", 0))
        guide_done = bool(progress.get("guide_done", 0))
        test_done = bool(progress.get("test_done", 0))
        help_uses = int(progress.get("help_uses", 0) or 0)
        max_help = int(b.get("teaching_charges", 5))
        b["show_done"] = show_done
        b["guide_done"] = guide_done
        b["test_done"] = test_done
        b["help_uses"] = help_uses
        b["help_remaining"] = max(0, max_help - help_uses)
        b["progress"] = (33 if show_done else 0) + (33 if guide_done else 0) + (34 if test_done else 0)
        b["unlocked"] = quest_prereqs.issubset(completed_ids) and book_prereqs.issubset(mastered_book_ids)
        if not b["unlocked"]:
            b["status"] = "Locked"
        elif test_done:
            b["status"] = "Mastered"
        elif guide_done:
            b["status"] = "Ready for Test"
        elif show_done:
            b["status"] = "Guide Me"
        else:
            b["status"] = "Show Me"
        books.append(b)
    seed["books"] = books

    completed_quests = [q for q in quests if q["status"] == "Completed"]
    total_quests = len(quests)
    completed_books = [b for b in books if b.get("status") == "Mastered"]
    boss_quests = [q for q in quests if q.get("type") == "Boss"]
    trial_quests = [q for q in quests if q.get("type") == "Trial"]
    seed["progress"] = {
        "quests_completed": len(completed_quests),
        "quests_total": total_quests,
        "books_mastered": len(completed_books),
        "books_total": len(books),
        "dungeons_cleared": len([q for q in boss_quests if q["status"] == "Completed"]),
        "dungeons_total": len(boss_quests),
        "trials_cleared": len([q for q in trial_quests if q["status"] == "Completed"]),
        "trials_total": len(trial_quests),
        "overall_percent": int(100 * len(completed_quests) / total_quests) if total_quests else 0,
    }

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
        conn.execute("DELETE FROM book_progress")
        conn.execute("DELETE FROM dev_state")
        conn.commit()


def find_book(book_id: str) -> dict[str, Any] | None:
    for book in state().get("books", []):
        if book["id"] == book_id:
            return book
    return None
