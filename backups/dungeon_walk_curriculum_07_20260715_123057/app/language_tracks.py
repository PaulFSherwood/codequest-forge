from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs

from fastapi import APIRouter, HTTPException, Query, Request
from fastapi.responses import RedirectResponse, Response
from starlette.middleware.base import BaseHTTPMiddleware

router = APIRouter(prefix="/learning", tags=["learning-tracks"])

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"
PROFILE_FILE = DATA_DIR / "learning_profile.json"
TRACKS_FILE = DATA_DIR / "language_tracks.json"
ADA_QUESTS_FILE = DATA_DIR / "ada_quests.json"
ADA_PROGRESS_FILE = DATA_DIR / "ada_progress.json"
ADA_MARKDOWN_FILE = DOCS_DIR / "ADA_PROJECT_PATH.md"
ADA_CSV_FILE = DOCS_DIR / "ADA_PROJECT_QUESTS.csv"
ADA_PATH_FILE = DOCS_DIR / "ADA_PROJECT_PATH.md"


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _read_json(path: Path, fallback: dict[str, Any]) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return fallback
    return value if isinstance(value, dict) else fallback


def _write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def _profile() -> dict[str, Any]:
    return _read_json(
        PROFILE_FILE,
        {
            "active_track": "ada",
            "active_stage": "ada-tooling-foundations",
            "quest_mode": "Recall",
            "review_enabled": True,
        },
    )


def _tracks() -> list[dict[str, Any]]:
    value = _read_json(TRACKS_FILE, {"tracks": []}).get("tracks", [])
    return value if isinstance(value, list) else []


def _quest_document() -> dict[str, Any]:
    return _read_json(ADA_QUESTS_FILE, {"version": 6, "quests": [], "projects": [], "stages": []})


def _quests() -> list[dict[str, Any]]:
    value = _quest_document().get("quests", [])
    return value if isinstance(value, list) else []


def _progress() -> dict[str, Any]:
    return _read_json(
        ADA_PROGRESS_FILE,
        {
            "version": 2,
            "quests": {},
            "last_opened": None,
        },
    )


def _safe_return_path(value: str | None) -> str:
    if not value or not value.startswith("/") or value.startswith("//"):
        return "/quests"
    return value


def _quest_by_slug(slug: str) -> dict[str, Any]:
    quest = next((item for item in _quests() if item.get("slug") == slug), None)
    if quest is None:
        raise HTTPException(status_code=404, detail="Unknown Ada quest")
    return quest


def _entry(progress: dict[str, Any], slug: str) -> dict[str, Any]:
    entries = progress.setdefault("quests", {})
    entry = entries.setdefault(
        slug,
        {
            "attempts": 0,
            "successful_reviews": 0,
            "status": "new",
            "last_answer": "",
            "last_attempt": None,
            "next_review": None,
        },
    )
    return entry


def _next_quest(quests: list[dict[str, Any]], progress: dict[str, Any]) -> dict[str, Any] | None:
    now = datetime.now(timezone.utc)
    entries = progress.get("quests", {})

    due: list[tuple[datetime, dict[str, Any]]] = []
    for quest in quests:
        entry = entries.get(quest["slug"], {})
        next_review = entry.get("next_review")
        if not next_review:
            continue
        try:
            due_time = datetime.fromisoformat(next_review)
        except ValueError:
            continue
        if due_time <= now:
            due.append((due_time, quest))

    if due:
        due.sort(key=lambda item: (item[0], item[1].get("sequence", 0)))
        return due[0][1]

    for quest in quests:
        if entries.get(quest["slug"], {}).get("status") != "mastered":
            return quest

    return quests[0] if quests else None


def _summary(quest: dict[str, Any] | None) -> dict[str, Any] | None:
    if quest is None:
        return None
    keys = (
        "slug",
        "quest_id",
        "sequence",
        "level",
        "stage_id",
        "stage_name",
        "project_id",
        "project_name",
        "chapter_id",
        "chapter_name",
        "workspace",
        "source_files",
        "deliverable",
        "kind",
        "concept",
        "difficulty",
        "title",
        "summary",
        "xp",
        "uses_gtkada",
    )
    return {key: quest.get(key) for key in keys}


