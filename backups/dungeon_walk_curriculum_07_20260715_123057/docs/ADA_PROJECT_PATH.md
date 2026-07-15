# Ada Project Mastery Path

This curriculum contains **1,020 quests**, but only **5 long-lived Alire projects**.

The quests are small cumulative steps. They do not create a new crate for every exercise.

## Projects

### Project 1 — Dungeon Walk

- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Focus:** Introductory Ada
- **Chapters:** 24
- **Quests:** 240
- **Final product:** A tested terminal raycaster with map loading, movement, collision, doors, simple entities, save/load, and release documentation.

Chapters:

1. **Create the Alire Workspace** — Create the dungeon_walk crate, understand alire.toml, build it, run it, and locate generated artifacts.
2. **Terminal Output and Player Commands** — Print a title screen, prompt for a command, read input, and echo a normalized command.
3. **Variables, Constants, and Game State** — Track player position, heading, running state, and immutable map dimensions.
4. **Constrain Coordinates and Angles** — Replace raw Integer values with coordinate, angle, row, and column subtypes that reject invalid states.
5. **Model Directions and Tiles** — Represent directions, commands, and tile kinds with enumerations instead of strings and integers.
6. **Build the Main Game Loop** — Create a stable input-update-render loop that exits only through a clear quit condition.
7. **Move Behavior into Procedures** — Extract prompting, movement, turning, and status display into procedures with deliberate parameter modes.
8. **Compute Instead of Mutate** — Implement functions for next position, normalized angle, tile lookup, and command parsing.
9. **Separate the Dungeon into Packages** — Create clear packages for types, maps, player state, math, input, rendering, and the game loop.
10. **Represent the Player and Camera** — Replace loose variables with Player_State, Camera_State, and Position records.
11. **Create the Map Grid** — Represent rooms and corridors as a two-dimensional tile array with explicit row and column ranges.
12. **Protect Map Invariants** — Wrap the raw grid in a Map type that guarantees solid outer walls and exactly one spawn point.
13. **Parse Commands Reliably** — Build a command parser that trims whitespace, normalizes case, and reports useful errors.
14. **Contain Errors at Boundaries** — Define domain-specific map and command errors while keeping the main loop alive after recoverable failures.
15. **Load Maps from Disk** — Read a map file, preserve line structure, and close files correctly on success and failure.
16. **Validate the Map Format** — Parse headers, dimensions, tiles, player spawn, doors, and comments into the Map model.
17. **Add Vector Mathematics** — Introduce 2D vectors for player position, direction, and camera plane while preserving map coordinates.
18. **Turn the Camera** — Rotate direction and camera vectors using sine and cosine with a clearly documented angle unit.
19. **Generate One Ray per Screen Column** — Convert a screen column into a camera-space X coordinate and a world-space ray direction.
20. **Find Walls with DDA** — Implement grid-based digital differential analysis to find the first wall hit by each ray.
21. **Render the Pseudo-3D View** — Convert ray distances into wall heights and render a buffered ASCII or ANSI frame with ceiling, walls, and floor.
22. **Move Through the Dungeon Safely** — Apply forward, backward, and strafing movement only when the destination is walkable.
23. **Doors, Pickups, and Save Data** — Add simple doors and pickups plus save/load of player state and changed map state.
24. **Finish Dungeon Walk** — Complete tests, clean package boundaries, warning-free builds, user instructions, sample maps, and a tagged release.

### Project 2 — Mission Systems Simulator

- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Focus:** Advanced Ada
- **Chapters:** 22
- **Quests:** 220
- **Final product:** A deterministic multi-component simulation with contracts, tasking, protected state, serialization, external interfaces, fault scenarios, and engineering documentation.

Chapters:

1. **Define the Simulator Architecture** — Create domain, runtime, adapters, and application layers with dependency rules.
2. **Create Strong Physical Units** — Model altitude, speed, heading, time, voltage, and fuel as incompatible types.
3. **Model Bus Messages** — Represent command, status, sensor, and fault messages with one validated message family.
4. **Define Replaceable Components** — Define component and sensor interfaces with initialization, step, status, and shutdown operations.
5. **Build Reusable Typed Utilities** — Create generic bounded buffers, value filters, and range monitors for strongly typed values.
6. **Manage Components and Events** — Store registered components, scheduled events, active faults, and telemetry history in appropriate containers.
7. **Control Dynamic Lifetime** — Use access values only where dynamic polymorphism or lifetime requires them and document the owner.
8. **Manage Resources Safely** — Wrap a log stream or external handle so initialization and finalization are reliable during exceptions.
9. **State Contracts Explicitly** — Add contracts to units, messages, scheduler operations, and component state transitions.
10. **Design Error and Logging Boundaries** — Separate configuration errors, data errors, component faults, and fatal runtime failures.
11. **Load Typed Configuration** — Load tick rate, component definitions, routes, and fault scenarios into validated records.
12. **Serialize Messages and State** — Serialize bus messages, snapshots, and replay records with an explicit format version.
13. **Introduce Active Components** — Run selected sensors or adapters as tasks while keeping the deterministic domain step explicit.
14. **Protect Shared Runtime State** — Create protected telemetry snapshots and bounded message queues.
15. **Coordinate with Entries and Select** — Build a control task that accepts pause, resume, step, snapshot, and shutdown requests.
16. **Use Real-Time Timing Correctly** — Drive wall-clock demonstrations with delay until while measuring deadline misses.
17. **Build a Deterministic Scheduler** — Advance all components in a stable order using integer simulation ticks independent of wall time.
18. **Schedule Events and Inject Faults** — Schedule timed commands, sensor failures, stale data, dropouts, and recovery events.
19. **Expose a Network Adapter** — Send telemetry and receive commands over a simple framed TCP or UDP protocol.
20. **Wrap a C Interface Safely** — Call a small C checksum or timing function through a narrow Ada wrapper.
21. **Test and Analyze the Simulator** — Build unit, integration, replay, concurrency, and contract tests for the deterministic core.
22. **Profile and Release Mission Sim** — Profile the scheduler, bound memory growth, document APIs, freeze a scenario format, and tag a release.

### Project 3 — Rescue Run SDL

- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Focus:** SDLada Game Development
- **Chapters:** 20
- **Quests:** 200
- **Final product:** A polished top-down game with maps, camera, animation, enemies, objectives, audio, configuration, tests, and a release build.

Chapters:

1. **Open an SDL Window** — Add SDLada through Alire, initialize SDL, create a window, and shut down safely.
2. **Draw Basic Shapes** — Create a renderer and draw the player, walls, and background using primitives.
3. **Process SDL Events** — Handle window close, keyboard, focus, and resize events without blocking rendering.
4. **Create an Input Abstraction** — Translate keyboard state into game commands independent of SDL scancodes.
5. **Use a Fixed Update Step** — Separate variable rendering frequency from a fixed game update rate.
6. **Move the Player** — Implement responsive top-down movement with normalized diagonal speed.
7. **Reuse the Map Format** — Load the Dungeon Walk map format into an SDL-oriented world model.
8. **Render Tile Maps** — Draw only visible floor, wall, hazard, and exit tiles.
9. **Follow the Player with a Camera** — Implement a smooth camera that follows the player and remains inside map bounds.
10. **Resolve Tile Collision** — Prevent the player from crossing walls while allowing smooth sliding.
11. **Load and Manage Textures** — Load a tileset and sprites through a texture cache with explicit ownership.
12. **Animate the Player** — Select idle, walk, and hurt animations based on player state and direction.
13. **Add Enemy Behavior** — Create enemies that idle, detect, chase, search, and return.
14. **Add Attacks and Projectiles** — Create projectiles or short-range attacks with owner, velocity, lifetime, and damage.
15. **Build Rescue Objectives** — Add survivors, pickups, exits, and a win condition based on completed rescues.
16. **Create a HUD** — Display health, rescued count, objective status, and pause state.
17. **Add Sound and Music** — Play movement, rescue, damage, attack, and victory audio from game events.
18. **Organize Game States** — Separate title, playing, paused, victory, and game-over states.
19. **Load Settings and Save Progress** — Persist controls, volume, window settings, best score, and unlocked maps.
20. **Finish Rescue Run SDL** — Complete maps, balance, tests, warning cleanup, asset licensing notes, and release instructions.

### Project 4 — Rescue Run ECS Conversion

- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Focus:** Entity-Component-System Architecture
- **Chapters:** 18
- **Quests:** 180
- **Final product:** An ECS-based version of Rescue Run with deterministic systems, data-driven entities, tests, profiling, and a documented migration.

Chapters:

1. **Plan the ECS Migration** — Inventory current entities, data, behavior, coupling, and frame phases before changing code.
2. **Create Stable Entity IDs** — Implement entity creation, destruction, validity checks, and ID reuse protection.
3. **Define Plain Components** — Create position, velocity, sprite, collider, health, AI, projectile, and objective components.
4. **Build Component Stores** — Create reusable typed stores supporting add, remove, get, contains, and iteration.
5. **Create the World API** — Combine entity management and component stores behind a coherent World package.
6. **Define System Phases** — Create input, movement, collision, combat, AI, animation, objective, cleanup, and rendering phases.
7. **Query Matching Entities** — Iterate only entities containing each system’s required component set.
8. **Defer Structural Changes** — Queue spawn, destroy, add, and remove operations until a defined synchronization point.
9. **Create an ECS Event Stream** — Publish collision, damage, rescue, sound, animation, and state-transition events.
10. **Migrate Movement** — Move player, enemies, and projectiles using position and velocity components.
11. **Migrate Rendering** — Render entities possessing transform and sprite components through the SDL adapter.
12. **Migrate Collision** — Detect tile and entity collisions from collider and transform components.
13. **Migrate Animation** — Advance animation components and derive clips from movement or action state.
14. **Migrate Enemy AI** — Represent AI state as components and update decisions separately from movement.
15. **Serialize ECS Worlds** — Save selected components and reconstruct entities without persisting runtime-only resources.
16. **Measure Data-Oriented Performance** — Measure system time, entity counts, store density, allocations, and query cost.
17. **Test and Debug the ECS** — Build focused system tests, lifecycle tests, schedule tests, and a component-inspection overlay.
18. **Complete the ECS Conversion** — Reach feature parity, remove obsolete object-oriented paths, document tradeoffs, and tag the ECS release.

### Project 5 — Forge Map Editor

- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Focus:** GtkAda Application Development
- **Chapters:** 18
- **Quests:** 180
- **Final product:** A desktop editor with a central map canvas, palette, layers, objects, properties, shortcuts, undo/redo, validation, autosave, and export.

Chapters:

1. **Create the GtkAda Application** — Add GtkAda through Alire and open a main application window with safe startup and shutdown.
2. **Build the Editor Shell** — Create a Tiled-like but simpler shell: central canvas, left palette, right properties/layers, bottom status area.
3. **Menus, Actions, and Shortcuts** — Add New, Open, Save, Save As, Undo, Redo, Validate, Export, and Quit actions.
4. **Separate the Document Model** — Create an editor document independent of Gtk widgets, containing map, layers, objects, selection, and dirty state.
5. **Draw the Map Canvas** — Render tiles, grid, spawn, objects, selection, and viewport through a drawing area.
6. **Pan, Zoom, and Pointer Input** — Support wheel zoom, middle-button or space-drag pan, cursor position, and coordinate conversion.
7. **Create the Tile Palette** — Show available tile types with names, icons/colors, and the current brush.
8. **Implement Map Painting Tools** — Add pencil, rectangle fill, flood fill, erase, and eyedropper tools.
9. **Add Layers** — Support tile, object, and trigger layers with add, delete, rename, reorder, visibility, and lock.
10. **Place Objects and Triggers** — Place spawn points, pickups, enemies, exits, rectangles, points, and trigger regions on object layers.
11. **Select and Manipulate Content** — Select tiles or objects, draw selection outlines, move objects, and delete selected content.
12. **Build the Properties Inspector** — Display and edit properties for map, layer, tile selection, or object selection.
13. **Implement Undo and Redo** — Represent painting, object movement, property changes, and layer edits as reversible commands.
14. **Open, Save, and Export** — Open and save editor documents plus export compatible map files for the games.
15. **Validate Maps and Show Errors** — Detect invalid borders, missing spawn, unreachable exits, bad properties, and overlapping critical objects.
16. **Autosave and Background Work** — Autosave snapshots and run expensive validation without freezing the UI.
17. **Custom Widgets and Visual Polish** — Create at least one reusable custom composite widget and load part of the UI through Gtk.Builder or Glade XML.
18. **Finish Forge Map Editor** — Complete the editor workflow, sample maps, tests, keyboard reference, recovery behavior, and release packaging.

## Quest Cycle Used in Every Chapter

1. Question
2. Code Reading
3. Predict
4. Implement
5. Extend
6. Test
7. Repair
8. Refactor
9. Integrate
10. Review

## Complete Quest List

### ADA-P1-01-01 — Create the Alire Workspace — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Alire Workspace
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** alire.toml, src/dungeon_walk.adb, README.md

Answer one focused question before editing code: How should Alire crates and build workflow be used to accomplish this milestone: Create the dungeon_walk crate, understand alire.toml, build it, run it, and locate generated artifacts.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-01-02 — Create the Alire Workspace — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Alire Workspace
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** alire.toml, src/dungeon_walk.adb, README.md

Read the current implementation around alire.toml, src/dungeon_walk.adb, README.md. Trace how data enters, changes, and leaves the code for this milestone: Create the dungeon_walk crate, understand alire.toml, build it, run it, and locate generated artifacts.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-01-03 — Create the Alire Workspace — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Alire Workspace
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** alire.toml, src/dungeon_walk.adb, README.md

Predict the exact behavior if the implementation encounters this problem: Running commands outside the crate or editing generated build artifacts instead of source.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-01-04 — Create the Alire Workspace — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Alire Workspace
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** alire.toml, src/dungeon_walk.adb, README.md

Implement the core milestone in the existing dungeon_walk crate: Create the dungeon_walk crate, understand alire.toml, build it, run it, and locate generated artifacts.

**Completion checks**

- alr build and alr run both succeed from the crate root.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-01-05 — Create the Alire Workspace — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Alire Workspace
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** alire.toml, src/dungeon_walk.adb, README.md

Extend the completed milestone with this practical variation: Add debug and release build profiles plus a repeatable run command.

**Completion checks**

- alr build and alr run both succeed from the crate root.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-01-06 — Create the Alire Workspace — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Alire Workspace
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** alire.toml, src/dungeon_walk.adb, README.md

Create automated or repeatable tests that prove the milestone and its boundaries: Create the dungeon_walk crate, understand alire.toml, build it, run it, and locate generated artifacts.

**Completion checks**

- alr build and alr run both succeed from the crate root.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-01-07 — Create the Alire Workspace — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Alire Workspace
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** alire.toml, src/dungeon_walk.adb, README.md

Reproduce and repair this defect class in the current project: Running commands outside the crate or editing generated build artifacts instead of source.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- alr build and alr run both succeed from the crate root.

### ADA-P1-01-08 — Create the Alire Workspace — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Alire Workspace
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** alire.toml, src/dungeon_walk.adb, README.md

Refactor the chapter implementation so Alire crates and build workflow is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-01-09 — Create the Alire Workspace — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Alire Workspace
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** alire.toml, src/dungeon_walk.adb, README.md

Integrate this chapter into the running final product so it works with earlier milestones: Create the dungeon_walk crate, understand alire.toml, build it, run it, and locate generated artifacts.

**Completion checks**

- alr build and alr run both succeed from the crate root.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-01-10 — Create the Alire Workspace — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Alire Workspace
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** alire.toml, src/dungeon_walk.adb, README.md

Perform a senior-style checkpoint review of Create the Alire Workspace in Dungeon Walk.

**Completion checks**

- alr build and alr run both succeed from the crate root.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-02-01 — Terminal Output and Player Commands — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Terminal Output and Player Commands
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/terminal_ui.ads, src/terminal_ui.adb

Answer one focused question before editing code: How should Ada.Text_IO and basic input be used to accomplish this milestone: Print a title screen, prompt for a command, read input, and echo a normalized command.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-02-02 — Terminal Output and Player Commands — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Terminal Output and Player Commands
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/terminal_ui.ads, src/terminal_ui.adb

Read the current implementation around src/dungeon_walk.adb, src/terminal_ui.ads, src/terminal_ui.adb. Trace how data enters, changes, and leaves the code for this milestone: Print a title screen, prompt for a command, read input, and echo a normalized command.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-02-03 — Terminal Output and Player Commands — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Terminal Output and Player Commands
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/terminal_ui.ads, src/terminal_ui.adb

Predict the exact behavior if the implementation encounters this problem: Get_Line length handling, leftover input, or comparing strings with unexpected spaces/case.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-02-04 — Terminal Output and Player Commands — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Terminal Output and Player Commands
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/terminal_ui.ads, src/terminal_ui.adb

Implement the core milestone in the existing dungeon_walk crate: Print a title screen, prompt for a command, read input, and echo a normalized command.

**Completion checks**

- The program repeatedly accepts Q, quit, W, A, S, and D without crashing.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-02-05 — Terminal Output and Player Commands — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Terminal Output and Player Commands
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/terminal_ui.ads, src/terminal_ui.adb

Extend the completed milestone with this practical variation: Support both full words and single-letter movement commands.

**Completion checks**

- The program repeatedly accepts Q, quit, W, A, S, and D without crashing.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-02-06 — Terminal Output and Player Commands — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Terminal Output and Player Commands
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/terminal_ui.ads, src/terminal_ui.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Print a title screen, prompt for a command, read input, and echo a normalized command.

**Completion checks**

- The program repeatedly accepts Q, quit, W, A, S, and D without crashing.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-02-07 — Terminal Output and Player Commands — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Terminal Output and Player Commands
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/terminal_ui.ads, src/terminal_ui.adb

Reproduce and repair this defect class in the current project: Get_Line length handling, leftover input, or comparing strings with unexpected spaces/case.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- The program repeatedly accepts Q, quit, W, A, S, and D without crashing.

### ADA-P1-02-08 — Terminal Output and Player Commands — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Terminal Output and Player Commands
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/terminal_ui.ads, src/terminal_ui.adb

Refactor the chapter implementation so Ada.Text_IO and basic input is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-02-09 — Terminal Output and Player Commands — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Terminal Output and Player Commands
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/terminal_ui.ads, src/terminal_ui.adb

Integrate this chapter into the running final product so it works with earlier milestones: Print a title screen, prompt for a command, read input, and echo a normalized command.

**Completion checks**

- The program repeatedly accepts Q, quit, W, A, S, and D without crashing.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-02-10 — Terminal Output and Player Commands — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Terminal Output and Player Commands
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/terminal_ui.ads, src/terminal_ui.adb

Perform a senior-style checkpoint review of Terminal Output and Player Commands in Dungeon Walk.

**Completion checks**

- The program repeatedly accepts Q, quit, W, A, S, and D without crashing.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-03-01 — Variables, Constants, and Game State — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Variables, Constants, and Game State
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_state.ads

Answer one focused question before editing code: How should Variables, constants, assignment, and scope be used to accomplish this milestone: Track player position, heading, running state, and immutable map dimensions.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-03-02 — Variables, Constants, and Game State — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Variables, Constants, and Game State
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_state.ads

Read the current implementation around src/dungeon_walk.adb, src/game_state.ads. Trace how data enters, changes, and leaves the code for this milestone: Track player position, heading, running state, and immutable map dimensions.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-03-03 — Variables, Constants, and Game State — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Variables, Constants, and Game State
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_state.ads

Predict the exact behavior if the implementation encounters this problem: Using magic numbers everywhere or accidentally shadowing state in a nested block.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-03-04 — Variables, Constants, and Game State — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Variables, Constants, and Game State
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_state.ads

Implement the core milestone in the existing dungeon_walk crate: Track player position, heading, running state, and immutable map dimensions.

**Completion checks**

- Movement changes variables while dimensions and configuration remain constant.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-03-05 — Variables, Constants, and Game State — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Variables, Constants, and Game State
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_state.ads

Extend the completed milestone with this practical variation: Add a turn counter and display the current state after every command.

**Completion checks**

- Movement changes variables while dimensions and configuration remain constant.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-03-06 — Variables, Constants, and Game State — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Variables, Constants, and Game State
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_state.ads

Create automated or repeatable tests that prove the milestone and its boundaries: Track player position, heading, running state, and immutable map dimensions.

**Completion checks**

- Movement changes variables while dimensions and configuration remain constant.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-03-07 — Variables, Constants, and Game State — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Variables, Constants, and Game State
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_state.ads

Reproduce and repair this defect class in the current project: Using magic numbers everywhere or accidentally shadowing state in a nested block.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Movement changes variables while dimensions and configuration remain constant.

### ADA-P1-03-08 — Variables, Constants, and Game State — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Variables, Constants, and Game State
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_state.ads

Refactor the chapter implementation so Variables, constants, assignment, and scope is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-03-09 — Variables, Constants, and Game State — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Variables, Constants, and Game State
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_state.ads

Integrate this chapter into the running final product so it works with earlier milestones: Track player position, heading, running state, and immutable map dimensions.

**Completion checks**

- Movement changes variables while dimensions and configuration remain constant.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-03-10 — Variables, Constants, and Game State — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Variables, Constants, and Game State
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_state.ads

Perform a senior-style checkpoint review of Variables, Constants, and Game State in Dungeon Walk.

**Completion checks**

- Movement changes variables while dimensions and configuration remain constant.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-04-01 — Constrain Coordinates and Angles — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Constrain Coordinates and Angles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/dungeon_types.adb, src/game_state.ads

Answer one focused question before editing code: How should Scalar types, subtypes, ranges, and conversions be used to accomplish this milestone: Replace raw Integer values with coordinate, angle, row, and column subtypes that reject invalid states.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-04-02 — Constrain Coordinates and Angles — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Constrain Coordinates and Angles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/dungeon_types.adb, src/game_state.ads

Read the current implementation around src/dungeon_types.ads, src/dungeon_types.adb, src/game_state.ads. Trace how data enters, changes, and leaves the code for this milestone: Replace raw Integer values with coordinate, angle, row, and column subtypes that reject invalid states.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-04-03 — Constrain Coordinates and Angles — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Constrain Coordinates and Angles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/dungeon_types.adb, src/game_state.ads

Predict the exact behavior if the implementation encounters this problem: Constraint_Error caused by converting before validating or mixing incompatible units.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-04-04 — Constrain Coordinates and Angles — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Constrain Coordinates and Angles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/dungeon_types.adb, src/game_state.ads

Implement the core milestone in the existing dungeon_walk crate: Replace raw Integer values with coordinate, angle, row, and column subtypes that reject invalid states.

**Completion checks**

- Out-of-range values are rejected at boundaries and valid movement still builds cleanly.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-04-05 — Constrain Coordinates and Angles — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Constrain Coordinates and Angles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/dungeon_types.adb, src/game_state.ads

Extend the completed milestone with this practical variation: Add safe conversion functions at input and file boundaries.

**Completion checks**

- Out-of-range values are rejected at boundaries and valid movement still builds cleanly.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-04-06 — Constrain Coordinates and Angles — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Constrain Coordinates and Angles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/dungeon_types.adb, src/game_state.ads

Create automated or repeatable tests that prove the milestone and its boundaries: Replace raw Integer values with coordinate, angle, row, and column subtypes that reject invalid states.

**Completion checks**

- Out-of-range values are rejected at boundaries and valid movement still builds cleanly.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-04-07 — Constrain Coordinates and Angles — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Constrain Coordinates and Angles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/dungeon_types.adb, src/game_state.ads

Reproduce and repair this defect class in the current project: Constraint_Error caused by converting before validating or mixing incompatible units.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Out-of-range values are rejected at boundaries and valid movement still builds cleanly.

### ADA-P1-04-08 — Constrain Coordinates and Angles — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Constrain Coordinates and Angles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/dungeon_types.adb, src/game_state.ads

Refactor the chapter implementation so Scalar types, subtypes, ranges, and conversions is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-04-09 — Constrain Coordinates and Angles — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Constrain Coordinates and Angles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/dungeon_types.adb, src/game_state.ads

Integrate this chapter into the running final product so it works with earlier milestones: Replace raw Integer values with coordinate, angle, row, and column subtypes that reject invalid states.

**Completion checks**

- Out-of-range values are rejected at boundaries and valid movement still builds cleanly.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-04-10 — Constrain Coordinates and Angles — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Constrain Coordinates and Angles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/dungeon_types.adb, src/game_state.ads

Perform a senior-style checkpoint review of Constrain Coordinates and Angles in Dungeon Walk.

**Completion checks**

- Out-of-range values are rejected at boundaries and valid movement still builds cleanly.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-05-01 — Model Directions and Tiles — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Model Directions and Tiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/command_parser.adb

Answer one focused question before editing code: How should Enumeration types, attributes, and case statements be used to accomplish this milestone: Represent directions, commands, and tile kinds with enumerations instead of strings and integers.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-05-02 — Model Directions and Tiles — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Model Directions and Tiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/command_parser.adb

Read the current implementation around src/dungeon_types.ads, src/command_parser.adb. Trace how data enters, changes, and leaves the code for this milestone: Represent directions, commands, and tile kinds with enumerations instead of strings and integers.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-05-03 — Model Directions and Tiles — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Model Directions and Tiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/command_parser.adb

Predict the exact behavior if the implementation encounters this problem: Missing case alternatives or allowing file-format text to leak throughout the domain model.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-05-04 — Model Directions and Tiles — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Model Directions and Tiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/command_parser.adb

Implement the core milestone in the existing dungeon_walk crate: Represent directions, commands, and tile kinds with enumerations instead of strings and integers.

**Completion checks**

- Every command and tile kind is handled explicitly by case statements.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-05-05 — Model Directions and Tiles — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Model Directions and Tiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/command_parser.adb

Extend the completed milestone with this practical variation: Use enumeration Image/Value helpers behind a safe parser.

**Completion checks**

- Every command and tile kind is handled explicitly by case statements.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-05-06 — Model Directions and Tiles — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Model Directions and Tiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/command_parser.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Represent directions, commands, and tile kinds with enumerations instead of strings and integers.

**Completion checks**

- Every command and tile kind is handled explicitly by case statements.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-05-07 — Model Directions and Tiles — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Model Directions and Tiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/command_parser.adb

Reproduce and repair this defect class in the current project: Missing case alternatives or allowing file-format text to leak throughout the domain model.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Every command and tile kind is handled explicitly by case statements.

### ADA-P1-05-08 — Model Directions and Tiles — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Model Directions and Tiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/command_parser.adb

Refactor the chapter implementation so Enumeration types, attributes, and case statements is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-05-09 — Model Directions and Tiles — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Model Directions and Tiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/command_parser.adb

Integrate this chapter into the running final product so it works with earlier milestones: Represent directions, commands, and tile kinds with enumerations instead of strings and integers.

**Completion checks**

- Every command and tile kind is handled explicitly by case statements.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-05-10 — Model Directions and Tiles — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Model Directions and Tiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/command_parser.adb

Perform a senior-style checkpoint review of Model Directions and Tiles in Dungeon Walk.

**Completion checks**

- Every command and tile kind is handled explicitly by case statements.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-06-01 — Build the Main Game Loop — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Build the Main Game Loop
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_loop.ads, src/game_loop.adb

Answer one focused question before editing code: How should loop, while, for, exit, and iteration invariants be used to accomplish this milestone: Create a stable input-update-render loop that exits only through a clear quit condition.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-06-02 — Build the Main Game Loop — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Build the Main Game Loop
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_loop.ads, src/game_loop.adb

Read the current implementation around src/dungeon_walk.adb, src/game_loop.ads, src/game_loop.adb. Trace how data enters, changes, and leaves the code for this milestone: Create a stable input-update-render loop that exits only through a clear quit condition.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-06-03 — Build the Main Game Loop — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Build the Main Game Loop
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_loop.ads, src/game_loop.adb

Predict the exact behavior if the implementation encounters this problem: Infinite loops, hidden exits, or updating state after the quit command.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-06-04 — Build the Main Game Loop — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Build the Main Game Loop
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_loop.ads, src/game_loop.adb

Implement the core milestone in the existing dungeon_walk crate: Create a stable input-update-render loop that exits only through a clear quit condition.

**Completion checks**

- The loop can run interactively, run a finite script, and exit cleanly.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-06-05 — Build the Main Game Loop — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Build the Main Game Loop
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_loop.ads, src/game_loop.adb

Extend the completed milestone with this practical variation: Add a bounded demo mode that replays a sequence of commands.

**Completion checks**

- The loop can run interactively, run a finite script, and exit cleanly.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-06-06 — Build the Main Game Loop — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Build the Main Game Loop
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_loop.ads, src/game_loop.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Create a stable input-update-render loop that exits only through a clear quit condition.

**Completion checks**

- The loop can run interactively, run a finite script, and exit cleanly.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-06-07 — Build the Main Game Loop — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Build the Main Game Loop
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_loop.ads, src/game_loop.adb

Reproduce and repair this defect class in the current project: Infinite loops, hidden exits, or updating state after the quit command.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- The loop can run interactively, run a finite script, and exit cleanly.

### ADA-P1-06-08 — Build the Main Game Loop — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Build the Main Game Loop
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_loop.ads, src/game_loop.adb

Refactor the chapter implementation so loop, while, for, exit, and iteration invariants is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-06-09 — Build the Main Game Loop — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Build the Main Game Loop
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_loop.ads, src/game_loop.adb

Integrate this chapter into the running final product so it works with earlier milestones: Create a stable input-update-render loop that exits only through a clear quit condition.

**Completion checks**

- The loop can run interactively, run a finite script, and exit cleanly.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-06-10 — Build the Main Game Loop — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Build the Main Game Loop
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_walk.adb, src/game_loop.ads, src/game_loop.adb

Perform a senior-style checkpoint review of Build the Main Game Loop in Dungeon Walk.

**Completion checks**

- The loop can run interactively, run a finite script, and exit cleanly.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-07-01 — Move Behavior into Procedures — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Behavior into Procedures
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.ads, src/player_actions.adb

Answer one focused question before editing code: How should Procedures and in/out/in out modes be used to accomplish this milestone: Extract prompting, movement, turning, and status display into procedures with deliberate parameter modes.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-07-02 — Move Behavior into Procedures — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Behavior into Procedures
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.ads, src/player_actions.adb

Read the current implementation around src/player_actions.ads, src/player_actions.adb. Trace how data enters, changes, and leaves the code for this milestone: Extract prompting, movement, turning, and status display into procedures with deliberate parameter modes.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-07-03 — Move Behavior into Procedures — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Behavior into Procedures
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.ads, src/player_actions.adb

Predict the exact behavior if the implementation encounters this problem: Using in out for everything or changing state through globals that should be parameters.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-07-04 — Move Behavior into Procedures — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Behavior into Procedures
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.ads, src/player_actions.adb

Implement the core milestone in the existing dungeon_walk crate: Extract prompting, movement, turning, and status display into procedures with deliberate parameter modes.

**Completion checks**

- Each procedure has a narrow purpose and correct parameter modes.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-07-05 — Move Behavior into Procedures — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Behavior into Procedures
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.ads, src/player_actions.adb

Extend the completed milestone with this practical variation: Add a procedure that resets the player to a spawn point.

**Completion checks**

- Each procedure has a narrow purpose and correct parameter modes.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-07-06 — Move Behavior into Procedures — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Behavior into Procedures
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.ads, src/player_actions.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Extract prompting, movement, turning, and status display into procedures with deliberate parameter modes.

**Completion checks**

- Each procedure has a narrow purpose and correct parameter modes.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-07-07 — Move Behavior into Procedures — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Behavior into Procedures
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.ads, src/player_actions.adb

Reproduce and repair this defect class in the current project: Using in out for everything or changing state through globals that should be parameters.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Each procedure has a narrow purpose and correct parameter modes.

### ADA-P1-07-08 — Move Behavior into Procedures — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Behavior into Procedures
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.ads, src/player_actions.adb

Refactor the chapter implementation so Procedures and in/out/in out modes is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-07-09 — Move Behavior into Procedures — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Behavior into Procedures
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.ads, src/player_actions.adb

Integrate this chapter into the running final product so it works with earlier milestones: Extract prompting, movement, turning, and status display into procedures with deliberate parameter modes.

**Completion checks**

- Each procedure has a narrow purpose and correct parameter modes.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-07-10 — Move Behavior into Procedures — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Behavior into Procedures
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.ads, src/player_actions.adb

Perform a senior-style checkpoint review of Move Behavior into Procedures in Dungeon Walk.

**Completion checks**

- Each procedure has a narrow purpose and correct parameter modes.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-08-01 — Compute Instead of Mutate — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Compute Instead of Mutate
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/dungeon_math.adb, src/command_parser.adb

Answer one focused question before editing code: How should Functions, return types, expression functions, and purity be used to accomplish this milestone: Implement functions for next position, normalized angle, tile lookup, and command parsing.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-08-02 — Compute Instead of Mutate — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Compute Instead of Mutate
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/dungeon_math.adb, src/command_parser.adb

Read the current implementation around src/dungeon_math.ads, src/dungeon_math.adb, src/command_parser.adb. Trace how data enters, changes, and leaves the code for this milestone: Implement functions for next position, normalized angle, tile lookup, and command parsing.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-08-03 — Compute Instead of Mutate — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Compute Instead of Mutate
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/dungeon_math.adb, src/command_parser.adb

Predict the exact behavior if the implementation encounters this problem: Functions unexpectedly changing shared state or returning unconstrained values without validation.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-08-04 — Compute Instead of Mutate — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Compute Instead of Mutate
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/dungeon_math.adb, src/command_parser.adb

Implement the core milestone in the existing dungeon_walk crate: Implement functions for next position, normalized angle, tile lookup, and command parsing.

**Completion checks**

- Core calculations can be tested without running the game loop.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-08-05 — Compute Instead of Mutate — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Compute Instead of Mutate
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/dungeon_math.adb, src/command_parser.adb

Extend the completed milestone with this practical variation: Add pure functions for Manhattan and Euclidean distance.

**Completion checks**

- Core calculations can be tested without running the game loop.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-08-06 — Compute Instead of Mutate — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Compute Instead of Mutate
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/dungeon_math.adb, src/command_parser.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Implement functions for next position, normalized angle, tile lookup, and command parsing.

**Completion checks**

- Core calculations can be tested without running the game loop.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-08-07 — Compute Instead of Mutate — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Compute Instead of Mutate
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/dungeon_math.adb, src/command_parser.adb

Reproduce and repair this defect class in the current project: Functions unexpectedly changing shared state or returning unconstrained values without validation.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Core calculations can be tested without running the game loop.

### ADA-P1-08-08 — Compute Instead of Mutate — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Compute Instead of Mutate
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/dungeon_math.adb, src/command_parser.adb

Refactor the chapter implementation so Functions, return types, expression functions, and purity is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-08-09 — Compute Instead of Mutate — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Compute Instead of Mutate
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/dungeon_math.adb, src/command_parser.adb

Integrate this chapter into the running final product so it works with earlier milestones: Implement functions for next position, normalized angle, tile lookup, and command parsing.

**Completion checks**

- Core calculations can be tested without running the game loop.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-08-10 — Compute Instead of Mutate — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Compute Instead of Mutate
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/dungeon_math.adb, src/command_parser.adb

Perform a senior-style checkpoint review of Compute Instead of Mutate in Dungeon Walk.

**Completion checks**

- Core calculations can be tested without running the game loop.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-09-01 — Separate the Dungeon into Packages — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Separate the Dungeon into Packages
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/maps.ads, src/player.ads, src/renderer.ads

Answer one focused question before editing code: How should Package specifications, bodies, visibility, with, and use type be used to accomplish this milestone: Create clear packages for types, maps, player state, math, input, rendering, and the game loop.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-09-02 — Separate the Dungeon into Packages — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Separate the Dungeon into Packages
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/maps.ads, src/player.ads, src/renderer.ads

Read the current implementation around src/dungeon_types.ads, src/maps.ads, src/player.ads, src/renderer.ads. Trace how data enters, changes, and leaves the code for this milestone: Create clear packages for types, maps, player state, math, input, rendering, and the game loop.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-09-03 — Separate the Dungeon into Packages — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Separate the Dungeon into Packages
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/maps.ads, src/player.ads, src/renderer.ads

Predict the exact behavior if the implementation encounters this problem: Circular dependencies or placing every declaration in one giant package.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-09-04 — Separate the Dungeon into Packages — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Separate the Dungeon into Packages
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/maps.ads, src/player.ads, src/renderer.ads

Implement the core milestone in the existing dungeon_walk crate: Create clear packages for types, maps, player state, math, input, rendering, and the game loop.

**Completion checks**

- The main procedure reads as orchestration rather than implementation.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-09-05 — Separate the Dungeon into Packages — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Separate the Dungeon into Packages
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/maps.ads, src/player.ads, src/renderer.ads

Extend the completed milestone with this practical variation: Hide implementation details behind private types where appropriate.

**Completion checks**

- The main procedure reads as orchestration rather than implementation.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-09-06 — Separate the Dungeon into Packages — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Separate the Dungeon into Packages
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/maps.ads, src/player.ads, src/renderer.ads

Create automated or repeatable tests that prove the milestone and its boundaries: Create clear packages for types, maps, player state, math, input, rendering, and the game loop.

**Completion checks**

- The main procedure reads as orchestration rather than implementation.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-09-07 — Separate the Dungeon into Packages — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Separate the Dungeon into Packages
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/maps.ads, src/player.ads, src/renderer.ads

Reproduce and repair this defect class in the current project: Circular dependencies or placing every declaration in one giant package.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- The main procedure reads as orchestration rather than implementation.

### ADA-P1-09-08 — Separate the Dungeon into Packages — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Separate the Dungeon into Packages
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/maps.ads, src/player.ads, src/renderer.ads

Refactor the chapter implementation so Package specifications, bodies, visibility, with, and use type is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-09-09 — Separate the Dungeon into Packages — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Separate the Dungeon into Packages
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/maps.ads, src/player.ads, src/renderer.ads

Integrate this chapter into the running final product so it works with earlier milestones: Create clear packages for types, maps, player state, math, input, rendering, and the game loop.

**Completion checks**

- The main procedure reads as orchestration rather than implementation.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-09-10 — Separate the Dungeon into Packages — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Separate the Dungeon into Packages
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_types.ads, src/maps.ads, src/player.ads, src/renderer.ads

Perform a senior-style checkpoint review of Separate the Dungeon into Packages in Dungeon Walk.

**Completion checks**

- The main procedure reads as orchestration rather than implementation.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-10-01 — Represent the Player and Camera — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Represent the Player and Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player.ads, src/player.adb, src/dungeon_types.ads

