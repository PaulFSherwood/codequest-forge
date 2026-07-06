# CodeQuest Forge

A local RPG-style developer training app for leveling up through finished GitHub projects.

Current campaign goal:

**Senior C++ / Systems Engineer**

Recommended path:

- Primary Class: Military Systems Dev
- Secondary Class: Game Dev
- Profession: Linux Toolsmith

## Run

```bash
cd ~/Documents/src/projects/codequest-forge
./setup.sh
./run.sh
```

Open:

```text
http://127.0.0.1:8000
```

## How to use it

1. Open the Dashboard.
2. Click **Begin Quest 001**.
3. Build the requested tiny project in GitHub.
4. Submit the GitHub repo link and console output.
5. Use the Quest Board as your current grind list.

## First quest

**Quest 001: Hello C++ Campfire**

Create a repo named:

```text
codequest-001-hello-cpp
```

Requirements:

- Add `main.cpp`.
- Print your name, quest number, and class goal.
- Add a README with build/run commands.
- Build and run it from a clean terminal.
- Paste console output into the quest submission.

## Important prototype note

v0.2.0 does not automatically award XP or unlock gear yet. It tracks submissions as proof. Review/approval, XP, gear unlocks, and map travel are planned next.

## Reset local submissions

Open:

```text
http://127.0.0.1:8000/reset
```

or delete:

```bash
rm -f instance/codequest_forge.db
```


## 0.4.0 campaign notes

This version adds the first large quest database and honor-system progression.
Start with **Add Two Numbers**. The early chain intentionally avoids memory/pointers and builds from tiny usable programs into CMake, GitHub proof, SDL, ECS, tools, military-systems demos, simulation, sustainment, and a final capstone.

Run:

```bash
./setup.sh
./run.sh
```

Then open `http://127.0.0.1:8000`.


## v0.4.0 Campaign Database

This release expands the quest database into a full 1-100 campaign spine with side quests, bosses, title trials, gear rewards, fog-of-war zone reveal, and optional dungeon memory mastery tests. Starter quests are Add Two Numbers and Concatenate Two Sentences.


## v0.4.0 Campaign Database

This release expands the quest database into a full 1-100 campaign spine with side quests, bosses, title trials, gear rewards, fog-of-war zone reveal, and optional dungeon memory mastery tests. Starter quests are Add Two Numbers and Concatenate Two Sentences.


## Books of Knowledge

Books are unlockable teaching aids. They do not award XP. They unlock after foundational quests and show what the concept teaches, small practice ideas, and a ChatGPT help prompt.

Example: 2D Arrays stay locked until loops, arrays, and nested-loop foundations are complete.


## v0.5.0

Adds Books of Knowledge training modes: Show Me, Guide Me, and Test Me. Books now track mastery progress, unlock from quests and other mastered books, and include five teaching-help charges.