@router.get("/api/state")
def state() -> dict[str, Any]:
    profile = _profile()
    document = _quest_document()
    quests = document.get("quests", [])
    progress = _progress()
    entries = progress.get("quests", {})

    mastered = sum(1 for quest in quests if entries.get(quest.get("slug", ""), {}).get("status") == "mastered")
    reviewing = sum(1 for quest in quests if entries.get(quest.get("slug", ""), {}).get("status") == "review")

    project_summaries = []
    for project in document.get("projects", []):
        project_id = project.get("id")
        project_quests = [quest for quest in quests if quest.get("project_id") == project_id]
        project_mastered = sum(1 for quest in project_quests if entries.get(quest.get("slug", ""), {}).get("status") == "mastered")
        project_reviewing = sum(1 for quest in project_quests if entries.get(quest.get("slug", ""), {}).get("status") == "review")
        project_summaries.append({
            "id": project_id,
            "name": project.get("name"),
            "short_name": project.get("short_name"),
            "goal": project.get("goal"),
            "final_product": project.get("final_product"),
            "workspace": project.get("workspace"),
            "chapter_count": project.get("chapter_count", 0),
            "total": len(project_quests),
            "mastered": project_mastered,
            "reviewing": project_reviewing,
        })

    return {
        "active_track": profile.get("active_track", "ada"),
        "tracks": [
            {
                "id": track.get("id"),
                "name": track.get("name"),
                "enabled": bool(track.get("enabled", False)),
            }
            for track in _tracks()
        ],
        "ada": {
            "total": len(quests),
            "mastered": mastered,
            "reviewing": reviewing,
            "project_count": len(project_summaries),
            "chapter_count": document.get("chapter_count", 0),
            "projects": project_summaries,
            "stages": [
                {"id": project.get("id"), "name": project.get("name"), "quest_count": project.get("total", 0)}
                for project in project_summaries
            ],
            "kinds": document.get("quest_kinds", []),
            "next_quest": _summary(_next_quest(quests, progress)),
        },
    }


@router.get("/api/ada/quests")
def list_ada_quests(
    offset: int = Query(0, ge=0),
    limit: int = Query(30, ge=1, le=100),
    stage: str = "",
    kind: str = "",
    search: str = "",
    status: str = "",
) -> dict[str, Any]:
    quests = _quests()
    entries = _progress().get("quests", {})
    needle = search.strip().casefold()

    filtered: list[dict[str, Any]] = []
    for quest in quests:
        entry = entries.get(quest["slug"], {})
        quest_status = entry.get("status", "new")

        if stage and quest.get("project_id", quest.get("stage_id")) != stage:
            continue
        if kind and quest.get("kind") != kind:
            continue
        if status and quest_status != status:
            continue
        if needle:
            haystack = " ".join(
                str(quest.get(key, ""))
                for key in ("quest_id", "title", "concept", "summary", "stage_name", "project_name", "chapter_name", "deliverable", "kind")
            ).casefold()
            if needle not in haystack:
                continue

        item = _summary(quest) or {}
        item["status"] = quest_status
        item["attempts"] = entry.get("attempts", 0)
        item["successful_reviews"] = entry.get("successful_reviews", 0)
        item["next_review"] = entry.get("next_review")
        filtered.append(item)

    total = len(filtered)
    return {
        "items": filtered[offset : offset + limit],
        "offset": offset,
        "limit": limit,
        "total": total,
    }


@router.get("/api/ada/quest/{slug}")
def get_ada_quest(slug: str) -> dict[str, Any]:
    quest = _quest_by_slug(slug)
    progress = _progress()
    progress["last_opened"] = slug
    _write_json(ADA_PROGRESS_FILE, progress)
    return {
        "quest": quest,
        "progress": progress.get("quests", {}).get(slug, {}),
    }


@router.post("/api/ada/quest/{slug}/answer")
async def save_answer(slug: str, request: Request) -> dict[str, Any]:
    quest = _quest_by_slug(slug)
    try:
        payload = await request.json()
    except json.JSONDecodeError:
        payload = {}

    answer = str(payload.get("answer", "")).strip()
    progress = _progress()
    entry = _entry(progress, slug)
    entry["attempts"] = int(entry.get("attempts", 0)) + 1
    entry["last_answer"] = answer
    entry["last_attempt"] = _utc_now()
    if entry.get("status") == "new":
        entry["status"] = "attempted"
    _write_json(ADA_PROGRESS_FILE, progress)

    return {
        "saved": True,
        "rubric": quest.get("rubric", quest.get("acceptance", [])),
        "message": "Answer saved. Compare it with the rubric, then mark the result.",
    }