Answer one focused question before editing code: How should Records, aggregates, defaults, and nested records be used to accomplish this milestone: Replace loose variables with Player_State, Camera_State, and Position records.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-10-02 — Represent the Player and Camera — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Represent the Player and Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player.ads, src/player.adb, src/dungeon_types.ads

Read the current implementation around src/player.ads, src/player.adb, src/dungeon_types.ads. Trace how data enters, changes, and leaves the code for this milestone: Replace loose variables with Player_State, Camera_State, and Position records.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-10-03 — Represent the Player and Camera — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Represent the Player and Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player.ads, src/player.adb, src/dungeon_types.ads

Predict the exact behavior if the implementation encounters this problem: Partially initialized records or duplicated coordinate fields that drift apart.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-10-04 — Represent the Player and Camera — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Represent the Player and Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player.ads, src/player.adb, src/dungeon_types.ads

Implement the core milestone in the existing dungeon_walk crate: Replace loose variables with Player_State, Camera_State, and Position records.

**Completion checks**

- Player state is initialized with named aggregates and passed as one coherent value.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-10-05 — Represent the Player and Camera — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Represent the Player and Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player.ads, src/player.adb, src/dungeon_types.ads

Extend the completed milestone with this practical variation: Add inventory and health records without coupling them to rendering.

**Completion checks**

- Player state is initialized with named aggregates and passed as one coherent value.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-10-06 — Represent the Player and Camera — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Represent the Player and Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player.ads, src/player.adb, src/dungeon_types.ads

Create automated or repeatable tests that prove the milestone and its boundaries: Replace loose variables with Player_State, Camera_State, and Position records.

**Completion checks**

- Player state is initialized with named aggregates and passed as one coherent value.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-10-07 — Represent the Player and Camera — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Represent the Player and Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player.ads, src/player.adb, src/dungeon_types.ads

Reproduce and repair this defect class in the current project: Partially initialized records or duplicated coordinate fields that drift apart.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Player state is initialized with named aggregates and passed as one coherent value.

### ADA-P1-10-08 — Represent the Player and Camera — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Represent the Player and Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player.ads, src/player.adb, src/dungeon_types.ads

Refactor the chapter implementation so Records, aggregates, defaults, and nested records is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-10-09 — Represent the Player and Camera — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Represent the Player and Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player.ads, src/player.adb, src/dungeon_types.ads

Integrate this chapter into the running final product so it works with earlier milestones: Replace loose variables with Player_State, Camera_State, and Position records.

**Completion checks**

- Player state is initialized with named aggregates and passed as one coherent value.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-10-10 — Represent the Player and Camera — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Represent the Player and Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player.ads, src/player.adb, src/dungeon_types.ads

Perform a senior-style checkpoint review of Represent the Player and Camera in Dungeon Walk.

**Completion checks**

- Player state is initialized with named aggregates and passed as one coherent value.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-11-01 — Create the Map Grid — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Map Grid
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb, data/maps/training.map

Answer one focused question before editing code: How should Constrained and unconstrained arrays be used to accomplish this milestone: Represent rooms and corridors as a two-dimensional tile array with explicit row and column ranges.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-11-02 — Create the Map Grid — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Map Grid
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb, data/maps/training.map

Read the current implementation around src/maps.ads, src/maps.adb, data/maps/training.map. Trace how data enters, changes, and leaves the code for this milestone: Represent rooms and corridors as a two-dimensional tile array with explicit row and column ranges.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-11-03 — Create the Map Grid — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Map Grid
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb, data/maps/training.map

Predict the exact behavior if the implementation encounters this problem: Reversing row/column order or assuming every map starts at index 1.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-11-04 — Create the Map Grid — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Map Grid
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb, data/maps/training.map

Implement the core milestone in the existing dungeon_walk crate: Represent rooms and corridors as a two-dimensional tile array with explicit row and column ranges.

**Completion checks**

- Tile lookup works at corners, edges, and interior cells for multiple map sizes.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-11-05 — Create the Map Grid — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Map Grid
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb, data/maps/training.map

Extend the completed milestone with this practical variation: Support maps of different dimensions through an unconstrained array type.

**Completion checks**

- Tile lookup works at corners, edges, and interior cells for multiple map sizes.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-11-06 — Create the Map Grid — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Map Grid
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb, data/maps/training.map

Create automated or repeatable tests that prove the milestone and its boundaries: Represent rooms and corridors as a two-dimensional tile array with explicit row and column ranges.

**Completion checks**

- Tile lookup works at corners, edges, and interior cells for multiple map sizes.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-11-07 — Create the Map Grid — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Map Grid
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb, data/maps/training.map

Reproduce and repair this defect class in the current project: Reversing row/column order or assuming every map starts at index 1.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Tile lookup works at corners, edges, and interior cells for multiple map sizes.

### ADA-P1-11-08 — Create the Map Grid — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Map Grid
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb, data/maps/training.map

Refactor the chapter implementation so Constrained and unconstrained arrays is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-11-09 — Create the Map Grid — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Map Grid
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb, data/maps/training.map

Integrate this chapter into the running final product so it works with earlier milestones: Represent rooms and corridors as a two-dimensional tile array with explicit row and column ranges.

**Completion checks**

- Tile lookup works at corners, edges, and interior cells for multiple map sizes.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-11-10 — Create the Map Grid — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Create the Map Grid
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb, data/maps/training.map

Perform a senior-style checkpoint review of Create the Map Grid in Dungeon Walk.

**Completion checks**

- Tile lookup works at corners, edges, and interior cells for multiple map sizes.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-12-01 — Protect Map Invariants — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Protect Map Invariants
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb

Answer one focused question before editing code: How should Private types, constructors, selectors, and invariants be used to accomplish this milestone: Wrap the raw grid in a Map type that guarantees solid outer walls and exactly one spawn point.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-12-02 — Protect Map Invariants — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Protect Map Invariants
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb

Read the current implementation around src/maps.ads, src/maps.adb. Trace how data enters, changes, and leaves the code for this milestone: Wrap the raw grid in a Map type that guarantees solid outer walls and exactly one spawn point.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-12-03 — Protect Map Invariants — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Protect Map Invariants
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb

Predict the exact behavior if the implementation encounters this problem: Exposing the backing array and allowing invalid maps to be created anywhere.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-12-04 — Protect Map Invariants — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Protect Map Invariants
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb

Implement the core milestone in the existing dungeon_walk crate: Wrap the raw grid in a Map type that guarantees solid outer walls and exactly one spawn point.

**Completion checks**

- Invalid border edits and duplicate spawn points are rejected by the map API.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-12-05 — Protect Map Invariants — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Protect Map Invariants
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb

Extend the completed milestone with this practical variation: Provide safe Set_Tile and Is_Walkable operations.

**Completion checks**

- Invalid border edits and duplicate spawn points are rejected by the map API.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-12-06 — Protect Map Invariants — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Protect Map Invariants
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Wrap the raw grid in a Map type that guarantees solid outer walls and exactly one spawn point.

**Completion checks**

- Invalid border edits and duplicate spawn points are rejected by the map API.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-12-07 — Protect Map Invariants — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Protect Map Invariants
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb

Reproduce and repair this defect class in the current project: Exposing the backing array and allowing invalid maps to be created anywhere.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Invalid border edits and duplicate spawn points are rejected by the map API.

### ADA-P1-12-08 — Protect Map Invariants — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Protect Map Invariants
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb

Refactor the chapter implementation so Private types, constructors, selectors, and invariants is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-12-09 — Protect Map Invariants — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Protect Map Invariants
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb

Integrate this chapter into the running final product so it works with earlier milestones: Wrap the raw grid in a Map type that guarantees solid outer walls and exactly one spawn point.

**Completion checks**

- Invalid border edits and duplicate spawn points are rejected by the map API.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-12-10 — Protect Map Invariants — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Protect Map Invariants
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/maps.ads, src/maps.adb

Perform a senior-style checkpoint review of Protect Map Invariants in Dungeon Walk.

**Completion checks**

- Invalid border edits and duplicate spawn points are rejected by the map API.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-13-01 — Parse Commands Reliably — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Parse Commands Reliably
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/command_parser.ads, src/command_parser.adb

Answer one focused question before editing code: How should String slices, fixed strings, unbounded strings, and character handling be used to accomplish this milestone: Build a command parser that trims whitespace, normalizes case, and reports useful errors.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-13-02 — Parse Commands Reliably — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Parse Commands Reliably
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/command_parser.ads, src/command_parser.adb

Read the current implementation around src/command_parser.ads, src/command_parser.adb. Trace how data enters, changes, and leaves the code for this milestone: Build a command parser that trims whitespace, normalizes case, and reports useful errors.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-13-03 — Parse Commands Reliably — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Parse Commands Reliably
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/command_parser.ads, src/command_parser.adb

Predict the exact behavior if the implementation encounters this problem: Assigning variable-length text into fixed-length strings or silently truncating input.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-13-04 — Parse Commands Reliably — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Parse Commands Reliably
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/command_parser.ads, src/command_parser.adb

Implement the core milestone in the existing dungeon_walk crate: Build a command parser that trims whitespace, normalizes case, and reports useful errors.

**Completion checks**

- Mixed-case commands and malformed input produce deterministic results.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-13-05 — Parse Commands Reliably — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Parse Commands Reliably
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/command_parser.ads, src/command_parser.adb

Extend the completed milestone with this practical variation: Support commands with arguments such as open north and save slot1.

**Completion checks**

- Mixed-case commands and malformed input produce deterministic results.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-13-06 — Parse Commands Reliably — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Parse Commands Reliably
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/command_parser.ads, src/command_parser.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Build a command parser that trims whitespace, normalizes case, and reports useful errors.

**Completion checks**

- Mixed-case commands and malformed input produce deterministic results.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-13-07 — Parse Commands Reliably — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Parse Commands Reliably
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/command_parser.ads, src/command_parser.adb

Reproduce and repair this defect class in the current project: Assigning variable-length text into fixed-length strings or silently truncating input.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Mixed-case commands and malformed input produce deterministic results.

### ADA-P1-13-08 — Parse Commands Reliably — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Parse Commands Reliably
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/command_parser.ads, src/command_parser.adb

Refactor the chapter implementation so String slices, fixed strings, unbounded strings, and character handling is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-13-09 — Parse Commands Reliably — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Parse Commands Reliably
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/command_parser.ads, src/command_parser.adb

Integrate this chapter into the running final product so it works with earlier milestones: Build a command parser that trims whitespace, normalizes case, and reports useful errors.

**Completion checks**

- Mixed-case commands and malformed input produce deterministic results.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-13-10 — Parse Commands Reliably — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Parse Commands Reliably
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/command_parser.ads, src/command_parser.adb

Perform a senior-style checkpoint review of Parse Commands Reliably in Dungeon Walk.

**Completion checks**

- Mixed-case commands and malformed input produce deterministic results.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-14-01 — Contain Errors at Boundaries — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Contain Errors at Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_errors.ads, src/game_loop.adb, src/map_files.adb

Answer one focused question before editing code: How should Exception declarations, handlers, propagation, and cleanup be used to accomplish this milestone: Define domain-specific map and command errors while keeping the main loop alive after recoverable failures.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-14-02 — Contain Errors at Boundaries — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Contain Errors at Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_errors.ads, src/game_loop.adb, src/map_files.adb

Read the current implementation around src/dungeon_errors.ads, src/game_loop.adb, src/map_files.adb. Trace how data enters, changes, and leaves the code for this milestone: Define domain-specific map and command errors while keeping the main loop alive after recoverable failures.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-14-03 — Contain Errors at Boundaries — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Contain Errors at Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_errors.ads, src/game_loop.adb, src/map_files.adb

Predict the exact behavior if the implementation encounters this problem: Catching others too early and hiding programming defects.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-14-04 — Contain Errors at Boundaries — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Contain Errors at Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_errors.ads, src/game_loop.adb, src/map_files.adb

Implement the core milestone in the existing dungeon_walk crate: Define domain-specific map and command errors while keeping the main loop alive after recoverable failures.

**Completion checks**

- Bad commands and bad map files are reported without corrupting current state.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-14-05 — Contain Errors at Boundaries — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Contain Errors at Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_errors.ads, src/game_loop.adb, src/map_files.adb

Extend the completed milestone with this practical variation: Add a top-level crash report for unexpected exceptions.

**Completion checks**

- Bad commands and bad map files are reported without corrupting current state.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-14-06 — Contain Errors at Boundaries — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Contain Errors at Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_errors.ads, src/game_loop.adb, src/map_files.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Define domain-specific map and command errors while keeping the main loop alive after recoverable failures.

**Completion checks**

- Bad commands and bad map files are reported without corrupting current state.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-14-07 — Contain Errors at Boundaries — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Contain Errors at Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_errors.ads, src/game_loop.adb, src/map_files.adb

Reproduce and repair this defect class in the current project: Catching others too early and hiding programming defects.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Bad commands and bad map files are reported without corrupting current state.

### ADA-P1-14-08 — Contain Errors at Boundaries — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Contain Errors at Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_errors.ads, src/game_loop.adb, src/map_files.adb

Refactor the chapter implementation so Exception declarations, handlers, propagation, and cleanup is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-14-09 — Contain Errors at Boundaries — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Contain Errors at Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_errors.ads, src/game_loop.adb, src/map_files.adb

Integrate this chapter into the running final product so it works with earlier milestones: Define domain-specific map and command errors while keeping the main loop alive after recoverable failures.

**Completion checks**

- Bad commands and bad map files are reported without corrupting current state.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-14-10 — Contain Errors at Boundaries — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Contain Errors at Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_errors.ads, src/game_loop.adb, src/map_files.adb

Perform a senior-style checkpoint review of Contain Errors at Boundaries in Dungeon Walk.

**Completion checks**

- Bad commands and bad map files are reported without corrupting current state.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-15-01 — Load Maps from Disk — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Load Maps from Disk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_files.ads, src/map_files.adb, data/maps/training.map

Answer one focused question before editing code: How should Text file input/output and resource management be used to accomplish this milestone: Read a map file, preserve line structure, and close files correctly on success and failure.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-15-02 — Load Maps from Disk — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Load Maps from Disk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_files.ads, src/map_files.adb, data/maps/training.map

Read the current implementation around src/map_files.ads, src/map_files.adb, data/maps/training.map. Trace how data enters, changes, and leaves the code for this milestone: Read a map file, preserve line structure, and close files correctly on success and failure.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-15-03 — Load Maps from Disk — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Load Maps from Disk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_files.ads, src/map_files.adb, data/maps/training.map

Predict the exact behavior if the implementation encounters this problem: Leaked open files, inconsistent line widths, or assuming the working directory.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-15-04 — Load Maps from Disk — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Load Maps from Disk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_files.ads, src/map_files.adb, data/maps/training.map

Implement the core milestone in the existing dungeon_walk crate: Read a map file, preserve line structure, and close files correctly on success and failure.

**Completion checks**

- Load-save-load produces the same logical map.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-15-05 — Load Maps from Disk — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Load Maps from Disk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_files.ads, src/map_files.adb, data/maps/training.map

Extend the completed milestone with this practical variation: Write the current map back to a new file with a canonical format.

**Completion checks**

- Load-save-load produces the same logical map.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-15-06 — Load Maps from Disk — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Load Maps from Disk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_files.ads, src/map_files.adb, data/maps/training.map

Create automated or repeatable tests that prove the milestone and its boundaries: Read a map file, preserve line structure, and close files correctly on success and failure.

**Completion checks**

- Load-save-load produces the same logical map.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-15-07 — Load Maps from Disk — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Load Maps from Disk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_files.ads, src/map_files.adb, data/maps/training.map

Reproduce and repair this defect class in the current project: Leaked open files, inconsistent line widths, or assuming the working directory.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Load-save-load produces the same logical map.

### ADA-P1-15-08 — Load Maps from Disk — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Load Maps from Disk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_files.ads, src/map_files.adb, data/maps/training.map

Refactor the chapter implementation so Text file input/output and resource management is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-15-09 — Load Maps from Disk — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Load Maps from Disk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_files.ads, src/map_files.adb, data/maps/training.map

Integrate this chapter into the running final product so it works with earlier milestones: Read a map file, preserve line structure, and close files correctly on success and failure.

**Completion checks**

- Load-save-load produces the same logical map.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-15-10 — Load Maps from Disk — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Load Maps from Disk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_files.ads, src/map_files.adb, data/maps/training.map

Perform a senior-style checkpoint review of Load Maps from Disk in Dungeon Walk.

**Completion checks**

- Load-save-load produces the same logical map.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-16-01 — Validate the Map Format — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Validate the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_parser.ads, src/map_parser.adb, tests/map_parser_tests.adb

Answer one focused question before editing code: How should Parsing, validation passes, and error reporting be used to accomplish this milestone: Parse headers, dimensions, tiles, player spawn, doors, and comments into the Map model.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-16-02 — Validate the Map Format — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Validate the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_parser.ads, src/map_parser.adb, tests/map_parser_tests.adb

Read the current implementation around src/map_parser.ads, src/map_parser.adb, tests/map_parser_tests.adb. Trace how data enters, changes, and leaves the code for this milestone: Parse headers, dimensions, tiles, player spawn, doors, and comments into the Map model.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-16-03 — Validate the Map Format — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Validate the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_parser.ads, src/map_parser.adb, tests/map_parser_tests.adb

Predict the exact behavior if the implementation encounters this problem: Mutating the active map before the entire new map has validated.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-16-04 — Validate the Map Format — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Validate the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_parser.ads, src/map_parser.adb, tests/map_parser_tests.adb

Implement the core milestone in the existing dungeon_walk crate: Parse headers, dimensions, tiles, player spawn, doors, and comments into the Map model.

**Completion checks**

- A suite of valid and invalid fixture maps produces precise results.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-16-05 — Validate the Map Format — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Validate the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_parser.ads, src/map_parser.adb, tests/map_parser_tests.adb

Extend the completed milestone with this practical variation: Report filename, line, and column for malformed symbols.

**Completion checks**

- A suite of valid and invalid fixture maps produces precise results.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-16-06 — Validate the Map Format — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Validate the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_parser.ads, src/map_parser.adb, tests/map_parser_tests.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Parse headers, dimensions, tiles, player spawn, doors, and comments into the Map model.

**Completion checks**

- A suite of valid and invalid fixture maps produces precise results.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-16-07 — Validate the Map Format — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Validate the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_parser.ads, src/map_parser.adb, tests/map_parser_tests.adb

Reproduce and repair this defect class in the current project: Mutating the active map before the entire new map has validated.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- A suite of valid and invalid fixture maps produces precise results.

### ADA-P1-16-08 — Validate the Map Format — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Validate the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_parser.ads, src/map_parser.adb, tests/map_parser_tests.adb

Refactor the chapter implementation so Parsing, validation passes, and error reporting is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-16-09 — Validate the Map Format — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Validate the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_parser.ads, src/map_parser.adb, tests/map_parser_tests.adb

Integrate this chapter into the running final product so it works with earlier milestones: Parse headers, dimensions, tiles, player spawn, doors, and comments into the Map model.

**Completion checks**

- A suite of valid and invalid fixture maps produces precise results.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-16-10 — Validate the Map Format — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Validate the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/map_parser.ads, src/map_parser.adb, tests/map_parser_tests.adb

Perform a senior-style checkpoint review of Validate the Map Format in Dungeon Walk.

**Completion checks**

- A suite of valid and invalid fixture maps produces precise results.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-17-01 — Add Vector Mathematics — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Add Vector Mathematics
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/vectors.ads, src/vectors.adb, src/player.ads

Answer one focused question before editing code: How should Floating-point types, vectors, operators, and numeric packages be used to accomplish this milestone: Introduce 2D vectors for player position, direction, and camera plane while preserving map coordinates.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-17-02 — Add Vector Mathematics — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Add Vector Mathematics
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/vectors.ads, src/vectors.adb, src/player.ads

Read the current implementation around src/vectors.ads, src/vectors.adb, src/player.ads. Trace how data enters, changes, and leaves the code for this milestone: Introduce 2D vectors for player position, direction, and camera plane while preserving map coordinates.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-17-03 — Add Vector Mathematics — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Add Vector Mathematics
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/vectors.ads, src/vectors.adb, src/player.ads

Predict the exact behavior if the implementation encounters this problem: Mixing degrees and radians or converting between integer cells and floating positions carelessly.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-17-04 — Add Vector Mathematics — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Add Vector Mathematics
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/vectors.ads, src/vectors.adb, src/player.ads

Implement the core milestone in the existing dungeon_walk crate: Introduce 2D vectors for player position, direction, and camera plane while preserving map coordinates.

**Completion checks**

- Vector operations pass tests for zero, axes, normalization, and common angles.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-17-05 — Add Vector Mathematics — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Add Vector Mathematics
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/vectors.ads, src/vectors.adb, src/player.ads

Extend the completed milestone with this practical variation: Overload only the vector operations that make game code clearer.

**Completion checks**

- Vector operations pass tests for zero, axes, normalization, and common angles.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-17-06 — Add Vector Mathematics — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Add Vector Mathematics
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/vectors.ads, src/vectors.adb, src/player.ads

Create automated or repeatable tests that prove the milestone and its boundaries: Introduce 2D vectors for player position, direction, and camera plane while preserving map coordinates.

**Completion checks**

- Vector operations pass tests for zero, axes, normalization, and common angles.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-17-07 — Add Vector Mathematics — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Add Vector Mathematics
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/vectors.ads, src/vectors.adb, src/player.ads

Reproduce and repair this defect class in the current project: Mixing degrees and radians or converting between integer cells and floating positions carelessly.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Vector operations pass tests for zero, axes, normalization, and common angles.

### ADA-P1-17-08 — Add Vector Mathematics — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Add Vector Mathematics
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/vectors.ads, src/vectors.adb, src/player.ads

Refactor the chapter implementation so Floating-point types, vectors, operators, and numeric packages is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-17-09 — Add Vector Mathematics — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Add Vector Mathematics
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/vectors.ads, src/vectors.adb, src/player.ads

Integrate this chapter into the running final product so it works with earlier milestones: Introduce 2D vectors for player position, direction, and camera plane while preserving map coordinates.

**Completion checks**

- Vector operations pass tests for zero, axes, normalization, and common angles.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-17-10 — Add Vector Mathematics — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Add Vector Mathematics
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/vectors.ads, src/vectors.adb, src/player.ads

Perform a senior-style checkpoint review of Add Vector Mathematics in Dungeon Walk.

**Completion checks**

- Vector operations pass tests for zero, axes, normalization, and common angles.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-18-01 — Turn the Camera — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Turn the Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/player_actions.adb

Answer one focused question before editing code: How should Ada.Numerics, trigonometry, modular angles, and precision be used to accomplish this milestone: Rotate direction and camera vectors using sine and cosine with a clearly documented angle unit.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-18-02 — Turn the Camera — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Turn the Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/player_actions.adb

Read the current implementation around src/dungeon_math.ads, src/player_actions.adb. Trace how data enters, changes, and leaves the code for this milestone: Rotate direction and camera vectors using sine and cosine with a clearly documented angle unit.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-18-03 — Turn the Camera — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Turn the Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/player_actions.adb

Predict the exact behavior if the implementation encounters this problem: Feeding degrees into radian functions or allowing floating drift to distort direction vectors.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-18-04 — Turn the Camera — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Turn the Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/player_actions.adb

Implement the core milestone in the existing dungeon_walk crate: Rotate direction and camera vectors using sine and cosine with a clearly documented angle unit.

**Completion checks**

- Four quarter-turns return the camera to its original orientation within tolerance.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-18-05 — Turn the Camera — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Turn the Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/player_actions.adb

Extend the completed milestone with this practical variation: Add configurable turn speed and clamp or normalize accumulated angles.

**Completion checks**

- Four quarter-turns return the camera to its original orientation within tolerance.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-18-06 — Turn the Camera — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Turn the Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/player_actions.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Rotate direction and camera vectors using sine and cosine with a clearly documented angle unit.

**Completion checks**

- Four quarter-turns return the camera to its original orientation within tolerance.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-18-07 — Turn the Camera — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Turn the Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/player_actions.adb

Reproduce and repair this defect class in the current project: Feeding degrees into radian functions or allowing floating drift to distort direction vectors.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Four quarter-turns return the camera to its original orientation within tolerance.

### ADA-P1-18-08 — Turn the Camera — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Turn the Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/player_actions.adb

Refactor the chapter implementation so Ada.Numerics, trigonometry, modular angles, and precision is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-18-09 — Turn the Camera — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Turn the Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/player_actions.adb

Integrate this chapter into the running final product so it works with earlier milestones: Rotate direction and camera vectors using sine and cosine with a clearly documented angle unit.

**Completion checks**

- Four quarter-turns return the camera to its original orientation within tolerance.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-18-10 — Turn the Camera — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Turn the Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/dungeon_math.ads, src/player_actions.adb

Perform a senior-style checkpoint review of Turn the Camera in Dungeon Walk.

**Completion checks**

- Four quarter-turns return the camera to its original orientation within tolerance.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-19-01 — Generate One Ray per Screen Column — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Generate One Ray per Screen Column
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb

Answer one focused question before editing code: How should Interpolation, coordinate transforms, and functions over ranges be used to accomplish this milestone: Convert a screen column into a camera-space X coordinate and a world-space ray direction.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-19-02 — Generate One Ray per Screen Column — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Generate One Ray per Screen Column
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb

Read the current implementation around src/raycast.ads, src/raycast.adb. Trace how data enters, changes, and leaves the code for this milestone: Convert a screen column into a camera-space X coordinate and a world-space ray direction.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-19-03 — Generate One Ray per Screen Column — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Generate One Ray per Screen Column
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb

Predict the exact behavior if the implementation encounters this problem: Integer division collapsing camera coordinates or an off-by-one at the final column.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-19-04 — Generate One Ray per Screen Column — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Generate One Ray per Screen Column
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb

Implement the core milestone in the existing dungeon_walk crate: Convert a screen column into a camera-space X coordinate and a world-space ray direction.

**Completion checks**

- Left, center, and right columns generate expected ray directions.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-19-05 — Generate One Ray per Screen Column — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Generate One Ray per Screen Column
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb

Extend the completed milestone with this practical variation: Visualize ray directions in a diagnostic top-down mode.

**Completion checks**

- Left, center, and right columns generate expected ray directions.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-19-06 — Generate One Ray per Screen Column — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Generate One Ray per Screen Column
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Convert a screen column into a camera-space X coordinate and a world-space ray direction.

**Completion checks**

- Left, center, and right columns generate expected ray directions.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-19-07 — Generate One Ray per Screen Column — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Generate One Ray per Screen Column
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb

Reproduce and repair this defect class in the current project: Integer division collapsing camera coordinates or an off-by-one at the final column.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Left, center, and right columns generate expected ray directions.

### ADA-P1-19-08 — Generate One Ray per Screen Column — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Generate One Ray per Screen Column
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb

Refactor the chapter implementation so Interpolation, coordinate transforms, and functions over ranges is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-19-09 — Generate One Ray per Screen Column — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Generate One Ray per Screen Column
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb

Integrate this chapter into the running final product so it works with earlier milestones: Convert a screen column into a camera-space X coordinate and a world-space ray direction.

**Completion checks**

- Left, center, and right columns generate expected ray directions.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-19-10 — Generate One Ray per Screen Column — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Generate One Ray per Screen Column
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb

Perform a senior-style checkpoint review of Generate One Ray per Screen Column in Dungeon Walk.

**Completion checks**

- Left, center, and right columns generate expected ray directions.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-20-01 — Find Walls with DDA — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Find Walls with DDA
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb, tests/raycast_tests.adb

Answer one focused question before editing code: How should Algorithmic loops, step selection, and termination be used to accomplish this milestone: Implement grid-based digital differential analysis to find the first wall hit by each ray.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-20-02 — Find Walls with DDA — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Find Walls with DDA
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb, tests/raycast_tests.adb

Read the current implementation around src/raycast.ads, src/raycast.adb, tests/raycast_tests.adb. Trace how data enters, changes, and leaves the code for this milestone: Implement grid-based digital differential analysis to find the first wall hit by each ray.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-20-03 — Find Walls with DDA — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Find Walls with DDA
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb, tests/raycast_tests.adb

Predict the exact behavior if the implementation encounters this problem: Division by zero, stepping outside the map, or fisheye distortion from the wrong distance.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-20-04 — Find Walls with DDA — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Find Walls with DDA
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb, tests/raycast_tests.adb

Implement the core milestone in the existing dungeon_walk crate: Implement grid-based digital differential analysis to find the first wall hit by each ray.

**Completion checks**

- Known rays hit known cells at expected distances and always terminate.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-20-05 — Find Walls with DDA — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Find Walls with DDA
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb, tests/raycast_tests.adb

Extend the completed milestone with this practical variation: Return hit side, map cell, distance, and texture coordinate information.

**Completion checks**

- Known rays hit known cells at expected distances and always terminate.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-20-06 — Find Walls with DDA — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Find Walls with DDA
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb, tests/raycast_tests.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Implement grid-based digital differential analysis to find the first wall hit by each ray.

**Completion checks**

- Known rays hit known cells at expected distances and always terminate.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-20-07 — Find Walls with DDA — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Find Walls with DDA
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb, tests/raycast_tests.adb

Reproduce and repair this defect class in the current project: Division by zero, stepping outside the map, or fisheye distortion from the wrong distance.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Known rays hit known cells at expected distances and always terminate.

### ADA-P1-20-08 — Find Walls with DDA — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Find Walls with DDA
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb, tests/raycast_tests.adb

Refactor the chapter implementation so Algorithmic loops, step selection, and termination is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-20-09 — Find Walls with DDA — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Find Walls with DDA
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb, tests/raycast_tests.adb

Integrate this chapter into the running final product so it works with earlier milestones: Implement grid-based digital differential analysis to find the first wall hit by each ray.

**Completion checks**

- Known rays hit known cells at expected distances and always terminate.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-20-10 — Find Walls with DDA — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Find Walls with DDA
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/raycast.ads, src/raycast.adb, tests/raycast_tests.adb

Perform a senior-style checkpoint review of Find Walls with DDA in Dungeon Walk.

**Completion checks**

- Known rays hit known cells at expected distances and always terminate.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-21-01 — Render the Pseudo-3D View — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Render the Pseudo-3D View
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/renderer.ads, src/renderer.adb, src/frame_buffer.ads

Answer one focused question before editing code: How should Formatting, nested loops, buffers, and separation of model/view be used to accomplish this milestone: Convert ray distances into wall heights and render a buffered ASCII or ANSI frame with ceiling, walls, and floor.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-21-02 — Render the Pseudo-3D View — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Render the Pseudo-3D View
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/renderer.ads, src/renderer.adb, src/frame_buffer.ads

Read the current implementation around src/renderer.ads, src/renderer.adb, src/frame_buffer.ads. Trace how data enters, changes, and leaves the code for this milestone: Convert ray distances into wall heights and render a buffered ASCII or ANSI frame with ceiling, walls, and floor.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-21-03 — Render the Pseudo-3D View — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Render the Pseudo-3D View
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/renderer.ads, src/renderer.adb, src/frame_buffer.ads

Predict the exact behavior if the implementation encounters this problem: Printing one character at a time too slowly or embedding game rules in the renderer.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-21-04 — Render the Pseudo-3D View — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Render the Pseudo-3D View
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/renderer.ads, src/renderer.adb, src/frame_buffer.ads

Implement the core milestone in the existing dungeon_walk crate: Convert ray distances into wall heights and render a buffered ASCII or ANSI frame with ceiling, walls, and floor.

**Completion checks**

- A static test scene renders repeatably and movement changes perspective correctly.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-21-05 — Render the Pseudo-3D View — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Render the Pseudo-3D View
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/renderer.ads, src/renderer.adb, src/frame_buffer.ads

Extend the completed milestone with this practical variation: Add distance shading and side shading without changing ray logic.

**Completion checks**

- A static test scene renders repeatably and movement changes perspective correctly.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-21-06 — Render the Pseudo-3D View — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Render the Pseudo-3D View
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/renderer.ads, src/renderer.adb, src/frame_buffer.ads

Create automated or repeatable tests that prove the milestone and its boundaries: Convert ray distances into wall heights and render a buffered ASCII or ANSI frame with ceiling, walls, and floor.

**Completion checks**

- A static test scene renders repeatably and movement changes perspective correctly.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-21-07 — Render the Pseudo-3D View — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Render the Pseudo-3D View
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/renderer.ads, src/renderer.adb, src/frame_buffer.ads

Reproduce and repair this defect class in the current project: Printing one character at a time too slowly or embedding game rules in the renderer.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- A static test scene renders repeatably and movement changes perspective correctly.

### ADA-P1-21-08 — Render the Pseudo-3D View — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Render the Pseudo-3D View
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/renderer.ads, src/renderer.adb, src/frame_buffer.ads

Refactor the chapter implementation so Formatting, nested loops, buffers, and separation of model/view is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-21-09 — Render the Pseudo-3D View — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Render the Pseudo-3D View
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/renderer.ads, src/renderer.adb, src/frame_buffer.ads

Integrate this chapter into the running final product so it works with earlier milestones: Convert ray distances into wall heights and render a buffered ASCII or ANSI frame with ceiling, walls, and floor.

**Completion checks**

- A static test scene renders repeatably and movement changes perspective correctly.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-21-10 — Render the Pseudo-3D View — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Render the Pseudo-3D View
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/renderer.ads, src/renderer.adb, src/frame_buffer.ads

Perform a senior-style checkpoint review of Render the Pseudo-3D View in Dungeon Walk.

**Completion checks**

- A static test scene renders repeatably and movement changes perspective correctly.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-22-01 — Move Through the Dungeon Safely — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Through the Dungeon Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.adb, src/maps.adb, tests/movement_tests.adb

Answer one focused question before editing code: How should State transitions, collision detection, and boundary checks be used to accomplish this milestone: Apply forward, backward, and strafing movement only when the destination is walkable.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-22-02 — Move Through the Dungeon Safely — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Through the Dungeon Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.adb, src/maps.adb, tests/movement_tests.adb

Read the current implementation around src/player_actions.adb, src/maps.adb, tests/movement_tests.adb. Trace how data enters, changes, and leaves the code for this milestone: Apply forward, backward, and strafing movement only when the destination is walkable.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-22-03 — Move Through the Dungeon Safely — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Through the Dungeon Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.adb, src/maps.adb, tests/movement_tests.adb

Predict the exact behavior if the implementation encounters this problem: Tunneling through corners or checking only the final cell for larger movements.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-22-04 — Move Through the Dungeon Safely — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Through the Dungeon Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.adb, src/maps.adb, tests/movement_tests.adb

Implement the core milestone in the existing dungeon_walk crate: Apply forward, backward, and strafing movement only when the destination is walkable.

**Completion checks**

- The player cannot enter solid tiles and can move smoothly through legal corridors.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-22-05 — Move Through the Dungeon Safely — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Through the Dungeon Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.adb, src/maps.adb, tests/movement_tests.adb

Extend the completed milestone with this practical variation: Add sliding along walls and a configurable collision radius.

**Completion checks**

- The player cannot enter solid tiles and can move smoothly through legal corridors.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-22-06 — Move Through the Dungeon Safely — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Through the Dungeon Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.adb, src/maps.adb, tests/movement_tests.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Apply forward, backward, and strafing movement only when the destination is walkable.

**Completion checks**

- The player cannot enter solid tiles and can move smoothly through legal corridors.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-22-07 — Move Through the Dungeon Safely — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Through the Dungeon Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.adb, src/maps.adb, tests/movement_tests.adb

Reproduce and repair this defect class in the current project: Tunneling through corners or checking only the final cell for larger movements.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- The player cannot enter solid tiles and can move smoothly through legal corridors.

### ADA-P1-22-08 — Move Through the Dungeon Safely — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Through the Dungeon Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.adb, src/maps.adb, tests/movement_tests.adb

Refactor the chapter implementation so State transitions, collision detection, and boundary checks is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-22-09 — Move Through the Dungeon Safely — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Through the Dungeon Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.adb, src/maps.adb, tests/movement_tests.adb

Integrate this chapter into the running final product so it works with earlier milestones: Apply forward, backward, and strafing movement only when the destination is walkable.

**Completion checks**

- The player cannot enter solid tiles and can move smoothly through legal corridors.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-22-10 — Move Through the Dungeon Safely — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Move Through the Dungeon Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/player_actions.adb, src/maps.adb, tests/movement_tests.adb

Perform a senior-style checkpoint review of Move Through the Dungeon Safely in Dungeon Walk.

**Completion checks**

- The player cannot enter solid tiles and can move smoothly through legal corridors.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-23-01 — Doors, Pickups, and Save Data — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Doors, Pickups, and Save Data
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/entities.ads, src/entities.adb, src/save_games.adb

Answer one focused question before editing code: How should Variant records, collections, and persistence be used to accomplish this milestone: Add simple doors and pickups plus save/load of player state and changed map state.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-23-02 — Doors, Pickups, and Save Data — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Doors, Pickups, and Save Data
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/entities.ads, src/entities.adb, src/save_games.adb

Read the current implementation around src/entities.ads, src/entities.adb, src/save_games.adb. Trace how data enters, changes, and leaves the code for this milestone: Add simple doors and pickups plus save/load of player state and changed map state.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-23-03 — Doors, Pickups, and Save Data — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Doors, Pickups, and Save Data
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/entities.ads, src/entities.adb, src/save_games.adb

Predict the exact behavior if the implementation encounters this problem: Saving pointers or transient rendering data instead of stable domain data.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-23-04 — Doors, Pickups, and Save Data — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Doors, Pickups, and Save Data
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/entities.ads, src/entities.adb, src/save_games.adb

Implement the core milestone in the existing dungeon_walk crate: Add simple doors and pickups plus save/load of player state and changed map state.

**Completion checks**

- Opening a door or taking a pickup persists through save and reload.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-23-05 — Doors, Pickups, and Save Data — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Doors, Pickups, and Save Data
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/entities.ads, src/entities.adb, src/save_games.adb

Extend the completed milestone with this practical variation: Give entities IDs and optional properties that later projects can reuse.

**Completion checks**

- Opening a door or taking a pickup persists through save and reload.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-23-06 — Doors, Pickups, and Save Data — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Doors, Pickups, and Save Data
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/entities.ads, src/entities.adb, src/save_games.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Add simple doors and pickups plus save/load of player state and changed map state.

**Completion checks**

- Opening a door or taking a pickup persists through save and reload.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-23-07 — Doors, Pickups, and Save Data — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Doors, Pickups, and Save Data
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/entities.ads, src/entities.adb, src/save_games.adb

Reproduce and repair this defect class in the current project: Saving pointers or transient rendering data instead of stable domain data.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Opening a door or taking a pickup persists through save and reload.

### ADA-P1-23-08 — Doors, Pickups, and Save Data — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Doors, Pickups, and Save Data
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/entities.ads, src/entities.adb, src/save_games.adb

