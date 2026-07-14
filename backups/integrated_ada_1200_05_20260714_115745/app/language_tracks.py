from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from fastapi import APIRouter, Body, FastAPI, Form, Request
from fastapi.responses import RedirectResponse, Response

router = APIRouter(prefix="/learning", tags=["learning"])

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
TRACKS_FILE = DATA_DIR / "language_tracks.json"
PROFILE_FILE = DATA_DIR / "learning_profile.json"
ADA_QUESTS_FILE = DATA_DIR / "ada_quests.json"
ADA_PROGRESS_FILE = DATA_DIR / "ada_progress.json"


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
    value = _read_json(TRACKS_FILE, {"tracks": []}).get("tracks", [])
    return value if isinstance(value, list) else []


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


def _ada_quests() -> list[dict[str, Any]]:
    value = _read_json(ADA_QUESTS_FILE, {"quests": []}).get("quests", [])
    return value if isinstance(value, list) else []


def _ada_progress() -> dict[str, Any]:
    return _read_json(
        ADA_PROGRESS_FILE,
        {
            "completed": [],
            "attempts": {},
            "last_answer": {},
            "active_quest": "alire-first-crate",
        },
    )


def _find_track(track_id: str) -> dict[str, Any] | None:
    return next((track for track in _tracks() if track.get("id") == track_id), None)


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
        if completed_count < required:
            break
        current = name
        if index + 1 < len(ranks):
            next_at, next_name = ranks[index + 1]

    return current, next_name, next_at


def _answer_is_correct(answer: str, accepted_groups: list[str]) -> bool:
    normalized = answer.casefold()
    for group in accepted_groups:
        alternatives = [part.strip().casefold() for part in group.split("|") if part.strip()]
        if not alternatives:
            continue
        if not any(alternative in normalized for alternative in alternatives):
            return False
    return True


def _markdown_curriculum() -> str:
    lines = [
        "# CodeQuest Forge — Ada Quest List",
        "",
        "This file is generated from `data/ada_quests.json`.",
        "",
    ]
    for quest in _ada_quests():
        lines.extend(
            [
                f"## Level {quest.get('level', '?')} — {quest.get('title', 'Untitled')}",
                "",
                f"- **Type:** {quest.get('kind', '')}",
                f"- **Concept:** {quest.get('concept', '')}",
                f"- **Difficulty:** {quest.get('difficulty', '')}",
                f"- **XP:** {quest.get('xp', 0)}",
                "",
                str(quest.get("summary", "")),
                "",
            ]
        )
        instructions = quest.get("instructions", [])
        if instructions:
            lines.append("### Instructions")
            lines.append("")
            lines.extend(f"{index}. {item}" for index, item in enumerate(instructions, start=1))
            lines.append("")
        acceptance = quest.get("acceptance", [])
        if acceptance:
            lines.append("### Completion checks")
            lines.append("")
            lines.extend(f"- {item}" for item in acceptance)
            lines.append("")
        if quest.get("question"):
            lines.extend(["### Question", "", str(quest["question"]), ""])
        if quest.get("commands"):
            lines.extend(["### Commands", "", "```bash", str(quest["commands"]), "```", ""])
        if quest.get("starter_code"):
            lines.extend(["### Starter code", "", "```ada", str(quest["starter_code"]), "```", ""])
    return "\n".join(lines).rstrip() + "\n"


@router.post("/tracks/select")
def select_track(track_id: str = Form(...), return_to: str = Form("/quests")):
    track = _find_track(track_id)
    if track is None or not track.get("enabled", False):
        return RedirectResponse("/quests?language_error=unavailable", status_code=303)

    profile = _profile()
    profile["active_track"] = track_id
    stages = track.get("stages", [])
    profile["active_stage"] = stages[0].get("id", "") if stages else ""
    _write_json(PROFILE_FILE, profile)

    safe_return = return_to if return_to.startswith("/") and not return_to.startswith("//") else "/quests"
    return RedirectResponse(safe_return, status_code=303)


@router.post("/tracks/stage")
def select_stage(stage_id: str = Form(...)):
    profile = _profile()
    profile["active_stage"] = stage_id
    _write_json(PROFILE_FILE, profile)
    return RedirectResponse("/quests", status_code=303)


@router.get("/tracks")
def tracks_home():
    return RedirectResponse("/quests", status_code=302)


@router.get("/ada")
def ada_home():
    return RedirectResponse("/quests", status_code=302)


@router.get("/ada/quests")
def old_ada_quests():
    return RedirectResponse("/quests", status_code=302)


@router.get("/ada/quest/{slug}")
def old_ada_quest(slug: str):
    return RedirectResponse(f"/quests?quest={slug}", status_code=302)


