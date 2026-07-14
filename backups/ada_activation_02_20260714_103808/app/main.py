from __future__ import annotations

from html import escape
from pathlib import Path

from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import storage
from app.language_tracks import router as language_tracks_router

ROOT = Path(__file__).resolve().parents[1]

app = FastAPI(title="CodeQuest Forge", version="0.5.3")
app.include_router(language_tracks_router)
DATA_IMAGES_DIR = ROOT / "data" / "images"
DATA_IMAGES_DIR.mkdir(parents=True, exist_ok=True)
app.mount("/static", StaticFiles(directory=ROOT / "app" / "static"), name="static")
app.mount("/images", StaticFiles(directory=DATA_IMAGES_DIR), name="images")
templates = Jinja2Templates(directory=ROOT / "app" / "templates")


def render(request: Request, template: str, **context):
    context["request"] = request
    context["state"] = storage.state()
    return templates.TemplateResponse(request=request, name=template, context=context)


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return render(request, "dashboard.html")


@app.get("/mini", response_class=HTMLResponse)
def mini(request: Request):
    return render(request, "mini.html")


@app.get("/map", response_class=HTMLResponse)
def world_map(request: Request):
    return render(request, "map.html")


@app.get("/classes", response_class=HTMLResponse)
def classes(request: Request):
    return render(request, "classes.html")


@app.get("/gear", response_class=HTMLResponse)
def gear(request: Request):
    return render(request, "gear.html")


@app.get("/books", response_class=HTMLResponse)
def books(request: Request):
    return render(request, "books.html")


@app.get("/book/{book_id}", response_class=HTMLResponse)
def book_detail(request: Request, book_id: str):
    book = storage.find_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return render(request, "book_detail.html", book=book)



@app.post("/book/{book_id}/stage")
def complete_book_stage(book_id: str, stage: str = Form(...)):
    book = storage.find_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    if not book.get("unlocked"):
        raise HTTPException(status_code=400, detail="Book is locked")
    if stage == "guide" and not book.get("show_done"):
        raise HTTPException(status_code=400, detail="Finish Show Me first")
    if stage == "test" and not book.get("guide_done"):
        raise HTTPException(status_code=400, detail="Finish Guide Me first")
    storage.mark_book_stage(book_id, stage)
    return RedirectResponse(url=f"/book/{book_id}?stage={stage}", status_code=303)


@app.post("/book/{book_id}/use-help")
def use_book_help(book_id: str):
    book = storage.find_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    if not book.get("unlocked"):
        raise HTTPException(status_code=400, detail="Book is locked")
    storage.use_book_help(book_id)
    return RedirectResponse(url=f"/book/{book_id}?help=1", status_code=303)


@app.post("/book/{book_id}/reset")
def reset_book(book_id: str):
    book = storage.find_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    storage.clear_book_progress(book_id)
    return RedirectResponse(url=f"/book/{book_id}?reset=1", status_code=303)


@app.get("/quests", response_class=HTMLResponse)
def quests(request: Request):
    return render(request, "quests.html")


@app.get("/quest/{quest_id}", response_class=HTMLResponse)
def quest_detail(request: Request, quest_id: str):
    quest = storage.find_quest(quest_id)
    if not quest:
        raise HTTPException(status_code=404, detail="Quest not found")
    return render(request, "quest_detail.html", quest=quest)


@app.post("/quest/{quest_id}/submit")
def submit_quest(
    quest_id: str,
    github_url: str = Form(...),
    screenshot_url: str = Form(""),
    release_tag: str = Form(""),
    console_output: str = Form(""),
    notes: str = Form(""),
):
    quest = storage.find_quest(quest_id)
    if not quest:
        raise HTTPException(status_code=404, detail="Quest not found")
    storage.add_submission(
        quest_id=quest_id,
        github_url=github_url.strip(),
        screenshot_url=screenshot_url.strip() or None,
        release_tag=release_tag.strip() or None,
        console_output=console_output.strip() or None,
        notes=notes.strip() or None,
    )
    return RedirectResponse(url=f"/quest/{quest_id}?submitted=1", status_code=303)


@app.post("/quest/{quest_id}/complete")
def complete_quest(quest_id: str):
    quest = storage.find_quest(quest_id)
    if not quest:
        raise HTTPException(status_code=404, detail="Quest not found")
    storage.mark_quest_complete(quest_id)
    return RedirectResponse(url=f"/quest/{quest_id}?completed=1", status_code=303)


@app.post("/quest/{quest_id}/undo")
def undo_quest(quest_id: str):
    quest = storage.find_quest(quest_id)
    if not quest:
        raise HTTPException(status_code=404, detail="Quest not found")
    storage.clear_quest_override(quest_id)
    return RedirectResponse(url=f"/quest/{quest_id}?undone=1", status_code=303)




@app.get("/admin", response_class=HTMLResponse)
def admin(request: Request):
    return render(request, "admin.html")


@app.post("/admin/level")
def admin_set_level(level: int = Form(...)):
    storage.set_dev_level(level)
    return RedirectResponse(url="/admin?level=1", status_code=303)