Refactor the chapter implementation so Variant records, collections, and persistence is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-23-09 — Doors, Pickups, and Save Data — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Doors, Pickups, and Save Data
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/entities.ads, src/entities.adb, src/save_games.adb

Integrate this chapter into the running final product so it works with earlier milestones: Add simple doors and pickups plus save/load of player state and changed map state.

**Completion checks**

- Opening a door or taking a pickup persists through save and reload.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-23-10 — Doors, Pickups, and Save Data — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Doors, Pickups, and Save Data
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** src/entities.ads, src/entities.adb, src/save_games.adb

Perform a senior-style checkpoint review of Doors, Pickups, and Save Data in Dungeon Walk.

**Completion checks**

- Opening a door or taking a pickup persists through save and reload.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P1-24-01 — Finish Dungeon Walk — Question

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Finish Dungeon Walk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** tests/, README.md, CHANGELOG.md, docs/architecture.md

Answer one focused question before editing code: How should AUnit, assertions, documentation, profiling, and release discipline be used to accomplish this milestone: Complete tests, clean package boundaries, warning-free builds, user instructions, sample maps, and a tagged release.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P1-24-02 — Finish Dungeon Walk — Code Reading

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Finish Dungeon Walk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** tests/, README.md, CHANGELOG.md, docs/architecture.md

Read the current implementation around tests/, README.md, CHANGELOG.md, docs/architecture.md. Trace how data enters, changes, and leaves the code for this milestone: Complete tests, clean package boundaries, warning-free builds, user instructions, sample maps, and a tagged release.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P1-24-03 — Finish Dungeon Walk — Predict

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Finish Dungeon Walk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** tests/, README.md, CHANGELOG.md, docs/architecture.md

Predict the exact behavior if the implementation encounters this problem: Declaring completion while core behavior is only manually tested or warnings are ignored.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P1-24-04 — Finish Dungeon Walk — Implement

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Finish Dungeon Walk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** tests/, README.md, CHANGELOG.md, docs/architecture.md

Implement the core milestone in the existing dungeon_walk crate: Complete tests, clean package boundaries, warning-free builds, user instructions, sample maps, and a tagged release.

**Completion checks**

- A fresh clone can build, test, and run the final dungeon using documented commands.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P1-24-05 — Finish Dungeon Walk — Extend

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Finish Dungeon Walk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** tests/, README.md, CHANGELOG.md, docs/architecture.md

Extend the completed milestone with this practical variation: Add a benchmark or frame-time report and a troubleshooting section.

**Completion checks**

- A fresh clone can build, test, and run the final dungeon using documented commands.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P1-24-06 — Finish Dungeon Walk — Test

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Finish Dungeon Walk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** tests/, README.md, CHANGELOG.md, docs/architecture.md

Create automated or repeatable tests that prove the milestone and its boundaries: Complete tests, clean package boundaries, warning-free builds, user instructions, sample maps, and a tagged release.

**Completion checks**

- A fresh clone can build, test, and run the final dungeon using documented commands.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P1-24-07 — Finish Dungeon Walk — Repair

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Finish Dungeon Walk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** tests/, README.md, CHANGELOG.md, docs/architecture.md

Reproduce and repair this defect class in the current project: Declaring completion while core behavior is only manually tested or warnings are ignored.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- A fresh clone can build, test, and run the final dungeon using documented commands.

### ADA-P1-24-08 — Finish Dungeon Walk — Refactor

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Finish Dungeon Walk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** tests/, README.md, CHANGELOG.md, docs/architecture.md

Refactor the chapter implementation so AUnit, assertions, documentation, profiling, and release discipline is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P1-24-09 — Finish Dungeon Walk — Integrate

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Finish Dungeon Walk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** tests/, README.md, CHANGELOG.md, docs/architecture.md

Integrate this chapter into the running final product so it works with earlier milestones: Complete tests, clean package boundaries, warning-free builds, user instructions, sample maps, and a tagged release.

**Completion checks**

- A fresh clone can build, test, and run the final dungeon using documented commands.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P1-24-10 — Finish Dungeon Walk — Review

- **Project:** Project 1 — Dungeon Walk
- **Chapter:** Finish Dungeon Walk
- **Workspace:** `~/Documents/src/projects/ada-mastery/dungeon_walk`
- **Files:** tests/, README.md, CHANGELOG.md, docs/architecture.md

Perform a senior-style checkpoint review of Finish Dungeon Walk in Dungeon Walk.

**Completion checks**

- A fresh clone can build, test, and run the final dungeon using documented commands.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-01-01 — Define the Simulator Architecture — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define the Simulator Architecture
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/mission_sim.adb, src/domain/, src/runtime/, docs/architecture.md

Answer one focused question before editing code: How should Layered architecture and GPR/Alire organization be used to accomplish this milestone: Create domain, runtime, adapters, and application layers with dependency rules.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-01-02 — Define the Simulator Architecture — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define the Simulator Architecture
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/mission_sim.adb, src/domain/, src/runtime/, docs/architecture.md

Read the current implementation around src/mission_sim.adb, src/domain/, src/runtime/, docs/architecture.md. Trace how data enters, changes, and leaves the code for this milestone: Create domain, runtime, adapters, and application layers with dependency rules.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-01-03 — Define the Simulator Architecture — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define the Simulator Architecture
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/mission_sim.adb, src/domain/, src/runtime/, docs/architecture.md

Predict the exact behavior if the implementation encounters this problem: Letting UI/network code own domain state or creating circular package dependencies.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-01-04 — Define the Simulator Architecture — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define the Simulator Architecture
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/mission_sim.adb, src/domain/, src/runtime/, docs/architecture.md

Implement the core milestone in the existing mission_sim crate: Create domain, runtime, adapters, and application layers with dependency rules.

**Completion checks**

- The dependency direction is documented and the empty layers build.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-01-05 — Define the Simulator Architecture — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define the Simulator Architecture
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/mission_sim.adb, src/domain/, src/runtime/, docs/architecture.md

Extend the completed milestone with this practical variation: Add an architecture decision record explaining the deterministic core.

**Completion checks**

- The dependency direction is documented and the empty layers build.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-01-06 — Define the Simulator Architecture — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define the Simulator Architecture
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/mission_sim.adb, src/domain/, src/runtime/, docs/architecture.md

Create automated or repeatable tests that prove the milestone and its boundaries: Create domain, runtime, adapters, and application layers with dependency rules.

**Completion checks**

- The dependency direction is documented and the empty layers build.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-01-07 — Define the Simulator Architecture — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define the Simulator Architecture
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/mission_sim.adb, src/domain/, src/runtime/, docs/architecture.md

Reproduce and repair this defect class in the current project: Letting UI/network code own domain state or creating circular package dependencies.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- The dependency direction is documented and the empty layers build.

### ADA-P2-01-08 — Define the Simulator Architecture — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define the Simulator Architecture
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/mission_sim.adb, src/domain/, src/runtime/, docs/architecture.md

Refactor the chapter implementation so Layered architecture and GPR/Alire organization is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-01-09 — Define the Simulator Architecture — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define the Simulator Architecture
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/mission_sim.adb, src/domain/, src/runtime/, docs/architecture.md

Integrate this chapter into the running final product so it works with earlier milestones: Create domain, runtime, adapters, and application layers with dependency rules.

**Completion checks**

- The dependency direction is documented and the empty layers build.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-01-10 — Define the Simulator Architecture — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define the Simulator Architecture
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/mission_sim.adb, src/domain/, src/runtime/, docs/architecture.md

Perform a senior-style checkpoint review of Define the Simulator Architecture in Mission Simulator.

**Completion checks**

- The dependency direction is documented and the empty layers build.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-02-01 — Create Strong Physical Units — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Create Strong Physical Units
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/units.ads, src/domain/units.adb

Answer one focused question before editing code: How should Derived numeric types, private types, and unit-safe APIs be used to accomplish this milestone: Model altitude, speed, heading, time, voltage, and fuel as incompatible types.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-02-02 — Create Strong Physical Units — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Create Strong Physical Units
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/units.ads, src/domain/units.adb

Read the current implementation around src/domain/units.ads, src/domain/units.adb. Trace how data enters, changes, and leaves the code for this milestone: Model altitude, speed, heading, time, voltage, and fuel as incompatible types.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-02-03 — Create Strong Physical Units — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Create Strong Physical Units
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/units.ads, src/domain/units.adb

Predict the exact behavior if the implementation encounters this problem: Combining values with different units because they share a primitive representation.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-02-04 — Create Strong Physical Units — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Create Strong Physical Units
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/units.ads, src/domain/units.adb

Implement the core milestone in the existing mission_sim crate: Model altitude, speed, heading, time, voltage, and fuel as incompatible types.

**Completion checks**

- Invalid unit mixing fails to compile and valid calculations remain readable.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-02-05 — Create Strong Physical Units — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Create Strong Physical Units
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/units.ads, src/domain/units.adb

Extend the completed milestone with this practical variation: Add explicit conversions and formatting at adapter boundaries.

**Completion checks**

- Invalid unit mixing fails to compile and valid calculations remain readable.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-02-06 — Create Strong Physical Units — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Create Strong Physical Units
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/units.ads, src/domain/units.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Model altitude, speed, heading, time, voltage, and fuel as incompatible types.

**Completion checks**

- Invalid unit mixing fails to compile and valid calculations remain readable.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-02-07 — Create Strong Physical Units — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Create Strong Physical Units
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/units.ads, src/domain/units.adb

Reproduce and repair this defect class in the current project: Combining values with different units because they share a primitive representation.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Invalid unit mixing fails to compile and valid calculations remain readable.

### ADA-P2-02-08 — Create Strong Physical Units — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Create Strong Physical Units
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/units.ads, src/domain/units.adb

Refactor the chapter implementation so Derived numeric types, private types, and unit-safe APIs is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-02-09 — Create Strong Physical Units — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Create Strong Physical Units
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/units.ads, src/domain/units.adb

Integrate this chapter into the running final product so it works with earlier milestones: Model altitude, speed, heading, time, voltage, and fuel as incompatible types.

**Completion checks**

- Invalid unit mixing fails to compile and valid calculations remain readable.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-02-10 — Create Strong Physical Units — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Create Strong Physical Units
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/units.ads, src/domain/units.adb

Perform a senior-style checkpoint review of Create Strong Physical Units in Mission Simulator.

**Completion checks**

- Invalid unit mixing fails to compile and valid calculations remain readable.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-03-01 — Model Bus Messages — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Model Bus Messages
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/messages.ads, src/domain/messages.adb

Answer one focused question before editing code: How should Discriminated records and variant parts be used to accomplish this milestone: Represent command, status, sensor, and fault messages with one validated message family.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-03-02 — Model Bus Messages — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Model Bus Messages
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/messages.ads, src/domain/messages.adb

Read the current implementation around src/domain/messages.ads, src/domain/messages.adb. Trace how data enters, changes, and leaves the code for this milestone: Represent command, status, sensor, and fault messages with one validated message family.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-03-03 — Model Bus Messages — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Model Bus Messages
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/messages.ads, src/domain/messages.adb

Predict the exact behavior if the implementation encounters this problem: Reading the wrong variant field or using an unchecked catch-all byte array everywhere.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-03-04 — Model Bus Messages — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Model Bus Messages
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/messages.ads, src/domain/messages.adb

Implement the core milestone in the existing mission_sim crate: Represent command, status, sensor, and fault messages with one validated message family.

**Completion checks**

- Every message kind has only the fields it legally requires.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-03-05 — Model Bus Messages — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Model Bus Messages
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/messages.ads, src/domain/messages.adb

Extend the completed milestone with this practical variation: Add source, destination, sequence, and timestamp metadata.

**Completion checks**

- Every message kind has only the fields it legally requires.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-03-06 — Model Bus Messages — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Model Bus Messages
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/messages.ads, src/domain/messages.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Represent command, status, sensor, and fault messages with one validated message family.

**Completion checks**

- Every message kind has only the fields it legally requires.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-03-07 — Model Bus Messages — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Model Bus Messages
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/messages.ads, src/domain/messages.adb

Reproduce and repair this defect class in the current project: Reading the wrong variant field or using an unchecked catch-all byte array everywhere.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Every message kind has only the fields it legally requires.

### ADA-P2-03-08 — Model Bus Messages — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Model Bus Messages
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/messages.ads, src/domain/messages.adb

Refactor the chapter implementation so Discriminated records and variant parts is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-03-09 — Model Bus Messages — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Model Bus Messages
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/messages.ads, src/domain/messages.adb

Integrate this chapter into the running final product so it works with earlier milestones: Represent command, status, sensor, and fault messages with one validated message family.

**Completion checks**

- Every message kind has only the fields it legally requires.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-03-10 — Model Bus Messages — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Model Bus Messages
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/messages.ads, src/domain/messages.adb

Perform a senior-style checkpoint review of Model Bus Messages in Mission Simulator.

**Completion checks**

- Every message kind has only the fields it legally requires.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-04-01 — Define Replaceable Components — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define Replaceable Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/components.ads, src/components/

Answer one focused question before editing code: How should Tagged types, interfaces, dispatching, and composition be used to accomplish this milestone: Define component and sensor interfaces with initialization, step, status, and shutdown operations.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-04-02 — Define Replaceable Components — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define Replaceable Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/components.ads, src/components/

Read the current implementation around src/domain/components.ads, src/components/. Trace how data enters, changes, and leaves the code for this milestone: Define component and sensor interfaces with initialization, step, status, and shutdown operations.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-04-03 — Define Replaceable Components — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define Replaceable Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/components.ads, src/components/

Predict the exact behavior if the implementation encounters this problem: Building a deep inheritance tree instead of composing focused interfaces.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-04-04 — Define Replaceable Components — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define Replaceable Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/components.ads, src/components/

Implement the core milestone in the existing mission_sim crate: Define component and sensor interfaces with initialization, step, status, and shutdown operations.

**Completion checks**

- The runtime can drive multiple implementations without type-specific case statements.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-04-05 — Define Replaceable Components — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define Replaceable Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/components.ads, src/components/

Extend the completed milestone with this practical variation: Provide two sensor implementations behind the same interface.

**Completion checks**

- The runtime can drive multiple implementations without type-specific case statements.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-04-06 — Define Replaceable Components — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define Replaceable Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/components.ads, src/components/

Create automated or repeatable tests that prove the milestone and its boundaries: Define component and sensor interfaces with initialization, step, status, and shutdown operations.

**Completion checks**

- The runtime can drive multiple implementations without type-specific case statements.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-04-07 — Define Replaceable Components — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define Replaceable Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/components.ads, src/components/

Reproduce and repair this defect class in the current project: Building a deep inheritance tree instead of composing focused interfaces.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- The runtime can drive multiple implementations without type-specific case statements.

### ADA-P2-04-08 — Define Replaceable Components — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define Replaceable Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/components.ads, src/components/

Refactor the chapter implementation so Tagged types, interfaces, dispatching, and composition is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-04-09 — Define Replaceable Components — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define Replaceable Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/components.ads, src/components/

Integrate this chapter into the running final product so it works with earlier milestones: Define component and sensor interfaces with initialization, step, status, and shutdown operations.

**Completion checks**

- The runtime can drive multiple implementations without type-specific case statements.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-04-10 — Define Replaceable Components — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Define Replaceable Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/components.ads, src/components/

Perform a senior-style checkpoint review of Define Replaceable Components in Mission Simulator.

**Completion checks**

- The runtime can drive multiple implementations without type-specific case statements.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-05-01 — Build Reusable Typed Utilities — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build Reusable Typed Utilities
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/generics/bounded_buffers.ads, src/generics/range_monitors.ads

Answer one focused question before editing code: How should Generic packages and formal parameters be used to accomplish this milestone: Create generic bounded buffers, value filters, and range monitors for strongly typed values.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-05-02 — Build Reusable Typed Utilities — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build Reusable Typed Utilities
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/generics/bounded_buffers.ads, src/generics/range_monitors.ads

Read the current implementation around src/generics/bounded_buffers.ads, src/generics/range_monitors.ads. Trace how data enters, changes, and leaves the code for this milestone: Create generic bounded buffers, value filters, and range monitors for strongly typed values.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-05-03 — Build Reusable Typed Utilities — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build Reusable Typed Utilities
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/generics/bounded_buffers.ads, src/generics/range_monitors.ads

Predict the exact behavior if the implementation encounters this problem: Writing one untyped utility using conversions instead of expressing requirements generically.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-05-04 — Build Reusable Typed Utilities — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build Reusable Typed Utilities
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/generics/bounded_buffers.ads, src/generics/range_monitors.ads

Implement the core milestone in the existing mission_sim crate: Create generic bounded buffers, value filters, and range monitors for strongly typed values.

**Completion checks**

- At least three instantiations compile and retain their distinct types.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-05-05 — Build Reusable Typed Utilities — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build Reusable Typed Utilities
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/generics/bounded_buffers.ads, src/generics/range_monitors.ads

Extend the completed milestone with this practical variation: Instantiate utilities for multiple unit types and message types.

**Completion checks**

- At least three instantiations compile and retain their distinct types.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-05-06 — Build Reusable Typed Utilities — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build Reusable Typed Utilities
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/generics/bounded_buffers.ads, src/generics/range_monitors.ads

Create automated or repeatable tests that prove the milestone and its boundaries: Create generic bounded buffers, value filters, and range monitors for strongly typed values.

**Completion checks**

- At least three instantiations compile and retain their distinct types.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-05-07 — Build Reusable Typed Utilities — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build Reusable Typed Utilities
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/generics/bounded_buffers.ads, src/generics/range_monitors.ads

Reproduce and repair this defect class in the current project: Writing one untyped utility using conversions instead of expressing requirements generically.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- At least three instantiations compile and retain their distinct types.

### ADA-P2-05-08 — Build Reusable Typed Utilities — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build Reusable Typed Utilities
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/generics/bounded_buffers.ads, src/generics/range_monitors.ads

Refactor the chapter implementation so Generic packages and formal parameters is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-05-09 — Build Reusable Typed Utilities — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build Reusable Typed Utilities
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/generics/bounded_buffers.ads, src/generics/range_monitors.ads

Integrate this chapter into the running final product so it works with earlier milestones: Create generic bounded buffers, value filters, and range monitors for strongly typed values.

**Completion checks**

- At least three instantiations compile and retain their distinct types.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-05-10 — Build Reusable Typed Utilities — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build Reusable Typed Utilities
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/generics/bounded_buffers.ads, src/generics/range_monitors.ads

Perform a senior-style checkpoint review of Build Reusable Typed Utilities in Mission Simulator.

**Completion checks**

- At least three instantiations compile and retain their distinct types.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-06-01 — Manage Components and Events — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Components and Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_registry.ads, src/runtime/event_store.ads

Answer one focused question before editing code: How should Ada.Containers vectors, maps, sets, and iteration be used to accomplish this milestone: Store registered components, scheduled events, active faults, and telemetry history in appropriate containers.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-06-02 — Manage Components and Events — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Components and Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_registry.ads, src/runtime/event_store.ads

Read the current implementation around src/runtime/component_registry.ads, src/runtime/event_store.ads. Trace how data enters, changes, and leaves the code for this milestone: Store registered components, scheduled events, active faults, and telemetry history in appropriate containers.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-06-03 — Manage Components and Events — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Components and Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_registry.ads, src/runtime/event_store.ads

Predict the exact behavior if the implementation encounters this problem: Depending on hashed-container iteration order for simulation behavior.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-06-04 — Manage Components and Events — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Components and Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_registry.ads, src/runtime/event_store.ads

Implement the core milestone in the existing mission_sim crate: Store registered components, scheduled events, active faults, and telemetry history in appropriate containers.

**Completion checks**

- Registry and event ordering are deterministic and tested.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-06-05 — Manage Components and Events — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Components and Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_registry.ads, src/runtime/event_store.ads

Extend the completed milestone with this practical variation: Add stable lookup by component ID and ordered iteration for deterministic runs.

**Completion checks**

- Registry and event ordering are deterministic and tested.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-06-06 — Manage Components and Events — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Components and Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_registry.ads, src/runtime/event_store.ads

Create automated or repeatable tests that prove the milestone and its boundaries: Store registered components, scheduled events, active faults, and telemetry history in appropriate containers.

**Completion checks**

- Registry and event ordering are deterministic and tested.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-06-07 — Manage Components and Events — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Components and Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_registry.ads, src/runtime/event_store.ads

Reproduce and repair this defect class in the current project: Depending on hashed-container iteration order for simulation behavior.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Registry and event ordering are deterministic and tested.

### ADA-P2-06-08 — Manage Components and Events — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Components and Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_registry.ads, src/runtime/event_store.ads

Refactor the chapter implementation so Ada.Containers vectors, maps, sets, and iteration is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-06-09 — Manage Components and Events — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Components and Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_registry.ads, src/runtime/event_store.ads

Integrate this chapter into the running final product so it works with earlier milestones: Store registered components, scheduled events, active faults, and telemetry history in appropriate containers.

**Completion checks**

- Registry and event ordering are deterministic and tested.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-06-10 — Manage Components and Events — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Components and Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_registry.ads, src/runtime/event_store.ads

Perform a senior-style checkpoint review of Manage Components and Events in Mission Simulator.

**Completion checks**

- Registry and event ordering are deterministic and tested.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-07-01 — Control Dynamic Lifetime — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Control Dynamic Lifetime
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_factory.ads, src/runtime/component_registry.adb

Answer one focused question before editing code: How should Access types, accessibility, aliased objects, and ownership boundaries be used to accomplish this milestone: Use access values only where dynamic polymorphism or lifetime requires them and document the owner.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-07-02 — Control Dynamic Lifetime — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Control Dynamic Lifetime
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_factory.ads, src/runtime/component_registry.adb

Read the current implementation around src/runtime/component_factory.ads, src/runtime/component_registry.adb. Trace how data enters, changes, and leaves the code for this milestone: Use access values only where dynamic polymorphism or lifetime requires them and document the owner.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-07-03 — Control Dynamic Lifetime — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Control Dynamic Lifetime
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_factory.ads, src/runtime/component_registry.adb

Predict the exact behavior if the implementation encounters this problem: Dangling references, anonymous access types spread through APIs, or unclear ownership.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-07-04 — Control Dynamic Lifetime — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Control Dynamic Lifetime
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_factory.ads, src/runtime/component_registry.adb

Implement the core milestone in the existing mission_sim crate: Use access values only where dynamic polymorphism or lifetime requires them and document the owner.

**Completion checks**

- Every allocated object has one documented owner and a tested shutdown path.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-07-05 — Control Dynamic Lifetime — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Control Dynamic Lifetime
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_factory.ads, src/runtime/component_registry.adb

Extend the completed milestone with this practical variation: Add a component factory with a clear destroy/shutdown path.

**Completion checks**

- Every allocated object has one documented owner and a tested shutdown path.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-07-06 — Control Dynamic Lifetime — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Control Dynamic Lifetime
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_factory.ads, src/runtime/component_registry.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Use access values only where dynamic polymorphism or lifetime requires them and document the owner.

**Completion checks**

- Every allocated object has one documented owner and a tested shutdown path.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-07-07 — Control Dynamic Lifetime — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Control Dynamic Lifetime
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_factory.ads, src/runtime/component_registry.adb

Reproduce and repair this defect class in the current project: Dangling references, anonymous access types spread through APIs, or unclear ownership.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Every allocated object has one documented owner and a tested shutdown path.

### ADA-P2-07-08 — Control Dynamic Lifetime — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Control Dynamic Lifetime
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_factory.ads, src/runtime/component_registry.adb

Refactor the chapter implementation so Access types, accessibility, aliased objects, and ownership boundaries is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-07-09 — Control Dynamic Lifetime — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Control Dynamic Lifetime
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_factory.ads, src/runtime/component_registry.adb

Integrate this chapter into the running final product so it works with earlier milestones: Use access values only where dynamic polymorphism or lifetime requires them and document the owner.

**Completion checks**

- Every allocated object has one documented owner and a tested shutdown path.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-07-10 — Control Dynamic Lifetime — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Control Dynamic Lifetime
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_factory.ads, src/runtime/component_registry.adb

Perform a senior-style checkpoint review of Control Dynamic Lifetime in Mission Simulator.

**Completion checks**

- Every allocated object has one documented owner and a tested shutdown path.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-08-01 — Manage Resources Safely — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Resources Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/managed_log.ads, src/adapters/managed_log.adb

Answer one focused question before editing code: How should Controlled and limited controlled types be used to accomplish this milestone: Wrap a log stream or external handle so initialization and finalization are reliable during exceptions.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-08-02 — Manage Resources Safely — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Resources Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/managed_log.ads, src/adapters/managed_log.adb

Read the current implementation around src/adapters/managed_log.ads, src/adapters/managed_log.adb. Trace how data enters, changes, and leaves the code for this milestone: Wrap a log stream or external handle so initialization and finalization are reliable during exceptions.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-08-03 — Manage Resources Safely — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Resources Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/managed_log.ads, src/adapters/managed_log.adb

Predict the exact behavior if the implementation encounters this problem: Double-closing copied resources or depending on manual cleanup at every call site.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-08-04 — Manage Resources Safely — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Resources Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/managed_log.ads, src/adapters/managed_log.adb

Implement the core milestone in the existing mission_sim crate: Wrap a log stream or external handle so initialization and finalization are reliable during exceptions.

**Completion checks**

- Resources close exactly once in normal and exceptional paths.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-08-05 — Manage Resources Safely — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Resources Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/managed_log.ads, src/adapters/managed_log.adb

Extend the completed milestone with this practical variation: Add adjustment rules or prohibit copying when duplication is unsafe.

**Completion checks**

- Resources close exactly once in normal and exceptional paths.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-08-06 — Manage Resources Safely — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Resources Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/managed_log.ads, src/adapters/managed_log.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Wrap a log stream or external handle so initialization and finalization are reliable during exceptions.

**Completion checks**

- Resources close exactly once in normal and exceptional paths.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-08-07 — Manage Resources Safely — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Resources Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/managed_log.ads, src/adapters/managed_log.adb

Reproduce and repair this defect class in the current project: Double-closing copied resources or depending on manual cleanup at every call site.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Resources close exactly once in normal and exceptional paths.

### ADA-P2-08-08 — Manage Resources Safely — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Resources Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/managed_log.ads, src/adapters/managed_log.adb

Refactor the chapter implementation so Controlled and limited controlled types is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-08-09 — Manage Resources Safely — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Resources Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/managed_log.ads, src/adapters/managed_log.adb

Integrate this chapter into the running final product so it works with earlier milestones: Wrap a log stream or external handle so initialization and finalization are reliable during exceptions.

**Completion checks**

- Resources close exactly once in normal and exceptional paths.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-08-10 — Manage Resources Safely — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Manage Resources Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/managed_log.ads, src/adapters/managed_log.adb

Perform a senior-style checkpoint review of Manage Resources Safely in Mission Simulator.

**Completion checks**

- Resources close exactly once in normal and exceptional paths.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-09-01 — State Contracts Explicitly — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** State Contracts Explicitly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/, src/runtime/, docs/contracts.md

Answer one focused question before editing code: How should Preconditions, postconditions, predicates, invariants, and assertions be used to accomplish this milestone: Add contracts to units, messages, scheduler operations, and component state transitions.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-09-02 — State Contracts Explicitly — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** State Contracts Explicitly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/, src/runtime/, docs/contracts.md

Read the current implementation around src/domain/, src/runtime/, docs/contracts.md. Trace how data enters, changes, and leaves the code for this milestone: Add contracts to units, messages, scheduler operations, and component state transitions.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-09-03 — State Contracts Explicitly — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** State Contracts Explicitly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/, src/runtime/, docs/contracts.md

Predict the exact behavior if the implementation encounters this problem: Writing contracts that repeat implementation details or have side effects.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-09-04 — State Contracts Explicitly — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** State Contracts Explicitly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/, src/runtime/, docs/contracts.md

Implement the core milestone in the existing mission_sim crate: Add contracts to units, messages, scheduler operations, and component state transitions.

**Completion checks**

- Boundary violations fail close to their source with useful diagnostics.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-09-05 — State Contracts Explicitly — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** State Contracts Explicitly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/, src/runtime/, docs/contracts.md

Extend the completed milestone with this practical variation: Enable contract checks in development and define a release policy.

**Completion checks**

- Boundary violations fail close to their source with useful diagnostics.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-09-06 — State Contracts Explicitly — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** State Contracts Explicitly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/, src/runtime/, docs/contracts.md

Create automated or repeatable tests that prove the milestone and its boundaries: Add contracts to units, messages, scheduler operations, and component state transitions.

**Completion checks**

- Boundary violations fail close to their source with useful diagnostics.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-09-07 — State Contracts Explicitly — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** State Contracts Explicitly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/, src/runtime/, docs/contracts.md

Reproduce and repair this defect class in the current project: Writing contracts that repeat implementation details or have side effects.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Boundary violations fail close to their source with useful diagnostics.

### ADA-P2-09-08 — State Contracts Explicitly — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** State Contracts Explicitly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/, src/runtime/, docs/contracts.md

Refactor the chapter implementation so Preconditions, postconditions, predicates, invariants, and assertions is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-09-09 — State Contracts Explicitly — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** State Contracts Explicitly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/, src/runtime/, docs/contracts.md

Integrate this chapter into the running final product so it works with earlier milestones: Add contracts to units, messages, scheduler operations, and component state transitions.

**Completion checks**

- Boundary violations fail close to their source with useful diagnostics.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-09-10 — State Contracts Explicitly — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** State Contracts Explicitly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/domain/, src/runtime/, docs/contracts.md

Perform a senior-style checkpoint review of State Contracts Explicitly in Mission Simulator.

**Completion checks**

- Boundary violations fail close to their source with useful diagnostics.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-10-01 — Design Error and Logging Boundaries — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Design Error and Logging Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/errors.ads, src/adapters/logging.ads, src/mission_sim.adb

Answer one focused question before editing code: How should Exception taxonomy, logging levels, and fault containment be used to accomplish this milestone: Separate configuration errors, data errors, component faults, and fatal runtime failures.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-10-02 — Design Error and Logging Boundaries — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Design Error and Logging Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/errors.ads, src/adapters/logging.ads, src/mission_sim.adb

Read the current implementation around src/runtime/errors.ads, src/adapters/logging.ads, src/mission_sim.adb. Trace how data enters, changes, and leaves the code for this milestone: Separate configuration errors, data errors, component faults, and fatal runtime failures.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-10-03 — Design Error and Logging Boundaries — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Design Error and Logging Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/errors.ads, src/adapters/logging.ads, src/mission_sim.adb

Predict the exact behavior if the implementation encounters this problem: Catching others inside every component and pretending the simulation succeeded.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-10-04 — Design Error and Logging Boundaries — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Design Error and Logging Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/errors.ads, src/adapters/logging.ads, src/mission_sim.adb

Implement the core milestone in the existing mission_sim crate: Separate configuration errors, data errors, component faults, and fatal runtime failures.

**Completion checks**

- Recoverable component faults are isolated while fatal corruption stops the run.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-10-05 — Design Error and Logging Boundaries — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Design Error and Logging Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/errors.ads, src/adapters/logging.ads, src/mission_sim.adb

Extend the completed milestone with this practical variation: Add structured context: tick, component, message, and scenario.

**Completion checks**

- Recoverable component faults are isolated while fatal corruption stops the run.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-10-06 — Design Error and Logging Boundaries — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Design Error and Logging Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/errors.ads, src/adapters/logging.ads, src/mission_sim.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Separate configuration errors, data errors, component faults, and fatal runtime failures.

**Completion checks**

- Recoverable component faults are isolated while fatal corruption stops the run.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-10-07 — Design Error and Logging Boundaries — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Design Error and Logging Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/errors.ads, src/adapters/logging.ads, src/mission_sim.adb

Reproduce and repair this defect class in the current project: Catching others inside every component and pretending the simulation succeeded.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Recoverable component faults are isolated while fatal corruption stops the run.

### ADA-P2-10-08 — Design Error and Logging Boundaries — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Design Error and Logging Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/errors.ads, src/adapters/logging.ads, src/mission_sim.adb

Refactor the chapter implementation so Exception taxonomy, logging levels, and fault containment is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-10-09 — Design Error and Logging Boundaries — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Design Error and Logging Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/errors.ads, src/adapters/logging.ads, src/mission_sim.adb

Integrate this chapter into the running final product so it works with earlier milestones: Separate configuration errors, data errors, component faults, and fatal runtime failures.

**Completion checks**

- Recoverable component faults are isolated while fatal corruption stops the run.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-10-10 — Design Error and Logging Boundaries — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Design Error and Logging Boundaries
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/errors.ads, src/adapters/logging.ads, src/mission_sim.adb

Perform a senior-style checkpoint review of Design Error and Logging Boundaries in Mission Simulator.

**Completion checks**

- Recoverable component faults are isolated while fatal corruption stops the run.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-11-01 — Load Typed Configuration — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Load Typed Configuration
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/configuration.ads, src/adapters/configuration.adb, data/scenarios/default.cfg

Answer one focused question before editing code: How should Configuration parsing, defaults, validation, and immutable startup state be used to accomplish this milestone: Load tick rate, component definitions, routes, and fault scenarios into validated records.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-11-02 — Load Typed Configuration — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Load Typed Configuration
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/configuration.ads, src/adapters/configuration.adb, data/scenarios/default.cfg

Read the current implementation around src/adapters/configuration.ads, src/adapters/configuration.adb, data/scenarios/default.cfg. Trace how data enters, changes, and leaves the code for this milestone: Load tick rate, component definitions, routes, and fault scenarios into validated records.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-11-03 — Load Typed Configuration — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Load Typed Configuration
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/configuration.ads, src/adapters/configuration.adb, data/scenarios/default.cfg

Predict the exact behavior if the implementation encounters this problem: Reading configuration repeatedly during deterministic execution or accepting unknown keys silently.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-11-04 — Load Typed Configuration — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Load Typed Configuration
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/configuration.ads, src/adapters/configuration.adb, data/scenarios/default.cfg

Implement the core milestone in the existing mission_sim crate: Load tick rate, component definitions, routes, and fault scenarios into validated records.

**Completion checks**

- Invalid configuration fails before startup and valid configuration becomes immutable.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-11-05 — Load Typed Configuration — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Load Typed Configuration
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/configuration.ads, src/adapters/configuration.adb, data/scenarios/default.cfg

Extend the completed milestone with this practical variation: Generate a human-readable effective configuration dump.

**Completion checks**

- Invalid configuration fails before startup and valid configuration becomes immutable.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-11-06 — Load Typed Configuration — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Load Typed Configuration
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/configuration.ads, src/adapters/configuration.adb, data/scenarios/default.cfg

Create automated or repeatable tests that prove the milestone and its boundaries: Load tick rate, component definitions, routes, and fault scenarios into validated records.

**Completion checks**

- Invalid configuration fails before startup and valid configuration becomes immutable.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-11-07 — Load Typed Configuration — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Load Typed Configuration
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/configuration.ads, src/adapters/configuration.adb, data/scenarios/default.cfg

Reproduce and repair this defect class in the current project: Reading configuration repeatedly during deterministic execution or accepting unknown keys silently.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Invalid configuration fails before startup and valid configuration becomes immutable.

### ADA-P2-11-08 — Load Typed Configuration — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Load Typed Configuration
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/configuration.ads, src/adapters/configuration.adb, data/scenarios/default.cfg

Refactor the chapter implementation so Configuration parsing, defaults, validation, and immutable startup state is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-11-09 — Load Typed Configuration — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Load Typed Configuration
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/configuration.ads, src/adapters/configuration.adb, data/scenarios/default.cfg

Integrate this chapter into the running final product so it works with earlier milestones: Load tick rate, component definitions, routes, and fault scenarios into validated records.

**Completion checks**

- Invalid configuration fails before startup and valid configuration becomes immutable.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-11-10 — Load Typed Configuration — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Load Typed Configuration
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/configuration.ads, src/adapters/configuration.adb, data/scenarios/default.cfg

Perform a senior-style checkpoint review of Load Typed Configuration in Mission Simulator.

**Completion checks**

- Invalid configuration fails before startup and valid configuration becomes immutable.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-12-01 — Serialize Messages and State — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Serialize Messages and State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/wire_format.ads, src/adapters/wire_format.adb

Answer one focused question before editing code: How should Streams, attributes, representation, and versioned formats be used to accomplish this milestone: Serialize bus messages, snapshots, and replay records with an explicit format version.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-12-02 — Serialize Messages and State — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Serialize Messages and State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/wire_format.ads, src/adapters/wire_format.adb

Read the current implementation around src/adapters/wire_format.ads, src/adapters/wire_format.adb. Trace how data enters, changes, and leaves the code for this milestone: Serialize bus messages, snapshots, and replay records with an explicit format version.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-12-03 — Serialize Messages and State — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Serialize Messages and State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/wire_format.ads, src/adapters/wire_format.adb

Predict the exact behavior if the implementation encounters this problem: Persisting compiler-dependent record layout without controlling the wire format.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-12-04 — Serialize Messages and State — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Serialize Messages and State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/wire_format.ads, src/adapters/wire_format.adb

Implement the core milestone in the existing mission_sim crate: Serialize bus messages, snapshots, and replay records with an explicit format version.

**Completion checks**

- Encode-decode round trips preserve all legal message variants.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-12-05 — Serialize Messages and State — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Serialize Messages and State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/wire_format.ads, src/adapters/wire_format.adb

Extend the completed milestone with this practical variation: Add round-trip tests and backward-compatible reading for one prior version.

**Completion checks**

- Encode-decode round trips preserve all legal message variants.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-12-06 — Serialize Messages and State — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Serialize Messages and State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/wire_format.ads, src/adapters/wire_format.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Serialize bus messages, snapshots, and replay records with an explicit format version.

**Completion checks**

- Encode-decode round trips preserve all legal message variants.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-12-07 — Serialize Messages and State — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Serialize Messages and State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/wire_format.ads, src/adapters/wire_format.adb

Reproduce and repair this defect class in the current project: Persisting compiler-dependent record layout without controlling the wire format.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Encode-decode round trips preserve all legal message variants.

### ADA-P2-12-08 — Serialize Messages and State — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Serialize Messages and State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/wire_format.ads, src/adapters/wire_format.adb

Refactor the chapter implementation so Streams, attributes, representation, and versioned formats is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-12-09 — Serialize Messages and State — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Serialize Messages and State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/wire_format.ads, src/adapters/wire_format.adb

Integrate this chapter into the running final product so it works with earlier milestones: Serialize bus messages, snapshots, and replay records with an explicit format version.

**Completion checks**

- Encode-decode round trips preserve all legal message variants.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-12-10 — Serialize Messages and State — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Serialize Messages and State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/wire_format.ads, src/adapters/wire_format.adb

Perform a senior-style checkpoint review of Serialize Messages and State in Mission Simulator.

**Completion checks**