@router.get("/api/state")
def learning_state():
    profile = _profile()
    active_track = str(profile.get("active_track", "ada"))
    tracks = [
        {
            "id": str(track.get("id", "")),
            "name": str(track.get("name", "")),
            "enabled": bool(track.get("enabled", False)),
        }
        for track in _tracks()
    ]

    result: dict[str, Any] = {
        "active_track": active_track,
        "tracks": tracks,
    }

    if active_track == "ada":
        quests = _ada_quests()
        progress = _ada_progress()
        completed = list(dict.fromkeys(str(item) for item in progress.get("completed", [])))
        current_title, next_title, next_at = _title_progress(len(completed))
        next_quest = next((quest for quest in quests if quest.get("slug") not in completed), None)
        result.update(
            {
                "quests": quests,
                "progress": {
                    "completed": completed,
                    "attempts": progress.get("attempts", {}),
                    "last_answer": progress.get("last_answer", {}),
                    "active_quest": progress.get("active_quest", ""),
                },
                "rank": {
                    "current": current_title,
                    "next": next_title,
                    "next_at": next_at,
                },
                "next_quest": next_quest,
            }
        )

    return result


@router.post("/api/ada/quest/{slug}/answer")
def answer_ada_quest(slug: str, payload: dict[str, Any] = Body(...)):
    quest = _find_ada_quest(slug)
    if quest is None:
        return Response(
            content=json.dumps({"ok": False, "error": "Unknown quest"}),
            status_code=404,
            media_type="application/json",
        )

    answer = str(payload.get("answer", "")).strip()
    accepted = [str(value) for value in quest.get("accepted_keywords", [])]
    correct = bool(accepted) and _answer_is_correct(answer, accepted)

    progress = _ada_progress()
    attempts = progress.setdefault("attempts", {})
    attempts[slug] = int(attempts.get(slug, 0)) + 1
    progress.setdefault("last_answer", {})[slug] = answer
    progress["active_quest"] = slug

    if correct:
        completed = progress.setdefault("completed", [])
        if slug not in completed:
            completed.append(slug)

    _write_json(ADA_PROGRESS_FILE, progress)
    return {"ok": True, "correct": correct, "attempts": attempts[slug]}


@router.post("/api/ada/quest/{slug}/complete")
def complete_ada_quest(slug: str):
    if _find_ada_quest(slug) is None:
        return Response(
            content=json.dumps({"ok": False, "error": "Unknown quest"}),
            status_code=404,
            media_type="application/json",
        )

    progress = _ada_progress()
    completed = progress.setdefault("completed", [])
    if slug not in completed:
        completed.append(slug)
    progress["active_quest"] = slug
    _write_json(ADA_PROGRESS_FILE, progress)
    return {"ok": True, "completed": True}


@router.get("/download/ada-quests.json")
def download_ada_json():
    content = ADA_QUESTS_FILE.read_text(encoding="utf-8")
    return Response(
        content=content,
        media_type="application/json",
        headers={"Content-Disposition": 'attachment; filename="ADA_QUESTS.json"'},
    )


@router.get("/download/ada-quests.md")
def download_ada_markdown():
    return Response(
        content=_markdown_curriculum(),
        media_type="text/markdown; charset=utf-8",
        headers={"Content-Disposition": 'attachment; filename="ADA_QUESTS.md"'},
    )


