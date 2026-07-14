from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/learning", tags=["learning"])

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
TRACKS_FILE = DATA_DIR / "language_tracks.json"
PROFILE_FILE = DATA_DIR / "learning_profile.json"
templates = Jinja2Templates(directory=str(ROOT / "templates"))


def _read_json(path: Path, fallback: dict[str, Any]) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return fallback


def _write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def _tracks() -> list[dict[str, Any]]:
    document = _read_json(TRACKS_FILE, {"tracks": []})
    tracks = document.get("tracks", [])
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
    return next(
        (track for track in _tracks() if track.get("id") == track_id),
        None,
    )


@router.get("/tracks")
def show_tracks(request: Request):
    tracks = _tracks()
    profile = _profile()
    active_track = _find_track(str(profile.get("active_track", "ada")))

    return templates.TemplateResponse(
        request=request,
        name="language_tracks.html",
        context={
            "tracks": tracks,
            "profile": profile,
            "active_track": active_track,
        },
    )


@router.post("/tracks/select")
def select_track(track_id: str = Form(...)):
    track = _find_track(track_id)
    if track is None or not track.get("enabled", False):
        return RedirectResponse("/learning/tracks?error=unknown-track", status_code=303)

    profile = _profile()
    profile["active_track"] = track_id

    stages = track.get("stages", [])
    if stages:
        profile["active_stage"] = stages[0].get("id", "")
    else:
        profile["active_stage"] = ""

    profile["quest_mode"] = "Recall"
    _write_json(PROFILE_FILE, profile)
    return RedirectResponse("/learning/tracks?changed=1", status_code=303)


@router.post("/tracks/stage")
def select_stage(stage_id: str = Form(...)):
    profile = _profile()
    track = _find_track(str(profile.get("active_track", "")))
    if track is None:
        return RedirectResponse("/learning/tracks?error=no-track", status_code=303)

    valid_ids = {
        str(stage.get("id"))
        for stage in track.get("stages", [])
        if stage.get("id")
    }
    if stage_id not in valid_ids:
        return RedirectResponse("/learning/tracks?error=unknown-stage", status_code=303)

    profile["active_stage"] = stage_id
    profile["quest_mode"] = "Recall"
    _write_json(PROFILE_FILE, profile)
    return RedirectResponse("/learning/tracks?stage=1", status_code=303)