@router.post("/api/ada/quest/{slug}/result")
async def record_result(slug: str, request: Request) -> dict[str, Any]:
    _quest_by_slug(slug)
    try:
        payload = await request.json()
    except json.JSONDecodeError:
        payload = {}

    result = str(payload.get("result", "review"))
    if result not in {"mastered", "review"}:
        raise HTTPException(status_code=400, detail="Result must be mastered or review")

    progress = _progress()
    entry = _entry(progress, slug)
    entry["last_attempt"] = _utc_now()

    now = datetime.now(timezone.utc)
    if result == "mastered":
        successes = int(entry.get("successful_reviews", 0)) + 1
        entry["successful_reviews"] = successes
        entry["status"] = "mastered"
        days = min(60, 2 ** min(successes, 6))
        entry["next_review"] = (now + timedelta(days=days)).isoformat()
    else:
        entry["status"] = "review"
        entry["next_review"] = (now + timedelta(days=1)).isoformat()

    _write_json(ADA_PROGRESS_FILE, progress)
    return {"ok": True, "progress": entry}


@router.post("/tracks/select")
async def select_track(request: Request) -> RedirectResponse:
    body = (await request.body()).decode("utf-8", errors="replace")
    form = parse_qs(body)
    track_id = form.get("track_id", [""])[0]
    return_to = _safe_return_path(form.get("return_to", ["/quests"])[0])

    valid = {
        str(track.get("id"))
        for track in _tracks()
        if track.get("enabled", False)
    }
    if track_id not in valid:
        return RedirectResponse(f"{return_to}?language_error=1", status_code=303)

    profile = _profile()
    profile["active_track"] = track_id
    _write_json(PROFILE_FILE, profile)
    return RedirectResponse(return_to, status_code=303)


@router.get("/tracks")
def tracks_page() -> RedirectResponse:
    return RedirectResponse("/quests", status_code=302)


@router.get("/ada/quests")
def old_ada_page() -> RedirectResponse:
    return RedirectResponse("/quests", status_code=302)


@router.get("/download/ada-quests.json")
def download_json() -> Response:
    return Response(
        ADA_QUESTS_FILE.read_text(encoding="utf-8"),
        media_type="application/json",
        headers={"Content-Disposition": 'attachment; filename="ADA_QUESTS.json"'},
    )


@router.get("/download/ada-quests.md")
def download_markdown() -> Response:
    return Response(
        ADA_MARKDOWN_FILE.read_text(encoding="utf-8"),
        media_type="text/markdown; charset=utf-8",
        headers={"Content-Disposition": 'attachment; filename="ADA_QUESTS.md"'},
    )


@router.get("/download/ada-quests.csv")
def download_csv() -> Response:
    return Response(
        ADA_CSV_FILE.read_text(encoding="utf-8"),
        media_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": 'attachment; filename="ADA_PROJECT_QUESTS.csv"'},
    )


@router.get("/download/ada-project-path.md")
def download_project_path() -> Response:
    return Response(
        ADA_PATH_FILE.read_text(encoding="utf-8"),
        media_type="text/markdown; charset=utf-8",
        headers={"Content-Disposition": 'attachment; filename="ADA_PROJECT_PATH.md"'},
    )