INTEGRATION_CSS = r"""
.cq-language-switcher {
  margin: 14px 10px;
  padding: 12px;
  border: 1px solid rgba(208, 170, 83, .45);
  border-radius: 9px;
  background: rgba(7, 13, 24, .72);
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
#cq-language-quest-root[hidden],
#cq-native-quest-content[hidden] {
  display: none !important;
}
.cq-track-panel {
  color: var(--text, #e9eef7);
}
.cq-track-header,
.cq-next-quest,
.cq-quest-card,
.cq-quest-detail {
  border: 1px solid var(--border, #35445c);
  border-radius: 11px;
  background: var(--panel, rgba(13, 23, 38, .94));
  box-shadow: 0 10px 24px rgba(0, 0, 0, .18);
}
.cq-track-header,
.cq-next-quest {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  align-items: center;
  margin-bottom: 14px;
  padding: 18px;
}
.cq-track-eyebrow,
.cq-quest-meta {
  color: var(--accent, #e6c676);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .1em;
  text-transform: uppercase;
}
.cq-track-header h1,
.cq-track-header h2,
.cq-next-quest h2,
.cq-quest-card h3,
.cq-quest-detail h2,
.cq-quest-detail h3 {
  margin-top: 4px;
  margin-bottom: 6px;
}
.cq-track-muted {
  color: var(--muted, #a9b4c6);
}
.cq-track-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 9px;
  align-items: center;
}
.cq-track-button,
.cq-track-link {
  display: inline-block;
  padding: 9px 13px;
  border: 1px solid #9b7833;
  border-radius: 7px;
  color: #171208 !important;
  background: var(--accent, #e6c676);
  font-weight: 800;
  text-decoration: none !important;
  cursor: pointer;
}
.cq-track-link.secondary {
  color: var(--text, #e9eef7) !important;
  background: transparent;
  border-color: var(--border, #526079);
}
.cq-progress-number {
  color: var(--accent, #e6c676);
  font-size: 28px;
  font-weight: 900;
  white-space: nowrap;
}
.cq-quest-grid {
  display: grid;
  gap: 10px;
}
.cq-quest-card {
  display: grid;
  grid-template-columns: 46px minmax(0, 1fr) auto;
  gap: 14px;
  align-items: center;
  padding: 15px;
}
.cq-quest-card.completed {
  border-color: #43c979;
}
.cq-quest-level {
  display: grid;
  place-items: center;
  width: 40px;
  height: 40px;
  border-radius: 999px;
  color: #08101b;
  background: #68a8ef;
  font-weight: 900;
}
.cq-quest-card.completed .cq-quest-level {
  background: #43c979;
}
.cq-quest-card p {
  margin-bottom: 0;
}
.cq-quest-detail {
  padding: 20px;
}
.cq-quest-detail pre {
  overflow-x: auto;
  padding: 14px;
  border: 1px solid var(--border, #35445c);
  border-radius: 8px;
  background: #080e17;
}
.cq-quest-detail textarea {
  width: 100%;
  min-height: 120px;
  box-sizing: border-box;
  padding: 12px;
  border: 1px solid var(--border, #526079);
  border-radius: 8px;
  color: var(--text, #eef3fb);
  background: #080e17;
  font: inherit;
}
.cq-result {
  margin: 12px 0;
  padding: 12px;
  border-radius: 8px;
  font-weight: 800;
}
.cq-result.good {
  border: 1px solid #43c979;
  color: #43c979;
}
.cq-result.review {
  border: 1px solid #e6c676;
  color: #e6c676;
}
@media (max-width: 760px) {
  .cq-track-header,
  .cq-next-quest {
    align-items: flex-start;
    flex-direction: column;
  }
  .cq-quest-card {
    grid-template-columns: 42px minmax(0, 1fr);
  }
  .cq-quest-card .cq-track-link {
    grid-column: 1 / -1;
    text-align: center;
  }
}
"""