- Encode-decode round trips preserve all legal message variants.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-13-01 — Introduce Active Components — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Introduce Active Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_tasks.ads, src/runtime/component_tasks.adb

Answer one focused question before editing code: How should Tasks, task types, activation, termination, and ownership be used to accomplish this milestone: Run selected sensors or adapters as tasks while keeping the deterministic domain step explicit.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-13-02 — Introduce Active Components — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Introduce Active Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_tasks.ads, src/runtime/component_tasks.adb

Read the current implementation around src/runtime/component_tasks.ads, src/runtime/component_tasks.adb. Trace how data enters, changes, and leaves the code for this milestone: Run selected sensors or adapters as tasks while keeping the deterministic domain step explicit.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-13-03 — Introduce Active Components — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Introduce Active Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_tasks.ads, src/runtime/component_tasks.adb

Predict the exact behavior if the implementation encounters this problem: Tasks starting before dependencies are initialized or hanging during shutdown.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-13-04 — Introduce Active Components — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Introduce Active Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_tasks.ads, src/runtime/component_tasks.adb

Implement the core milestone in the existing mission_sim crate: Run selected sensors or adapters as tasks while keeping the deterministic domain step explicit.

**Completion checks**

- All tasks start after initialization and terminate without forced process exit.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-13-05 — Introduce Active Components — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Introduce Active Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_tasks.ads, src/runtime/component_tasks.adb

Extend the completed milestone with this practical variation: Add orderly startup and shutdown coordination.

**Completion checks**

- All tasks start after initialization and terminate without forced process exit.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-13-06 — Introduce Active Components — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Introduce Active Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_tasks.ads, src/runtime/component_tasks.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Run selected sensors or adapters as tasks while keeping the deterministic domain step explicit.

**Completion checks**

- All tasks start after initialization and terminate without forced process exit.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-13-07 — Introduce Active Components — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Introduce Active Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_tasks.ads, src/runtime/component_tasks.adb

Reproduce and repair this defect class in the current project: Tasks starting before dependencies are initialized or hanging during shutdown.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- All tasks start after initialization and terminate without forced process exit.

### ADA-P2-13-08 — Introduce Active Components — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Introduce Active Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_tasks.ads, src/runtime/component_tasks.adb

Refactor the chapter implementation so Tasks, task types, activation, termination, and ownership is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-13-09 — Introduce Active Components — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Introduce Active Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_tasks.ads, src/runtime/component_tasks.adb

Integrate this chapter into the running final product so it works with earlier milestones: Run selected sensors or adapters as tasks while keeping the deterministic domain step explicit.

**Completion checks**

- All tasks start after initialization and terminate without forced process exit.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-13-10 — Introduce Active Components — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Introduce Active Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/component_tasks.ads, src/runtime/component_tasks.adb

Perform a senior-style checkpoint review of Introduce Active Components in Mission Simulator.

**Completion checks**

- All tasks start after initialization and terminate without forced process exit.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-14-01 — Protect Shared Runtime State — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Protect Shared Runtime State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/protected_queues.ads, src/runtime/telemetry_store.ads

Answer one focused question before editing code: How should Protected objects, protected functions, procedures, and entries be used to accomplish this milestone: Create protected telemetry snapshots and bounded message queues.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-14-02 — Protect Shared Runtime State — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Protect Shared Runtime State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/protected_queues.ads, src/runtime/telemetry_store.ads

Read the current implementation around src/runtime/protected_queues.ads, src/runtime/telemetry_store.ads. Trace how data enters, changes, and leaves the code for this milestone: Create protected telemetry snapshots and bounded message queues.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-14-03 — Protect Shared Runtime State — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Protect Shared Runtime State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/protected_queues.ads, src/runtime/telemetry_store.ads

Predict the exact behavior if the implementation encounters this problem: Holding protected locks while performing file or network I/O.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-14-04 — Protect Shared Runtime State — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Protect Shared Runtime State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/protected_queues.ads, src/runtime/telemetry_store.ads

Implement the core milestone in the existing mission_sim crate: Create protected telemetry snapshots and bounded message queues.

**Completion checks**

- Concurrent producers and consumers preserve data and never race.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-14-05 — Protect Shared Runtime State — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Protect Shared Runtime State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/protected_queues.ads, src/runtime/telemetry_store.ads

Extend the completed milestone with this practical variation: Add blocking and nonblocking queue operations with clear capacity behavior.

**Completion checks**

- Concurrent producers and consumers preserve data and never race.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-14-06 — Protect Shared Runtime State — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Protect Shared Runtime State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/protected_queues.ads, src/runtime/telemetry_store.ads

Create automated or repeatable tests that prove the milestone and its boundaries: Create protected telemetry snapshots and bounded message queues.

**Completion checks**

- Concurrent producers and consumers preserve data and never race.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-14-07 — Protect Shared Runtime State — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Protect Shared Runtime State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/protected_queues.ads, src/runtime/telemetry_store.ads

Reproduce and repair this defect class in the current project: Holding protected locks while performing file or network I/O.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Concurrent producers and consumers preserve data and never race.

### ADA-P2-14-08 — Protect Shared Runtime State — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Protect Shared Runtime State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/protected_queues.ads, src/runtime/telemetry_store.ads

Refactor the chapter implementation so Protected objects, protected functions, procedures, and entries is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-14-09 — Protect Shared Runtime State — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Protect Shared Runtime State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/protected_queues.ads, src/runtime/telemetry_store.ads

Integrate this chapter into the running final product so it works with earlier milestones: Create protected telemetry snapshots and bounded message queues.

**Completion checks**

- Concurrent producers and consumers preserve data and never race.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-14-10 — Protect Shared Runtime State — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Protect Shared Runtime State
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/protected_queues.ads, src/runtime/telemetry_store.ads

Perform a senior-style checkpoint review of Protect Shared Runtime State in Mission Simulator.

**Completion checks**

- Concurrent producers and consumers preserve data and never race.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-15-01 — Coordinate with Entries and Select — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Coordinate with Entries and Select
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/control_task.ads, src/runtime/control_task.adb

Answer one focused question before editing code: How should Rendezvous, entry guards, selective accept, and asynchronous transfer concepts be used to accomplish this milestone: Build a control task that accepts pause, resume, step, snapshot, and shutdown requests.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-15-02 — Coordinate with Entries and Select — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Coordinate with Entries and Select
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/control_task.ads, src/runtime/control_task.adb

Read the current implementation around src/runtime/control_task.ads, src/runtime/control_task.adb. Trace how data enters, changes, and leaves the code for this milestone: Build a control task that accepts pause, resume, step, snapshot, and shutdown requests.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-15-03 — Coordinate with Entries and Select — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Coordinate with Entries and Select
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/control_task.ads, src/runtime/control_task.adb

Predict the exact behavior if the implementation encounters this problem: Designing a rendezvous that can never be accepted in one runtime state.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-15-04 — Coordinate with Entries and Select — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Coordinate with Entries and Select
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/control_task.ads, src/runtime/control_task.adb

Implement the core milestone in the existing mission_sim crate: Build a control task that accepts pause, resume, step, snapshot, and shutdown requests.

**Completion checks**

- Every control request either completes or times out predictably.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-15-05 — Coordinate with Entries and Select — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Coordinate with Entries and Select
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/control_task.ads, src/runtime/control_task.adb

Extend the completed milestone with this practical variation: Add a timeout path for an unresponsive component.

**Completion checks**

- Every control request either completes or times out predictably.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-15-06 — Coordinate with Entries and Select — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Coordinate with Entries and Select
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/control_task.ads, src/runtime/control_task.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Build a control task that accepts pause, resume, step, snapshot, and shutdown requests.

**Completion checks**

- Every control request either completes or times out predictably.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-15-07 — Coordinate with Entries and Select — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Coordinate with Entries and Select
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/control_task.ads, src/runtime/control_task.adb

Reproduce and repair this defect class in the current project: Designing a rendezvous that can never be accepted in one runtime state.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Every control request either completes or times out predictably.

### ADA-P2-15-08 — Coordinate with Entries and Select — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Coordinate with Entries and Select
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/control_task.ads, src/runtime/control_task.adb

Refactor the chapter implementation so Rendezvous, entry guards, selective accept, and asynchronous transfer concepts is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-15-09 — Coordinate with Entries and Select — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Coordinate with Entries and Select
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/control_task.ads, src/runtime/control_task.adb

Integrate this chapter into the running final product so it works with earlier milestones: Build a control task that accepts pause, resume, step, snapshot, and shutdown requests.

**Completion checks**

- Every control request either completes or times out predictably.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-15-10 — Coordinate with Entries and Select — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Coordinate with Entries and Select
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/control_task.ads, src/runtime/control_task.adb

Perform a senior-style checkpoint review of Coordinate with Entries and Select in Mission Simulator.

**Completion checks**

- Every control request either completes or times out predictably.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-16-01 — Use Real-Time Timing Correctly — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Use Real-Time Timing Correctly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/clock.ads, src/runtime/clock.adb

Answer one focused question before editing code: How should Ada.Real_Time, Time_Span, delay until, priorities, and drift be used to accomplish this milestone: Drive wall-clock demonstrations with delay until while measuring deadline misses.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-16-02 — Use Real-Time Timing Correctly — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Use Real-Time Timing Correctly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/clock.ads, src/runtime/clock.adb

Read the current implementation around src/runtime/clock.ads, src/runtime/clock.adb. Trace how data enters, changes, and leaves the code for this milestone: Drive wall-clock demonstrations with delay until while measuring deadline misses.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-16-03 — Use Real-Time Timing Correctly — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Use Real-Time Timing Correctly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/clock.ads, src/runtime/clock.adb

Predict the exact behavior if the implementation encounters this problem: Using relative delays that accumulate drift or mixing Calendar with Real_Time.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-16-04 — Use Real-Time Timing Correctly — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Use Real-Time Timing Correctly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/clock.ads, src/runtime/clock.adb

Implement the core milestone in the existing mission_sim crate: Drive wall-clock demonstrations with delay until while measuring deadline misses.

**Completion checks**

- A long run shows bounded drift and reports missed deadlines.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-16-05 — Use Real-Time Timing Correctly — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Use Real-Time Timing Correctly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/clock.ads, src/runtime/clock.adb

Extend the completed milestone with this practical variation: Add configurable real-time, accelerated, and single-step modes.

**Completion checks**

- A long run shows bounded drift and reports missed deadlines.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-16-06 — Use Real-Time Timing Correctly — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Use Real-Time Timing Correctly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/clock.ads, src/runtime/clock.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Drive wall-clock demonstrations with delay until while measuring deadline misses.

**Completion checks**

- A long run shows bounded drift and reports missed deadlines.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-16-07 — Use Real-Time Timing Correctly — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Use Real-Time Timing Correctly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/clock.ads, src/runtime/clock.adb

Reproduce and repair this defect class in the current project: Using relative delays that accumulate drift or mixing Calendar with Real_Time.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- A long run shows bounded drift and reports missed deadlines.

### ADA-P2-16-08 — Use Real-Time Timing Correctly — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Use Real-Time Timing Correctly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/clock.ads, src/runtime/clock.adb

Refactor the chapter implementation so Ada.Real_Time, Time_Span, delay until, priorities, and drift is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-16-09 — Use Real-Time Timing Correctly — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Use Real-Time Timing Correctly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/clock.ads, src/runtime/clock.adb

Integrate this chapter into the running final product so it works with earlier milestones: Drive wall-clock demonstrations with delay until while measuring deadline misses.

**Completion checks**

- A long run shows bounded drift and reports missed deadlines.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-16-10 — Use Real-Time Timing Correctly — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Use Real-Time Timing Correctly
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/clock.ads, src/runtime/clock.adb

Perform a senior-style checkpoint review of Use Real-Time Timing Correctly in Mission Simulator.

**Completion checks**

- A long run shows bounded drift and reports missed deadlines.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-17-01 — Build a Deterministic Scheduler — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build a Deterministic Scheduler
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/scheduler.ads, src/runtime/scheduler.adb

Answer one focused question before editing code: How should Logical time, ordering, fixed steps, and reproducibility be used to accomplish this milestone: Advance all components in a stable order using integer simulation ticks independent of wall time.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-17-02 — Build a Deterministic Scheduler — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build a Deterministic Scheduler
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/scheduler.ads, src/runtime/scheduler.adb

Read the current implementation around src/runtime/scheduler.ads, src/runtime/scheduler.adb. Trace how data enters, changes, and leaves the code for this milestone: Advance all components in a stable order using integer simulation ticks independent of wall time.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-17-03 — Build a Deterministic Scheduler — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build a Deterministic Scheduler
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/scheduler.ads, src/runtime/scheduler.adb

Predict the exact behavior if the implementation encounters this problem: Reading wall-clock time or unordered containers inside domain calculations.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-17-04 — Build a Deterministic Scheduler — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build a Deterministic Scheduler
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/scheduler.ads, src/runtime/scheduler.adb

Implement the core milestone in the existing mission_sim crate: Advance all components in a stable order using integer simulation ticks independent of wall time.

**Completion checks**

- Two runs with the same inputs produce identical event logs.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-17-05 — Build a Deterministic Scheduler — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build a Deterministic Scheduler
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/scheduler.ads, src/runtime/scheduler.adb

Extend the completed milestone with this practical variation: Record and replay the seed, configuration hash, and event order.

**Completion checks**

- Two runs with the same inputs produce identical event logs.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-17-06 — Build a Deterministic Scheduler — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build a Deterministic Scheduler
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/scheduler.ads, src/runtime/scheduler.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Advance all components in a stable order using integer simulation ticks independent of wall time.

**Completion checks**

- Two runs with the same inputs produce identical event logs.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-17-07 — Build a Deterministic Scheduler — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build a Deterministic Scheduler
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/scheduler.ads, src/runtime/scheduler.adb

Reproduce and repair this defect class in the current project: Reading wall-clock time or unordered containers inside domain calculations.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Two runs with the same inputs produce identical event logs.

### ADA-P2-17-08 — Build a Deterministic Scheduler — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build a Deterministic Scheduler
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/scheduler.ads, src/runtime/scheduler.adb

Refactor the chapter implementation so Logical time, ordering, fixed steps, and reproducibility is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-17-09 — Build a Deterministic Scheduler — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build a Deterministic Scheduler
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/scheduler.ads, src/runtime/scheduler.adb

Integrate this chapter into the running final product so it works with earlier milestones: Advance all components in a stable order using integer simulation ticks independent of wall time.

**Completion checks**

- Two runs with the same inputs produce identical event logs.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-17-10 — Build a Deterministic Scheduler — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Build a Deterministic Scheduler
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/scheduler.ads, src/runtime/scheduler.adb

Perform a senior-style checkpoint review of Build a Deterministic Scheduler in Mission Simulator.

**Completion checks**

- Two runs with the same inputs produce identical event logs.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-18-01 — Schedule Events and Inject Faults — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Schedule Events and Inject Faults
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/event_queue.ads, src/domain/faults.ads, data/scenarios/fault_demo.cfg

Answer one focused question before editing code: How should Priority queues, state machines, and scenario execution be used to accomplish this milestone: Schedule timed commands, sensor failures, stale data, dropouts, and recovery events.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-18-02 — Schedule Events and Inject Faults — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Schedule Events and Inject Faults
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/event_queue.ads, src/domain/faults.ads, data/scenarios/fault_demo.cfg

Read the current implementation around src/runtime/event_queue.ads, src/domain/faults.ads, data/scenarios/fault_demo.cfg. Trace how data enters, changes, and leaves the code for this milestone: Schedule timed commands, sensor failures, stale data, dropouts, and recovery events.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-18-03 — Schedule Events and Inject Faults — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Schedule Events and Inject Faults
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/event_queue.ads, src/domain/faults.ads, data/scenarios/fault_demo.cfg

Predict the exact behavior if the implementation encounters this problem: Applying faults outside the scheduler and making replay order ambiguous.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-18-04 — Schedule Events and Inject Faults — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Schedule Events and Inject Faults
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/event_queue.ads, src/domain/faults.ads, data/scenarios/fault_demo.cfg

Implement the core milestone in the existing mission_sim crate: Schedule timed commands, sensor failures, stale data, dropouts, and recovery events.

**Completion checks**

- Fault scenarios replay identically and recovery is observable in telemetry.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-18-05 — Schedule Events and Inject Faults — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Schedule Events and Inject Faults
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/event_queue.ads, src/domain/faults.ads, data/scenarios/fault_demo.cfg

Extend the completed milestone with this practical variation: Support fault duration, repetition, and conditional triggering.

**Completion checks**

- Fault scenarios replay identically and recovery is observable in telemetry.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-18-06 — Schedule Events and Inject Faults — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Schedule Events and Inject Faults
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/event_queue.ads, src/domain/faults.ads, data/scenarios/fault_demo.cfg

Create automated or repeatable tests that prove the milestone and its boundaries: Schedule timed commands, sensor failures, stale data, dropouts, and recovery events.

**Completion checks**

- Fault scenarios replay identically and recovery is observable in telemetry.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-18-07 — Schedule Events and Inject Faults — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Schedule Events and Inject Faults
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/event_queue.ads, src/domain/faults.ads, data/scenarios/fault_demo.cfg

Reproduce and repair this defect class in the current project: Applying faults outside the scheduler and making replay order ambiguous.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Fault scenarios replay identically and recovery is observable in telemetry.

### ADA-P2-18-08 — Schedule Events and Inject Faults — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Schedule Events and Inject Faults
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/event_queue.ads, src/domain/faults.ads, data/scenarios/fault_demo.cfg

Refactor the chapter implementation so Priority queues, state machines, and scenario execution is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-18-09 — Schedule Events and Inject Faults — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Schedule Events and Inject Faults
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/event_queue.ads, src/domain/faults.ads, data/scenarios/fault_demo.cfg

Integrate this chapter into the running final product so it works with earlier milestones: Schedule timed commands, sensor failures, stale data, dropouts, and recovery events.

**Completion checks**

- Fault scenarios replay identically and recovery is observable in telemetry.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-18-10 — Schedule Events and Inject Faults — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Schedule Events and Inject Faults
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/runtime/event_queue.ads, src/domain/faults.ads, data/scenarios/fault_demo.cfg

Perform a senior-style checkpoint review of Schedule Events and Inject Faults in Mission Simulator.

**Completion checks**

- Fault scenarios replay identically and recovery is observable in telemetry.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-19-01 — Expose a Network Adapter — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Expose a Network Adapter
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/network.ads, src/adapters/network.adb

Answer one focused question before editing code: How should Sockets, framing, partial reads, timeouts, and adapter isolation be used to accomplish this milestone: Send telemetry and receive commands over a simple framed TCP or UDP protocol.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-19-02 — Expose a Network Adapter — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Expose a Network Adapter
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/network.ads, src/adapters/network.adb

Read the current implementation around src/adapters/network.ads, src/adapters/network.adb. Trace how data enters, changes, and leaves the code for this milestone: Send telemetry and receive commands over a simple framed TCP or UDP protocol.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-19-03 — Expose a Network Adapter — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Expose a Network Adapter
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/network.ads, src/adapters/network.adb

Predict the exact behavior if the implementation encounters this problem: Assuming one read equals one message or allowing network timing to alter deterministic state order.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-19-04 — Expose a Network Adapter — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Expose a Network Adapter
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/network.ads, src/adapters/network.adb

Implement the core milestone in the existing mission_sim crate: Send telemetry and receive commands over a simple framed TCP or UDP protocol.

**Completion checks**

- Fragmented and delayed traffic is handled without corrupting message boundaries.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-19-05 — Expose a Network Adapter — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Expose a Network Adapter
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/network.ads, src/adapters/network.adb

Extend the completed milestone with this practical variation: Add a mock adapter so tests require no live network.

**Completion checks**

- Fragmented and delayed traffic is handled without corrupting message boundaries.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-19-06 — Expose a Network Adapter — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Expose a Network Adapter
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/network.ads, src/adapters/network.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Send telemetry and receive commands over a simple framed TCP or UDP protocol.

**Completion checks**

- Fragmented and delayed traffic is handled without corrupting message boundaries.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-19-07 — Expose a Network Adapter — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Expose a Network Adapter
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/network.ads, src/adapters/network.adb

Reproduce and repair this defect class in the current project: Assuming one read equals one message or allowing network timing to alter deterministic state order.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Fragmented and delayed traffic is handled without corrupting message boundaries.

### ADA-P2-19-08 — Expose a Network Adapter — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Expose a Network Adapter
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/network.ads, src/adapters/network.adb

Refactor the chapter implementation so Sockets, framing, partial reads, timeouts, and adapter isolation is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-19-09 — Expose a Network Adapter — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Expose a Network Adapter
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/network.ads, src/adapters/network.adb

Integrate this chapter into the running final product so it works with earlier milestones: Send telemetry and receive commands over a simple framed TCP or UDP protocol.

**Completion checks**

- Fragmented and delayed traffic is handled without corrupting message boundaries.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-19-10 — Expose a Network Adapter — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Expose a Network Adapter
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/network.ads, src/adapters/network.adb

Perform a senior-style checkpoint review of Expose a Network Adapter in Mission Simulator.

**Completion checks**

- Fragmented and delayed traffic is handled without corrupting message boundaries.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-20-01 — Wrap a C Interface Safely — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Wrap a C Interface Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/c_api.ads, src/adapters/c_api.adb, c/checksum.c

Answer one focused question before editing code: How should Interfaces.C, Convention, import/export, pointers, and representation clauses be used to accomplish this milestone: Call a small C checksum or timing function through a narrow Ada wrapper.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-20-02 — Wrap a C Interface Safely — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Wrap a C Interface Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/c_api.ads, src/adapters/c_api.adb, c/checksum.c

Read the current implementation around src/adapters/c_api.ads, src/adapters/c_api.adb, c/checksum.c. Trace how data enters, changes, and leaves the code for this milestone: Call a small C checksum or timing function through a narrow Ada wrapper.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-20-03 — Wrap a C Interface Safely — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Wrap a C Interface Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/c_api.ads, src/adapters/c_api.adb, c/checksum.c

Predict the exact behavior if the implementation encounters this problem: Passing Ada-managed memory with the wrong lifetime or mismatched C integer sizes.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-20-04 — Wrap a C Interface Safely — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Wrap a C Interface Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/c_api.ads, src/adapters/c_api.adb, c/checksum.c

Implement the core milestone in the existing mission_sim crate: Call a small C checksum or timing function through a narrow Ada wrapper.

**Completion checks**

- Ada and C agree on sizes, ownership, and results across boundary tests.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-20-05 — Wrap a C Interface Safely — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Wrap a C Interface Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/c_api.ads, src/adapters/c_api.adb, c/checksum.c

Extend the completed milestone with this practical variation: Export one Ada callback while hiding raw C types from the domain layer.

**Completion checks**

- Ada and C agree on sizes, ownership, and results across boundary tests.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-20-06 — Wrap a C Interface Safely — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Wrap a C Interface Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/c_api.ads, src/adapters/c_api.adb, c/checksum.c

Create automated or repeatable tests that prove the milestone and its boundaries: Call a small C checksum or timing function through a narrow Ada wrapper.

**Completion checks**

- Ada and C agree on sizes, ownership, and results across boundary tests.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-20-07 — Wrap a C Interface Safely — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Wrap a C Interface Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/c_api.ads, src/adapters/c_api.adb, c/checksum.c

Reproduce and repair this defect class in the current project: Passing Ada-managed memory with the wrong lifetime or mismatched C integer sizes.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Ada and C agree on sizes, ownership, and results across boundary tests.

### ADA-P2-20-08 — Wrap a C Interface Safely — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Wrap a C Interface Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/c_api.ads, src/adapters/c_api.adb, c/checksum.c

Refactor the chapter implementation so Interfaces.C, Convention, import/export, pointers, and representation clauses is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-20-09 — Wrap a C Interface Safely — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Wrap a C Interface Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/c_api.ads, src/adapters/c_api.adb, c/checksum.c

Integrate this chapter into the running final product so it works with earlier milestones: Call a small C checksum or timing function through a narrow Ada wrapper.

**Completion checks**

- Ada and C agree on sizes, ownership, and results across boundary tests.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-20-10 — Wrap a C Interface Safely — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Wrap a C Interface Safely
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** src/adapters/c_api.ads, src/adapters/c_api.adb, c/checksum.c

Perform a senior-style checkpoint review of Wrap a C Interface Safely in Mission Simulator.

**Completion checks**

- Ada and C agree on sizes, ownership, and results across boundary tests.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-21-01 — Test and Analyze the Simulator — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Test and Analyze the Simulator
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** tests/, src/domain/, docs/verification.md

Answer one focused question before editing code: How should AUnit, property-style tests, SPARK boundaries, and static analysis be used to accomplish this milestone: Build unit, integration, replay, concurrency, and contract tests for the deterministic core.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-21-02 — Test and Analyze the Simulator — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Test and Analyze the Simulator
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** tests/, src/domain/, docs/verification.md

Read the current implementation around tests/, src/domain/, docs/verification.md. Trace how data enters, changes, and leaves the code for this milestone: Build unit, integration, replay, concurrency, and contract tests for the deterministic core.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-21-03 — Test and Analyze the Simulator — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Test and Analyze the Simulator
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** tests/, src/domain/, docs/verification.md

Predict the exact behavior if the implementation encounters this problem: Testing only happy paths or trying to prove code that still mixes I/O and global state.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-21-04 — Test and Analyze the Simulator — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Test and Analyze the Simulator
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** tests/, src/domain/, docs/verification.md

Implement the core milestone in the existing mission_sim crate: Build unit, integration, replay, concurrency, and contract tests for the deterministic core.

**Completion checks**

- Tests cover boundaries, replay, concurrency shutdown, malformed inputs, and fault scenarios.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-21-05 — Test and Analyze the Simulator — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Test and Analyze the Simulator
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** tests/, src/domain/, docs/verification.md

Extend the completed milestone with this practical variation: Select one pure package for SPARK-oriented proof or flow analysis.

**Completion checks**

- Tests cover boundaries, replay, concurrency shutdown, malformed inputs, and fault scenarios.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-21-06 — Test and Analyze the Simulator — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Test and Analyze the Simulator
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** tests/, src/domain/, docs/verification.md

Create automated or repeatable tests that prove the milestone and its boundaries: Build unit, integration, replay, concurrency, and contract tests for the deterministic core.

**Completion checks**

- Tests cover boundaries, replay, concurrency shutdown, malformed inputs, and fault scenarios.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-21-07 — Test and Analyze the Simulator — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Test and Analyze the Simulator
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** tests/, src/domain/, docs/verification.md

Reproduce and repair this defect class in the current project: Testing only happy paths or trying to prove code that still mixes I/O and global state.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Tests cover boundaries, replay, concurrency shutdown, malformed inputs, and fault scenarios.

### ADA-P2-21-08 — Test and Analyze the Simulator — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Test and Analyze the Simulator
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** tests/, src/domain/, docs/verification.md

Refactor the chapter implementation so AUnit, property-style tests, SPARK boundaries, and static analysis is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-21-09 — Test and Analyze the Simulator — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Test and Analyze the Simulator
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** tests/, src/domain/, docs/verification.md

Integrate this chapter into the running final product so it works with earlier milestones: Build unit, integration, replay, concurrency, and contract tests for the deterministic core.

**Completion checks**

- Tests cover boundaries, replay, concurrency shutdown, malformed inputs, and fault scenarios.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-21-10 — Test and Analyze the Simulator — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Test and Analyze the Simulator
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** tests/, src/domain/, docs/verification.md

Perform a senior-style checkpoint review of Test and Analyze the Simulator in Mission Simulator.

**Completion checks**

- Tests cover boundaries, replay, concurrency shutdown, malformed inputs, and fault scenarios.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P2-22-01 — Profile and Release Mission Sim — Question

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Profile and Release Mission Sim
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** README.md, CHANGELOG.md, docs/performance.md, docs/formats.md

Answer one focused question before editing code: How should Performance measurement, diagnostics, compatibility, and release engineering be used to accomplish this milestone: Profile the scheduler, bound memory growth, document APIs, freeze a scenario format, and tag a release.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P2-22-02 — Profile and Release Mission Sim — Code Reading

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Profile and Release Mission Sim
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** README.md, CHANGELOG.md, docs/performance.md, docs/formats.md

Read the current implementation around README.md, CHANGELOG.md, docs/performance.md, docs/formats.md. Trace how data enters, changes, and leaves the code for this milestone: Profile the scheduler, bound memory growth, document APIs, freeze a scenario format, and tag a release.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P2-22-03 — Profile and Release Mission Sim — Predict

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Profile and Release Mission Sim
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** README.md, CHANGELOG.md, docs/performance.md, docs/formats.md

Predict the exact behavior if the implementation encounters this problem: Optimizing without measurements or changing persisted formats without version handling.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P2-22-04 — Profile and Release Mission Sim — Implement

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Profile and Release Mission Sim
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** README.md, CHANGELOG.md, docs/performance.md, docs/formats.md

Implement the core milestone in the existing mission_sim crate: Profile the scheduler, bound memory growth, document APIs, freeze a scenario format, and tag a release.

**Completion checks**

- A clean checkout builds, tests, runs a scenario, replays it, and documents measured limits.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P2-22-05 — Profile and Release Mission Sim — Extend

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Profile and Release Mission Sim
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** README.md, CHANGELOG.md, docs/performance.md, docs/formats.md

Extend the completed milestone with this practical variation: Add a migration note for the next configuration or wire-format version.

**Completion checks**

- A clean checkout builds, tests, runs a scenario, replays it, and documents measured limits.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P2-22-06 — Profile and Release Mission Sim — Test

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Profile and Release Mission Sim
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** README.md, CHANGELOG.md, docs/performance.md, docs/formats.md

Create automated or repeatable tests that prove the milestone and its boundaries: Profile the scheduler, bound memory growth, document APIs, freeze a scenario format, and tag a release.

**Completion checks**

- A clean checkout builds, tests, runs a scenario, replays it, and documents measured limits.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P2-22-07 — Profile and Release Mission Sim — Repair

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Profile and Release Mission Sim
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** README.md, CHANGELOG.md, docs/performance.md, docs/formats.md

Reproduce and repair this defect class in the current project: Optimizing without measurements or changing persisted formats without version handling.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- A clean checkout builds, tests, runs a scenario, replays it, and documents measured limits.

### ADA-P2-22-08 — Profile and Release Mission Sim — Refactor

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Profile and Release Mission Sim
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** README.md, CHANGELOG.md, docs/performance.md, docs/formats.md

Refactor the chapter implementation so Performance measurement, diagnostics, compatibility, and release engineering is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P2-22-09 — Profile and Release Mission Sim — Integrate

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Profile and Release Mission Sim
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** README.md, CHANGELOG.md, docs/performance.md, docs/formats.md

Integrate this chapter into the running final product so it works with earlier milestones: Profile the scheduler, bound memory growth, document APIs, freeze a scenario format, and tag a release.

**Completion checks**

- A clean checkout builds, tests, runs a scenario, replays it, and documents measured limits.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P2-22-10 — Profile and Release Mission Sim — Review

- **Project:** Project 2 — Mission Systems Simulator
- **Chapter:** Profile and Release Mission Sim
- **Workspace:** `~/Documents/src/projects/ada-mastery/mission_sim`
- **Files:** README.md, CHANGELOG.md, docs/performance.md, docs/formats.md

Perform a senior-style checkpoint review of Profile and Release Mission Sim in Mission Simulator.

**Completion checks**

- A clean checkout builds, tests, runs a scenario, replays it, and documents measured limits.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-01-01 — Open an SDL Window — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Open an SDL Window
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** alire.toml, src/rescue_run_sdl.adb, src/sdl_context.ads

Answer one focused question before editing code: How should SDLada dependency and lifecycle be used to accomplish this milestone: Add SDLada through Alire, initialize SDL, create a window, and shut down safely.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-01-02 — Open an SDL Window — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Open an SDL Window
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** alire.toml, src/rescue_run_sdl.adb, src/sdl_context.ads

Read the current implementation around alire.toml, src/rescue_run_sdl.adb, src/sdl_context.ads. Trace how data enters, changes, and leaves the code for this milestone: Add SDLada through Alire, initialize SDL, create a window, and shut down safely.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-01-03 — Open an SDL Window — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Open an SDL Window
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** alire.toml, src/rescue_run_sdl.adb, src/sdl_context.ads

Predict the exact behavior if the implementation encounters this problem: Leaking SDL resources or calling subsystems before successful initialization.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-01-04 — Open an SDL Window — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Open an SDL Window
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** alire.toml, src/rescue_run_sdl.adb, src/sdl_context.ads

Implement the core milestone in the existing rescue_run_sdl crate: Add SDLada through Alire, initialize SDL, create a window, and shut down safely.

**Completion checks**

- The window opens, reports errors clearly, and exits without leaked resources.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-01-05 — Open an SDL Window — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Open an SDL Window
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** alire.toml, src/rescue_run_sdl.adb, src/sdl_context.ads

Extend the completed milestone with this practical variation: Wrap initialization and cleanup in a limited controlled application context.

**Completion checks**

- The window opens, reports errors clearly, and exits without leaked resources.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-01-06 — Open an SDL Window — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Open an SDL Window
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** alire.toml, src/rescue_run_sdl.adb, src/sdl_context.ads

Create automated or repeatable tests that prove the milestone and its boundaries: Add SDLada through Alire, initialize SDL, create a window, and shut down safely.

**Completion checks**

- The window opens, reports errors clearly, and exits without leaked resources.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-01-07 — Open an SDL Window — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Open an SDL Window
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** alire.toml, src/rescue_run_sdl.adb, src/sdl_context.ads

Reproduce and repair this defect class in the current project: Leaking SDL resources or calling subsystems before successful initialization.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- The window opens, reports errors clearly, and exits without leaked resources.

### ADA-P3-01-08 — Open an SDL Window — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Open an SDL Window
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** alire.toml, src/rescue_run_sdl.adb, src/sdl_context.ads

Refactor the chapter implementation so SDLada dependency and lifecycle is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-01-09 — Open an SDL Window — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Open an SDL Window
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** alire.toml, src/rescue_run_sdl.adb, src/sdl_context.ads

Integrate this chapter into the running final product so it works with earlier milestones: Add SDLada through Alire, initialize SDL, create a window, and shut down safely.

**Completion checks**

- The window opens, reports errors clearly, and exits without leaked resources.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-01-10 — Open an SDL Window — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Open an SDL Window
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** alire.toml, src/rescue_run_sdl.adb, src/sdl_context.ads

Perform a senior-style checkpoint review of Open an SDL Window in Rescue Run SDL.

**Completion checks**

- The window opens, reports errors clearly, and exits without leaked resources.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-02-01 — Draw Basic Shapes — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Draw Basic Shapes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/rendering.ads, src/rendering.adb

Answer one focused question before editing code: How should Renderers, colors, coordinates, and resource wrappers be used to accomplish this milestone: Create a renderer and draw the player, walls, and background using primitives.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-02-02 — Draw Basic Shapes — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Draw Basic Shapes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/rendering.ads, src/rendering.adb

Read the current implementation around src/rendering.ads, src/rendering.adb. Trace how data enters, changes, and leaves the code for this milestone: Create a renderer and draw the player, walls, and background using primitives.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-02-03 — Draw Basic Shapes — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Draw Basic Shapes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/rendering.ads, src/rendering.adb

Predict the exact behavior if the implementation encounters this problem: Mixing world and screen coordinates or using invalid destroyed handles.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-02-04 — Draw Basic Shapes — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Draw Basic Shapes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/rendering.ads, src/rendering.adb

Implement the core milestone in the existing rescue_run_sdl crate: Create a renderer and draw the player, walls, and background using primitives.

**Completion checks**

- A deterministic scene draws at expected pixel positions.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-02-05 — Draw Basic Shapes — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Draw Basic Shapes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/rendering.ads, src/rendering.adb

Extend the completed milestone with this practical variation: Add a small render command abstraction to keep SDL calls out of game rules.

**Completion checks**

- A deterministic scene draws at expected pixel positions.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-02-06 — Draw Basic Shapes — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Draw Basic Shapes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/rendering.ads, src/rendering.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Create a renderer and draw the player, walls, and background using primitives.

**Completion checks**

- A deterministic scene draws at expected pixel positions.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-02-07 — Draw Basic Shapes — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Draw Basic Shapes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/rendering.ads, src/rendering.adb

Reproduce and repair this defect class in the current project: Mixing world and screen coordinates or using invalid destroyed handles.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- A deterministic scene draws at expected pixel positions.

### ADA-P3-02-08 — Draw Basic Shapes — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Draw Basic Shapes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/rendering.ads, src/rendering.adb

Refactor the chapter implementation so Renderers, colors, coordinates, and resource wrappers is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-02-09 — Draw Basic Shapes — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Draw Basic Shapes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/rendering.ads, src/rendering.adb

Integrate this chapter into the running final product so it works with earlier milestones: Create a renderer and draw the player, walls, and background using primitives.

**Completion checks**

- A deterministic scene draws at expected pixel positions.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-02-10 — Draw Basic Shapes — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Draw Basic Shapes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/rendering.ads, src/rendering.adb

Perform a senior-style checkpoint review of Draw Basic Shapes in Rescue Run SDL.

**Completion checks**

- A deterministic scene draws at expected pixel positions.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-03-01 — Process SDL Events — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Process SDL Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input_events.ads, src/input_events.adb

Answer one focused question before editing code: How should Event unions, polling loops, and quit behavior be used to accomplish this milestone: Handle window close, keyboard, focus, and resize events without blocking rendering.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-03-02 — Process SDL Events — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Process SDL Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input_events.ads, src/input_events.adb

Read the current implementation around src/input_events.ads, src/input_events.adb. Trace how data enters, changes, and leaves the code for this milestone: Handle window close, keyboard, focus, and resize events without blocking rendering.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-03-03 — Process SDL Events — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Process SDL Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input_events.ads, src/input_events.adb

Predict the exact behavior if the implementation encounters this problem: Reading the wrong event variant or placing all behavior inside the event switch.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-03-04 — Process SDL Events — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Process SDL Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input_events.ads, src/input_events.adb

Implement the core milestone in the existing rescue_run_sdl crate: Handle window close, keyboard, focus, and resize events without blocking rendering.

**Completion checks**

- Quit and resize work reliably and the loop remains responsive.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-03-05 — Process SDL Events — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Process SDL Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input_events.ads, src/input_events.adb

Extend the completed milestone with this practical variation: Log unknown events in a development mode.

**Completion checks**

- Quit and resize work reliably and the loop remains responsive.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-03-06 — Process SDL Events — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Process SDL Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input_events.ads, src/input_events.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Handle window close, keyboard, focus, and resize events without blocking rendering.

**Completion checks**

- Quit and resize work reliably and the loop remains responsive.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-03-07 — Process SDL Events — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Process SDL Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input_events.ads, src/input_events.adb

