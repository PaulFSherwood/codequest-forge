# Quest Database Design Notes - v0.4.0

CodeQuest Forge now uses a zone-based progression inspired by the user-provided C++ learning lists.

The first quests are intentionally tiny:

1. Add Two Numbers
2. Concatenate Two Sentences

The campaign delays raw memory/pointers until the player has already shipped useful console tools, data programs, SDL demos, gameplay demos, ECS demos, and tooling. The structure borrows the gradual beginner order from Bucky/thenewboston and Bro Code, while the later zones pull in modern C++ topics from Mike Shah: references, pointers, RAII, smart pointers, interface/implementation split, STL containers/algorithms, fixed-width integers, bit manipulation, exceptions/error handling, and architecture.

## Level Bands

- 1-10: The Compiler Yard - baby C++ and first useful utility boss.
- 10-20: Utility Crossroads - console tools, validation, logs, config.
- 20-30: Data Homestead - strings, vectors, structs, records, search/sort, persistence.
- 30-40: SDL Fields - SDL window, renderer, events, keyboard, mouse, delta time.
- 40-50: Gameplay Garrison - game states, collision, score, animation, complete tiny game.
- 50-60: ECS Catacombs - entity IDs, components, systems, inspector, ECS sandbox.
- 60-70: Toolmaker’s Valley - logging, config, dev console, tests, profiling, releases.
- 70-80: Simulation Highlands - fixed timestep, telemetry, replay, fault injection.
- 80-90: Military Systems Range - Ada/C++ style, message parsing, 1553-style schedule, HIL mocks, sustainment.
- 90-100: Senior Citadel - RAII, smart pointers, architecture, STL, tests, performance, capstone.

## Quest Rule

Every quest should build something that can be shown in GitHub. No reading-only XP.

Generated: 2026-07-06T08:35:50
