from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from fastapi import APIRouter, FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/learning", tags=["learning"])

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
TRACKS_FILE = DATA_DIR / "language_tracks.json"
PROFILE_FILE = DATA_DIR / "learning_profile.json"
ADA_QUESTS_FILE = DATA_DIR / "ada_quests.json"
ADA_PROGRESS_FILE = DATA_DIR / "ada_progress.json"
templates = Jinja2Templates(directory=str(ROOT / "templates"))


def _read_json(path: Path, fallback: dict[str, Any]) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else fallback
    except (OSError, json.JSONDecodeError):
        return fallback


def _write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def _tracks() -> list[dict[str, Any]]:
    tracks = _read_json(TRACKS_FILE, {"tracks": []}).get("tracks", [])
    return tracks if isinstance(tracks, list) else []


def _profile() -> dict[str, Any]:
    return _read_json(
        PROFILE_FILE,
        {
            "active_track": "ada",
            "active_stage": "ada-foundations",
            "quest_mode": "Recall",
            "review_enabled": True,
        },
    )


def _find_track(track_id: str) -> dict[str, Any] | None:
    return next((track for track in _tracks() if track.get("id") == track_id), None)


def _ada_quests() -> list[dict[str, Any]]:
    quests = _read_json(ADA_QUESTS_FILE, {"quests": []}).get("quests", [])
    return quests if isinstance(quests, list) else []


def _ada_progress() -> dict[str, Any]:
    return _read_json(
        ADA_PROGRESS_FILE,
        {"completed": [], "attempts": {}, "last_answer": {}, "active_quest": "alire-first-crate"},
    )


def _find_ada_quest(slug: str) -> dict[str, Any] | None:
    return next((quest for quest in _ada_quests() if quest.get("slug") == slug), None)


def _title_progress(completed_count: int) -> tuple[str, str, int]:
    ranks = [
        (0, "Ada Initiate"),
        (3, "Alire Apprentice"),
        (6, "Ada Programmer"),
        (10, "Ada Developer"),
        (14, "Ada Engineer"),
    ]
    current = ranks[0][1]
    next_name = "Senior Ada Path"
    next_at = 20
    for index, (required, name) in enumerate(ranks):
        if completed_count >= required:
            current = name
            if index + 1 < len(ranks):
                next_at, next_name = ranks[index + 1]
        else:
            break
    return current, next_name, next_at


def _answer_is_correct(answer: str, accepted_groups: list[str]) -> bool:
    normalized = answer.casefold()
    for group in accepted_groups:
        alternatives = [part.strip().casefold() for part in group.split("|") if part.strip()]
        if not alternatives:
            continue
        matched = False
        for alternative in alternatives:
            if alternative.endswith("iz"):
                matched = alternative[:-2] in normalized
            elif alternative in normalized:
                matched = True
            if matched:
                break
        if not matched:
            return False
    return True


@router.get("/tracks")
def show_tracks(request: Request):
    tracks = _tracks()
    profile = _profile()
    active_track = _find_track(str(profile.get("active_track", "ada")))
    return templates.TemplateResponse(
        request=request,
        name="language_tracks.html",
        context={"tracks": tracks, "profile": profile, "active_track": active_track},
    )


@router.post("/tracks/select")
def select_track(track_id: str = Form(...)):
    track = _find_track(track_id)
    if track is None or not track.get("enabled", False):
        return RedirectResponse("/learning/tracks?error=unknown-track", status_code=303)

    profile = _profile()
    profile["active_track"] = track_id
    stages = track.get("stages", [])
    profile["active_stage"] = stages[0].get("id", "") if stages else ""
    profile["quest_mode"] = "Recall"
    _write_json(PROFILE_FILE, profile)

    if track_id == "ada":
        return RedirectResponse("/learning/ada/quests?changed=1", status_code=303)
    return RedirectResponse("/learning/tracks?changed=1", status_code=303)


@router.post("/tracks/stage")
def select_stage(stage_id: str = Form(...)):
    profile = _profile()
    track = _find_track(str(profile.get("active_track", "")))
    if track is None:
        return RedirectResponse("/learning/tracks?error=no-track", status_code=303)

    valid_ids = {str(stage.get("id")) for stage in track.get("stages", []) if stage.get("id")}
    if stage_id not in valid_ids:
        return RedirectResponse("/learning/tracks?error=unknown-stage", status_code=303)

    profile["active_stage"] = stage_id
    profile["quest_mode"] = "Recall"
    _write_json(PROFILE_FILE, profile)
    if str(profile.get("active_track")) == "ada":
        return RedirectResponse("/learning/ada/quests?stage=1", status_code=303)
    return RedirectResponse("/learning/tracks?stage=1", status_code=303)


@router.get("/ada")
def ada_home():
    return RedirectResponse("/learning/ada/quests", status_code=302)


@router.get("/ada/quests")
def ada_quest_list(request: Request):
    quests = _ada_quests()
    progress = _ada_progress()
    completed = set(progress.get("completed", []))
    current_title, next_title, next_at = _title_progress(len(completed))
    next_quest = next((quest for quest in quests if quest.get("slug") not in completed), None)
    if next_quest is not None:
        progress["active_quest"] = next_quest.get("slug")
        _write_json(ADA_PROGRESS_FILE, progress)

    return templates.TemplateResponse(
        request=request,
        name="ada_quests.html",
        context={
            "quests": quests,
            "completed": completed,
            "completed_count": len(completed),
            "total_count": len(quests),
            "current_title": current_title,
            "next_title": next_title,
            "next_at": next_at,
            "next_quest": next_quest,
        },
    )