Reproduce and repair this defect class in the current project: Reading the wrong event variant or placing all behavior inside the event switch.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Quit and resize work reliably and the loop remains responsive.

### ADA-P3-03-08 — Process SDL Events — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Process SDL Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input_events.ads, src/input_events.adb

Refactor the chapter implementation so Event unions, polling loops, and quit behavior is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-03-09 — Process SDL Events — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Process SDL Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input_events.ads, src/input_events.adb

Integrate this chapter into the running final product so it works with earlier milestones: Handle window close, keyboard, focus, and resize events without blocking rendering.

**Completion checks**

- Quit and resize work reliably and the loop remains responsive.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-03-10 — Process SDL Events — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Process SDL Events
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input_events.ads, src/input_events.adb

Perform a senior-style checkpoint review of Process SDL Events in Rescue Run SDL.

**Completion checks**

- Quit and resize work reliably and the loop remains responsive.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-04-01 — Create an Input Abstraction — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create an Input Abstraction
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input.ads, src/input.adb, data/settings.cfg

Answer one focused question before editing code: How should State versus events and command mapping be used to accomplish this milestone: Translate keyboard state into game commands independent of SDL scancodes.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-04-02 — Create an Input Abstraction — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create an Input Abstraction
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input.ads, src/input.adb, data/settings.cfg

Read the current implementation around src/input.ads, src/input.adb, data/settings.cfg. Trace how data enters, changes, and leaves the code for this milestone: Translate keyboard state into game commands independent of SDL scancodes.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-04-03 — Create an Input Abstraction — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create an Input Abstraction
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input.ads, src/input.adb, data/settings.cfg

Predict the exact behavior if the implementation encounters this problem: Tying player logic directly to SDL packages or missing key-release behavior.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-04-04 — Create an Input Abstraction — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create an Input Abstraction
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input.ads, src/input.adb, data/settings.cfg

Implement the core milestone in the existing rescue_run_sdl crate: Translate keyboard state into game commands independent of SDL scancodes.

**Completion checks**

- Game logic can be tested with synthetic input snapshots.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-04-05 — Create an Input Abstraction — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create an Input Abstraction
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input.ads, src/input.adb, data/settings.cfg

Extend the completed milestone with this practical variation: Support remappable controls loaded from configuration.

**Completion checks**

- Game logic can be tested with synthetic input snapshots.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-04-06 — Create an Input Abstraction — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create an Input Abstraction
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input.ads, src/input.adb, data/settings.cfg

Create automated or repeatable tests that prove the milestone and its boundaries: Translate keyboard state into game commands independent of SDL scancodes.

**Completion checks**

- Game logic can be tested with synthetic input snapshots.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-04-07 — Create an Input Abstraction — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create an Input Abstraction
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input.ads, src/input.adb, data/settings.cfg

Reproduce and repair this defect class in the current project: Tying player logic directly to SDL packages or missing key-release behavior.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Game logic can be tested with synthetic input snapshots.

### ADA-P3-04-08 — Create an Input Abstraction — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create an Input Abstraction
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input.ads, src/input.adb, data/settings.cfg

Refactor the chapter implementation so State versus events and command mapping is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-04-09 — Create an Input Abstraction — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create an Input Abstraction
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input.ads, src/input.adb, data/settings.cfg

Integrate this chapter into the running final product so it works with earlier milestones: Translate keyboard state into game commands independent of SDL scancodes.

**Completion checks**

- Game logic can be tested with synthetic input snapshots.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-04-10 — Create an Input Abstraction — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create an Input Abstraction
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/input.ads, src/input.adb, data/settings.cfg

Perform a senior-style checkpoint review of Create an Input Abstraction in Rescue Run SDL.

**Completion checks**

- Game logic can be tested with synthetic input snapshots.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-05-01 — Use a Fixed Update Step — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Use a Fixed Update Step
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_clock.ads, src/game_clock.adb, src/game_loop.adb

Answer one focused question before editing code: How should Frame time, accumulator loops, and interpolation be used to accomplish this milestone: Separate variable rendering frequency from a fixed game update rate.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-05-02 — Use a Fixed Update Step — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Use a Fixed Update Step
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_clock.ads, src/game_clock.adb, src/game_loop.adb

Read the current implementation around src/game_clock.ads, src/game_clock.adb, src/game_loop.adb. Trace how data enters, changes, and leaves the code for this milestone: Separate variable rendering frequency from a fixed game update rate.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-05-03 — Use a Fixed Update Step — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Use a Fixed Update Step
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_clock.ads, src/game_clock.adb, src/game_loop.adb

Predict the exact behavior if the implementation encounters this problem: Moving by pixels per frame or allowing a long pause to run thousands of updates.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-05-04 — Use a Fixed Update Step — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Use a Fixed Update Step
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_clock.ads, src/game_clock.adb, src/game_loop.adb

Implement the core milestone in the existing rescue_run_sdl crate: Separate variable rendering frequency from a fixed game update rate.

**Completion checks**

- Movement speed is stable at different render rates.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-05-05 — Use a Fixed Update Step — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Use a Fixed Update Step
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_clock.ads, src/game_clock.adb, src/game_loop.adb

Extend the completed milestone with this practical variation: Add frame-time statistics and a maximum catch-up limit.

**Completion checks**

- Movement speed is stable at different render rates.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-05-06 — Use a Fixed Update Step — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Use a Fixed Update Step
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_clock.ads, src/game_clock.adb, src/game_loop.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Separate variable rendering frequency from a fixed game update rate.

**Completion checks**

- Movement speed is stable at different render rates.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-05-07 — Use a Fixed Update Step — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Use a Fixed Update Step
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_clock.ads, src/game_clock.adb, src/game_loop.adb

Reproduce and repair this defect class in the current project: Moving by pixels per frame or allowing a long pause to run thousands of updates.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Movement speed is stable at different render rates.

### ADA-P3-05-08 — Use a Fixed Update Step — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Use a Fixed Update Step
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_clock.ads, src/game_clock.adb, src/game_loop.adb

Refactor the chapter implementation so Frame time, accumulator loops, and interpolation is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-05-09 — Use a Fixed Update Step — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Use a Fixed Update Step
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_clock.ads, src/game_clock.adb, src/game_loop.adb

Integrate this chapter into the running final product so it works with earlier milestones: Separate variable rendering frequency from a fixed game update rate.

**Completion checks**

- Movement speed is stable at different render rates.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-05-10 — Use a Fixed Update Step — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Use a Fixed Update Step
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_clock.ads, src/game_clock.adb, src/game_loop.adb

Perform a senior-style checkpoint review of Use a Fixed Update Step in Rescue Run SDL.

**Completion checks**

- Movement speed is stable at different render rates.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-06-01 — Move the Player — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Move the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/player.ads, src/player.adb, src/game_update.adb

Answer one focused question before editing code: How should Vectors, velocity, acceleration, and input response be used to accomplish this milestone: Implement responsive top-down movement with normalized diagonal speed.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-06-02 — Move the Player — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Move the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/player.ads, src/player.adb, src/game_update.adb

Read the current implementation around src/player.ads, src/player.adb, src/game_update.adb. Trace how data enters, changes, and leaves the code for this milestone: Implement responsive top-down movement with normalized diagonal speed.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-06-03 — Move the Player — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Move the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/player.ads, src/player.adb, src/game_update.adb

Predict the exact behavior if the implementation encounters this problem: Diagonal movement being faster or velocity retaining stale input.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-06-04 — Move the Player — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Move the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/player.ads, src/player.adb, src/game_update.adb

Implement the core milestone in the existing rescue_run_sdl crate: Implement responsive top-down movement with normalized diagonal speed.

**Completion checks**

- Cardinal and diagonal travel cover expected distances.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-06-05 — Move the Player — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Move the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/player.ads, src/player.adb, src/game_update.adb

Extend the completed milestone with this practical variation: Add sprint or acceleration while preserving deterministic updates.

**Completion checks**

- Cardinal and diagonal travel cover expected distances.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-06-06 — Move the Player — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Move the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/player.ads, src/player.adb, src/game_update.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Implement responsive top-down movement with normalized diagonal speed.

**Completion checks**

- Cardinal and diagonal travel cover expected distances.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-06-07 — Move the Player — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Move the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/player.ads, src/player.adb, src/game_update.adb

Reproduce and repair this defect class in the current project: Diagonal movement being faster or velocity retaining stale input.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Cardinal and diagonal travel cover expected distances.

### ADA-P3-06-08 — Move the Player — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Move the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/player.ads, src/player.adb, src/game_update.adb

Refactor the chapter implementation so Vectors, velocity, acceleration, and input response is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-06-09 — Move the Player — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Move the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/player.ads, src/player.adb, src/game_update.adb

Integrate this chapter into the running final product so it works with earlier milestones: Implement responsive top-down movement with normalized diagonal speed.

**Completion checks**

- Cardinal and diagonal travel cover expected distances.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-06-10 — Move the Player — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Move the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/player.ads, src/player.adb, src/game_update.adb

Perform a senior-style checkpoint review of Move the Player in Rescue Run SDL.

**Completion checks**

- Cardinal and diagonal travel cover expected distances.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-07-01 — Reuse the Map Format — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Reuse the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/map_loader.ads, src/map_loader.adb, data/maps/rescue.map

Answer one focused question before editing code: How should Data adapters and shared format concepts be used to accomplish this milestone: Load the Dungeon Walk map format into an SDL-oriented world model.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-07-02 — Reuse the Map Format — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Reuse the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/map_loader.ads, src/map_loader.adb, data/maps/rescue.map

Read the current implementation around src/map_loader.ads, src/map_loader.adb, data/maps/rescue.map. Trace how data enters, changes, and leaves the code for this milestone: Load the Dungeon Walk map format into an SDL-oriented world model.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-07-03 — Reuse the Map Format — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Reuse the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/map_loader.ads, src/map_loader.adb, data/maps/rescue.map

Predict the exact behavior if the implementation encounters this problem: Copying renderer concerns into the parser or silently accepting unsupported symbols.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-07-04 — Reuse the Map Format — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Reuse the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/map_loader.ads, src/map_loader.adb, data/maps/rescue.map

Implement the core milestone in the existing rescue_run_sdl crate: Load the Dungeon Walk map format into an SDL-oriented world model.

**Completion checks**

- The same logical map can be viewed in terminal and SDL projects.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-07-05 — Reuse the Map Format — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Reuse the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/map_loader.ads, src/map_loader.adb, data/maps/rescue.map

Extend the completed milestone with this practical variation: Support metadata for tile size, spawn, and named exits.

**Completion checks**

- The same logical map can be viewed in terminal and SDL projects.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-07-06 — Reuse the Map Format — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Reuse the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/map_loader.ads, src/map_loader.adb, data/maps/rescue.map

Create automated or repeatable tests that prove the milestone and its boundaries: Load the Dungeon Walk map format into an SDL-oriented world model.

**Completion checks**

- The same logical map can be viewed in terminal and SDL projects.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-07-07 — Reuse the Map Format — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Reuse the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/map_loader.ads, src/map_loader.adb, data/maps/rescue.map

Reproduce and repair this defect class in the current project: Copying renderer concerns into the parser or silently accepting unsupported symbols.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- The same logical map can be viewed in terminal and SDL projects.

### ADA-P3-07-08 — Reuse the Map Format — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Reuse the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/map_loader.ads, src/map_loader.adb, data/maps/rescue.map

Refactor the chapter implementation so Data adapters and shared format concepts is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-07-09 — Reuse the Map Format — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Reuse the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/map_loader.ads, src/map_loader.adb, data/maps/rescue.map

Integrate this chapter into the running final product so it works with earlier milestones: Load the Dungeon Walk map format into an SDL-oriented world model.

**Completion checks**

- The same logical map can be viewed in terminal and SDL projects.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-07-10 — Reuse the Map Format — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Reuse the Map Format
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/map_loader.ads, src/map_loader.adb, data/maps/rescue.map

Perform a senior-style checkpoint review of Reuse the Map Format in Rescue Run SDL.

**Completion checks**

- The same logical map can be viewed in terminal and SDL projects.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-08-01 — Render Tile Maps — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Render Tile Maps
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/tile_renderer.ads, src/tile_renderer.adb

Answer one focused question before editing code: How should Nested iteration, clipping, and tile lookup be used to accomplish this milestone: Draw only visible floor, wall, hazard, and exit tiles.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-08-02 — Render Tile Maps — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Render Tile Maps
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/tile_renderer.ads, src/tile_renderer.adb

Read the current implementation around src/tile_renderer.ads, src/tile_renderer.adb. Trace how data enters, changes, and leaves the code for this milestone: Draw only visible floor, wall, hazard, and exit tiles.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-08-03 — Render Tile Maps — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Render Tile Maps
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/tile_renderer.ads, src/tile_renderer.adb

Predict the exact behavior if the implementation encounters this problem: Drawing the full world every frame or swapping row and column axes.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-08-04 — Render Tile Maps — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Render Tile Maps
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/tile_renderer.ads, src/tile_renderer.adb

Implement the core milestone in the existing rescue_run_sdl crate: Draw only visible floor, wall, hazard, and exit tiles.

**Completion checks**

- A large map renders correctly with visible-region clipping.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-08-05 — Render Tile Maps — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Render Tile Maps
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/tile_renderer.ads, src/tile_renderer.adb

Extend the completed milestone with this practical variation: Add debug grid and collision overlays.

**Completion checks**

- A large map renders correctly with visible-region clipping.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-08-06 — Render Tile Maps — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Render Tile Maps
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/tile_renderer.ads, src/tile_renderer.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Draw only visible floor, wall, hazard, and exit tiles.

**Completion checks**

- A large map renders correctly with visible-region clipping.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-08-07 — Render Tile Maps — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Render Tile Maps
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/tile_renderer.ads, src/tile_renderer.adb

Reproduce and repair this defect class in the current project: Drawing the full world every frame or swapping row and column axes.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- A large map renders correctly with visible-region clipping.

### ADA-P3-08-08 — Render Tile Maps — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Render Tile Maps
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/tile_renderer.ads, src/tile_renderer.adb

Refactor the chapter implementation so Nested iteration, clipping, and tile lookup is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-08-09 — Render Tile Maps — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Render Tile Maps
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/tile_renderer.ads, src/tile_renderer.adb

Integrate this chapter into the running final product so it works with earlier milestones: Draw only visible floor, wall, hazard, and exit tiles.

**Completion checks**

- A large map renders correctly with visible-region clipping.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-08-10 — Render Tile Maps — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Render Tile Maps
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/tile_renderer.ads, src/tile_renderer.adb

Perform a senior-style checkpoint review of Render Tile Maps in Rescue Run SDL.

**Completion checks**

- A large map renders correctly with visible-region clipping.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-09-01 — Follow the Player with a Camera — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Follow the Player with a Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/camera.ads, src/camera.adb

Answer one focused question before editing code: How should World-to-screen transforms and clamping be used to accomplish this milestone: Implement a smooth camera that follows the player and remains inside map bounds.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-09-02 — Follow the Player with a Camera — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Follow the Player with a Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/camera.ads, src/camera.adb

Read the current implementation around src/camera.ads, src/camera.adb. Trace how data enters, changes, and leaves the code for this milestone: Implement a smooth camera that follows the player and remains inside map bounds.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-09-03 — Follow the Player with a Camera — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Follow the Player with a Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/camera.ads, src/camera.adb

Predict the exact behavior if the implementation encounters this problem: Updating world positions in screen coordinates or exposing camera offsets to domain code.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-09-04 — Follow the Player with a Camera — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Follow the Player with a Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/camera.ads, src/camera.adb

Implement the core milestone in the existing rescue_run_sdl crate: Implement a smooth camera that follows the player and remains inside map bounds.

**Completion checks**

- The camera centers when possible and clamps cleanly near map edges.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-09-05 — Follow the Player with a Camera — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Follow the Player with a Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/camera.ads, src/camera.adb

Extend the completed milestone with this practical variation: Add camera shake as a separate effect layer.

**Completion checks**

- The camera centers when possible and clamps cleanly near map edges.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-09-06 — Follow the Player with a Camera — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Follow the Player with a Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/camera.ads, src/camera.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Implement a smooth camera that follows the player and remains inside map bounds.

**Completion checks**

- The camera centers when possible and clamps cleanly near map edges.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-09-07 — Follow the Player with a Camera — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Follow the Player with a Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/camera.ads, src/camera.adb

Reproduce and repair this defect class in the current project: Updating world positions in screen coordinates or exposing camera offsets to domain code.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- The camera centers when possible and clamps cleanly near map edges.

### ADA-P3-09-08 — Follow the Player with a Camera — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Follow the Player with a Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/camera.ads, src/camera.adb

Refactor the chapter implementation so World-to-screen transforms and clamping is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-09-09 — Follow the Player with a Camera — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Follow the Player with a Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/camera.ads, src/camera.adb

Integrate this chapter into the running final product so it works with earlier milestones: Implement a smooth camera that follows the player and remains inside map bounds.

**Completion checks**

- The camera centers when possible and clamps cleanly near map edges.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-09-10 — Follow the Player with a Camera — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Follow the Player with a Camera
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/camera.ads, src/camera.adb

Perform a senior-style checkpoint review of Follow the Player with a Camera in Rescue Run SDL.

**Completion checks**

- The camera centers when possible and clamps cleanly near map edges.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-10-01 — Resolve Tile Collision — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Resolve Tile Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/collision.ads, src/collision.adb

Answer one focused question before editing code: How should Bounding boxes, swept movement, and axis separation be used to accomplish this milestone: Prevent the player from crossing walls while allowing smooth sliding.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-10-02 — Resolve Tile Collision — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Resolve Tile Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/collision.ads, src/collision.adb

Read the current implementation around src/collision.ads, src/collision.adb. Trace how data enters, changes, and leaves the code for this milestone: Prevent the player from crossing walls while allowing smooth sliding.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-10-03 — Resolve Tile Collision — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Resolve Tile Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/collision.ads, src/collision.adb

Predict the exact behavior if the implementation encounters this problem: Resolving both axes together and sticking at corners or tunneling at high speed.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-10-04 — Resolve Tile Collision — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Resolve Tile Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/collision.ads, src/collision.adb

Implement the core milestone in the existing rescue_run_sdl crate: Prevent the player from crossing walls while allowing smooth sliding.

**Completion checks**

- Collision tests cover corners, narrow passages, and high-speed movement.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-10-05 — Resolve Tile Collision — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Resolve Tile Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/collision.ads, src/collision.adb

Extend the completed milestone with this practical variation: Add hazards and one-way or trigger tiles.

**Completion checks**

- Collision tests cover corners, narrow passages, and high-speed movement.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-10-06 — Resolve Tile Collision — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Resolve Tile Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/collision.ads, src/collision.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Prevent the player from crossing walls while allowing smooth sliding.

**Completion checks**

- Collision tests cover corners, narrow passages, and high-speed movement.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-10-07 — Resolve Tile Collision — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Resolve Tile Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/collision.ads, src/collision.adb

Reproduce and repair this defect class in the current project: Resolving both axes together and sticking at corners or tunneling at high speed.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Collision tests cover corners, narrow passages, and high-speed movement.

### ADA-P3-10-08 — Resolve Tile Collision — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Resolve Tile Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/collision.ads, src/collision.adb

Refactor the chapter implementation so Bounding boxes, swept movement, and axis separation is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-10-09 — Resolve Tile Collision — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Resolve Tile Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/collision.ads, src/collision.adb

Integrate this chapter into the running final product so it works with earlier milestones: Prevent the player from crossing walls while allowing smooth sliding.

**Completion checks**

- Collision tests cover corners, narrow passages, and high-speed movement.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-10-10 — Resolve Tile Collision — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Resolve Tile Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/collision.ads, src/collision.adb

Perform a senior-style checkpoint review of Resolve Tile Collision in Rescue Run SDL.

**Completion checks**

- Collision tests cover corners, narrow passages, and high-speed movement.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-11-01 — Load and Manage Textures — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load and Manage Textures
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/assets.ads, src/assets.adb, assets/

Answer one focused question before editing code: How should SDL_image, ownership, caching, and failure fallback be used to accomplish this milestone: Load a tileset and sprites through a texture cache with explicit ownership.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-11-02 — Load and Manage Textures — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load and Manage Textures
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/assets.ads, src/assets.adb, assets/

Read the current implementation around src/assets.ads, src/assets.adb, assets/. Trace how data enters, changes, and leaves the code for this milestone: Load a tileset and sprites through a texture cache with explicit ownership.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-11-03 — Load and Manage Textures — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load and Manage Textures
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/assets.ads, src/assets.adb, assets/

Predict the exact behavior if the implementation encounters this problem: Loading every texture every frame or destroying shared textures too early.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-11-04 — Load and Manage Textures — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load and Manage Textures
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/assets.ads, src/assets.adb, assets/

Implement the core milestone in the existing rescue_run_sdl crate: Load a tileset and sprites through a texture cache with explicit ownership.

**Completion checks**

- Each asset loads once, is reused, and is released at shutdown.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-11-05 — Load and Manage Textures — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load and Manage Textures
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/assets.ads, src/assets.adb, assets/

Extend the completed milestone with this practical variation: Provide placeholder graphics when an asset is missing.

**Completion checks**

- Each asset loads once, is reused, and is released at shutdown.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-11-06 — Load and Manage Textures — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load and Manage Textures
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/assets.ads, src/assets.adb, assets/

Create automated or repeatable tests that prove the milestone and its boundaries: Load a tileset and sprites through a texture cache with explicit ownership.

**Completion checks**

- Each asset loads once, is reused, and is released at shutdown.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-11-07 — Load and Manage Textures — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load and Manage Textures
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/assets.ads, src/assets.adb, assets/

Reproduce and repair this defect class in the current project: Loading every texture every frame or destroying shared textures too early.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Each asset loads once, is reused, and is released at shutdown.

### ADA-P3-11-08 — Load and Manage Textures — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load and Manage Textures
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/assets.ads, src/assets.adb, assets/

Refactor the chapter implementation so SDL_image, ownership, caching, and failure fallback is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-11-09 — Load and Manage Textures — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load and Manage Textures
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/assets.ads, src/assets.adb, assets/

Integrate this chapter into the running final product so it works with earlier milestones: Load a tileset and sprites through a texture cache with explicit ownership.

**Completion checks**

- Each asset loads once, is reused, and is released at shutdown.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-11-10 — Load and Manage Textures — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load and Manage Textures
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/assets.ads, src/assets.adb, assets/

Perform a senior-style checkpoint review of Load and Manage Textures in Rescue Run SDL.

**Completion checks**

- Each asset loads once, is reused, and is released at shutdown.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-12-01 — Animate the Player — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Animate the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/animation.ads, src/animation.adb, src/player_view.adb

Answer one focused question before editing code: How should Sprite sheets, frame timing, and state machines be used to accomplish this milestone: Select idle, walk, and hurt animations based on player state and direction.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-12-02 — Animate the Player — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Animate the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/animation.ads, src/animation.adb, src/player_view.adb

Read the current implementation around src/animation.ads, src/animation.adb, src/player_view.adb. Trace how data enters, changes, and leaves the code for this milestone: Select idle, walk, and hurt animations based on player state and direction.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-12-03 — Animate the Player — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Animate the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/animation.ads, src/animation.adb, src/player_view.adb

Predict the exact behavior if the implementation encounters this problem: Using render frame count as animation time or restarting clips every update.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-12-04 — Animate the Player — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Animate the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/animation.ads, src/animation.adb, src/player_view.adb

Implement the core milestone in the existing rescue_run_sdl crate: Select idle, walk, and hurt animations based on player state and direction.

**Completion checks**

- Animations advance by time and transition without flicker.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-12-05 — Animate the Player — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Animate the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/animation.ads, src/animation.adb, src/player_view.adb

Extend the completed milestone with this practical variation: Add per-animation frame durations and non-looping clips.

**Completion checks**

- Animations advance by time and transition without flicker.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-12-06 — Animate the Player — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Animate the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/animation.ads, src/animation.adb, src/player_view.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Select idle, walk, and hurt animations based on player state and direction.

**Completion checks**

- Animations advance by time and transition without flicker.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-12-07 — Animate the Player — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Animate the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/animation.ads, src/animation.adb, src/player_view.adb

Reproduce and repair this defect class in the current project: Using render frame count as animation time or restarting clips every update.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Animations advance by time and transition without flicker.

### ADA-P3-12-08 — Animate the Player — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Animate the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/animation.ads, src/animation.adb, src/player_view.adb

Refactor the chapter implementation so Sprite sheets, frame timing, and state machines is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-12-09 — Animate the Player — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Animate the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/animation.ads, src/animation.adb, src/player_view.adb

Integrate this chapter into the running final product so it works with earlier milestones: Select idle, walk, and hurt animations based on player state and direction.

**Completion checks**

- Animations advance by time and transition without flicker.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-12-10 — Animate the Player — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Animate the Player
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/animation.ads, src/animation.adb, src/player_view.adb

Perform a senior-style checkpoint review of Animate the Player in Rescue Run SDL.

**Completion checks**

- Animations advance by time and transition without flicker.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-13-01 — Add Enemy Behavior — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Enemy Behavior
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/enemies.ads, src/enemies.adb

Answer one focused question before editing code: How should Finite-state machines and steering be used to accomplish this milestone: Create enemies that idle, detect, chase, search, and return.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-13-02 — Add Enemy Behavior — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Enemy Behavior
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/enemies.ads, src/enemies.adb

Read the current implementation around src/enemies.ads, src/enemies.adb. Trace how data enters, changes, and leaves the code for this milestone: Create enemies that idle, detect, chase, search, and return.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-13-03 — Add Enemy Behavior — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Enemy Behavior
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/enemies.ads, src/enemies.adb

Predict the exact behavior if the implementation encounters this problem: Encoding AI as tangled booleans or allowing enemies to ignore collision.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-13-04 — Add Enemy Behavior — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Enemy Behavior
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/enemies.ads, src/enemies.adb

Implement the core milestone in the existing rescue_run_sdl crate: Create enemies that idle, detect, chase, search, and return.

**Completion checks**

- Enemy transitions are visible, deterministic, and testable.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-13-05 — Add Enemy Behavior — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Enemy Behavior
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/enemies.ads, src/enemies.adb

Extend the completed milestone with this practical variation: Add line-of-sight or hearing using the tile map.

**Completion checks**

- Enemy transitions are visible, deterministic, and testable.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-13-06 — Add Enemy Behavior — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Enemy Behavior
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/enemies.ads, src/enemies.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Create enemies that idle, detect, chase, search, and return.

**Completion checks**

- Enemy transitions are visible, deterministic, and testable.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-13-07 — Add Enemy Behavior — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Enemy Behavior
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/enemies.ads, src/enemies.adb

Reproduce and repair this defect class in the current project: Encoding AI as tangled booleans or allowing enemies to ignore collision.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Enemy transitions are visible, deterministic, and testable.

### ADA-P3-13-08 — Add Enemy Behavior — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Enemy Behavior
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/enemies.ads, src/enemies.adb

Refactor the chapter implementation so Finite-state machines and steering is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-13-09 — Add Enemy Behavior — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Enemy Behavior
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/enemies.ads, src/enemies.adb

Integrate this chapter into the running final product so it works with earlier milestones: Create enemies that idle, detect, chase, search, and return.

**Completion checks**

- Enemy transitions are visible, deterministic, and testable.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-13-10 — Add Enemy Behavior — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Enemy Behavior
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/enemies.ads, src/enemies.adb

Perform a senior-style checkpoint review of Add Enemy Behavior in Rescue Run SDL.

**Completion checks**

- Enemy transitions are visible, deterministic, and testable.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-14-01 — Add Attacks and Projectiles — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Attacks and Projectiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/combat.ads, src/combat.adb

Answer one focused question before editing code: How should Object lifetime, collision queries, and cooldowns be used to accomplish this milestone: Create projectiles or short-range attacks with owner, velocity, lifetime, and damage.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-14-02 — Add Attacks and Projectiles — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Attacks and Projectiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/combat.ads, src/combat.adb

Read the current implementation around src/combat.ads, src/combat.adb. Trace how data enters, changes, and leaves the code for this milestone: Create projectiles or short-range attacks with owner, velocity, lifetime, and damage.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-14-03 — Add Attacks and Projectiles — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Attacks and Projectiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/combat.ads, src/combat.adb

Predict the exact behavior if the implementation encounters this problem: Removing objects while iterating unsafely or damaging the owner immediately.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-14-04 — Add Attacks and Projectiles — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Attacks and Projectiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/combat.ads, src/combat.adb

Implement the core milestone in the existing rescue_run_sdl crate: Create projectiles or short-range attacks with owner, velocity, lifetime, and damage.

**Completion checks**

- Attacks respect cooldowns, collide once, and expire cleanly.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-14-05 — Add Attacks and Projectiles — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Attacks and Projectiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/combat.ads, src/combat.adb

Extend the completed milestone with this practical variation: Add enemy attacks using the same reusable model.

**Completion checks**

- Attacks respect cooldowns, collide once, and expire cleanly.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-14-06 — Add Attacks and Projectiles — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Attacks and Projectiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/combat.ads, src/combat.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Create projectiles or short-range attacks with owner, velocity, lifetime, and damage.

**Completion checks**

- Attacks respect cooldowns, collide once, and expire cleanly.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-14-07 — Add Attacks and Projectiles — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Attacks and Projectiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/combat.ads, src/combat.adb

Reproduce and repair this defect class in the current project: Removing objects while iterating unsafely or damaging the owner immediately.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Attacks respect cooldowns, collide once, and expire cleanly.

### ADA-P3-14-08 — Add Attacks and Projectiles — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Attacks and Projectiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/combat.ads, src/combat.adb

Refactor the chapter implementation so Object lifetime, collision queries, and cooldowns is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-14-09 — Add Attacks and Projectiles — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Attacks and Projectiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/combat.ads, src/combat.adb

Integrate this chapter into the running final product so it works with earlier milestones: Create projectiles or short-range attacks with owner, velocity, lifetime, and damage.

**Completion checks**

- Attacks respect cooldowns, collide once, and expire cleanly.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-14-10 — Add Attacks and Projectiles — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Attacks and Projectiles
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/combat.ads, src/combat.adb

Perform a senior-style checkpoint review of Add Attacks and Projectiles in Rescue Run SDL.

**Completion checks**

- Attacks respect cooldowns, collide once, and expire cleanly.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-15-01 — Build Rescue Objectives — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Build Rescue Objectives
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/objectives.ads, src/objectives.adb

Answer one focused question before editing code: How should Collections, triggers, and game rules be used to accomplish this milestone: Add survivors, pickups, exits, and a win condition based on completed rescues.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-15-02 — Build Rescue Objectives — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Build Rescue Objectives
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/objectives.ads, src/objectives.adb

Read the current implementation around src/objectives.ads, src/objectives.adb. Trace how data enters, changes, and leaves the code for this milestone: Add survivors, pickups, exits, and a win condition based on completed rescues.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-15-03 — Build Rescue Objectives — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Build Rescue Objectives
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/objectives.ads, src/objectives.adb

Predict the exact behavior if the implementation encounters this problem: Letting render objects become the authoritative game state.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-15-04 — Build Rescue Objectives — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Build Rescue Objectives
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/objectives.ads, src/objectives.adb

Implement the core milestone in the existing rescue_run_sdl crate: Add survivors, pickups, exits, and a win condition based on completed rescues.

**Completion checks**

- The objective state updates from game events and drives a clear win condition.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-15-05 — Build Rescue Objectives — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Build Rescue Objectives
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/objectives.ads, src/objectives.adb

Extend the completed milestone with this practical variation: Support optional objectives and scoring.

**Completion checks**

- The objective state updates from game events and drives a clear win condition.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-15-06 — Build Rescue Objectives — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Build Rescue Objectives
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/objectives.ads, src/objectives.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Add survivors, pickups, exits, and a win condition based on completed rescues.

**Completion checks**

- The objective state updates from game events and drives a clear win condition.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-15-07 — Build Rescue Objectives — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Build Rescue Objectives
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/objectives.ads, src/objectives.adb

Reproduce and repair this defect class in the current project: Letting render objects become the authoritative game state.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- The objective state updates from game events and drives a clear win condition.

### ADA-P3-15-08 — Build Rescue Objectives — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Build Rescue Objectives
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/objectives.ads, src/objectives.adb

Refactor the chapter implementation so Collections, triggers, and game rules is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-15-09 — Build Rescue Objectives — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Build Rescue Objectives
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/objectives.ads, src/objectives.adb

Integrate this chapter into the running final product so it works with earlier milestones: Add survivors, pickups, exits, and a win condition based on completed rescues.

**Completion checks**

- The objective state updates from game events and drives a clear win condition.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-15-10 — Build Rescue Objectives — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Build Rescue Objectives
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/objectives.ads, src/objectives.adb

Perform a senior-style checkpoint review of Build Rescue Objectives in Rescue Run SDL.

**Completion checks**

- The objective state updates from game events and drives a clear win condition.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-16-01 — Create a HUD — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create a HUD
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/hud.ads, src/hud.adb

Answer one focused question before editing code: How should SDL_ttf, formatting, and view models be used to accomplish this milestone: Display health, rescued count, objective status, and pause state.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-16-02 — Create a HUD — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create a HUD
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/hud.ads, src/hud.adb

Read the current implementation around src/hud.ads, src/hud.adb. Trace how data enters, changes, and leaves the code for this milestone: Display health, rescued count, objective status, and pause state.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-16-03 — Create a HUD — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create a HUD
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/hud.ads, src/hud.adb

Predict the exact behavior if the implementation encounters this problem: Rebuilding fonts every frame or letting HUD formatting mutate game state.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-16-04 — Create a HUD — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create a HUD
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/hud.ads, src/hud.adb

Implement the core milestone in the existing rescue_run_sdl crate: Display health, rescued count, objective status, and pause state.

**Completion checks**

- HUD values match the domain model and resize sensibly.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-16-05 — Create a HUD — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create a HUD
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/hud.ads, src/hud.adb

Extend the completed milestone with this practical variation: Add debug statistics behind a toggle.

**Completion checks**

- HUD values match the domain model and resize sensibly.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-16-06 — Create a HUD — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create a HUD
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/hud.ads, src/hud.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Display health, rescued count, objective status, and pause state.

**Completion checks**

- HUD values match the domain model and resize sensibly.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-16-07 — Create a HUD — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create a HUD
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/hud.ads, src/hud.adb

Reproduce and repair this defect class in the current project: Rebuilding fonts every frame or letting HUD formatting mutate game state.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- HUD values match the domain model and resize sensibly.

### ADA-P3-16-08 — Create a HUD — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create a HUD
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/hud.ads, src/hud.adb

Refactor the chapter implementation so SDL_ttf, formatting, and view models is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-16-09 — Create a HUD — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create a HUD
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/hud.ads, src/hud.adb

Integrate this chapter into the running final product so it works with earlier milestones: Display health, rescued count, objective status, and pause state.

**Completion checks**

- HUD values match the domain model and resize sensibly.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-16-10 — Create a HUD — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Create a HUD
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/hud.ads, src/hud.adb

Perform a senior-style checkpoint review of Create a HUD in Rescue Run SDL.

**Completion checks**

- HUD values match the domain model and resize sensibly.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-17-01 — Add Sound and Music — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Sound and Music
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/audio.ads, src/audio.adb

Answer one focused question before editing code: How should SDL_mixer, channels, resource policy, and events be used to accomplish this milestone: Play movement, rescue, damage, attack, and victory audio from game events.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-17-02 — Add Sound and Music — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Sound and Music
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/audio.ads, src/audio.adb

Read the current implementation around src/audio.ads, src/audio.adb. Trace how data enters, changes, and leaves the code for this milestone: Play movement, rescue, damage, attack, and victory audio from game events.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-17-03 — Add Sound and Music — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Sound and Music
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/audio.ads, src/audio.adb

Predict the exact behavior if the implementation encounters this problem: Calling audio directly from domain rules or failing startup when no audio device exists.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-17-04 — Add Sound and Music — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Sound and Music
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/audio.ads, src/audio.adb

Implement the core milestone in the existing rescue_run_sdl crate: Play movement, rescue, damage, attack, and victory audio from game events.

**Completion checks**

- Audio responds to events and can be disabled without changing gameplay.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-17-05 — Add Sound and Music — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Sound and Music
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/audio.ads, src/audio.adb

Extend the completed milestone with this practical variation: Add volume settings and graceful no-audio operation.

**Completion checks**

- Audio responds to events and can be disabled without changing gameplay.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-17-06 — Add Sound and Music — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Sound and Music
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/audio.ads, src/audio.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Play movement, rescue, damage, attack, and victory audio from game events.

**Completion checks**

- Audio responds to events and can be disabled without changing gameplay.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-17-07 — Add Sound and Music — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Sound and Music
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/audio.ads, src/audio.adb

Reproduce and repair this defect class in the current project: Calling audio directly from domain rules or failing startup when no audio device exists.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Audio responds to events and can be disabled without changing gameplay.

### ADA-P3-17-08 — Add Sound and Music — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Sound and Music
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/audio.ads, src/audio.adb

Refactor the chapter implementation so SDL_mixer, channels, resource policy, and events is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-17-09 — Add Sound and Music — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Sound and Music
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/audio.ads, src/audio.adb

Integrate this chapter into the running final product so it works with earlier milestones: Play movement, rescue, damage, attack, and victory audio from game events.

**Completion checks**

- Audio responds to events and can be disabled without changing gameplay.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-17-10 — Add Sound and Music — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Add Sound and Music
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/audio.ads, src/audio.adb

Perform a senior-style checkpoint review of Add Sound and Music in Rescue Run SDL.

**Completion checks**

- Audio responds to events and can be disabled without changing gameplay.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-18-01 — Organize Game States — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Organize Game States
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_states.ads, src/game_states.adb

Answer one focused question before editing code: How should State pattern, pause, menus, and transitions be used to accomplish this milestone: Separate title, playing, paused, victory, and game-over states.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-18-02 — Organize Game States — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Organize Game States
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_states.ads, src/game_states.adb

Read the current implementation around src/game_states.ads, src/game_states.adb. Trace how data enters, changes, and leaves the code for this milestone: Separate title, playing, paused, victory, and game-over states.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-18-03 — Organize Game States — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Organize Game States
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_states.ads, src/game_states.adb

Predict the exact behavior if the implementation encounters this problem: Using many unrelated global flags or updating gameplay while paused.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-18-04 — Organize Game States — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Organize Game States
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_states.ads, src/game_states.adb

Implement the core milestone in the existing rescue_run_sdl crate: Separate title, playing, paused, victory, and game-over states.

**Completion checks**

- Each state owns its input/update/render behavior and transitions explicitly.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-18-05 — Organize Game States — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Organize Game States
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_states.ads, src/game_states.adb