INTEGRATION_CSS = r"""
.cq-language-switcher {
  margin: 12px;
  padding: 12px;
  border: 1px solid rgba(209, 171, 85, .52);
  border-radius: 9px;
  background: rgba(8, 14, 24, .9);
  color: #eef3fb;
  font-family: system-ui, sans-serif;
}
.cq-language-switcher.cq-floating {
  position: fixed;
  z-index: 10000;
  top: 12px;
  right: 12px;
  width: 220px;
  box-shadow: 0 10px 28px rgba(0,0,0,.35);
}
.cq-language-switcher label {
  display: block;
  margin-bottom: 6px;
  color: #e6c676;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .1em;
  text-transform: uppercase;
}
.cq-language-switcher select {
  width: 100%;
  padding: 8px 9px;
  border: 1px solid #526079;
  border-radius: 7px;
  color: #eef3fb;
  background: #101827;
  font: inherit;
}
.cq-ada-root {
  color: var(--text, #e9eef7);
  font-family: inherit;
}
.cq-ada-toolbar,
.cq-ada-summary,
.cq-ada-next,
.cq-ada-card,
.cq-ada-detail {
  border: 1px solid var(--border, #35445c);
  border-radius: 11px;
  background: var(--panel, rgba(13, 23, 38, .96));
  box-shadow: 0 10px 24px rgba(0,0,0,.18);
}
.cq-ada-summary,
.cq-ada-next {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 18px;
  margin-bottom: 14px;
  padding: 18px;
}
.cq-ada-summary h1,
.cq-ada-summary h2,
.cq-ada-next h2,
.cq-ada-card h3,
.cq-ada-detail h2,
.cq-ada-detail h3 {
  margin-top: 4px;
  margin-bottom: 6px;
}
.cq-ada-eyebrow,
.cq-ada-meta {
  color: var(--accent, #e6c676);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .1em;
  text-transform: uppercase;
}
.cq-ada-muted { color: var(--muted, #a9b4c6); }
.cq-ada-count {
  color: var(--accent, #e6c676);
  font-size: 28px;
  font-weight: 900;
  white-space: nowrap;
}
.cq-ada-toolbar {
  display: grid;
  grid-template-columns: minmax(180px, 2fr) repeat(3, minmax(140px, 1fr)) auto;
  gap: 9px;
  margin-bottom: 14px;
  padding: 13px;
}
.cq-ada-toolbar input,
.cq-ada-toolbar select,
.cq-ada-detail textarea {
  width: 100%;
  box-sizing: border-box;
  padding: 9px 10px;
  border: 1px solid var(--border, #526079);
  border-radius: 7px;
  color: var(--text, #eef3fb);
  background: #080e17;
  font: inherit;
}
.cq-ada-grid { display: grid; gap: 10px; }
.cq-ada-card {
  display: grid;
  grid-template-columns: 52px minmax(0,1fr) auto;
  gap: 14px;
  align-items: center;
  padding: 15px;
}
.cq-ada-card[data-status="mastered"] { border-color: #43c979; }
.cq-ada-card[data-status="review"] { border-color: #e6a84e; }
.cq-ada-level {
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border-radius: 999px;
  color: #08101b;
  background: #68a8ef;
  font-weight: 900;
}
.cq-ada-card[data-status="mastered"] .cq-ada-level { background: #43c979; }
.cq-ada-card p { margin-bottom: 0; }
.cq-ada-button,
.cq-ada-link {
  display: inline-block;
  padding: 9px 13px;
  border: 1px solid #9b7833;
  border-radius: 7px;
  color: #171208 !important;
  background: var(--accent, #e6c676);
  font: inherit;
  font-weight: 800;
  text-align: center;
  text-decoration: none !important;
  cursor: pointer;
}
.cq-ada-link.secondary,
.cq-ada-button.secondary {
  color: var(--text, #e9eef7) !important;
  background: transparent;
  border-color: var(--border, #526079);
}
.cq-ada-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 9px;
  align-items: center;
}
.cq-ada-pager {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  align-items: center;
  margin: 14px 0;
}
.cq-ada-detail { padding: 20px; }
.cq-ada-detail pre {
  overflow-x: auto;
  padding: 14px;
  border: 1px solid var(--border, #35445c);
  border-radius: 8px;
  background: #080e17;
}
.cq-ada-rubric {
  margin: 12px 0;
  padding: 12px 16px;
  border: 1px solid #526079;
  border-radius: 8px;
  background: rgba(9,16,27,.72);
}
.cq-ada-notice {
  margin: 12px 0;
  padding: 12px;
  border: 1px solid #68a8ef;
  border-radius: 8px;
  color: #bcd9ff;
}

.cq-project-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  gap: 10px;
  margin-bottom: 14px;
}
.cq-project-card {
  padding: 14px;
  border: 1px solid var(--border, #35445c);
  border-radius: 10px;
  background: var(--panel, rgba(13, 23, 38, .96));
}
.cq-project-card h3 { margin: 5px 0; }
.cq-project-progress {
  margin-top: 10px;
  color: var(--accent, #e6c676);
  font-weight: 800;
}
.cq-workspace-box {
  margin: 12px 0;
  padding: 12px;
  border: 1px solid var(--border, #526079);
  border-radius: 8px;
  background: rgba(9,16,27,.72);
}

@media (max-width: 900px) {
  .cq-ada-toolbar { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 700px) {
  .cq-ada-summary,
  .cq-ada-next { align-items: flex-start; flex-direction: column; }
  .cq-ada-toolbar { grid-template-columns: 1fr; }
  .cq-ada-card { grid-template-columns: 44px minmax(0,1fr); }
  .cq-ada-card .cq-ada-link { grid-column: 1 / -1; }
}
"""