INTEGRATION_JS = r"""
(() => {
  const escapeHtml = (value) => String(value ?? "").replace(/[&<>\"']/g, (char) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;", "'": "&#039;"
  }[char]));

  const api = async (url, options = {}) => {
    const response = await fetch(url, {cache: "no-store", ...options});
    if (!response.ok) throw new Error(`Request failed: ${response.status}`);
    return response.json();
  };

  const hydrateSelectors = (state) => {
    document.querySelectorAll(".cq-language-select").forEach((select) => {
      select.value = state.active_track;
    });
  };

  const listItems = (items) => items?.length
    ? `<ol>${items.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ol>`
    : "";

  const renderQuestDetail = (root, state, quest) => {
    const completed = new Set(state.progress?.completed || []);
    const lastAnswer = state.progress?.last_answer?.[quest.slug] || "";
    const question = quest.question
      ? `<section><h3>Question</h3><p>${escapeHtml(quest.question)}</p>
          <form id="cq-answer-form">
            <textarea name="answer" required>${escapeHtml(lastAnswer)}</textarea>
            <button class="cq-track-button" type="submit">Check Answer</button>
          </form>
          <div id="cq-answer-result"></div></section>`
      : `<button id="cq-complete-button" class="cq-track-button" type="button">
           ${completed.has(quest.slug) ? "Completed — Mark Again" : "Mark Quest Complete"}
         </button>`;

    root.innerHTML = `<div class="cq-track-panel cq-quest-detail">
      <div class="cq-track-actions">
        <a class="cq-track-link secondary" href="/quests">← All Ada Quests</a>
        <a class="cq-track-link secondary" href="/learning/download/ada-quests.md">Offline Quest List</a>
      </div>
      <div class="cq-track-eyebrow">Level ${escapeHtml(quest.level)} · ${escapeHtml(quest.kind)} · ${escapeHtml(quest.xp)} XP</div>
      <h2>${escapeHtml(quest.title)}</h2>
      <p class="cq-track-muted">${escapeHtml(quest.summary)}</p>
      ${quest.instructions?.length ? `<h3>Instructions</h3>${listItems(quest.instructions)}` : ""}
      ${quest.acceptance?.length ? `<h3>Completion Checks</h3>${listItems(quest.acceptance)}` : ""}
      ${quest.commands ? `<h3>Commands</h3><pre><code>${escapeHtml(quest.commands)}</code></pre>` : ""}
      ${quest.starter_code ? `<h3>Starter Code</h3><pre><code>${escapeHtml(quest.starter_code)}</code></pre>` : ""}
      ${question}
    </div>`;

    const answerForm = document.getElementById("cq-answer-form");
    if (answerForm) {
      answerForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const answer = new FormData(answerForm).get("answer");
        const result = await api(`/learning/api/ada/quest/${encodeURIComponent(quest.slug)}/answer`, {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({answer})
        });
        const box = document.getElementById("cq-answer-result");
        box.className = `cq-result ${result.correct ? "good" : "review"}`;
        box.textContent = result.correct
          ? "Correct. Quest completed."
          : "Not quite. Review the completion checks and try again.";
      });
    }

    const completeButton = document.getElementById("cq-complete-button");
    if (completeButton) {
      completeButton.addEventListener("click", async () => {
        await api(`/learning/api/ada/quest/${encodeURIComponent(quest.slug)}/complete`, {method: "POST"});
        completeButton.textContent = "Quest Completed";
      });
    }
  };

  const renderAdaList = (root, state) => {
    const quests = state.quests || [];
    const completed = new Set(state.progress?.completed || []);
    const next = state.next_quest;
    const cards = quests.map((quest) => `<article class="cq-quest-card ${completed.has(quest.slug) ? "completed" : ""}">
      <div class="cq-quest-level">${escapeHtml(quest.level)}</div>
      <div>
        <div class="cq-quest-meta">${escapeHtml(quest.kind)} · ${escapeHtml(quest.concept)} · ${escapeHtml(quest.xp)} XP</div>
        <h3>${escapeHtml(quest.title)}</h3>
        <p class="cq-track-muted">${escapeHtml(quest.summary)}</p>
      </div>
      <a class="cq-track-link" href="/quests?quest=${encodeURIComponent(quest.slug)}">
        ${completed.has(quest.slug) ? "Review" : "Open"}
      </a>
    </article>`).join("");

    root.innerHTML = `<div class="cq-track-panel">
      <section class="cq-track-header">
        <div>
          <div class="cq-track-eyebrow">ACTIVE LANGUAGE · ADA</div>
          <h1>Ada Mastery Quests</h1>
          <p class="cq-track-muted">Alire first. Repetition, systems programming, real-time Ada, and GtkAda.</p>
        </div>
        <div>
          <div class="cq-progress-number">${completed.size} / ${quests.length}</div>
          <div class="cq-track-muted">${escapeHtml(state.rank?.current || "Ada Initiate")}</div>
        </div>
      </section>
      ${next ? `<section class="cq-next-quest">
        <div>
          <div class="cq-track-eyebrow">DO THIS NEXT</div>
          <h2>${escapeHtml(next.title)}</h2>
          <p class="cq-track-muted">${escapeHtml(next.summary)}</p>
        </div>
        <a class="cq-track-link" href="/quests?quest=${encodeURIComponent(next.slug)}">Start Next Quest</a>
      </section>` : ""}
      <div class="cq-track-actions" style="margin-bottom:14px">
        <a class="cq-track-link secondary" href="/learning/download/ada-quests.md">Download Markdown Quest List</a>
        <a class="cq-track-link secondary" href="/learning/download/ada-quests.json">Download JSON Quest Data</a>
      </div>
      <section class="cq-quest-grid">${cards}</section>
    </div>`;
  };

  const initialize = async () => {
    let state;
    try {
      state = await api("/learning/api/state");
    } catch (error) {
      console.error("CodeQuest language tracks:", error);
      return;
    }

    hydrateSelectors(state);

    const root = document.getElementById("cq-language-quest-root");
    const nativeContent = document.getElementById("cq-native-quest-content");
    if (!root || !nativeContent) return;

    if (state.active_track !== "ada") {
      root.hidden = true;
      nativeContent.hidden = false;
      return;
    }

    nativeContent.hidden = true;
    root.hidden = false;

    const slug = new URLSearchParams(window.location.search).get("quest");
    if (slug) {
      const quest = (state.quests || []).find((item) => item.slug === slug);
      if (quest) {
        renderQuestDetail(root, state, quest);
        return;
      }
    }
    renderAdaList(root, state);
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initialize);
  } else {
    initialize();
  }
})();
"""


@router.get("/assets/integration.css")
def integration_css():
    return Response(content=INTEGRATION_CSS, media_type="text/css")


@router.get("/assets/quest-tracks.js")
def integration_javascript():
    return Response(content=INTEGRATION_JS, media_type="application/javascript")


def install_learning_track_support(app: FastAPI) -> None:
    """Compatibility hook retained for app/main.py from earlier patches.

    Integration now happens through the real templates and /quests page. No
    redirecting or full-page HTML middleware is installed here.
    """
    app.state.learning_track_support_installed = True