Extend the completed milestone with this practical variation: Add restart and map-selection flows.

**Completion checks**

- Each state owns its input/update/render behavior and transitions explicitly.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-18-06 — Organize Game States — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Organize Game States
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_states.ads, src/game_states.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Separate title, playing, paused, victory, and game-over states.

**Completion checks**

- Each state owns its input/update/render behavior and transitions explicitly.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-18-07 — Organize Game States — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Organize Game States
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_states.ads, src/game_states.adb

Reproduce and repair this defect class in the current project: Using many unrelated global flags or updating gameplay while paused.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Each state owns its input/update/render behavior and transitions explicitly.

### ADA-P3-18-08 — Organize Game States — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Organize Game States
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_states.ads, src/game_states.adb

Refactor the chapter implementation so State pattern, pause, menus, and transitions is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-18-09 — Organize Game States — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Organize Game States
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_states.ads, src/game_states.adb

Integrate this chapter into the running final product so it works with earlier milestones: Separate title, playing, paused, victory, and game-over states.

**Completion checks**

- Each state owns its input/update/render behavior and transitions explicitly.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-18-10 — Organize Game States — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Organize Game States
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/game_states.ads, src/game_states.adb

Perform a senior-style checkpoint review of Organize Game States in Rescue Run SDL.

**Completion checks**

- Each state owns its input/update/render behavior and transitions explicitly.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-19-01 — Load Settings and Save Progress — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load Settings and Save Progress
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/settings.ads, src/save_data.ads, data/

Answer one focused question before editing code: How should Configuration, save data, and compatibility be used to accomplish this milestone: Persist controls, volume, window settings, best score, and unlocked maps.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-19-02 — Load Settings and Save Progress — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load Settings and Save Progress
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/settings.ads, src/save_data.ads, data/

Read the current implementation around src/settings.ads, src/save_data.ads, data/. Trace how data enters, changes, and leaves the code for this milestone: Persist controls, volume, window settings, best score, and unlocked maps.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-19-03 — Load Settings and Save Progress — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load Settings and Save Progress
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/settings.ads, src/save_data.ads, data/

Predict the exact behavior if the implementation encounters this problem: Saving SDL handles or failing the entire game because optional settings are malformed.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-19-04 — Load Settings and Save Progress — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load Settings and Save Progress
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/settings.ads, src/save_data.ads, data/

Implement the core milestone in the existing rescue_run_sdl crate: Persist controls, volume, window settings, best score, and unlocked maps.

**Completion checks**

- Settings round-trip and corrupt optional data falls back safely.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-19-05 — Load Settings and Save Progress — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load Settings and Save Progress
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/settings.ads, src/save_data.ads, data/

Extend the completed milestone with this practical variation: Version the save format and recover from a damaged file.

**Completion checks**

- Settings round-trip and corrupt optional data falls back safely.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-19-06 — Load Settings and Save Progress — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load Settings and Save Progress
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/settings.ads, src/save_data.ads, data/

Create automated or repeatable tests that prove the milestone and its boundaries: Persist controls, volume, window settings, best score, and unlocked maps.

**Completion checks**

- Settings round-trip and corrupt optional data falls back safely.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-19-07 — Load Settings and Save Progress — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load Settings and Save Progress
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/settings.ads, src/save_data.ads, data/

Reproduce and repair this defect class in the current project: Saving SDL handles or failing the entire game because optional settings are malformed.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Settings round-trip and corrupt optional data falls back safely.

### ADA-P3-19-08 — Load Settings and Save Progress — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load Settings and Save Progress
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/settings.ads, src/save_data.ads, data/

Refactor the chapter implementation so Configuration, save data, and compatibility is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-19-09 — Load Settings and Save Progress — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load Settings and Save Progress
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/settings.ads, src/save_data.ads, data/

Integrate this chapter into the running final product so it works with earlier milestones: Persist controls, volume, window settings, best score, and unlocked maps.

**Completion checks**

- Settings round-trip and corrupt optional data falls back safely.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-19-10 — Load Settings and Save Progress — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Load Settings and Save Progress
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** src/settings.ads, src/save_data.ads, data/

Perform a senior-style checkpoint review of Load Settings and Save Progress in Rescue Run SDL.

**Completion checks**

- Settings round-trip and corrupt optional data falls back safely.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P3-20-01 — Finish Rescue Run SDL — Question

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Finish Rescue Run SDL
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** tests/, README.md, CHANGELOG.md, docs/

Answer one focused question before editing code: How should Integration tests, performance, packaging, and release polish be used to accomplish this milestone: Complete maps, balance, tests, warning cleanup, asset licensing notes, and release instructions.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P3-20-02 — Finish Rescue Run SDL — Code Reading

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Finish Rescue Run SDL
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** tests/, README.md, CHANGELOG.md, docs/

Read the current implementation around tests/, README.md, CHANGELOG.md, docs/. Trace how data enters, changes, and leaves the code for this milestone: Complete maps, balance, tests, warning cleanup, asset licensing notes, and release instructions.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P3-20-03 — Finish Rescue Run SDL — Predict

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Finish Rescue Run SDL
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** tests/, README.md, CHANGELOG.md, docs/

Predict the exact behavior if the implementation encounters this problem: Treating a playable prototype as finished without reproducible builds and tests.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P3-20-04 — Finish Rescue Run SDL — Implement

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Finish Rescue Run SDL
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** tests/, README.md, CHANGELOG.md, docs/

Implement the core milestone in the existing rescue_run_sdl crate: Complete maps, balance, tests, warning cleanup, asset licensing notes, and release instructions.

**Completion checks**

- A fresh clone installs dependencies, builds, tests, and runs a complete game session.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P3-20-05 — Finish Rescue Run SDL — Extend

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Finish Rescue Run SDL
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** tests/, README.md, CHANGELOG.md, docs/

Extend the completed milestone with this practical variation: Add a frame-time budget and profile the slowest render/update paths.

**Completion checks**

- A fresh clone installs dependencies, builds, tests, and runs a complete game session.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P3-20-06 — Finish Rescue Run SDL — Test

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Finish Rescue Run SDL
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** tests/, README.md, CHANGELOG.md, docs/

Create automated or repeatable tests that prove the milestone and its boundaries: Complete maps, balance, tests, warning cleanup, asset licensing notes, and release instructions.

**Completion checks**

- A fresh clone installs dependencies, builds, tests, and runs a complete game session.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P3-20-07 — Finish Rescue Run SDL — Repair

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Finish Rescue Run SDL
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** tests/, README.md, CHANGELOG.md, docs/

Reproduce and repair this defect class in the current project: Treating a playable prototype as finished without reproducible builds and tests.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- A fresh clone installs dependencies, builds, tests, and runs a complete game session.

### ADA-P3-20-08 — Finish Rescue Run SDL — Refactor

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Finish Rescue Run SDL
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** tests/, README.md, CHANGELOG.md, docs/

Refactor the chapter implementation so Integration tests, performance, packaging, and release polish is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P3-20-09 — Finish Rescue Run SDL — Integrate

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Finish Rescue Run SDL
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** tests/, README.md, CHANGELOG.md, docs/

Integrate this chapter into the running final product so it works with earlier milestones: Complete maps, balance, tests, warning cleanup, asset licensing notes, and release instructions.

**Completion checks**

- A fresh clone installs dependencies, builds, tests, and runs a complete game session.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P3-20-10 — Finish Rescue Run SDL — Review