@app.post("/admin/xp")
def admin_adjust_xp(delta: int = Form(...)):
    storage.adjust_dev_xp(delta)
    return RedirectResponse(url="/admin?xp=1", status_code=303)


@app.post("/admin/clear-dev")
def admin_clear_dev():
    storage.clear_dev_state()
    return RedirectResponse(url="/admin?cleared=1", status_code=303)


@app.get("/api/state")
def api_state():
    return storage.state()


@app.post("/reset")
def reset():
    storage.reset_local_progress()
    return RedirectResponse(url="/", status_code=303)


@app.get("/lock-card.svg")
def lock_card_svg():
    s = storage.state()
    p = s["profile"]
    active = next((q for q in s["quests"] if q["status"] in {"Available", "In Progress", "Pending Review"}), next((q for q in s["quests"] if q["status"] != "Hidden"), s["quests"][0]))
    progress = int((p["xp"] / p["xp_next"]) * 100)
    class_lines = "".join(
        f'<text x="54" y="{610 + i*44}" class="small">{escape(c["name"])} · Lv {c["level"]}</text>'
        f'<rect x="315" y="{596 + i*44}" width="220" height="12" rx="6" class="bar" />'
        f'<rect x="315" y="{596 + i*44}" width="{int(220 * c["xp"] / c["xp_next"])}" height="12" rx="6" class="fill" />'
        for i, c in enumerate(s["classes"])
    )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1170" height="2532" viewBox="0 0 1170 2532">
      <defs>
        <linearGradient id="g" x1="0" x2="1" y1="0" y2="1">
          <stop stop-color="#090d16" offset="0"/><stop stop-color="#14102b" offset="0.55"/><stop stop-color="#05070d" offset="1"/>
        </linearGradient>
        <linearGradient id="p" x1="0" x2="1"><stop stop-color="#7c3aed"/><stop offset="1" stop-color="#d946ef"/></linearGradient>
        <style>
          .title{{font:700 64px system-ui;fill:#fff}}
          .subtitle{{font:500 34px system-ui;fill:#b9b7d7}}
          .label{{font:700 30px system-ui;fill:#c084fc;letter-spacing:2px}}
          .small{{font:500 28px system-ui;fill:#e7e3ff}}
          .muted{{font:500 24px system-ui;fill:#a7a3c6}}
          .big{{font:800 170px system-ui;fill:#fff}}
          .card{{fill:#0d1320;stroke:#293147;stroke-width:3;rx:38}}
          .bar{{fill:#252a3c}}
          .fill{{fill:url(#p)}}
        </style>
      </defs>
      <rect width="1170" height="2532" fill="url(#g)"/>
      <rect x="60" y="150" width="1050" height="2100" rx="60" fill="#070b13" stroke="#30384e" stroke-width="4"/>
      <text x="100" y="270" class="title">{escape(p["name"])}</text>
      <text x="100" y="325" class="subtitle">{escape(p["epithet"])}</text>
      <text x="100" y="480" class="label">LEVEL</text>
      <text x="100" y="650" class="big">{p["level"]}</text>
      <text x="415" y="500" class="label">{escape(p["current_title"].upper())}</text>
      <text x="415" y="565" class="subtitle">XP: {p["xp"]:,} / {p["xp_next"]:,}</text>
      <rect x="415" y="605" width="570" height="26" rx="13" class="bar"/>
      <rect x="415" y="605" width="{int(570*progress/100)}" height="26" rx="13" class="fill"/>
      <text x="415" y="690" class="muted">{p["xp_next"]-p["xp"]} XP to next level</text>

      <rect x="100" y="790" width="970" height="345" class="card"/>
      <text x="140" y="865" class="label">NEXT TITLE · LEVEL {p["next_title_level"]}</text>
      <text x="140" y="930" class="subtitle">{escape(p["next_title"])}</text>
      <text x="140" y="1005" class="small">Current Trial: defeat The Broken Build Mine.</text>
      <text x="140" y="1055" class="muted">CMake · README · Fresh clone · Console proof · Release</text>

      <rect x="100" y="1195" width="970" height="430" class="card"/>
      <text x="140" y="1270" class="label">CLASS PROGRESS</text>
      {class_lines}

      <rect x="100" y="1685" width="970" height="350" class="card"/>
      <text x="140" y="1760" class="label">CURRENT QUEST</text>
      <text x="140" y="1825" class="subtitle">{escape(active["name"])}</text>
      <text x="140" y="1885" class="small">{escape(active["summary"][:80])}</text>
      <rect x="140" y="1935" width="600" height="18" rx="9" class="bar"/>
      <rect x="140" y="1935" width="{int(600*active["progress"]/100)}" height="18" rx="9" class="fill"/>
      <text x="770" y="1952" class="small">{active["progress"]}%</text>

      <text x="100" y="2155" class="muted">Daily streak: {p["streak_days"]} days · Today: {p["today_goal_minutes"]}/{p["today_goal_total"]} minutes</text>
    </svg>'''
    return Response(content=svg, media_type="image/svg+xml")