INTEGRATION_JS = r"""
(() => {
  const esc = (value) => String(value ?? "").replace(/[&<>\"']/g, (ch) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;", "'": "&#039;"
  }[ch]));

  const requestJson = async (url, options = {}) => {
    const response = await fetch(url, {cache: "no-store", ...options});
    if (!response.ok) throw new Error(`${response.status} ${response.statusText}`);
    return response.json();
  };

  const sidebarScore = (element) => {
    const links = [...element.querySelectorAll("a")].map((a) => `${a.textContent} ${a.getAttribute("href") || ""}`.toLowerCase());
    let score = 0;
    if (links.some((v) => v.includes("dashboard") || v.includes("/"))) score += 2;
    if (links.some((v) => v.includes("/quests") || v.includes("quests"))) score += 4;
    if (links.some((v) => v.includes("/map") || v.includes("map"))) score += 4;
    if (element.matches("aside, nav, [class*='sidebar'], [id*='sidebar']")) score += 5;
    return score;
  };

  const findSidebar = () => {
    const candidates = [...document.querySelectorAll("aside, nav, [class*='sidebar'], [id*='sidebar']")];
    candidates.sort((a, b) => sidebarScore(b) - sidebarScore(a));
    return candidates[0] || null;
  };

  const installSwitcher = (state) => {
    if (document.getElementById("cq-language-switcher")) return;

    const wrapper = document.createElement("div");
    wrapper.id = "cq-language-switcher";
    wrapper.className = "cq-language-switcher";

    const options = (state.tracks || [])
      .map((track) => `<option value="${esc(track.id)}" ${track.enabled ? "" : "disabled"}>${esc(track.name)}${track.enabled ? "" : " — coming later"}</option>`)
      .join("");

    wrapper.innerHTML = `<form method="post" action="/learning/tracks/select">
      <input type="hidden" name="return_to" value="${esc(location.pathname + location.search)}">
      <label for="cq-language-select">Learning Language</label>
      <select id="cq-language-select" name="track_id">${options}</select>
    </form>`;

    const select = wrapper.querySelector("select");
    select.value = state.active_track;
    select.addEventListener("change", () => select.form.submit());

    const sidebar = findSidebar();
    if (sidebar) {
      const questLink = [...sidebar.querySelectorAll("a")].find((a) => (a.getAttribute("href") || "").startsWith("/quests"));
      const target = questLink?.parentElement || sidebar;
      target.insertAdjacentElement(questLink ? "afterend" : "beforeend", wrapper);
    } else {
      wrapper.classList.add("cq-floating");
      document.body.appendChild(wrapper);
    }
  };

  const visibleArea = (element) => {
    const rect = element.getBoundingClientRect();
    if (rect.width < 250 || rect.height < 120) return 0;
    return rect.width * rect.height;
  };

  const findQuestHost = () => {
    const textTarget = [...document.querySelectorAll("h1,h2,h3,section,div")]
      .filter((element) => {
        const text = (element.textContent || "").trim().toLowerCase();
        return text === "current grind" || text === "new spawn" || text.startsWith("current grind ");
      })
      .sort((a, b) => visibleArea(a) - visibleArea(b))[0];

    if (textTarget) {
      const host = textTarget.closest("main, [role='main'], .main-content, #main-content, .content, #content, section");
      if (host && !host.matches("aside,nav") && !findSidebar()?.contains(host)) return host;
    }

    const selectors = [
      "[role='main']", "main", "#main-content", ".main-content", ".page-content", ".content-area", "#content", ".content"
    ];
    const candidates = [...new Set(selectors.flatMap((selector) => [...document.querySelectorAll(selector)]))]
      .filter((element) => !element.matches("aside,nav") && !findSidebar()?.contains(element));

    candidates.sort((a, b) => visibleArea(b) - visibleArea(a));
    for (const candidate of candidates) {
      const direct = [...candidate.children]
        .filter((child) => !child.matches("aside,nav,[class*='sidebar'],[id*='sidebar']"))
        .sort((a, b) => visibleArea(b) - visibleArea(a));
      if (candidate.querySelector("aside,nav,[class*='sidebar'],[id*='sidebar']") && direct[0]) return direct[0];
      return candidate;
    }

    const fallback = document.createElement("main");
    fallback.style.margin = "24px";
    document.body.appendChild(fallback);
    return fallback;
  };

  const orderedList = (items) => items?.length
    ? `<ol>${items.map((item) => `<li>${esc(item)}</li>`).join("")}</ol>`
    : "";

  const state = {
    offset: 0,
    limit: 30,
    stage: "",
    kind: "",
    search: "",
    status: "",
    total: 0,
  };

  const setQuestUrl = (slug = "") => {
    const url = new URL(location.href);
    if (slug) url.searchParams.set("quest", slug);
    else url.searchParams.delete("quest");
    history.pushState({}, "", url);
  };

  const showQuest = async (root, slug) => {
    const data = await requestJson(`/learning/api/ada/quest/${encodeURIComponent(slug)}`);
    const quest = data.quest;
    const progress = data.progress || {};

    root.innerHTML = `<div class="cq-ada-root cq-ada-detail">
      <div class="cq-ada-actions">
        <button class="cq-ada-button secondary" id="cq-back-to-list">← Project Quest List</button>
        <a class="cq-ada-link secondary" href="/learning/download/ada-project-path.md">Project Path</a>
        <a class="cq-ada-link secondary" href="/learning/download/ada-quests.csv">CSV</a>
        <a class="cq-ada-link secondary" href="/learning/download/ada-quests.json">JSON</a>
      </div>
      <div class="cq-ada-eyebrow">${esc(quest.quest_id)} · Level ${esc(quest.level)} · ${esc(quest.kind)} · ${esc(quest.xp)} XP</div>
      <h2>${esc(quest.title)}</h2>
      <p class="cq-ada-muted">${esc(quest.summary)}</p>
      <p><strong>Project:</strong> ${esc(quest.project_name)}<br><strong>Chapter:</strong> ${esc(quest.chapter_name)}<br><strong>Concept:</strong> ${esc(quest.concept)}</p>
      <div class="cq-workspace-box"><strong>Workspace</strong><pre><code>${esc(quest.workspace)}</code></pre><strong>Primary files</strong>${orderedList(quest.source_files || [])}</div>
      <h3>Quest</h3>
      <p>${esc(quest.prompt)}</p>
      ${quest.instructions?.length ? `<h3>Steps</h3>${orderedList(quest.instructions)}` : ""}
      ${quest.acceptance?.length ? `<h3>Completion checks</h3>${orderedList(quest.acceptance)}` : ""}
      ${quest.alire_commands ? `<h3>Alire workflow</h3><pre><code>${esc(quest.alire_commands)}</code></pre>` : ""}
      <h3>Your answer or engineering notes</h3>
      <textarea id="cq-answer" rows="10">${esc(progress.last_answer || "")}</textarea>
      <div class="cq-ada-actions" style="margin-top:10px">
        <button class="cq-ada-button" id="cq-save-answer">Save Answer and Show Rubric</button>
        <button class="cq-ada-button" id="cq-mark-mastered">I Got It</button>
        <button class="cq-ada-button secondary" id="cq-mark-review">Review Again Tomorrow</button>
      </div>
      <div id="cq-result"></div>
    </div>`;

    root.querySelector("#cq-back-to-list").addEventListener("click", () => {
      setQuestUrl("");
      renderList(root, window.cqAdaState);
    });

    root.querySelector("#cq-save-answer").addEventListener("click", async () => {
      const answer = root.querySelector("#cq-answer").value;
      const result = await requestJson(`/learning/api/ada/quest/${encodeURIComponent(slug)}/answer`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({answer}),
      });
      root.querySelector("#cq-result").innerHTML = `<div class="cq-ada-notice">${esc(result.message)}</div>
        <div class="cq-ada-rubric"><strong>Rubric</strong>${orderedList(result.rubric)}</div>`;
    });

    const record = async (result) => {
      const response = await requestJson(`/learning/api/ada/quest/${encodeURIComponent(slug)}/result`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({result}),
      });
      root.querySelector("#cq-result").innerHTML = `<div class="cq-ada-notice">Saved as ${esc(response.progress.status)}. Next review: ${esc(response.progress.next_review)}</div>`;
    };

    root.querySelector("#cq-mark-mastered").addEventListener("click", () => record("mastered"));
    root.querySelector("#cq-mark-review").addEventListener("click", () => record("review"));
  };

  const renderList = async (root, appState) => {
    const params = new URLSearchParams({
      offset: String(state.offset), limit: String(state.limit), stage: state.stage,
      kind: state.kind, search: state.search, status: state.status,
    });
    const data = await requestJson(`/learning/api/ada/quests?${params}`);
    state.total = data.total;

    const stages = (appState.ada.stages || []).map((stage) => `<option value="${esc(stage.id)}">${esc(stage.name)} (${esc(stage.quest_count)})</option>`).join("");
    const projectCards = (appState.ada.projects || []).map((project) => `<article class="cq-project-card"><div class="cq-ada-eyebrow">${esc(project.short_name)}</div><h3>${esc(project.name)}</h3><p class="cq-ada-muted">${esc(project.goal)}</p><div class="cq-project-progress">${esc(project.mastered)} / ${esc(project.total)} mastered</div><button class="cq-ada-link secondary cq-project-filter" data-project="${esc(project.id)}" style="margin-top:9px">Open project</button></article>`).join("");
    const kinds = (appState.ada.kinds || []).map((kind) => `<option value="${esc(kind)}">${esc(kind)}</option>`).join("");
    const cards = data.items.map((quest) => `<article class="cq-ada-card" data-status="${esc(quest.status)}">
      <div class="cq-ada-level">${esc(quest.level)}</div>
      <div>
        <div class="cq-ada-meta">${esc(quest.quest_id)} · ${esc(quest.kind)} · ${esc(quest.project_name)} · ${esc(quest.chapter_name)} · ${esc(quest.xp)} XP</div>
        <h3>${esc(quest.title)}</h3>
        <p class="cq-ada-muted">${esc(quest.summary)}</p>
      </div>
      <button class="cq-ada-link cq-open-quest" data-slug="${esc(quest.slug)}">${quest.status === "mastered" ? "Review" : "Open"}</button>
    </article>`).join("");

    const start = data.total ? data.offset + 1 : 0;
    const end = Math.min(data.offset + data.limit, data.total);
    const next = appState.ada.next_quest;

    root.innerHTML = `<div class="cq-ada-root">
      <section class="cq-ada-summary">
        <div>
          <div class="cq-ada-eyebrow">ACTIVE LANGUAGE · ADA</div>
          <h1>Ada Project Mastery</h1>
          <p class="cq-ada-muted">${esc(appState.ada.total)} cumulative quests across ${esc(appState.ada.project_count)} long-lived Alire projects and ${esc(appState.ada.chapter_count)} project chapters.</p>
        </div>
        <div>
          <div class="cq-ada-count">${esc(appState.ada.mastered)} / ${esc(appState.ada.total)}</div>
          <div class="cq-ada-muted">Mastered</div>
        </div>
      </section>
      <section class="cq-project-grid">${projectCards}</section>
      ${next ? `<section class="cq-ada-next"><div><div class="cq-ada-eyebrow">DO THIS NEXT</div><h2>${esc(next.title)}</h2><p class="cq-ada-muted">${esc(next.summary)}</p></div><button class="cq-ada-link" id="cq-open-next">Start</button></section>` : ""}
      <div class="cq-ada-actions" style="margin-bottom:14px">
        <a class="cq-ada-link secondary" href="/learning/download/ada-project-path.md">Offline Project Path</a>
        <a class="cq-ada-link secondary" href="/learning/download/ada-quests.csv">Offline CSV</a>
        <a class="cq-ada-link secondary" href="/learning/download/ada-quests.json">Editable JSON</a>
      </div>
      <section class="cq-ada-toolbar">
        <input id="cq-search" value="${esc(state.search)}" placeholder="Search ${esc(appState.ada.total)} project quests">
        <select id="cq-stage"><option value="">All projects</option>${stages}</select>
        <select id="cq-kind"><option value="">All quest types</option>${kinds}</select>
        <select id="cq-status"><option value="">All progress</option><option value="new">New</option><option value="attempted">Attempted</option><option value="review">Review</option><option value="mastered">Mastered</option></select>
        <button class="cq-ada-button" id="cq-filter">Apply</button>
      </section>
      <div class="cq-ada-pager"><span>Showing ${start}-${end} of ${data.total}</span><div class="cq-ada-actions"><button class="cq-ada-button secondary" id="cq-prev" ${state.offset === 0 ? "disabled" : ""}>Previous</button><button class="cq-ada-button secondary" id="cq-next" ${state.offset + state.limit >= data.total ? "disabled" : ""}>Next</button></div></div>
      <section class="cq-ada-grid">${cards || "<p>No quests matched these filters.</p>"}</section>
    </div>`;

    root.querySelector("#cq-stage").value = state.stage;
    root.querySelector("#cq-kind").value = state.kind;
    root.querySelector("#cq-status").value = state.status;

    root.querySelectorAll(".cq-open-quest").forEach((button) => button.addEventListener("click", () => {
      setQuestUrl(button.dataset.slug);
      showQuest(root, button.dataset.slug);
    }));

    root.querySelectorAll(".cq-project-filter").forEach((button) => button.addEventListener("click", () => {
      state.stage = button.dataset.project;
      state.offset = 0;
      renderList(root, appState);
    }));

    root.querySelector("#cq-open-next")?.addEventListener("click", () => {
      setQuestUrl(next.slug);
      showQuest(root, next.slug);
    });

    root.querySelector("#cq-filter").addEventListener("click", () => {
      state.search = root.querySelector("#cq-search").value.trim();
      state.stage = root.querySelector("#cq-stage").value;
      state.kind = root.querySelector("#cq-kind").value;
      state.status = root.querySelector("#cq-status").value;
      state.offset = 0;
      renderList(root, appState);
    });

    root.querySelector("#cq-prev").addEventListener("click", () => {
      state.offset = Math.max(0, state.offset - state.limit);
      renderList(root, appState);
    });
    root.querySelector("#cq-next").addEventListener("click", () => {
      state.offset += state.limit;
      renderList(root, appState);
    });
  };

  const initialize = async () => {
    let appState;
    try {
      appState = await requestJson("/learning/api/state");
    } catch (error) {
      console.error("CodeQuest language tracks failed:", error);
      return;
    }

    window.cqAdaState = appState;
    installSwitcher(appState);

    if (location.pathname !== "/quests" || appState.active_track !== "ada") return;

    const root = findQuestHost();
    root.classList.add("cq-ada-host");
    const slug = new URL(location.href).searchParams.get("quest");
    if (slug) await showQuest(root, slug);
    else await renderList(root, appState);
  };

  window.addEventListener("popstate", () => location.reload());
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initialize);
  else initialize();
})();
"""