- **Project:** Project 3 — Rescue Run SDL
- **Chapter:** Finish Rescue Run SDL
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_sdl`
- **Files:** tests/, README.md, CHANGELOG.md, docs/

Perform a senior-style checkpoint review of Finish Rescue Run SDL in Rescue Run SDL.

**Completion checks**

- A fresh clone installs dependencies, builds, tests, and runs a complete game session.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P4-01-01 — Plan the ECS Migration — Question

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Plan the ECS Migration
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** docs/ecs_plan.md, tests/golden_scenarios/

Answer one focused question before editing code: How should Architecture assessment and behavior baselines be used to accomplish this milestone: Inventory current entities, data, behavior, coupling, and frame phases before changing code.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P4-01-02 — Plan the ECS Migration — Code Reading

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Plan the ECS Migration
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** docs/ecs_plan.md, tests/golden_scenarios/

Read the current implementation around docs/ecs_plan.md, tests/golden_scenarios/. Trace how data enters, changes, and leaves the code for this milestone: Inventory current entities, data, behavior, coupling, and frame phases before changing code.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P4-01-03 — Plan the ECS Migration — Predict

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Plan the ECS Migration
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** docs/ecs_plan.md, tests/golden_scenarios/

Predict the exact behavior if the implementation encounters this problem: Starting the rewrite without a behavior baseline or clear migration seams.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P4-01-04 — Plan the ECS Migration — Implement

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Plan the ECS Migration
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** docs/ecs_plan.md, tests/golden_scenarios/

Implement the core milestone in the existing rescue_run_ecs crate: Inventory current entities, data, behavior, coupling, and frame phases before changing code.

**Completion checks**

- The plan maps every existing feature to data, systems, or adapters.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P4-01-05 — Plan the ECS Migration — Extend

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Plan the ECS Migration
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** docs/ecs_plan.md, tests/golden_scenarios/

Extend the completed milestone with this practical variation: Capture golden gameplay scenarios and performance measurements.

**Completion checks**

- The plan maps every existing feature to data, systems, or adapters.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P4-01-06 — Plan the ECS Migration — Test

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Plan the ECS Migration
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** docs/ecs_plan.md, tests/golden_scenarios/

Create automated or repeatable tests that prove the milestone and its boundaries: Inventory current entities, data, behavior, coupling, and frame phases before changing code.

**Completion checks**

- The plan maps every existing feature to data, systems, or adapters.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P4-01-07 — Plan the ECS Migration — Repair

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Plan the ECS Migration
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** docs/ecs_plan.md, tests/golden_scenarios/

Reproduce and repair this defect class in the current project: Starting the rewrite without a behavior baseline or clear migration seams.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- The plan maps every existing feature to data, systems, or adapters.

### ADA-P4-01-08 — Plan the ECS Migration — Refactor

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Plan the ECS Migration
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** docs/ecs_plan.md, tests/golden_scenarios/

Refactor the chapter implementation so Architecture assessment and behavior baselines is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P4-01-09 — Plan the ECS Migration — Integrate

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Plan the ECS Migration
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** docs/ecs_plan.md, tests/golden_scenarios/

Integrate this chapter into the running final product so it works with earlier milestones: Inventory current entities, data, behavior, coupling, and frame phases before changing code.

**Completion checks**

- The plan maps every existing feature to data, systems, or adapters.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P4-01-10 — Plan the ECS Migration — Review

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Plan the ECS Migration
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** docs/ecs_plan.md, tests/golden_scenarios/

Perform a senior-style checkpoint review of Plan the ECS Migration in Rescue Run ECS.

**Completion checks**

- The plan maps every existing feature to data, systems, or adapters.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P4-02-01 — Create Stable Entity IDs — Question

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create Stable Entity IDs
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/entities.ads, src/ecs/entities.adb

Answer one focused question before editing code: How should Opaque identifiers, generations, and lifecycle be used to accomplish this milestone: Implement entity creation, destruction, validity checks, and ID reuse protection.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P4-02-02 — Create Stable Entity IDs — Code Reading

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create Stable Entity IDs
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/entities.ads, src/ecs/entities.adb

Read the current implementation around src/ecs/entities.ads, src/ecs/entities.adb. Trace how data enters, changes, and leaves the code for this milestone: Implement entity creation, destruction, validity checks, and ID reuse protection.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P4-02-03 — Create Stable Entity IDs — Predict

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create Stable Entity IDs
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/entities.ads, src/ecs/entities.adb

Predict the exact behavior if the implementation encounters this problem: Using raw container indexes as permanent identity.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P4-02-04 — Create Stable Entity IDs — Implement

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create Stable Entity IDs
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/entities.ads, src/ecs/entities.adb

Implement the core milestone in the existing rescue_run_ecs crate: Implement entity creation, destruction, validity checks, and ID reuse protection.

**Completion checks**

- Destroyed IDs cannot accidentally refer to newly created entities.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P4-02-05 — Create Stable Entity IDs — Extend

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create Stable Entity IDs
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/entities.ads, src/ecs/entities.adb

Extend the completed milestone with this practical variation: Add generation counters or another stale-ID defense.

**Completion checks**

- Destroyed IDs cannot accidentally refer to newly created entities.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P4-02-06 — Create Stable Entity IDs — Test

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create Stable Entity IDs
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/entities.ads, src/ecs/entities.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Implement entity creation, destruction, validity checks, and ID reuse protection.

**Completion checks**

- Destroyed IDs cannot accidentally refer to newly created entities.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P4-02-07 — Create Stable Entity IDs — Repair

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create Stable Entity IDs
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/entities.ads, src/ecs/entities.adb

Reproduce and repair this defect class in the current project: Using raw container indexes as permanent identity.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Destroyed IDs cannot accidentally refer to newly created entities.

### ADA-P4-02-08 — Create Stable Entity IDs — Refactor

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create Stable Entity IDs
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/entities.ads, src/ecs/entities.adb

Refactor the chapter implementation so Opaque identifiers, generations, and lifecycle is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P4-02-09 — Create Stable Entity IDs — Integrate

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create Stable Entity IDs
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/entities.ads, src/ecs/entities.adb

Integrate this chapter into the running final product so it works with earlier milestones: Implement entity creation, destruction, validity checks, and ID reuse protection.

**Completion checks**

- Destroyed IDs cannot accidentally refer to newly created entities.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P4-02-10 — Create Stable Entity IDs — Review

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create Stable Entity IDs
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/entities.ads, src/ecs/entities.adb

Perform a senior-style checkpoint review of Create Stable Entity IDs in Rescue Run ECS.

**Completion checks**

- Destroyed IDs cannot accidentally refer to newly created entities.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P4-03-01 — Define Plain Components — Question

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define Plain Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/components/

Answer one focused question before editing code: How should Data-oriented records and component boundaries be used to accomplish this milestone: Create position, velocity, sprite, collider, health, AI, projectile, and objective components.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P4-03-02 — Define Plain Components — Code Reading

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define Plain Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/components/

Read the current implementation around src/components/. Trace how data enters, changes, and leaves the code for this milestone: Create position, velocity, sprite, collider, health, AI, projectile, and objective components.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P4-03-03 — Define Plain Components — Predict

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define Plain Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/components/

Predict the exact behavior if the implementation encounters this problem: Putting methods, SDL handles, and unrelated state into giant components.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P4-03-04 — Define Plain Components — Implement

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define Plain Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/components/

Implement the core milestone in the existing rescue_run_ecs crate: Create position, velocity, sprite, collider, health, AI, projectile, and objective components.

**Completion checks**

- Components are small data records with clear ownership and units.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P4-03-05 — Define Plain Components — Extend

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define Plain Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/components/

Extend the completed milestone with this practical variation: Split optional behavior into separate components rather than flags.

**Completion checks**

- Components are small data records with clear ownership and units.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P4-03-06 — Define Plain Components — Test

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define Plain Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/components/

Create automated or repeatable tests that prove the milestone and its boundaries: Create position, velocity, sprite, collider, health, AI, projectile, and objective components.

**Completion checks**

- Components are small data records with clear ownership and units.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P4-03-07 — Define Plain Components — Repair

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define Plain Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/components/

Reproduce and repair this defect class in the current project: Putting methods, SDL handles, and unrelated state into giant components.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Components are small data records with clear ownership and units.

### ADA-P4-03-08 — Define Plain Components — Refactor

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define Plain Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/components/

Refactor the chapter implementation so Data-oriented records and component boundaries is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P4-03-09 — Define Plain Components — Integrate

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define Plain Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/components/

Integrate this chapter into the running final product so it works with earlier milestones: Create position, velocity, sprite, collider, health, AI, projectile, and objective components.

**Completion checks**

- Components are small data records with clear ownership and units.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P4-03-10 — Define Plain Components — Review

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define Plain Components
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/components/

Perform a senior-style checkpoint review of Define Plain Components in Rescue Run ECS.

**Completion checks**

- Components are small data records with clear ownership and units.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P4-04-01 — Build Component Stores — Question

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Build Component Stores
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/component_store.ads, src/ecs/component_store.adb

Answer one focused question before editing code: How should Generics, sparse/dense storage, and membership be used to accomplish this milestone: Create reusable typed stores supporting add, remove, get, contains, and iteration.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P4-04-02 — Build Component Stores — Code Reading

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Build Component Stores
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/component_store.ads, src/ecs/component_store.adb

Read the current implementation around src/ecs/component_store.ads, src/ecs/component_store.adb. Trace how data enters, changes, and leaves the code for this milestone: Create reusable typed stores supporting add, remove, get, contains, and iteration.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P4-04-03 — Build Component Stores — Predict

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Build Component Stores
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/component_store.ads, src/ecs/component_store.adb

Predict the exact behavior if the implementation encounters this problem: Returning references that outlive store mutations or confusing absent/default values.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P4-04-04 — Build Component Stores — Implement

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Build Component Stores
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/component_store.ads, src/ecs/component_store.adb

Implement the core milestone in the existing rescue_run_ecs crate: Create reusable typed stores supporting add, remove, get, contains, and iteration.

**Completion checks**

- Stores pass lifecycle, iteration, and boundary tests for several component types.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P4-04-05 — Build Component Stores — Extend

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Build Component Stores
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/component_store.ads, src/ecs/component_store.adb

Extend the completed milestone with this practical variation: Prevent structural modification during unsafe iteration.

**Completion checks**

- Stores pass lifecycle, iteration, and boundary tests for several component types.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P4-04-06 — Build Component Stores — Test

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Build Component Stores
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/component_store.ads, src/ecs/component_store.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Create reusable typed stores supporting add, remove, get, contains, and iteration.

**Completion checks**

- Stores pass lifecycle, iteration, and boundary tests for several component types.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P4-04-07 — Build Component Stores — Repair

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Build Component Stores
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/component_store.ads, src/ecs/component_store.adb

Reproduce and repair this defect class in the current project: Returning references that outlive store mutations or confusing absent/default values.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Stores pass lifecycle, iteration, and boundary tests for several component types.

### ADA-P4-04-08 — Build Component Stores — Refactor

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Build Component Stores
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/component_store.ads, src/ecs/component_store.adb

Refactor the chapter implementation so Generics, sparse/dense storage, and membership is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P4-04-09 — Build Component Stores — Integrate

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Build Component Stores
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/component_store.ads, src/ecs/component_store.adb

Integrate this chapter into the running final product so it works with earlier milestones: Create reusable typed stores supporting add, remove, get, contains, and iteration.

**Completion checks**

- Stores pass lifecycle, iteration, and boundary tests for several component types.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P4-04-10 — Build Component Stores — Review

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Build Component Stores
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/component_store.ads, src/ecs/component_store.adb

Perform a senior-style checkpoint review of Build Component Stores in Rescue Run ECS.

**Completion checks**

- Stores pass lifecycle, iteration, and boundary tests for several component types.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P4-05-01 — Create the World API — Question

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create the World API
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/world.ads, src/ecs/world.adb

Answer one focused question before editing code: How should Encapsulation, composition, and entity construction be used to accomplish this milestone: Combine entity management and component stores behind a coherent World package.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P4-05-02 — Create the World API — Code Reading

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create the World API
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/world.ads, src/ecs/world.adb

Read the current implementation around src/ecs/world.ads, src/ecs/world.adb. Trace how data enters, changes, and leaves the code for this milestone: Combine entity management and component stores behind a coherent World package.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P4-05-03 — Create the World API — Predict

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create the World API
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/world.ads, src/ecs/world.adb

Predict the exact behavior if the implementation encounters this problem: Exposing every store globally or allowing half-created entities after an exception.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P4-05-04 — Create the World API — Implement

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create the World API
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/world.ads, src/ecs/world.adb

Implement the core milestone in the existing rescue_run_ecs crate: Combine entity management and component stores behind a coherent World package.

**Completion checks**

- Entity construction either completes validly or rolls back.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P4-05-05 — Create the World API — Extend

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create the World API
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/world.ads, src/ecs/world.adb

Extend the completed milestone with this practical variation: Add named constructors for player, survivor, enemy, and projectile entities.

**Completion checks**

- Entity construction either completes validly or rolls back.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P4-05-06 — Create the World API — Test

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create the World API
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/world.ads, src/ecs/world.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Combine entity management and component stores behind a coherent World package.

**Completion checks**

- Entity construction either completes validly or rolls back.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P4-05-07 — Create the World API — Repair

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create the World API
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/world.ads, src/ecs/world.adb

Reproduce and repair this defect class in the current project: Exposing every store globally or allowing half-created entities after an exception.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Entity construction either completes validly or rolls back.

### ADA-P4-05-08 — Create the World API — Refactor

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create the World API
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/world.ads, src/ecs/world.adb

Refactor the chapter implementation so Encapsulation, composition, and entity construction is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P4-05-09 — Create the World API — Integrate

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create the World API
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/world.ads, src/ecs/world.adb

Integrate this chapter into the running final product so it works with earlier milestones: Combine entity management and component stores behind a coherent World package.

**Completion checks**

- Entity construction either completes validly or rolls back.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P4-05-10 — Create the World API — Review

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create the World API
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/world.ads, src/ecs/world.adb

Perform a senior-style checkpoint review of Create the World API in Rescue Run ECS.

**Completion checks**

- Entity construction either completes validly or rolls back.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P4-06-01 — Define System Phases — Question

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define System Phases
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/systems.ads, src/ecs/schedule.adb

Answer one focused question before editing code: How should System interfaces, ordering, and dependencies be used to accomplish this milestone: Create input, movement, collision, combat, AI, animation, objective, cleanup, and rendering phases.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P4-06-02 — Define System Phases — Code Reading

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define System Phases
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/systems.ads, src/ecs/schedule.adb

Read the current implementation around src/ecs/systems.ads, src/ecs/schedule.adb. Trace how data enters, changes, and leaves the code for this milestone: Create input, movement, collision, combat, AI, animation, objective, cleanup, and rendering phases.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P4-06-03 — Define System Phases — Predict

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define System Phases
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/systems.ads, src/ecs/schedule.adb

Predict the exact behavior if the implementation encounters this problem: Letting arbitrary system order change results without detection.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P4-06-04 — Define System Phases — Implement

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define System Phases
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/systems.ads, src/ecs/schedule.adb

Implement the core milestone in the existing rescue_run_ecs crate: Create input, movement, collision, combat, AI, animation, objective, cleanup, and rendering phases.

**Completion checks**

- The schedule is explicit, deterministic, and justified.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P4-06-05 — Define System Phases — Extend

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define System Phases
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/systems.ads, src/ecs/schedule.adb

Extend the completed milestone with this practical variation: Document read/write sets and ordering constraints.

**Completion checks**

- The schedule is explicit, deterministic, and justified.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P4-06-06 — Define System Phases — Test

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define System Phases
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/systems.ads, src/ecs/schedule.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Create input, movement, collision, combat, AI, animation, objective, cleanup, and rendering phases.

**Completion checks**

- The schedule is explicit, deterministic, and justified.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P4-06-07 — Define System Phases — Repair

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define System Phases
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/systems.ads, src/ecs/schedule.adb

Reproduce and repair this defect class in the current project: Letting arbitrary system order change results without detection.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- The schedule is explicit, deterministic, and justified.

### ADA-P4-06-08 — Define System Phases — Refactor

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define System Phases
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/systems.ads, src/ecs/schedule.adb

Refactor the chapter implementation so System interfaces, ordering, and dependencies is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P4-06-09 — Define System Phases — Integrate

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define System Phases
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/systems.ads, src/ecs/schedule.adb

Integrate this chapter into the running final product so it works with earlier milestones: Create input, movement, collision, combat, AI, animation, objective, cleanup, and rendering phases.

**Completion checks**

- The schedule is explicit, deterministic, and justified.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P4-06-10 — Define System Phases — Review

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Define System Phases
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/systems.ads, src/ecs/schedule.adb

Perform a senior-style checkpoint review of Define System Phases in Rescue Run ECS.

**Completion checks**

- The schedule is explicit, deterministic, and justified.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P4-07-01 — Query Matching Entities — Question

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Query Matching Entities
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/queries.ads, src/ecs/queries.adb

Answer one focused question before editing code: How should Component signatures and iteration joins be used to accomplish this milestone: Iterate only entities containing each system’s required component set.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P4-07-02 — Query Matching Entities — Code Reading

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Query Matching Entities
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/queries.ads, src/ecs/queries.adb

Read the current implementation around src/ecs/queries.ads, src/ecs/queries.adb. Trace how data enters, changes, and leaves the code for this milestone: Iterate only entities containing each system’s required component set.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P4-07-03 — Query Matching Entities — Predict

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Query Matching Entities
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/queries.ads, src/ecs/queries.adb

Predict the exact behavior if the implementation encounters this problem: Scanning unrelated data repeatedly or assuming every entity has every component.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P4-07-04 — Query Matching Entities — Implement

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Query Matching Entities
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/queries.ads, src/ecs/queries.adb

Implement the core milestone in the existing rescue_run_ecs crate: Iterate only entities containing each system’s required component set.

**Completion checks**

- Queries return exactly the expected entities before and after component changes.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P4-07-05 — Query Matching Entities — Extend

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Query Matching Entities
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/queries.ads, src/ecs/queries.adb

Extend the completed milestone with this practical variation: Add reusable queries for common signatures.

**Completion checks**

- Queries return exactly the expected entities before and after component changes.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P4-07-06 — Query Matching Entities — Test

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Query Matching Entities
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/queries.ads, src/ecs/queries.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Iterate only entities containing each system’s required component set.

**Completion checks**

- Queries return exactly the expected entities before and after component changes.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P4-07-07 — Query Matching Entities — Repair

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Query Matching Entities
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/queries.ads, src/ecs/queries.adb

Reproduce and repair this defect class in the current project: Scanning unrelated data repeatedly or assuming every entity has every component.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Queries return exactly the expected entities before and after component changes.

### ADA-P4-07-08 — Query Matching Entities — Refactor

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Query Matching Entities
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/queries.ads, src/ecs/queries.adb

Refactor the chapter implementation so Component signatures and iteration joins is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P4-07-09 — Query Matching Entities — Integrate

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Query Matching Entities
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/queries.ads, src/ecs/queries.adb

Integrate this chapter into the running final product so it works with earlier milestones: Iterate only entities containing each system’s required component set.

**Completion checks**

- Queries return exactly the expected entities before and after component changes.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P4-07-10 — Query Matching Entities — Review

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Query Matching Entities
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/queries.ads, src/ecs/queries.adb

Perform a senior-style checkpoint review of Query Matching Entities in Rescue Run ECS.

**Completion checks**

- Queries return exactly the expected entities before and after component changes.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P4-08-01 — Defer Structural Changes — Question

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Defer Structural Changes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/commands.ads, src/ecs/commands.adb

Answer one focused question before editing code: How should Command buffers and safe mutation phases be used to accomplish this milestone: Queue spawn, destroy, add, and remove operations until a defined synchronization point.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P4-08-02 — Defer Structural Changes — Code Reading

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Defer Structural Changes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/commands.ads, src/ecs/commands.adb

Read the current implementation around src/ecs/commands.ads, src/ecs/commands.adb. Trace how data enters, changes, and leaves the code for this milestone: Queue spawn, destroy, add, and remove operations until a defined synchronization point.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P4-08-03 — Defer Structural Changes — Predict

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Defer Structural Changes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/commands.ads, src/ecs/commands.adb

Predict the exact behavior if the implementation encounters this problem: Destroying entities during system iteration and invalidating active traversals.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P4-08-04 — Defer Structural Changes — Implement

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Defer Structural Changes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/commands.ads, src/ecs/commands.adb

Implement the core milestone in the existing rescue_run_ecs crate: Queue spawn, destroy, add, and remove operations until a defined synchronization point.

**Completion checks**

- Structural commands apply in stable order after systems finish.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P4-08-05 — Defer Structural Changes — Extend

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Defer Structural Changes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/commands.ads, src/ecs/commands.adb

Extend the completed milestone with this practical variation: Support deterministic command ordering and conflict rules.

**Completion checks**

- Structural commands apply in stable order after systems finish.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P4-08-06 — Defer Structural Changes — Test

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Defer Structural Changes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/commands.ads, src/ecs/commands.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Queue spawn, destroy, add, and remove operations until a defined synchronization point.

**Completion checks**

- Structural commands apply in stable order after systems finish.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P4-08-07 — Defer Structural Changes — Repair

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Defer Structural Changes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/commands.ads, src/ecs/commands.adb

Reproduce and repair this defect class in the current project: Destroying entities during system iteration and invalidating active traversals.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Structural commands apply in stable order after systems finish.

### ADA-P4-08-08 — Defer Structural Changes — Refactor

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Defer Structural Changes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/commands.ads, src/ecs/commands.adb

Refactor the chapter implementation so Command buffers and safe mutation phases is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P4-08-09 — Defer Structural Changes — Integrate

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Defer Structural Changes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/commands.ads, src/ecs/commands.adb

Integrate this chapter into the running final product so it works with earlier milestones: Queue spawn, destroy, add, and remove operations until a defined synchronization point.

**Completion checks**

- Structural commands apply in stable order after systems finish.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P4-08-10 — Defer Structural Changes — Review

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Defer Structural Changes
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/commands.ads, src/ecs/commands.adb

Perform a senior-style checkpoint review of Defer Structural Changes in Rescue Run ECS.

**Completion checks**

- Structural commands apply in stable order after systems finish.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P4-09-01 — Create an ECS Event Stream — Question

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create an ECS Event Stream
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/events.ads, src/ecs/events.adb

Answer one focused question before editing code: How should Typed events, buffering, and decoupling be used to accomplish this milestone: Publish collision, damage, rescue, sound, animation, and state-transition events.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P4-09-02 — Create an ECS Event Stream — Code Reading

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create an ECS Event Stream
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/events.ads, src/ecs/events.adb

Read the current implementation around src/ecs/events.ads, src/ecs/events.adb. Trace how data enters, changes, and leaves the code for this milestone: Publish collision, damage, rescue, sound, animation, and state-transition events.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P4-09-03 — Create an ECS Event Stream — Predict

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create an ECS Event Stream
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/events.ads, src/ecs/events.adb

Predict the exact behavior if the implementation encounters this problem: Using events as permanent state or processing the same event multiple times.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P4-09-04 — Create an ECS Event Stream — Implement

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create an ECS Event Stream
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/events.ads, src/ecs/events.adb

Implement the core milestone in the existing rescue_run_ecs crate: Publish collision, damage, rescue, sound, animation, and state-transition events.

**Completion checks**

- Events are consumed in defined phases and cleared predictably.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P4-09-05 — Create an ECS Event Stream — Extend

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create an ECS Event Stream
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/events.ads, src/ecs/events.adb

Extend the completed milestone with this practical variation: Separate current-frame and next-frame event buffers.

**Completion checks**

- Events are consumed in defined phases and cleared predictably.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P4-09-06 — Create an ECS Event Stream — Test

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create an ECS Event Stream
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/events.ads, src/ecs/events.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Publish collision, damage, rescue, sound, animation, and state-transition events.

**Completion checks**

- Events are consumed in defined phases and cleared predictably.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P4-09-07 — Create an ECS Event Stream — Repair

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create an ECS Event Stream
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/events.ads, src/ecs/events.adb

Reproduce and repair this defect class in the current project: Using events as permanent state or processing the same event multiple times.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Events are consumed in defined phases and cleared predictably.

### ADA-P4-09-08 — Create an ECS Event Stream — Refactor

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create an ECS Event Stream
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/events.ads, src/ecs/events.adb

Refactor the chapter implementation so Typed events, buffering, and decoupling is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P4-09-09 — Create an ECS Event Stream — Integrate

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create an ECS Event Stream
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/events.ads, src/ecs/events.adb

Integrate this chapter into the running final product so it works with earlier milestones: Publish collision, damage, rescue, sound, animation, and state-transition events.

**Completion checks**

- Events are consumed in defined phases and cleared predictably.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P4-09-10 — Create an ECS Event Stream — Review

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Create an ECS Event Stream
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/events.ads, src/ecs/events.adb

Perform a senior-style checkpoint review of Create an ECS Event Stream in Rescue Run ECS.

**Completion checks**

- Events are consumed in defined phases and cleared predictably.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P4-10-01 — Migrate Movement — Question

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Movement
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/movement_system.adb

Answer one focused question before editing code: How should Pure systems and component transforms be used to accomplish this milestone: Move player, enemies, and projectiles using position and velocity components.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P4-10-02 — Migrate Movement — Code Reading

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Movement
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/movement_system.adb

Read the current implementation around src/systems/movement_system.adb. Trace how data enters, changes, and leaves the code for this milestone: Move player, enemies, and projectiles using position and velocity components.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P4-10-03 — Migrate Movement — Predict

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Movement
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/movement_system.adb

Predict the exact behavior if the implementation encounters this problem: Reading SDL input inside the system or updating render positions separately.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P4-10-04 — Migrate Movement — Implement

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Movement
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/movement_system.adb

Implement the core milestone in the existing rescue_run_ecs crate: Move player, enemies, and projectiles using position and velocity components.

**Completion checks**

- Golden movement scenarios match the original SDL version.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P4-10-05 — Migrate Movement — Extend

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Movement
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/movement_system.adb

Extend the completed milestone with this practical variation: Keep input mapping outside the movement system.

**Completion checks**

- Golden movement scenarios match the original SDL version.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P4-10-06 — Migrate Movement — Test

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Movement
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/movement_system.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Move player, enemies, and projectiles using position and velocity components.

**Completion checks**

- Golden movement scenarios match the original SDL version.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P4-10-07 — Migrate Movement — Repair

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Movement
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/movement_system.adb

Reproduce and repair this defect class in the current project: Reading SDL input inside the system or updating render positions separately.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Golden movement scenarios match the original SDL version.

### ADA-P4-10-08 — Migrate Movement — Refactor

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Movement
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/movement_system.adb

Refactor the chapter implementation so Pure systems and component transforms is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P4-10-09 — Migrate Movement — Integrate

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Movement
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/movement_system.adb

Integrate this chapter into the running final product so it works with earlier milestones: Move player, enemies, and projectiles using position and velocity components.

**Completion checks**

- Golden movement scenarios match the original SDL version.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P4-10-10 — Migrate Movement — Review

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Movement
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/movement_system.adb

Perform a senior-style checkpoint review of Migrate Movement in Rescue Run ECS.

**Completion checks**

- Golden movement scenarios match the original SDL version.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P4-11-01 — Migrate Rendering — Question

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Rendering
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/render_system.adb, src/adapters/sdl_rendering.adb

Answer one focused question before editing code: How should Read-only systems and adapter boundaries be used to accomplish this milestone: Render entities possessing transform and sprite components through the SDL adapter.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P4-11-02 — Migrate Rendering — Code Reading

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Rendering
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/render_system.adb, src/adapters/sdl_rendering.adb

Read the current implementation around src/systems/render_system.adb, src/adapters/sdl_rendering.adb. Trace how data enters, changes, and leaves the code for this milestone: Render entities possessing transform and sprite components through the SDL adapter.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P4-11-03 — Migrate Rendering — Predict

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Rendering
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/render_system.adb, src/adapters/sdl_rendering.adb

Predict the exact behavior if the implementation encounters this problem: Making rendering mutate gameplay state or storing textures directly in every entity.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P4-11-04 — Migrate Rendering — Implement

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Rendering
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/render_system.adb, src/adapters/sdl_rendering.adb

Implement the core milestone in the existing rescue_run_ecs crate: Render entities possessing transform and sprite components through the SDL adapter.

**Completion checks**

- Rendering consumes a read-only world view and matches original visuals.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P4-11-05 — Migrate Rendering — Extend

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Rendering
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/render_system.adb, src/adapters/sdl_rendering.adb

Extend the completed milestone with this practical variation: Add layers or sort keys without placing SDL types in components.

**Completion checks**

- Rendering consumes a read-only world view and matches original visuals.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P4-11-06 — Migrate Rendering — Test

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Rendering
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/render_system.adb, src/adapters/sdl_rendering.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Render entities possessing transform and sprite components through the SDL adapter.

**Completion checks**

- Rendering consumes a read-only world view and matches original visuals.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P4-11-07 — Migrate Rendering — Repair

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Rendering
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/render_system.adb, src/adapters/sdl_rendering.adb

Reproduce and repair this defect class in the current project: Making rendering mutate gameplay state or storing textures directly in every entity.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Rendering consumes a read-only world view and matches original visuals.

### ADA-P4-11-08 — Migrate Rendering — Refactor

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Rendering
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/render_system.adb, src/adapters/sdl_rendering.adb

Refactor the chapter implementation so Read-only systems and adapter boundaries is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P4-11-09 — Migrate Rendering — Integrate

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Rendering
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/render_system.adb, src/adapters/sdl_rendering.adb

Integrate this chapter into the running final product so it works with earlier milestones: Render entities possessing transform and sprite components through the SDL adapter.

**Completion checks**

- Rendering consumes a read-only world view and matches original visuals.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P4-11-10 — Migrate Rendering — Review

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Rendering
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/render_system.adb, src/adapters/sdl_rendering.adb

Perform a senior-style checkpoint review of Migrate Rendering in Rescue Run ECS.

**Completion checks**

- Rendering consumes a read-only world view and matches original visuals.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P4-12-01 — Migrate Collision — Question

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/collision_system.adb

Answer one focused question before editing code: How should Broad phase, narrow phase, and event generation be used to accomplish this milestone: Detect tile and entity collisions from collider and transform components.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P4-12-02 — Migrate Collision — Code Reading

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/collision_system.adb

Read the current implementation around src/systems/collision_system.adb. Trace how data enters, changes, and leaves the code for this milestone: Detect tile and entity collisions from collider and transform components.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P4-12-03 — Migrate Collision — Predict

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/collision_system.adb

Predict the exact behavior if the implementation encounters this problem: A single monolithic loop changing positions, health, audio, and objectives at once.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P4-12-04 — Migrate Collision — Implement

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/collision_system.adb

Implement the core milestone in the existing rescue_run_ecs crate: Detect tile and entity collisions from collider and transform components.

**Completion checks**

- Collision outcomes match baseline tests and remain order-stable.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P4-12-05 — Migrate Collision — Extend

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/collision_system.adb

Extend the completed milestone with this practical variation: Separate detection from response using events or command buffers.

**Completion checks**

- Collision outcomes match baseline tests and remain order-stable.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P4-12-06 — Migrate Collision — Test

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/collision_system.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Detect tile and entity collisions from collider and transform components.

**Completion checks**

- Collision outcomes match baseline tests and remain order-stable.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P4-12-07 — Migrate Collision — Repair

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/collision_system.adb

Reproduce and repair this defect class in the current project: A single monolithic loop changing positions, health, audio, and objectives at once.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Collision outcomes match baseline tests and remain order-stable.

### ADA-P4-12-08 — Migrate Collision — Refactor

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/collision_system.adb

Refactor the chapter implementation so Broad phase, narrow phase, and event generation is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P4-12-09 — Migrate Collision — Integrate

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/collision_system.adb

Integrate this chapter into the running final product so it works with earlier milestones: Detect tile and entity collisions from collider and transform components.

**Completion checks**

- Collision outcomes match baseline tests and remain order-stable.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P4-12-10 — Migrate Collision — Review

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Collision
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/collision_system.adb

Perform a senior-style checkpoint review of Migrate Collision in Rescue Run ECS.

**Completion checks**

- Collision outcomes match baseline tests and remain order-stable.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P4-13-01 — Migrate Animation — Question

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Animation
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/animation_system.adb

Answer one focused question before editing code: How should Component state and time-driven systems be used to accomplish this milestone: Advance animation components and derive clips from movement or action state.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P4-13-02 — Migrate Animation — Code Reading

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Animation
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/animation_system.adb

Read the current implementation around src/systems/animation_system.adb. Trace how data enters, changes, and leaves the code for this milestone: Advance animation components and derive clips from movement or action state.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P4-13-03 — Migrate Animation — Predict

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Animation
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/animation_system.adb

Predict the exact behavior if the implementation encounters this problem: Embedding animation frame counters in unrelated gameplay components.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P4-13-04 — Migrate Animation — Implement

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Animation
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/animation_system.adb

Implement the core milestone in the existing rescue_run_ecs crate: Advance animation components and derive clips from movement or action state.

**Completion checks**

- Animation timing matches the SDL project at multiple frame rates.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P4-13-05 — Migrate Animation — Extend

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Animation
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/animation_system.adb

Extend the completed milestone with this practical variation: Publish completion events for one-shot animations.

**Completion checks**

- Animation timing matches the SDL project at multiple frame rates.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P4-13-06 — Migrate Animation — Test

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Animation
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/animation_system.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Advance animation components and derive clips from movement or action state.

**Completion checks**

- Animation timing matches the SDL project at multiple frame rates.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P4-13-07 — Migrate Animation — Repair

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Animation
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/animation_system.adb

Reproduce and repair this defect class in the current project: Embedding animation frame counters in unrelated gameplay components.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Animation timing matches the SDL project at multiple frame rates.

### ADA-P4-13-08 — Migrate Animation — Refactor

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Animation
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/animation_system.adb

Refactor the chapter implementation so Component state and time-driven systems is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P4-13-09 — Migrate Animation — Integrate

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Animation
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/animation_system.adb

Integrate this chapter into the running final product so it works with earlier milestones: Advance animation components and derive clips from movement or action state.

**Completion checks**

- Animation timing matches the SDL project at multiple frame rates.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P4-13-10 — Migrate Animation — Review

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Animation
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/animation_system.adb

Perform a senior-style checkpoint review of Migrate Animation in Rescue Run ECS.

**Completion checks**

- Animation timing matches the SDL project at multiple frame rates.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P4-14-01 — Migrate Enemy AI — Question

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Enemy AI
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/ai_system.adb, src/components/ai.ads

Answer one focused question before editing code: How should State components, decision systems, and navigation data be used to accomplish this milestone: Represent AI state as components and update decisions separately from movement.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P4-14-02 — Migrate Enemy AI — Code Reading

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Enemy AI
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/ai_system.adb, src/components/ai.ads

Read the current implementation around src/systems/ai_system.adb, src/components/ai.ads. Trace how data enters, changes, and leaves the code for this milestone: Represent AI state as components and update decisions separately from movement.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P4-14-03 — Migrate Enemy AI — Predict

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Enemy AI
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/ai_system.adb, src/components/ai.ads

Predict the exact behavior if the implementation encounters this problem: Creating one system per enemy instance or storing object pointers in AI components.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P4-14-04 — Migrate Enemy AI — Implement

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Enemy AI
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/ai_system.adb, src/components/ai.ads

Implement the core milestone in the existing rescue_run_ecs crate: Represent AI state as components and update decisions separately from movement.

**Completion checks**

- Multiple enemy types share systems while differing through component data.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P4-14-05 — Migrate Enemy AI — Extend

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Enemy AI
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/ai_system.adb, src/components/ai.ads

Extend the completed milestone with this practical variation: Add reusable perception queries and simple path selection.

**Completion checks**

- Multiple enemy types share systems while differing through component data.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P4-14-06 — Migrate Enemy AI — Test

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Enemy AI
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/ai_system.adb, src/components/ai.ads

Create automated or repeatable tests that prove the milestone and its boundaries: Represent AI state as components and update decisions separately from movement.

**Completion checks**

- Multiple enemy types share systems while differing through component data.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P4-14-07 — Migrate Enemy AI — Repair

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Enemy AI
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/ai_system.adb, src/components/ai.ads

Reproduce and repair this defect class in the current project: Creating one system per enemy instance or storing object pointers in AI components.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Multiple enemy types share systems while differing through component data.

### ADA-P4-14-08 — Migrate Enemy AI — Refactor

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Enemy AI
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/ai_system.adb, src/components/ai.ads

Refactor the chapter implementation so State components, decision systems, and navigation data is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P4-14-09 — Migrate Enemy AI — Integrate

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Enemy AI
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/ai_system.adb, src/components/ai.ads

Integrate this chapter into the running final product so it works with earlier milestones: Represent AI state as components and update decisions separately from movement.

**Completion checks**

- Multiple enemy types share systems while differing through component data.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P4-14-10 — Migrate Enemy AI — Review

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Migrate Enemy AI
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/systems/ai_system.adb, src/components/ai.ads

Perform a senior-style checkpoint review of Migrate Enemy AI in Rescue Run ECS.

**Completion checks**

- Multiple enemy types share systems while differing through component data.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P4-15-01 — Serialize ECS Worlds — Question

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Serialize ECS Worlds
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/serialization.ads, src/ecs/serialization.adb

Answer one focused question before editing code: How should Stable IDs, component schemas, and versioning be used to accomplish this milestone: Save selected components and reconstruct entities without persisting runtime-only resources.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P4-15-02 — Serialize ECS Worlds — Code Reading

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Serialize ECS Worlds
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/serialization.ads, src/ecs/serialization.adb

Read the current implementation around src/ecs/serialization.ads, src/ecs/serialization.adb. Trace how data enters, changes, and leaves the code for this milestone: Save selected components and reconstruct entities without persisting runtime-only resources.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P4-15-03 — Serialize ECS Worlds — Predict

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Serialize ECS Worlds
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/serialization.ads, src/ecs/serialization.adb

Predict the exact behavior if the implementation encounters this problem: Serializing memory layout, store indexes, or SDL handles.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P4-15-04 — Serialize ECS Worlds — Implement

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Serialize ECS Worlds
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/serialization.ads, src/ecs/serialization.adb

Implement the core milestone in the existing rescue_run_ecs crate: Save selected components and reconstruct entities without persisting runtime-only resources.

**Completion checks**

- Save-load reproduces the same logical world and passes version tests.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P4-15-05 — Serialize ECS Worlds — Extend

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Serialize ECS Worlds
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/serialization.ads, src/ecs/serialization.adb

Extend the completed milestone with this practical variation: Add migration for one changed component schema.

**Completion checks**

- Save-load reproduces the same logical world and passes version tests.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P4-15-06 — Serialize ECS Worlds — Test

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Serialize ECS Worlds
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/serialization.ads, src/ecs/serialization.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Save selected components and reconstruct entities without persisting runtime-only resources.

**Completion checks**

- Save-load reproduces the same logical world and passes version tests.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P4-15-07 — Serialize ECS Worlds — Repair

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Serialize ECS Worlds
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/serialization.ads, src/ecs/serialization.adb

Reproduce and repair this defect class in the current project: Serializing memory layout, store indexes, or SDL handles.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Save-load reproduces the same logical world and passes version tests.

### ADA-P4-15-08 — Serialize ECS Worlds — Refactor

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Serialize ECS Worlds
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/serialization.ads, src/ecs/serialization.adb

Refactor the chapter implementation so Stable IDs, component schemas, and versioning is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P4-15-09 — Serialize ECS Worlds — Integrate

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Serialize ECS Worlds
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/serialization.ads, src/ecs/serialization.adb

Integrate this chapter into the running final product so it works with earlier milestones: Save selected components and reconstruct entities without persisting runtime-only resources.

**Completion checks**

- Save-load reproduces the same logical world and passes version tests.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P4-15-10 — Serialize ECS Worlds — Review

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Serialize ECS Worlds
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/ecs/serialization.ads, src/ecs/serialization.adb

Perform a senior-style checkpoint review of Serialize ECS Worlds in Rescue Run ECS.

**Completion checks**

- Save-load reproduces the same logical world and passes version tests.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P4-16-01 — Measure Data-Oriented Performance — Question

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Measure Data-Oriented Performance
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/diagnostics/metrics.ads, docs/performance.md

Answer one focused question before editing code: How should Profiling, cache behavior, allocations, and complexity be used to accomplish this milestone: Measure system time, entity counts, store density, allocations, and query cost.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P4-16-02 — Measure Data-Oriented Performance — Code Reading

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Measure Data-Oriented Performance
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/diagnostics/metrics.ads, docs/performance.md

Read the current implementation around src/diagnostics/metrics.ads, docs/performance.md. Trace how data enters, changes, and leaves the code for this milestone: Measure system time, entity counts, store density, allocations, and query cost.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P4-16-03 — Measure Data-Oriented Performance — Predict

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Measure Data-Oriented Performance
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/diagnostics/metrics.ads, docs/performance.md

Predict the exact behavior if the implementation encounters this problem: Claiming ECS is faster without comparable measurements.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P4-16-04 — Measure Data-Oriented Performance — Implement

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Measure Data-Oriented Performance
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/diagnostics/metrics.ads, docs/performance.md

Implement the core milestone in the existing rescue_run_ecs crate: Measure system time, entity counts, store density, allocations, and query cost.

**Completion checks**

- A repeatable benchmark explains where ECS helps and where it does not.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P4-16-05 — Measure Data-Oriented Performance — Extend

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Measure Data-Oriented Performance
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/diagnostics/metrics.ads, docs/performance.md

Extend the completed milestone with this practical variation: Compare results to the original SDL architecture with the same scenario.

**Completion checks**

- A repeatable benchmark explains where ECS helps and where it does not.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P4-16-06 — Measure Data-Oriented Performance — Test

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Measure Data-Oriented Performance
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/diagnostics/metrics.ads, docs/performance.md

Create automated or repeatable tests that prove the milestone and its boundaries: Measure system time, entity counts, store density, allocations, and query cost.

**Completion checks**

- A repeatable benchmark explains where ECS helps and where it does not.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P4-16-07 — Measure Data-Oriented Performance — Repair

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Measure Data-Oriented Performance
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/diagnostics/metrics.ads, docs/performance.md

Reproduce and repair this defect class in the current project: Claiming ECS is faster without comparable measurements.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- A repeatable benchmark explains where ECS helps and where it does not.

### ADA-P4-16-08 — Measure Data-Oriented Performance — Refactor

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Measure Data-Oriented Performance
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/diagnostics/metrics.ads, docs/performance.md

Refactor the chapter implementation so Profiling, cache behavior, allocations, and complexity is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P4-16-09 — Measure Data-Oriented Performance — Integrate

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Measure Data-Oriented Performance
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/diagnostics/metrics.ads, docs/performance.md

Integrate this chapter into the running final product so it works with earlier milestones: Measure system time, entity counts, store density, allocations, and query cost.

**Completion checks**

- A repeatable benchmark explains where ECS helps and where it does not.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P4-16-10 — Measure Data-Oriented Performance — Review

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Measure Data-Oriented Performance
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** src/diagnostics/metrics.ads, docs/performance.md

Perform a senior-style checkpoint review of Measure Data-Oriented Performance in Rescue Run ECS.

**Completion checks**

- A repeatable benchmark explains where ECS helps and where it does not.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P4-17-01 — Test and Debug the ECS — Question

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Test and Debug the ECS
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** tests/, src/diagnostics/ecs_debug.adb

Answer one focused question before editing code: How should System isolation, world fixtures, invariants, and debug views be used to accomplish this milestone: Build focused system tests, lifecycle tests, schedule tests, and a component-inspection overlay.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P4-17-02 — Test and Debug the ECS — Code Reading

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Test and Debug the ECS
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** tests/, src/diagnostics/ecs_debug.adb

Read the current implementation around tests/, src/diagnostics/ecs_debug.adb. Trace how data enters, changes, and leaves the code for this milestone: Build focused system tests, lifecycle tests, schedule tests, and a component-inspection overlay.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P4-17-03 — Test and Debug the ECS — Predict

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Test and Debug the ECS
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** tests/, src/diagnostics/ecs_debug.adb

Predict the exact behavior if the implementation encounters this problem: Only testing the full game and making failures impossible to localize.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P4-17-04 — Test and Debug the ECS — Implement

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Test and Debug the ECS
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** tests/, src/diagnostics/ecs_debug.adb

Implement the core milestone in the existing rescue_run_ecs crate: Build focused system tests, lifecycle tests, schedule tests, and a component-inspection overlay.

**Completion checks**

- Failures identify the responsible system, entity, and component state.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P4-17-05 — Test and Debug the ECS — Extend

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Test and Debug the ECS
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** tests/, src/diagnostics/ecs_debug.adb

Extend the completed milestone with this practical variation: Add invariant checks after each system in debug builds.

**Completion checks**

- Failures identify the responsible system, entity, and component state.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P4-17-06 — Test and Debug the ECS — Test

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Test and Debug the ECS
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** tests/, src/diagnostics/ecs_debug.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Build focused system tests, lifecycle tests, schedule tests, and a component-inspection overlay.

**Completion checks**

- Failures identify the responsible system, entity, and component state.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P4-17-07 — Test and Debug the ECS — Repair

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Test and Debug the ECS
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** tests/, src/diagnostics/ecs_debug.adb

Reproduce and repair this defect class in the current project: Only testing the full game and making failures impossible to localize.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Failures identify the responsible system, entity, and component state.

### ADA-P4-17-08 — Test and Debug the ECS — Refactor

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Test and Debug the ECS
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** tests/, src/diagnostics/ecs_debug.adb

Refactor the chapter implementation so System isolation, world fixtures, invariants, and debug views is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P4-17-09 — Test and Debug the ECS — Integrate

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Test and Debug the ECS
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** tests/, src/diagnostics/ecs_debug.adb

Integrate this chapter into the running final product so it works with earlier milestones: Build focused system tests, lifecycle tests, schedule tests, and a component-inspection overlay.

**Completion checks**

- Failures identify the responsible system, entity, and component state.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P4-17-10 — Test and Debug the ECS — Review

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Test and Debug the ECS
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** tests/, src/diagnostics/ecs_debug.adb

Perform a senior-style checkpoint review of Test and Debug the ECS in Rescue Run ECS.

**Completion checks**

- Failures identify the responsible system, entity, and component state.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P4-18-01 — Complete the ECS Conversion — Question

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Complete the ECS Conversion
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** README.md, docs/migration_report.md, CHANGELOG.md

Answer one focused question before editing code: How should Migration completion, architecture review, and release comparison be used to accomplish this milestone: Reach feature parity, remove obsolete object-oriented paths, document tradeoffs, and tag the ECS release.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P4-18-02 — Complete the ECS Conversion — Code Reading

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Complete the ECS Conversion
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** README.md, docs/migration_report.md, CHANGELOG.md

Read the current implementation around README.md, docs/migration_report.md, CHANGELOG.md. Trace how data enters, changes, and leaves the code for this milestone: Reach feature parity, remove obsolete object-oriented paths, document tradeoffs, and tag the ECS release.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P4-18-03 — Complete the ECS Conversion — Predict

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Complete the ECS Conversion
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** README.md, docs/migration_report.md, CHANGELOG.md

Predict the exact behavior if the implementation encounters this problem: Maintaining two incomplete architectures indefinitely or deleting the baseline too early.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P4-18-04 — Complete the ECS Conversion — Implement

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Complete the ECS Conversion
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** README.md, docs/migration_report.md, CHANGELOG.md

Implement the core milestone in the existing rescue_run_ecs crate: Reach feature parity, remove obsolete object-oriented paths, document tradeoffs, and tag the ECS release.

**Completion checks**

- The ECS build passes golden behavior tests and documents measured differences.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P4-18-05 — Complete the ECS Conversion — Extend

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Complete the ECS Conversion
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** README.md, docs/migration_report.md, CHANGELOG.md

Extend the completed milestone with this practical variation: Provide a side-by-side architecture and performance report.

**Completion checks**

- The ECS build passes golden behavior tests and documents measured differences.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P4-18-06 — Complete the ECS Conversion — Test

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Complete the ECS Conversion
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** README.md, docs/migration_report.md, CHANGELOG.md

Create automated or repeatable tests that prove the milestone and its boundaries: Reach feature parity, remove obsolete object-oriented paths, document tradeoffs, and tag the ECS release.

**Completion checks**

- The ECS build passes golden behavior tests and documents measured differences.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P4-18-07 — Complete the ECS Conversion — Repair

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Complete the ECS Conversion
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** README.md, docs/migration_report.md, CHANGELOG.md

Reproduce and repair this defect class in the current project: Maintaining two incomplete architectures indefinitely or deleting the baseline too early.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- The ECS build passes golden behavior tests and documents measured differences.

### ADA-P4-18-08 — Complete the ECS Conversion — Refactor

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Complete the ECS Conversion
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** README.md, docs/migration_report.md, CHANGELOG.md

Refactor the chapter implementation so Migration completion, architecture review, and release comparison is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P4-18-09 — Complete the ECS Conversion — Integrate

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Complete the ECS Conversion
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** README.md, docs/migration_report.md, CHANGELOG.md

Integrate this chapter into the running final product so it works with earlier milestones: Reach feature parity, remove obsolete object-oriented paths, document tradeoffs, and tag the ECS release.

**Completion checks**

- The ECS build passes golden behavior tests and documents measured differences.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P4-18-10 — Complete the ECS Conversion — Review

- **Project:** Project 4 — Rescue Run ECS Conversion
- **Chapter:** Complete the ECS Conversion
- **Workspace:** `~/Documents/src/projects/ada-mastery/rescue_run_ecs`
- **Files:** README.md, docs/migration_report.md, CHANGELOG.md

Perform a senior-style checkpoint review of Complete the ECS Conversion in Rescue Run ECS.

**Completion checks**

- The ECS build passes golden behavior tests and documents measured differences.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P5-01-01 — Create the GtkAda Application — Question

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the GtkAda Application
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** alire.toml, src/forge_map_editor.adb, src/editor_application.ads

Answer one focused question before editing code: How should GtkAda dependency, initialization, application/window lifecycle be used to accomplish this milestone: Add GtkAda through Alire and open a main application window with safe startup and shutdown.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P5-01-02 — Create the GtkAda Application — Code Reading

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the GtkAda Application
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** alire.toml, src/forge_map_editor.adb, src/editor_application.ads

Read the current implementation around alire.toml, src/forge_map_editor.adb, src/editor_application.ads. Trace how data enters, changes, and leaves the code for this milestone: Add GtkAda through Alire and open a main application window with safe startup and shutdown.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P5-01-03 — Create the GtkAda Application — Predict

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the GtkAda Application
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** alire.toml, src/forge_map_editor.adb, src/editor_application.ads

Predict the exact behavior if the implementation encounters this problem: Using widget objects before initialization or relying on abrupt process exit for cleanup.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P5-01-04 — Create the GtkAda Application — Implement

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the GtkAda Application
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** alire.toml, src/forge_map_editor.adb, src/editor_application.ads

Implement the core milestone in the existing forge_map_editor crate: Add GtkAda through Alire and open a main application window with safe startup and shutdown.

**Completion checks**

- The application opens one main window and exits cleanly from menu or window close.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P5-01-05 — Create the GtkAda Application — Extend

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the GtkAda Application
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** alire.toml, src/forge_map_editor.adb, src/editor_application.ads

Extend the completed milestone with this practical variation: Add application metadata, default size, and restored window geometry.

**Completion checks**

- The application opens one main window and exits cleanly from menu or window close.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P5-01-06 — Create the GtkAda Application — Test

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the GtkAda Application
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** alire.toml, src/forge_map_editor.adb, src/editor_application.ads

Create automated or repeatable tests that prove the milestone and its boundaries: Add GtkAda through Alire and open a main application window with safe startup and shutdown.

**Completion checks**

- The application opens one main window and exits cleanly from menu or window close.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P5-01-07 — Create the GtkAda Application — Repair

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the GtkAda Application
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** alire.toml, src/forge_map_editor.adb, src/editor_application.ads

Reproduce and repair this defect class in the current project: Using widget objects before initialization or relying on abrupt process exit for cleanup.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- The application opens one main window and exits cleanly from menu or window close.

### ADA-P5-01-08 — Create the GtkAda Application — Refactor

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the GtkAda Application
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** alire.toml, src/forge_map_editor.adb, src/editor_application.ads

Refactor the chapter implementation so GtkAda dependency, initialization, application/window lifecycle is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P5-01-09 — Create the GtkAda Application — Integrate

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the GtkAda Application
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** alire.toml, src/forge_map_editor.adb, src/editor_application.ads

Integrate this chapter into the running final product so it works with earlier milestones: Add GtkAda through Alire and open a main application window with safe startup and shutdown.

**Completion checks**

- The application opens one main window and exits cleanly from menu or window close.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P5-01-10 — Create the GtkAda Application — Review

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the GtkAda Application
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** alire.toml, src/forge_map_editor.adb, src/editor_application.ads

Perform a senior-style checkpoint review of Create the GtkAda Application in Forge Map Editor.

**Completion checks**

- The application opens one main window and exits cleanly from menu or window close.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P5-02-01 — Build the Editor Shell — Question

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Editor Shell
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/main_window.ads, src/ui/main_window.adb

Answer one focused question before editing code: How should Hierarchical widget composition and containers be used to accomplish this milestone: Create a Tiled-like but simpler shell: central canvas, left palette, right properties/layers, bottom status area.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P5-02-02 — Build the Editor Shell — Code Reading

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Editor Shell
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/main_window.ads, src/ui/main_window.adb

Read the current implementation around src/ui/main_window.ads, src/ui/main_window.adb. Trace how data enters, changes, and leaves the code for this milestone: Create a Tiled-like but simpler shell: central canvas, left palette, right properties/layers, bottom status area.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P5-02-03 — Build the Editor Shell — Predict

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Editor Shell
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/main_window.ads, src/ui/main_window.adb

Predict the exact behavior if the implementation encounters this problem: Hard-coding fixed widget sizes or mixing document logic into layout construction.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P5-02-04 — Build the Editor Shell — Implement

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Editor Shell
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/main_window.ads, src/ui/main_window.adb

Implement the core milestone in the existing forge_map_editor crate: Create a Tiled-like but simpler shell: central canvas, left palette, right properties/layers, bottom status area.

**Completion checks**

- Panels resize sensibly and the central canvas receives remaining space.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P5-02-05 — Build the Editor Shell — Extend

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Editor Shell
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/main_window.ads, src/ui/main_window.adb

Extend the completed milestone with this practical variation: Add resizable panes and persist divider positions.

**Completion checks**

- Panels resize sensibly and the central canvas receives remaining space.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P5-02-06 — Build the Editor Shell — Test

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Editor Shell
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/main_window.ads, src/ui/main_window.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Create a Tiled-like but simpler shell: central canvas, left palette, right properties/layers, bottom status area.

**Completion checks**

- Panels resize sensibly and the central canvas receives remaining space.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P5-02-07 — Build the Editor Shell — Repair

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Editor Shell
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/main_window.ads, src/ui/main_window.adb

Reproduce and repair this defect class in the current project: Hard-coding fixed widget sizes or mixing document logic into layout construction.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Panels resize sensibly and the central canvas receives remaining space.

### ADA-P5-02-08 — Build the Editor Shell — Refactor

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Editor Shell
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/main_window.ads, src/ui/main_window.adb

Refactor the chapter implementation so Hierarchical widget composition and containers is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P5-02-09 — Build the Editor Shell — Integrate

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Editor Shell
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/main_window.ads, src/ui/main_window.adb

Integrate this chapter into the running final product so it works with earlier milestones: Create a Tiled-like but simpler shell: central canvas, left palette, right properties/layers, bottom status area.

**Completion checks**

- Panels resize sensibly and the central canvas receives remaining space.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P5-02-10 — Build the Editor Shell — Review

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Editor Shell
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/main_window.ads, src/ui/main_window.adb

Perform a senior-style checkpoint review of Build the Editor Shell in Forge Map Editor.

**Completion checks**

- Panels resize sensibly and the central canvas receives remaining space.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P5-03-01 — Menus, Actions, and Shortcuts — Question

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Menus, Actions, and Shortcuts
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/editor_actions.ads, src/ui/editor_actions.adb

Answer one focused question before editing code: How should Gtk actions, menus, accelerators, and command routing be used to accomplish this milestone: Add New, Open, Save, Save As, Undo, Redo, Validate, Export, and Quit actions.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P5-03-02 — Menus, Actions, and Shortcuts — Code Reading

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Menus, Actions, and Shortcuts
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/editor_actions.ads, src/ui/editor_actions.adb

Read the current implementation around src/ui/editor_actions.ads, src/ui/editor_actions.adb. Trace how data enters, changes, and leaves the code for this milestone: Add New, Open, Save, Save As, Undo, Redo, Validate, Export, and Quit actions.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P5-03-03 — Menus, Actions, and Shortcuts — Predict

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Menus, Actions, and Shortcuts
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/editor_actions.ads, src/ui/editor_actions.adb

Predict the exact behavior if the implementation encounters this problem: Duplicating behavior in every signal callback or allowing actions in invalid states.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P5-03-04 — Menus, Actions, and Shortcuts — Implement

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Menus, Actions, and Shortcuts
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/editor_actions.ads, src/ui/editor_actions.adb

Implement the core milestone in the existing forge_map_editor crate: Add New, Open, Save, Save As, Undo, Redo, Validate, Export, and Quit actions.

**Completion checks**

- Menus, buttons, and shortcuts invoke one shared command path.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P5-03-05 — Menus, Actions, and Shortcuts — Extend

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Menus, Actions, and Shortcuts
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/editor_actions.ads, src/ui/editor_actions.adb

Extend the completed milestone with this practical variation: Connect toolbar buttons and keyboard shortcuts to the same command objects.

**Completion checks**

- Menus, buttons, and shortcuts invoke one shared command path.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P5-03-06 — Menus, Actions, and Shortcuts — Test

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Menus, Actions, and Shortcuts
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/editor_actions.ads, src/ui/editor_actions.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Add New, Open, Save, Save As, Undo, Redo, Validate, Export, and Quit actions.

**Completion checks**

- Menus, buttons, and shortcuts invoke one shared command path.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P5-03-07 — Menus, Actions, and Shortcuts — Repair

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Menus, Actions, and Shortcuts
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/editor_actions.ads, src/ui/editor_actions.adb

Reproduce and repair this defect class in the current project: Duplicating behavior in every signal callback or allowing actions in invalid states.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Menus, buttons, and shortcuts invoke one shared command path.

### ADA-P5-03-08 — Menus, Actions, and Shortcuts — Refactor

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Menus, Actions, and Shortcuts
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/editor_actions.ads, src/ui/editor_actions.adb

Refactor the chapter implementation so Gtk actions, menus, accelerators, and command routing is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P5-03-09 — Menus, Actions, and Shortcuts — Integrate

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Menus, Actions, and Shortcuts
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/editor_actions.ads, src/ui/editor_actions.adb

Integrate this chapter into the running final product so it works with earlier milestones: Add New, Open, Save, Save As, Undo, Redo, Validate, Export, and Quit actions.

**Completion checks**

- Menus, buttons, and shortcuts invoke one shared command path.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P5-03-10 — Menus, Actions, and Shortcuts — Review

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Menus, Actions, and Shortcuts
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/editor_actions.ads, src/ui/editor_actions.adb

Perform a senior-style checkpoint review of Menus, Actions, and Shortcuts in Forge Map Editor.

**Completion checks**

- Menus, buttons, and shortcuts invoke one shared command path.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P5-04-01 — Separate the Document Model — Question

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Separate the Document Model
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/editor_document.ads, src/model/editor_document.adb

Answer one focused question before editing code: How should Model-view separation, observable state, and domain APIs be used to accomplish this milestone: Create an editor document independent of Gtk widgets, containing map, layers, objects, selection, and dirty state.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P5-04-02 — Separate the Document Model — Code Reading

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Separate the Document Model
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/editor_document.ads, src/model/editor_document.adb

Read the current implementation around src/model/editor_document.ads, src/model/editor_document.adb. Trace how data enters, changes, and leaves the code for this milestone: Create an editor document independent of Gtk widgets, containing map, layers, objects, selection, and dirty state.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P5-04-03 — Separate the Document Model — Predict

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Separate the Document Model
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/editor_document.ads, src/model/editor_document.adb

Predict the exact behavior if the implementation encounters this problem: Treating widgets as the authoritative map data or calling Gtk from model packages.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P5-04-04 — Separate the Document Model — Implement

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Separate the Document Model
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/editor_document.ads, src/model/editor_document.adb

Implement the core milestone in the existing forge_map_editor crate: Create an editor document independent of Gtk widgets, containing map, layers, objects, selection, and dirty state.

**Completion checks**

- Document tests run without starting Gtk.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P5-04-05 — Separate the Document Model — Extend

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Separate the Document Model
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/editor_document.ads, src/model/editor_document.adb

Extend the completed milestone with this practical variation: Add change notifications or a controlled refresh mechanism.

**Completion checks**

- Document tests run without starting Gtk.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P5-04-06 — Separate the Document Model — Test

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Separate the Document Model
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/editor_document.ads, src/model/editor_document.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Create an editor document independent of Gtk widgets, containing map, layers, objects, selection, and dirty state.

**Completion checks**

- Document tests run without starting Gtk.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P5-04-07 — Separate the Document Model — Repair

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Separate the Document Model
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/editor_document.ads, src/model/editor_document.adb

Reproduce and repair this defect class in the current project: Treating widgets as the authoritative map data or calling Gtk from model packages.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Document tests run without starting Gtk.

### ADA-P5-04-08 — Separate the Document Model — Refactor

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Separate the Document Model
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/editor_document.ads, src/model/editor_document.adb

Refactor the chapter implementation so Model-view separation, observable state, and domain APIs is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P5-04-09 — Separate the Document Model — Integrate

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Separate the Document Model
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/editor_document.ads, src/model/editor_document.adb

Integrate this chapter into the running final product so it works with earlier milestones: Create an editor document independent of Gtk widgets, containing map, layers, objects, selection, and dirty state.

**Completion checks**

- Document tests run without starting Gtk.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P5-04-10 — Separate the Document Model — Review

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Separate the Document Model
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/editor_document.ads, src/model/editor_document.adb

Perform a senior-style checkpoint review of Separate the Document Model in Forge Map Editor.

**Completion checks**

- Document tests run without starting Gtk.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P5-05-01 — Draw the Map Canvas — Question

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Draw the Map Canvas
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas.ads, src/ui/map_canvas.adb

Answer one focused question before editing code: How should Gtk.Drawing_Area, Cairo, expose/draw callbacks, and coordinate transforms be used to accomplish this milestone: Render tiles, grid, spawn, objects, selection, and viewport through a drawing area.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P5-05-02 — Draw the Map Canvas — Code Reading

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Draw the Map Canvas
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas.ads, src/ui/map_canvas.adb

Read the current implementation around src/ui/map_canvas.ads, src/ui/map_canvas.adb. Trace how data enters, changes, and leaves the code for this milestone: Render tiles, grid, spawn, objects, selection, and viewport through a drawing area.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P5-05-03 — Draw the Map Canvas — Predict

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Draw the Map Canvas
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas.ads, src/ui/map_canvas.adb

Predict the exact behavior if the implementation encounters this problem: Doing file I/O inside draw callbacks or confusing world and device coordinates.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P5-05-04 — Draw the Map Canvas — Implement

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Draw the Map Canvas
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas.ads, src/ui/map_canvas.adb

Implement the core milestone in the existing forge_map_editor crate: Render tiles, grid, spawn, objects, selection, and viewport through a drawing area.

**Completion checks**

- The canvas redraws correctly after resize, scroll, and document changes.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P5-05-05 — Draw the Map Canvas — Extend

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Draw the Map Canvas
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas.ads, src/ui/map_canvas.adb

Extend the completed milestone with this practical variation: Add dirty-region redraw where practical.

**Completion checks**

- The canvas redraws correctly after resize, scroll, and document changes.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P5-05-06 — Draw the Map Canvas — Test

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Draw the Map Canvas
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas.ads, src/ui/map_canvas.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Render tiles, grid, spawn, objects, selection, and viewport through a drawing area.

**Completion checks**

- The canvas redraws correctly after resize, scroll, and document changes.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P5-05-07 — Draw the Map Canvas — Repair

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Draw the Map Canvas
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas.ads, src/ui/map_canvas.adb

Reproduce and repair this defect class in the current project: Doing file I/O inside draw callbacks or confusing world and device coordinates.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- The canvas redraws correctly after resize, scroll, and document changes.

### ADA-P5-05-08 — Draw the Map Canvas — Refactor

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Draw the Map Canvas
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas.ads, src/ui/map_canvas.adb

Refactor the chapter implementation so Gtk.Drawing_Area, Cairo, expose/draw callbacks, and coordinate transforms is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P5-05-09 — Draw the Map Canvas — Integrate

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Draw the Map Canvas
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas.ads, src/ui/map_canvas.adb

Integrate this chapter into the running final product so it works with earlier milestones: Render tiles, grid, spawn, objects, selection, and viewport through a drawing area.

**Completion checks**

- The canvas redraws correctly after resize, scroll, and document changes.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P5-05-10 — Draw the Map Canvas — Review

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Draw the Map Canvas
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas.ads, src/ui/map_canvas.adb

Perform a senior-style checkpoint review of Draw the Map Canvas in Forge Map Editor.

**Completion checks**

- The canvas redraws correctly after resize, scroll, and document changes.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P5-06-01 — Pan, Zoom, and Pointer Input — Question

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Pan, Zoom, and Pointer Input
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas_input.ads, src/ui/viewport.ads

Answer one focused question before editing code: How should Signals, event masks, gestures, and viewport math be used to accomplish this milestone: Support wheel zoom, middle-button or space-drag pan, cursor position, and coordinate conversion.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P5-06-02 — Pan, Zoom, and Pointer Input — Code Reading

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Pan, Zoom, and Pointer Input
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas_input.ads, src/ui/viewport.ads

Read the current implementation around src/ui/map_canvas_input.ads, src/ui/viewport.ads. Trace how data enters, changes, and leaves the code for this milestone: Support wheel zoom, middle-button or space-drag pan, cursor position, and coordinate conversion.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P5-06-03 — Pan, Zoom, and Pointer Input — Predict

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Pan, Zoom, and Pointer Input
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas_input.ads, src/ui/viewport.ads

Predict the exact behavior if the implementation encounters this problem: Accumulating transform error or letting zoom produce unusable scales.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P5-06-04 — Pan, Zoom, and Pointer Input — Implement

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Pan, Zoom, and Pointer Input
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas_input.ads, src/ui/viewport.ads

Implement the core milestone in the existing forge_map_editor crate: Support wheel zoom, middle-button or space-drag pan, cursor position, and coordinate conversion.

**Completion checks**

- Pointer-to-tile conversion remains correct across pan and zoom levels.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P5-06-05 — Pan, Zoom, and Pointer Input — Extend

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Pan, Zoom, and Pointer Input
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas_input.ads, src/ui/viewport.ads

Extend the completed milestone with this practical variation: Zoom around the pointer and add fit-map/reset-view actions.

**Completion checks**

- Pointer-to-tile conversion remains correct across pan and zoom levels.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P5-06-06 — Pan, Zoom, and Pointer Input — Test

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Pan, Zoom, and Pointer Input
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas_input.ads, src/ui/viewport.ads

Create automated or repeatable tests that prove the milestone and its boundaries: Support wheel zoom, middle-button or space-drag pan, cursor position, and coordinate conversion.

**Completion checks**

- Pointer-to-tile conversion remains correct across pan and zoom levels.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P5-06-07 — Pan, Zoom, and Pointer Input — Repair

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Pan, Zoom, and Pointer Input
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas_input.ads, src/ui/viewport.ads

Reproduce and repair this defect class in the current project: Accumulating transform error or letting zoom produce unusable scales.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Pointer-to-tile conversion remains correct across pan and zoom levels.

### ADA-P5-06-08 — Pan, Zoom, and Pointer Input — Refactor

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Pan, Zoom, and Pointer Input
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas_input.ads, src/ui/viewport.ads

Refactor the chapter implementation so Signals, event masks, gestures, and viewport math is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P5-06-09 — Pan, Zoom, and Pointer Input — Integrate

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Pan, Zoom, and Pointer Input
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas_input.ads, src/ui/viewport.ads

Integrate this chapter into the running final product so it works with earlier milestones: Support wheel zoom, middle-button or space-drag pan, cursor position, and coordinate conversion.

**Completion checks**

- Pointer-to-tile conversion remains correct across pan and zoom levels.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P5-06-10 — Pan, Zoom, and Pointer Input — Review

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Pan, Zoom, and Pointer Input
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/map_canvas_input.ads, src/ui/viewport.ads

Perform a senior-style checkpoint review of Pan, Zoom, and Pointer Input in Forge Map Editor.

**Completion checks**

- Pointer-to-tile conversion remains correct across pan and zoom levels.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P5-07-01 — Create the Tile Palette — Question

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the Tile Palette
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/tile_palette.ads, src/ui/tile_palette.adb

Answer one focused question before editing code: How should Lists, icon views, selection models, and reusable widgets be used to accomplish this milestone: Show available tile types with names, icons/colors, and the current brush.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P5-07-02 — Create the Tile Palette — Code Reading

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the Tile Palette
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/tile_palette.ads, src/ui/tile_palette.adb

Read the current implementation around src/ui/tile_palette.ads, src/ui/tile_palette.adb. Trace how data enters, changes, and leaves the code for this milestone: Show available tile types with names, icons/colors, and the current brush.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P5-07-03 — Create the Tile Palette — Predict

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the Tile Palette
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/tile_palette.ads, src/ui/tile_palette.adb

Predict the exact behavior if the implementation encounters this problem: Storing the selected tile only inside the widget instead of editor tool state.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P5-07-04 — Create the Tile Palette — Implement

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the Tile Palette
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/tile_palette.ads, src/ui/tile_palette.adb

Implement the core milestone in the existing forge_map_editor crate: Show available tile types with names, icons/colors, and the current brush.

**Completion checks**

- Palette selection updates tool state and survives document refreshes.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P5-07-05 — Create the Tile Palette — Extend

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the Tile Palette
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/tile_palette.ads, src/ui/tile_palette.adb

Extend the completed milestone with this practical variation: Add search or categories and keyboard selection.

**Completion checks**

- Palette selection updates tool state and survives document refreshes.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P5-07-06 — Create the Tile Palette — Test

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the Tile Palette
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/tile_palette.ads, src/ui/tile_palette.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Show available tile types with names, icons/colors, and the current brush.

**Completion checks**

- Palette selection updates tool state and survives document refreshes.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P5-07-07 — Create the Tile Palette — Repair

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the Tile Palette
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/tile_palette.ads, src/ui/tile_palette.adb

Reproduce and repair this defect class in the current project: Storing the selected tile only inside the widget instead of editor tool state.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Palette selection updates tool state and survives document refreshes.

### ADA-P5-07-08 — Create the Tile Palette — Refactor

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the Tile Palette
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/tile_palette.ads, src/ui/tile_palette.adb

Refactor the chapter implementation so Lists, icon views, selection models, and reusable widgets is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P5-07-09 — Create the Tile Palette — Integrate

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the Tile Palette
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/tile_palette.ads, src/ui/tile_palette.adb

Integrate this chapter into the running final product so it works with earlier milestones: Show available tile types with names, icons/colors, and the current brush.

**Completion checks**

- Palette selection updates tool state and survives document refreshes.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P5-07-10 — Create the Tile Palette — Review

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Create the Tile Palette
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/tile_palette.ads, src/ui/tile_palette.adb

Perform a senior-style checkpoint review of Create the Tile Palette in Forge Map Editor.

**Completion checks**

- Palette selection updates tool state and survives document refreshes.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P5-08-01 — Implement Map Painting Tools — Question

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Map Painting Tools
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/tools/paint_tools.ads, src/tools/paint_tools.adb

Answer one focused question before editing code: How should Mouse signals, tools, drag operations, and model updates be used to accomplish this milestone: Add pencil, rectangle fill, flood fill, erase, and eyedropper tools.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P5-08-02 — Implement Map Painting Tools — Code Reading

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Map Painting Tools
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/tools/paint_tools.ads, src/tools/paint_tools.adb

Read the current implementation around src/tools/paint_tools.ads, src/tools/paint_tools.adb. Trace how data enters, changes, and leaves the code for this milestone: Add pencil, rectangle fill, flood fill, erase, and eyedropper tools.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P5-08-03 — Implement Map Painting Tools — Predict

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Map Painting Tools
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/tools/paint_tools.ads, src/tools/paint_tools.adb

Predict the exact behavior if the implementation encounters this problem: Creating hundreds of undo entries during one drag or modifying outside map bounds.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P5-08-04 — Implement Map Painting Tools — Implement

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Map Painting Tools
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/tools/paint_tools.ads, src/tools/paint_tools.adb

Implement the core milestone in the existing forge_map_editor crate: Add pencil, rectangle fill, flood fill, erase, and eyedropper tools.

**Completion checks**

- Every tool changes the model predictably and creates appropriate undo history.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P5-08-05 — Implement Map Painting Tools — Extend

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Map Painting Tools
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/tools/paint_tools.ads, src/tools/paint_tools.adb

Extend the completed milestone with this practical variation: Preview changes during drag and commit one undoable command on release.

**Completion checks**

- Every tool changes the model predictably and creates appropriate undo history.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P5-08-06 — Implement Map Painting Tools — Test

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Map Painting Tools
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/tools/paint_tools.ads, src/tools/paint_tools.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Add pencil, rectangle fill, flood fill, erase, and eyedropper tools.

**Completion checks**

- Every tool changes the model predictably and creates appropriate undo history.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P5-08-07 — Implement Map Painting Tools — Repair

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Map Painting Tools
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/tools/paint_tools.ads, src/tools/paint_tools.adb

Reproduce and repair this defect class in the current project: Creating hundreds of undo entries during one drag or modifying outside map bounds.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Every tool changes the model predictably and creates appropriate undo history.

### ADA-P5-08-08 — Implement Map Painting Tools — Refactor

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Map Painting Tools
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/tools/paint_tools.ads, src/tools/paint_tools.adb

Refactor the chapter implementation so Mouse signals, tools, drag operations, and model updates is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P5-08-09 — Implement Map Painting Tools — Integrate

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Map Painting Tools
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/tools/paint_tools.ads, src/tools/paint_tools.adb

Integrate this chapter into the running final product so it works with earlier milestones: Add pencil, rectangle fill, flood fill, erase, and eyedropper tools.

**Completion checks**

- Every tool changes the model predictably and creates appropriate undo history.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P5-08-10 — Implement Map Painting Tools — Review

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Map Painting Tools
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/tools/paint_tools.ads, src/tools/paint_tools.adb

Perform a senior-style checkpoint review of Implement Map Painting Tools in Forge Map Editor.

**Completion checks**

- Every tool changes the model predictably and creates appropriate undo history.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P5-09-01 — Add Layers — Question

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Add Layers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/layers.ads, src/ui/layers_panel.ads

Answer one focused question before editing code: How should Tree/list models, visibility, locking, ordering, and composition be used to accomplish this milestone: Support tile, object, and trigger layers with add, delete, rename, reorder, visibility, and lock.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P5-09-02 — Add Layers — Code Reading

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Add Layers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/layers.ads, src/ui/layers_panel.ads

Read the current implementation around src/model/layers.ads, src/ui/layers_panel.ads. Trace how data enters, changes, and leaves the code for this milestone: Support tile, object, and trigger layers with add, delete, rename, reorder, visibility, and lock.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P5-09-03 — Add Layers — Predict

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Add Layers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/layers.ads, src/ui/layers_panel.ads

Predict the exact behavior if the implementation encounters this problem: Editing hidden/locked layers or using list position as permanent identity.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P5-09-04 — Add Layers — Implement

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Add Layers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/layers.ads, src/ui/layers_panel.ads

Implement the core milestone in the existing forge_map_editor crate: Support tile, object, and trigger layers with add, delete, rename, reorder, visibility, and lock.

**Completion checks**

- Layer operations update both panel and canvas while preserving stable IDs.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P5-09-05 — Add Layers — Extend

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Add Layers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/layers.ads, src/ui/layers_panel.ads

Extend the completed milestone with this practical variation: Reflect layer order in canvas rendering and export.

**Completion checks**

- Layer operations update both panel and canvas while preserving stable IDs.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P5-09-06 — Add Layers — Test

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Add Layers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/layers.ads, src/ui/layers_panel.ads

Create automated or repeatable tests that prove the milestone and its boundaries: Support tile, object, and trigger layers with add, delete, rename, reorder, visibility, and lock.

**Completion checks**

- Layer operations update both panel and canvas while preserving stable IDs.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P5-09-07 — Add Layers — Repair

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Add Layers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/layers.ads, src/ui/layers_panel.ads

Reproduce and repair this defect class in the current project: Editing hidden/locked layers or using list position as permanent identity.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Layer operations update both panel and canvas while preserving stable IDs.

### ADA-P5-09-08 — Add Layers — Refactor

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Add Layers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/layers.ads, src/ui/layers_panel.ads

Refactor the chapter implementation so Tree/list models, visibility, locking, ordering, and composition is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P5-09-09 — Add Layers — Integrate

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Add Layers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/layers.ads, src/ui/layers_panel.ads

Integrate this chapter into the running final product so it works with earlier milestones: Support tile, object, and trigger layers with add, delete, rename, reorder, visibility, and lock.

**Completion checks**

- Layer operations update both panel and canvas while preserving stable IDs.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P5-09-10 — Add Layers — Review

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Add Layers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/layers.ads, src/ui/layers_panel.ads

Perform a senior-style checkpoint review of Add Layers in Forge Map Editor.

**Completion checks**

- Layer operations update both panel and canvas while preserving stable IDs.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P5-10-01 — Place Objects and Triggers — Question

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Place Objects and Triggers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/map_objects.ads, src/tools/object_tool.adb

Answer one focused question before editing code: How should Object models, shapes, hit testing, and custom data be used to accomplish this milestone: Place spawn points, pickups, enemies, exits, rectangles, points, and trigger regions on object layers.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P5-10-02 — Place Objects and Triggers — Code Reading

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Place Objects and Triggers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/map_objects.ads, src/tools/object_tool.adb

Read the current implementation around src/model/map_objects.ads, src/tools/object_tool.adb. Trace how data enters, changes, and leaves the code for this milestone: Place spawn points, pickups, enemies, exits, rectangles, points, and trigger regions on object layers.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P5-10-03 — Place Objects and Triggers — Predict

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Place Objects and Triggers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/map_objects.ads, src/tools/object_tool.adb

Predict the exact behavior if the implementation encounters this problem: Forcing free-position objects into tile storage or mixing trigger execution into the editor model.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P5-10-04 — Place Objects and Triggers — Implement

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Place Objects and Triggers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/map_objects.ads, src/tools/object_tool.adb

Implement the core milestone in the existing forge_map_editor crate: Place spawn points, pickups, enemies, exits, rectangles, points, and trigger regions on object layers.

**Completion checks**

- Objects can be created, selected, saved, loaded, and rendered independently of tiles.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P5-10-05 — Place Objects and Triggers — Extend

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Place Objects and Triggers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/map_objects.ads, src/tools/object_tool.adb

Extend the completed milestone with this practical variation: Add named object types and custom properties.

**Completion checks**

- Objects can be created, selected, saved, loaded, and rendered independently of tiles.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P5-10-06 — Place Objects and Triggers — Test

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Place Objects and Triggers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/map_objects.ads, src/tools/object_tool.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Place spawn points, pickups, enemies, exits, rectangles, points, and trigger regions on object layers.

**Completion checks**

- Objects can be created, selected, saved, loaded, and rendered independently of tiles.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P5-10-07 — Place Objects and Triggers — Repair

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Place Objects and Triggers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/map_objects.ads, src/tools/object_tool.adb

Reproduce and repair this defect class in the current project: Forcing free-position objects into tile storage or mixing trigger execution into the editor model.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Objects can be created, selected, saved, loaded, and rendered independently of tiles.

### ADA-P5-10-08 — Place Objects and Triggers — Refactor

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Place Objects and Triggers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/map_objects.ads, src/tools/object_tool.adb

Refactor the chapter implementation so Object models, shapes, hit testing, and custom data is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P5-10-09 — Place Objects and Triggers — Integrate

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Place Objects and Triggers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/map_objects.ads, src/tools/object_tool.adb

Integrate this chapter into the running final product so it works with earlier milestones: Place spawn points, pickups, enemies, exits, rectangles, points, and trigger regions on object layers.

**Completion checks**

- Objects can be created, selected, saved, loaded, and rendered independently of tiles.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P5-10-10 — Place Objects and Triggers — Review

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Place Objects and Triggers
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/map_objects.ads, src/tools/object_tool.adb

Perform a senior-style checkpoint review of Place Objects and Triggers in Forge Map Editor.

**Completion checks**

- Objects can be created, selected, saved, loaded, and rendered independently of tiles.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P5-11-01 — Select and Manipulate Content — Question

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Select and Manipulate Content
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/selection.ads, src/tools/selection_tool.adb

Answer one focused question before editing code: How should Selection models, hit testing, drag/resize, and multi-selection be used to accomplish this milestone: Select tiles or objects, draw selection outlines, move objects, and delete selected content.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P5-11-02 — Select and Manipulate Content — Code Reading

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Select and Manipulate Content
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/selection.ads, src/tools/selection_tool.adb

Read the current implementation around src/model/selection.ads, src/tools/selection_tool.adb. Trace how data enters, changes, and leaves the code for this milestone: Select tiles or objects, draw selection outlines, move objects, and delete selected content.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P5-11-03 — Select and Manipulate Content — Predict

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Select and Manipulate Content
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/selection.ads, src/tools/selection_tool.adb

Predict the exact behavior if the implementation encounters this problem: Selection referring to deleted objects or drag operations bypassing undo.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P5-11-04 — Select and Manipulate Content — Implement

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Select and Manipulate Content
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/selection.ads, src/tools/selection_tool.adb

Implement the core milestone in the existing forge_map_editor crate: Select tiles or objects, draw selection outlines, move objects, and delete selected content.

**Completion checks**

- Selection remains valid after edits and manipulation is undoable.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P5-11-05 — Select and Manipulate Content — Extend

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Select and Manipulate Content
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/selection.ads, src/tools/selection_tool.adb

Extend the completed milestone with this practical variation: Add multi-selection and snap-to-grid toggling.

**Completion checks**

- Selection remains valid after edits and manipulation is undoable.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P5-11-06 — Select and Manipulate Content — Test

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Select and Manipulate Content
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/selection.ads, src/tools/selection_tool.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Select tiles or objects, draw selection outlines, move objects, and delete selected content.

**Completion checks**

- Selection remains valid after edits and manipulation is undoable.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P5-11-07 — Select and Manipulate Content — Repair

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Select and Manipulate Content
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/selection.ads, src/tools/selection_tool.adb

Reproduce and repair this defect class in the current project: Selection referring to deleted objects or drag operations bypassing undo.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Selection remains valid after edits and manipulation is undoable.

### ADA-P5-11-08 — Select and Manipulate Content — Refactor

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Select and Manipulate Content
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/selection.ads, src/tools/selection_tool.adb

Refactor the chapter implementation so Selection models, hit testing, drag/resize, and multi-selection is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P5-11-09 — Select and Manipulate Content — Integrate

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Select and Manipulate Content
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/selection.ads, src/tools/selection_tool.adb

Integrate this chapter into the running final product so it works with earlier milestones: Select tiles or objects, draw selection outlines, move objects, and delete selected content.

**Completion checks**

- Selection remains valid after edits and manipulation is undoable.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P5-11-10 — Select and Manipulate Content — Review

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Select and Manipulate Content
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/model/selection.ads, src/tools/selection_tool.adb

Perform a senior-style checkpoint review of Select and Manipulate Content in Forge Map Editor.

**Completion checks**

- Selection remains valid after edits and manipulation is undoable.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P5-12-01 — Build the Properties Inspector — Question

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Properties Inspector
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/properties_panel.ads, src/ui/property_editors.adb

Answer one focused question before editing code: How should Forms, widget binding, validation, and context-sensitive panels be used to accomplish this milestone: Display and edit properties for map, layer, tile selection, or object selection.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P5-12-02 — Build the Properties Inspector — Code Reading

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Properties Inspector
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/properties_panel.ads, src/ui/property_editors.adb

Read the current implementation around src/ui/properties_panel.ads, src/ui/property_editors.adb. Trace how data enters, changes, and leaves the code for this milestone: Display and edit properties for map, layer, tile selection, or object selection.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P5-12-03 — Build the Properties Inspector — Predict

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Properties Inspector
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/properties_panel.ads, src/ui/property_editors.adb

Predict the exact behavior if the implementation encounters this problem: Updating the model on every invalid keystroke or creating callback feedback loops.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P5-12-04 — Build the Properties Inspector — Implement

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Properties Inspector
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/properties_panel.ads, src/ui/property_editors.adb

Implement the core milestone in the existing forge_map_editor crate: Display and edit properties for map, layer, tile selection, or object selection.

**Completion checks**

- The inspector changes context correctly and validates before committing.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P5-12-05 — Build the Properties Inspector — Extend

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Properties Inspector
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/properties_panel.ads, src/ui/property_editors.adb

Extend the completed milestone with this practical variation: Support multi-selection for shared properties where sensible.

**Completion checks**

- The inspector changes context correctly and validates before committing.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P5-12-06 — Build the Properties Inspector — Test

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Properties Inspector
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/properties_panel.ads, src/ui/property_editors.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Display and edit properties for map, layer, tile selection, or object selection.

**Completion checks**

- The inspector changes context correctly and validates before committing.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P5-12-07 — Build the Properties Inspector — Repair

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Properties Inspector
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/properties_panel.ads, src/ui/property_editors.adb

Reproduce and repair this defect class in the current project: Updating the model on every invalid keystroke or creating callback feedback loops.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- The inspector changes context correctly and validates before committing.

### ADA-P5-12-08 — Build the Properties Inspector — Refactor

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Properties Inspector
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/properties_panel.ads, src/ui/property_editors.adb

Refactor the chapter implementation so Forms, widget binding, validation, and context-sensitive panels is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P5-12-09 — Build the Properties Inspector — Integrate

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Properties Inspector
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/properties_panel.ads, src/ui/property_editors.adb

Integrate this chapter into the running final product so it works with earlier milestones: Display and edit properties for map, layer, tile selection, or object selection.

**Completion checks**

- The inspector changes context correctly and validates before committing.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P5-12-10 — Build the Properties Inspector — Review

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Build the Properties Inspector
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/properties_panel.ads, src/ui/property_editors.adb

Perform a senior-style checkpoint review of Build the Properties Inspector in Forge Map Editor.

**Completion checks**

- The inspector changes context correctly and validates before committing.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P5-13-01 — Implement Undo and Redo — Question

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Undo and Redo
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/commands/editor_commands.ads, src/commands/history.adb

Answer one focused question before editing code: How should Command pattern, reversible changes, stacks, and grouping be used to accomplish this milestone: Represent painting, object movement, property changes, and layer edits as reversible commands.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P5-13-02 — Implement Undo and Redo — Code Reading

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Undo and Redo
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/commands/editor_commands.ads, src/commands/history.adb

Read the current implementation around src/commands/editor_commands.ads, src/commands/history.adb. Trace how data enters, changes, and leaves the code for this milestone: Represent painting, object movement, property changes, and layer edits as reversible commands.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P5-13-03 — Implement Undo and Redo — Predict

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Undo and Redo
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/commands/editor_commands.ads, src/commands/history.adb

Predict the exact behavior if the implementation encounters this problem: Capturing mutable references instead of stable before/after data.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P5-13-04 — Implement Undo and Redo — Implement

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Undo and Redo
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/commands/editor_commands.ads, src/commands/history.adb

Implement the core milestone in the existing forge_map_editor crate: Represent painting, object movement, property changes, and layer edits as reversible commands.

**Completion checks**

- Mixed edits undo and redo in exact reverse order without corrupting selection.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P5-13-05 — Implement Undo and Redo — Extend

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Undo and Redo
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/commands/editor_commands.ads, src/commands/history.adb

Extend the completed milestone with this practical variation: Group drag/paint operations and cap history memory.

**Completion checks**

- Mixed edits undo and redo in exact reverse order without corrupting selection.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P5-13-06 — Implement Undo and Redo — Test

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Undo and Redo
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/commands/editor_commands.ads, src/commands/history.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Represent painting, object movement, property changes, and layer edits as reversible commands.

**Completion checks**

- Mixed edits undo and redo in exact reverse order without corrupting selection.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P5-13-07 — Implement Undo and Redo — Repair

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Undo and Redo
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/commands/editor_commands.ads, src/commands/history.adb

Reproduce and repair this defect class in the current project: Capturing mutable references instead of stable before/after data.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Mixed edits undo and redo in exact reverse order without corrupting selection.

### ADA-P5-13-08 — Implement Undo and Redo — Refactor

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Undo and Redo
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/commands/editor_commands.ads, src/commands/history.adb

Refactor the chapter implementation so Command pattern, reversible changes, stacks, and grouping is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P5-13-09 — Implement Undo and Redo — Integrate

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Undo and Redo
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/commands/editor_commands.ads, src/commands/history.adb

Integrate this chapter into the running final product so it works with earlier milestones: Represent painting, object movement, property changes, and layer edits as reversible commands.

**Completion checks**

- Mixed edits undo and redo in exact reverse order without corrupting selection.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P5-13-10 — Implement Undo and Redo — Review

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Implement Undo and Redo
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/commands/editor_commands.ads, src/commands/history.adb

Perform a senior-style checkpoint review of Implement Undo and Redo in Forge Map Editor.

**Completion checks**

- Mixed edits undo and redo in exact reverse order without corrupting selection.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P5-14-01 — Open, Save, and Export — Question

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Open, Save, and Export
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/file_dialogs.ads, src/adapters/editor_files.adb

Answer one focused question before editing code: How should Gtk file dialogs, recent files, serialization, and atomic writes be used to accomplish this milestone: Open and save editor documents plus export compatible map files for the games.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P5-14-02 — Open, Save, and Export — Code Reading

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Open, Save, and Export
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/file_dialogs.ads, src/adapters/editor_files.adb

Read the current implementation around src/ui/file_dialogs.ads, src/adapters/editor_files.adb. Trace how data enters, changes, and leaves the code for this milestone: Open and save editor documents plus export compatible map files for the games.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P5-14-03 — Open, Save, and Export — Predict

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Open, Save, and Export
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/file_dialogs.ads, src/adapters/editor_files.adb

Predict the exact behavior if the implementation encounters this problem: Writing directly over the only copy or marking clean before an atomic save succeeds.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P5-14-04 — Open, Save, and Export — Implement

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Open, Save, and Export
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/file_dialogs.ads, src/adapters/editor_files.adb

Implement the core milestone in the existing forge_map_editor crate: Open and save editor documents plus export compatible map files for the games.

**Completion checks**

- Cancel paths are safe and save-load-export round trips preserve supported data.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P5-14-05 — Open, Save, and Export — Extend

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Open, Save, and Export
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/file_dialogs.ads, src/adapters/editor_files.adb

Extend the completed milestone with this practical variation: Add recent files and Save As while keeping document identity clear.

**Completion checks**

- Cancel paths are safe and save-load-export round trips preserve supported data.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P5-14-06 — Open, Save, and Export — Test

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Open, Save, and Export
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/file_dialogs.ads, src/adapters/editor_files.adb

Create automated or repeatable tests that prove the milestone and its boundaries: Open and save editor documents plus export compatible map files for the games.

**Completion checks**

- Cancel paths are safe and save-load-export round trips preserve supported data.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P5-14-07 — Open, Save, and Export — Repair

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Open, Save, and Export
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/file_dialogs.ads, src/adapters/editor_files.adb

Reproduce and repair this defect class in the current project: Writing directly over the only copy or marking clean before an atomic save succeeds.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Cancel paths are safe and save-load-export round trips preserve supported data.

### ADA-P5-14-08 — Open, Save, and Export — Refactor

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Open, Save, and Export
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/file_dialogs.ads, src/adapters/editor_files.adb

Refactor the chapter implementation so Gtk file dialogs, recent files, serialization, and atomic writes is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P5-14-09 — Open, Save, and Export — Integrate

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Open, Save, and Export
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/file_dialogs.ads, src/adapters/editor_files.adb

Integrate this chapter into the running final product so it works with earlier milestones: Open and save editor documents plus export compatible map files for the games.

**Completion checks**

- Cancel paths are safe and save-load-export round trips preserve supported data.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P5-14-10 — Open, Save, and Export — Review

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Open, Save, and Export
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/file_dialogs.ads, src/adapters/editor_files.adb

Perform a senior-style checkpoint review of Open, Save, and Export in Forge Map Editor.

**Completion checks**

- Cancel paths are safe and save-load-export round trips preserve supported data.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P5-15-01 — Validate Maps and Show Errors — Question

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Validate Maps and Show Errors
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/validation/map_validator.ads, src/ui/diagnostics_panel.ads

Answer one focused question before editing code: How should Dialogs, list views, diagnostics, and navigation to errors be used to accomplish this milestone: Detect invalid borders, missing spawn, unreachable exits, bad properties, and overlapping critical objects.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P5-15-02 — Validate Maps and Show Errors — Code Reading

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Validate Maps and Show Errors
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/validation/map_validator.ads, src/ui/diagnostics_panel.ads

Read the current implementation around src/validation/map_validator.ads, src/ui/diagnostics_panel.ads. Trace how data enters, changes, and leaves the code for this milestone: Detect invalid borders, missing spawn, unreachable exits, bad properties, and overlapping critical objects.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P5-15-03 — Validate Maps and Show Errors — Predict

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Validate Maps and Show Errors
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/validation/map_validator.ads, src/ui/diagnostics_panel.ads

Predict the exact behavior if the implementation encounters this problem: Displaying only a generic error dialog or mutating the document during validation.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P5-15-04 — Validate Maps and Show Errors — Implement

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Validate Maps and Show Errors
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/validation/map_validator.ads, src/ui/diagnostics_panel.ads

Implement the core milestone in the existing forge_map_editor crate: Detect invalid borders, missing spawn, unreachable exits, bad properties, and overlapping critical objects.

**Completion checks**

- Each diagnostic includes severity, message, and navigable location.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P5-15-05 — Validate Maps and Show Errors — Extend

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Validate Maps and Show Errors
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/validation/map_validator.ads, src/ui/diagnostics_panel.ads

Extend the completed milestone with this practical variation: Show a diagnostics panel that selects the offending location.

**Completion checks**

- Each diagnostic includes severity, message, and navigable location.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P5-15-06 — Validate Maps and Show Errors — Test

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Validate Maps and Show Errors
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/validation/map_validator.ads, src/ui/diagnostics_panel.ads

Create automated or repeatable tests that prove the milestone and its boundaries: Detect invalid borders, missing spawn, unreachable exits, bad properties, and overlapping critical objects.

**Completion checks**

- Each diagnostic includes severity, message, and navigable location.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P5-15-07 — Validate Maps and Show Errors — Repair

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Validate Maps and Show Errors
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/validation/map_validator.ads, src/ui/diagnostics_panel.ads

Reproduce and repair this defect class in the current project: Displaying only a generic error dialog or mutating the document during validation.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- Each diagnostic includes severity, message, and navigable location.

### ADA-P5-15-08 — Validate Maps and Show Errors — Refactor

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Validate Maps and Show Errors
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/validation/map_validator.ads, src/ui/diagnostics_panel.ads

Refactor the chapter implementation so Dialogs, list views, diagnostics, and navigation to errors is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P5-15-09 — Validate Maps and Show Errors — Integrate

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Validate Maps and Show Errors
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/validation/map_validator.ads, src/ui/diagnostics_panel.ads

Integrate this chapter into the running final product so it works with earlier milestones: Detect invalid borders, missing spawn, unreachable exits, bad properties, and overlapping critical objects.

**Completion checks**

- Each diagnostic includes severity, message, and navigable location.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P5-15-10 — Validate Maps and Show Errors — Review

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Validate Maps and Show Errors
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/validation/map_validator.ads, src/ui/diagnostics_panel.ads

Perform a senior-style checkpoint review of Validate Maps and Show Errors in Forge Map Editor.

**Completion checks**

- Each diagnostic includes severity, message, and navigable location.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P5-16-01 — Autosave and Background Work — Question

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Autosave and Background Work
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/services/autosave.ads, src/services/background_jobs.ads

Answer one focused question before editing code: How should Gtk main loop, tasks, synchronization, and idle callbacks be used to accomplish this milestone: Autosave snapshots and run expensive validation without freezing the UI.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P5-16-02 — Autosave and Background Work — Code Reading

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Autosave and Background Work
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/services/autosave.ads, src/services/background_jobs.ads

Read the current implementation around src/services/autosave.ads, src/services/background_jobs.ads. Trace how data enters, changes, and leaves the code for this milestone: Autosave snapshots and run expensive validation without freezing the UI.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P5-16-03 — Autosave and Background Work — Predict

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Autosave and Background Work
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/services/autosave.ads, src/services/background_jobs.ads

Predict the exact behavior if the implementation encounters this problem: Touching Gtk widgets from a worker task or racing the active document.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P5-16-04 — Autosave and Background Work — Implement

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Autosave and Background Work
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/services/autosave.ads, src/services/background_jobs.ads

Implement the core milestone in the existing forge_map_editor crate: Autosave snapshots and run expensive validation without freezing the UI.

**Completion checks**

- The UI remains responsive and worker results return through a safe main-loop handoff.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P5-16-05 — Autosave and Background Work — Extend

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Autosave and Background Work
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/services/autosave.ads, src/services/background_jobs.ads

Extend the completed milestone with this practical variation: Report progress and allow safe cancellation of long operations.

**Completion checks**

- The UI remains responsive and worker results return through a safe main-loop handoff.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P5-16-06 — Autosave and Background Work — Test

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Autosave and Background Work
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/services/autosave.ads, src/services/background_jobs.ads

Create automated or repeatable tests that prove the milestone and its boundaries: Autosave snapshots and run expensive validation without freezing the UI.

**Completion checks**

- The UI remains responsive and worker results return through a safe main-loop handoff.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P5-16-07 — Autosave and Background Work — Repair

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Autosave and Background Work
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/services/autosave.ads, src/services/background_jobs.ads

Reproduce and repair this defect class in the current project: Touching Gtk widgets from a worker task or racing the active document.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- The UI remains responsive and worker results return through a safe main-loop handoff.

### ADA-P5-16-08 — Autosave and Background Work — Refactor

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Autosave and Background Work
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/services/autosave.ads, src/services/background_jobs.ads

Refactor the chapter implementation so Gtk main loop, tasks, synchronization, and idle callbacks is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P5-16-09 — Autosave and Background Work — Integrate

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Autosave and Background Work
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/services/autosave.ads, src/services/background_jobs.ads

Integrate this chapter into the running final product so it works with earlier milestones: Autosave snapshots and run expensive validation without freezing the UI.

**Completion checks**

- The UI remains responsive and worker results return through a safe main-loop handoff.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P5-16-10 — Autosave and Background Work — Review

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Autosave and Background Work
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/services/autosave.ads, src/services/background_jobs.ads

Perform a senior-style checkpoint review of Autosave and Background Work in Forge Map Editor.

**Completion checks**

- The UI remains responsive and worker results return through a safe main-loop handoff.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P5-17-01 — Custom Widgets and Visual Polish — Question

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Custom Widgets and Visual Polish
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/widgets/, ui/main_window.ui, ui/editor.css

Answer one focused question before editing code: How should Widget composition, Gtk.Builder, CSS themes, and reusable controls be used to accomplish this milestone: Create at least one reusable custom composite widget and load part of the UI through Gtk.Builder or Glade XML.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P5-17-02 — Custom Widgets and Visual Polish — Code Reading

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Custom Widgets and Visual Polish
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/widgets/, ui/main_window.ui, ui/editor.css

Read the current implementation around src/ui/widgets/, ui/main_window.ui, ui/editor.css. Trace how data enters, changes, and leaves the code for this milestone: Create at least one reusable custom composite widget and load part of the UI through Gtk.Builder or Glade XML.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P5-17-03 — Custom Widgets and Visual Polish — Predict

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Custom Widgets and Visual Polish
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/widgets/, ui/main_window.ui, ui/editor.css

Predict the exact behavior if the implementation encounters this problem: Using old examples blindly or embedding all UI in one generated file.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P5-17-04 — Custom Widgets and Visual Polish — Implement

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Custom Widgets and Visual Polish
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/widgets/, ui/main_window.ui, ui/editor.css

Implement the core milestone in the existing forge_map_editor crate: Create at least one reusable custom composite widget and load part of the UI through Gtk.Builder or Glade XML.

**Completion checks**

- The custom widget has a focused API and Builder-loaded signals connect reliably.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P5-17-05 — Custom Widgets and Visual Polish — Extend

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Custom Widgets and Visual Polish
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/widgets/, ui/main_window.ui, ui/editor.css

Extend the completed milestone with this practical variation: Add theme-aware styling, icons, tooltips, and status feedback.

**Completion checks**

- The custom widget has a focused API and Builder-loaded signals connect reliably.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P5-17-06 — Custom Widgets and Visual Polish — Test

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Custom Widgets and Visual Polish
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/widgets/, ui/main_window.ui, ui/editor.css

Create automated or repeatable tests that prove the milestone and its boundaries: Create at least one reusable custom composite widget and load part of the UI through Gtk.Builder or Glade XML.

**Completion checks**

- The custom widget has a focused API and Builder-loaded signals connect reliably.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P5-17-07 — Custom Widgets and Visual Polish — Repair

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Custom Widgets and Visual Polish
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/widgets/, ui/main_window.ui, ui/editor.css

Reproduce and repair this defect class in the current project: Using old examples blindly or embedding all UI in one generated file.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- The custom widget has a focused API and Builder-loaded signals connect reliably.

### ADA-P5-17-08 — Custom Widgets and Visual Polish — Refactor

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Custom Widgets and Visual Polish
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/widgets/, ui/main_window.ui, ui/editor.css

Refactor the chapter implementation so Widget composition, Gtk.Builder, CSS themes, and reusable controls is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P5-17-09 — Custom Widgets and Visual Polish — Integrate

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Custom Widgets and Visual Polish
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/widgets/, ui/main_window.ui, ui/editor.css

Integrate this chapter into the running final product so it works with earlier milestones: Create at least one reusable custom composite widget and load part of the UI through Gtk.Builder or Glade XML.

**Completion checks**

- The custom widget has a focused API and Builder-loaded signals connect reliably.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P5-17-10 — Custom Widgets and Visual Polish — Review

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Custom Widgets and Visual Polish
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** src/ui/widgets/, ui/main_window.ui, ui/editor.css

Perform a senior-style checkpoint review of Custom Widgets and Visual Polish in Forge Map Editor.

**Completion checks**

- The custom widget has a focused API and Builder-loaded signals connect reliably.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

### ADA-P5-18-01 — Finish Forge Map Editor — Question

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Finish Forge Map Editor
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** tests/, README.md, docs/user_guide.md, CHANGELOG.md

Answer one focused question before editing code: How should End-to-end integration, usability testing, packaging, and documentation be used to accomplish this milestone: Complete the editor workflow, sample maps, tests, keyboard reference, recovery behavior, and release packaging.

**Completion checks**

- The answer explains the concept in your own words.
- The answer connects the concept to a concrete package or data boundary.
- The answer identifies a plausible failure and how the design prevents it.

### ADA-P5-18-02 — Finish Forge Map Editor — Code Reading

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Finish Forge Map Editor
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** tests/, README.md, docs/user_guide.md, CHANGELOG.md

Read the current implementation around tests/, README.md, docs/user_guide.md, CHANGELOG.md. Trace how data enters, changes, and leaves the code for this milestone: Complete the editor workflow, sample maps, tests, keyboard reference, recovery behavior, and release packaging.

**Completion checks**

- The trace names actual packages and operations.
- The trace separates domain logic from I/O or framework adapters.
- At least one improvement or confirmed good design choice is justified.

### ADA-P5-18-03 — Finish Forge Map Editor — Predict

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Finish Forge Map Editor
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** tests/, README.md, docs/user_guide.md, CHANGELOG.md

Predict the exact behavior if the implementation encounters this problem: Adding endless professional-editor features before the core workflow is reliable.

**Completion checks**

- The prediction includes output, state change, exception, or compile-time result.
- The experiment changes one relevant factor.
- The final explanation identifies the Ada rule or architecture decision involved.

### ADA-P5-18-04 — Finish Forge Map Editor — Implement

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Finish Forge Map Editor
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** tests/, README.md, docs/user_guide.md, CHANGELOG.md

Implement the core milestone in the existing forge_map_editor crate: Complete the editor workflow, sample maps, tests, keyboard reference, recovery behavior, and release packaging.

**Completion checks**

- A fresh clone builds, opens, edits, validates, saves, exports, and reopens a playable map.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The implementation uses deliberate Ada types rather than raw primitive values where the domain differs.
- The main procedure remains orchestration rather than absorbing the implementation.

### ADA-P5-18-05 — Finish Forge Map Editor — Extend

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Finish Forge Map Editor
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** tests/, README.md, docs/user_guide.md, CHANGELOG.md

Extend the completed milestone with this practical variation: Open a map created by the editor in both game projects and document compatibility limits.

**Completion checks**

- A fresh clone builds, opens, edits, validates, saves, exports, and reopens a playable map.
- The project still builds from its existing Alire crate; no new crate is created for this quest.
- Record what changed and why in your quest answer or engineering notes.
- The extension does not duplicate the original implementation unnecessarily.
- Existing behavior still passes its checks.

### ADA-P5-18-06 — Finish Forge Map Editor — Test

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Finish Forge Map Editor
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** tests/, README.md, docs/user_guide.md, CHANGELOG.md

Create automated or repeatable tests that prove the milestone and its boundaries: Complete the editor workflow, sample maps, tests, keyboard reference, recovery behavior, and release packaging.

**Completion checks**

- A fresh clone builds, opens, edits, validates, saves, exports, and reopens a playable map.
- A failing implementation would cause at least one test or check to fail.
- Tests are named by behavior rather than by implementation function number.
- The test output is repeatable.

### ADA-P5-18-07 — Finish Forge Map Editor — Repair

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Finish Forge Map Editor
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** tests/, README.md, docs/user_guide.md, CHANGELOG.md

Reproduce and repair this defect class in the current project: Adding endless professional-editor features before the core workflow is reliable.

**Completion checks**

- The defect is reproduced before the fix.
- The repair is located at the correct ownership or validation boundary.
- The regression check remains after the repair.
- A fresh clone builds, opens, edits, validates, saves, exports, and reopens a playable map.

### ADA-P5-18-08 — Finish Forge Map Editor — Refactor

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Finish Forge Map Editor
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** tests/, README.md, docs/user_guide.md, CHANGELOG.md

Refactor the chapter implementation so End-to-end integration, usability testing, packaging, and documentation is clearer without changing behavior.

**Completion checks**

- Behavior and external file formats remain unchanged unless explicitly documented.
- Package responsibilities and names are clearer after the change.
- Tests pass before and after the refactor.
- The answer explains why the new design is easier to maintain.

### ADA-P5-18-09 — Finish Forge Map Editor — Integrate

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Finish Forge Map Editor
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** tests/, README.md, docs/user_guide.md, CHANGELOG.md

Integrate this chapter into the running final product so it works with earlier milestones: Complete the editor workflow, sample maps, tests, keyboard reference, recovery behavior, and release packaging.

**Completion checks**

- A fresh clone builds, opens, edits, validates, saves, exports, and reopens a playable map.
- The feature is reachable through the normal program workflow.
- At least one prior feature still works in the same run.
- No new crate or duplicate application entry point was created.

### ADA-P5-18-10 — Finish Forge Map Editor — Review

- **Project:** Project 5 — Forge Map Editor
- **Chapter:** Finish Forge Map Editor
- **Workspace:** `~/Documents/src/projects/ada-mastery/forge_map_editor`
- **Files:** tests/, README.md, docs/user_guide.md, CHANGELOG.md

Perform a senior-style checkpoint review of Finish Forge Map Editor in Forge Map Editor.

**Completion checks**

- A fresh clone builds, opens, edits, validates, saves, exports, and reopens a playable map.
- The review cites actual files and code decisions.
- The review distinguishes correctness problems from style preferences.
- The checkpoint leaves the project building and tests passing.