@router.get("/ada/quest/{slug}")
def ada_quest_detail(request: Request, slug: str):
    quest = _find_ada_quest(slug)
    if quest is None:
        return RedirectResponse("/learning/ada/quests?error=unknown-quest", status_code=303)
    progress = _ada_progress()
    progress["active_quest"] = slug
    _write_json(ADA_PROGRESS_FILE, progress)
    return templates.TemplateResponse(
        request=request,
        name="ada_quest.html",
        context={
            "quest": quest,
            "completed": slug in set(progress.get("completed", [])),
            "attempts": int(progress.get("attempts", {}).get(slug, 0)),
            "last_answer": progress.get("last_answer", {}).get(slug, ""),
            "result": request.query_params.get("result", ""),
        },
    )


@router.post("/ada/quest/{slug}/answer")
def answer_ada_quest(slug: str, answer: str = Form(...)):
    quest = _find_ada_quest(slug)
    if quest is None:
        return RedirectResponse("/learning/ada/quests?error=unknown-quest", status_code=303)

    accepted = quest.get("accepted_keywords", [])
    correct = bool(accepted) and _answer_is_correct(answer, accepted)
    progress = _ada_progress()
    attempts = progress.setdefault("attempts", {})
    attempts[slug] = int(attempts.get(slug, 0)) + 1
    progress.setdefault("last_answer", {})[slug] = answer

    if correct:
        completed = progress.setdefault("completed", [])
        if slug not in completed:
            completed.append(slug)
    _write_json(ADA_PROGRESS_FILE, progress)

    result = "correct" if correct else "review"
    return RedirectResponse(f"/learning/ada/quest/{slug}?result={result}", status_code=303)


@router.post("/ada/quest/{slug}/complete")
def complete_ada_quest(slug: str):
    if _find_ada_quest(slug) is None:
        return RedirectResponse("/learning/ada/quests?error=unknown-quest", status_code=303)
    progress = _ada_progress()
    completed = progress.setdefault("completed", [])
    if slug not in completed:
        completed.append(slug)
    _write_json(ADA_PROGRESS_FILE, progress)
    return RedirectResponse("/learning/ada/quests?completed=1", status_code=303)


def install_learning_track_support(app: FastAPI) -> None:
    """Connect the selected language to the existing CodeQuest routes and UI."""
    if getattr(app.state, "learning_track_support_installed", False):
        return
    app.state.learning_track_support_installed = True

    @app.middleware("http")
    async def active_learning_track_middleware(request: Request, call_next):
        profile = _profile()
        active_track = str(profile.get("active_track", "ada"))
        path = request.url.path

        if active_track == "ada" and path == "/quests":
            return RedirectResponse("/learning/ada/quests", status_code=302)

        response = await call_next(request)
        content_type = response.headers.get("content-type", "")
        if active_track != "ada" or "text/html" not in content_type or path.startswith("/learning/"):
            return response

        body = b""
        async for chunk in response.body_iterator:
            body += chunk
        charset = response.charset or "utf-8"
        html = body.decode(charset, errors="replace")

        replacements = {
            "C++ / SDL / ECS": "Ada / Alire / GtkAda",
            "THE JOURNEY OF A C++ HERO": "THE JOURNEY OF AN ADA ENGINEER",
            "The Journey of a C++ Hero": "The Journey of an Ada Engineer",
            "C++ Recruit": "Ada Apprentice",
            "New Spawn": "Ada Initiate",
            "Modern C++": "Senior Ada",
        }
        for old, new in replacements.items():
            html = html.replace(old, new)

        progress = _ada_progress()
        current_title, next_title, next_at = _title_progress(len(set(progress.get("completed", []))))
        badge = f"""
        <aside id="cq-active-language" style="position:fixed;right:16px;bottom:16px;z-index:99999;
          min-width:240px;padding:12px 14px;border:1px solid #d2a84b;border-radius:10px;
          background:#101827;color:#eef2ff;box-shadow:0 8px 28px rgba(0,0,0,.45);font-family:system-ui,sans-serif">
          <div style="font-size:11px;letter-spacing:.12em;color:#f0c66a;font-weight:800">ACTIVE LANGUAGE</div>
          <div style="font-size:18px;font-weight:900;margin:2px 0">Ada · {current_title}</div>
          <div style="font-size:12px;color:#b9c3d6;margin-bottom:8px">Next: {next_title} at {next_at} completed quests</div>
          <a href="/learning/ada/quests" style="display:block;text-align:center;padding:7px 10px;border-radius:7px;
            background:#f0c66a;color:#16110a;text-decoration:none;font-weight:900">Open Ada Quests</a>
        </aside>
        """
        if "</body>" in html:
            html = html.replace("</body>", badge + "</body>", 1)
        else:
            html += badge

        headers = dict(response.headers)
        headers.pop("content-length", None)
        headers.pop("content-type", None)
        return HTMLResponse(content=html, status_code=response.status_code, headers=headers)