@router.get("/assets/integration.css")
def integration_css() -> Response:
    return Response(INTEGRATION_CSS, media_type="text/css; charset=utf-8")


@router.get("/assets/integration.js")
def integration_js() -> Response:
    return Response(INTEGRATION_JS, media_type="application/javascript; charset=utf-8")


class CQLanguageInjectionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        content_type = response.headers.get("content-type", "")
        if request.method != "GET" or "text/html" not in content_type.lower():
            return response

        try:
            body = b"".join([chunk async for chunk in response.body_iterator])
            text = body.decode("utf-8")
        except (UnicodeDecodeError, AttributeError):
            return response

        marker = "cq-language-integration-v6"
        if marker not in text and "</head>" in text.lower():
            insertion = (
                f'<link id="{marker}" rel="stylesheet" href="/learning/assets/integration.css?v=6">'
                '<script defer src="/learning/assets/integration.js?v=6"></script>'
            )
            lower = text.lower()
            index = lower.rfind("</head>")
            text = text[:index] + insertion + text[index:]

        rebuilt = Response(
            content=text.encode("utf-8"),
            status_code=response.status_code,
            background=response.background,
        )
        rebuilt.raw_headers = [
            (key, value)
            for key, value in response.raw_headers
            if key.lower() not in {b"content-length", b"content-encoding"}
        ]
        rebuilt.headers["content-length"] = str(len(text.encode("utf-8")))
        return rebuilt


def install_learning_track_support(app) -> None:
    if getattr(app.state, "cq_language_tracks_installed", False):
        return
    app.add_middleware(CQLanguageInjectionMiddleware)
    app.state.cq_language_tracks_installed = True
