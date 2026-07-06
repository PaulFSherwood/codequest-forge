# CodeQuest Forge Design Notes

## Core Loop

```text
Quest -> GitHub proof -> review -> XP -> dungeon unlock -> boss -> gear -> harder quests -> title trial
```

XP helps progression, but titles must be earned with completed applications.

## Developer Classes

### Military Systems Dev
Focus: Ada, C++, Python tools, Linux, GUIs, telemetry, message buses, deterministic loops, simulation support, HIL-style testing, fault injection, sustainment, config/release discipline.

### Game Dev
Focus: SDL, input, rendering, textures, animation, collision, ECS, game loops, UI, audio, level loading, small playable games.

### Linux Toolsmith
Focus: Bash/Python utilities, `/proc`, `/sys`, logs, inventory tools, monitors, packaging, install scripts.

### Future Classes
- Web Tool Dev
- Embedded Dev
- Simulation Dev
- Engine Dev
- Security Toolsmith

## Zones

1. The Compiler Yard
2. SDL Fields
3. The Input Marsh
4. ECS Catacombs
5. Collision Keep
6. Toolmaker's Valley
7. Simulation Highlands
8. Engine Citadel
9. Systems Frontier
10. Grandmaster Trial Grounds

## Dungeon Definition

```text
Dungeon = 4-8 linked quests that teach one system.
Boss = finished application proving the system.
Loot = earned tool/ability that unlocks better quests.
```

## Gear Philosophy

Gear is not cosmetic. Gear unlocks app abilities or harder quests.

Example:

```text
Command Window Hotkey
Earned from: The Input Marsh boss
Effect: Unlocks Ctrl+K command palette and future console-command bonus objectives.
```

## Title Philosophy

Every 10 levels gets a new title, but only after a trial boss.

```text
Level 10: C++ Recruit
Level 20: SDL Apprentice
Level 30: Junior Gameplay Engineer
Level 40: ECS Engineer
Level 50: Tools Engineer
Level 60: Simulation Engineer
Level 70: Senior C++ Engineer
Level 80: Engine Architect
Level 90: Staff Systems Builder
Level 100: Grand Marshal of the Build
```

## Lock Screen Reminder

The first version provides `/mini` and `/lock-card.svg`. Later this could become an iOS widget, but the SVG card is enough to screenshot or save as a daily reminder.
