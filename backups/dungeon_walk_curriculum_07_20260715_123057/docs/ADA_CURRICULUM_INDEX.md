# Ada Project Curriculum Index

- Projects: **5**
- Chapters: **102**
- Quests: **1020**

## Project 1 — Dungeon Walk

Build a terminal-rendered, Doom-style 3D dungeon that loads maps and lets the player walk through rooms and corridors.

Workspace: `~/Documents/src/projects/ada-mastery/dungeon_walk`

Final product: A tested terminal raycaster with map loading, movement, collision, doors, simple entities, save/load, and release documentation.

1. Create the Alire Workspace — Alire crates and build workflow
2. Terminal Output and Player Commands — Ada.Text_IO and basic input
3. Variables, Constants, and Game State — Variables, constants, assignment, and scope
4. Constrain Coordinates and Angles — Scalar types, subtypes, ranges, and conversions
5. Model Directions and Tiles — Enumeration types, attributes, and case statements
6. Build the Main Game Loop — loop, while, for, exit, and iteration invariants
7. Move Behavior into Procedures — Procedures and in/out/in out modes
8. Compute Instead of Mutate — Functions, return types, expression functions, and purity
9. Separate the Dungeon into Packages — Package specifications, bodies, visibility, with, and use type
10. Represent the Player and Camera — Records, aggregates, defaults, and nested records
11. Create the Map Grid — Constrained and unconstrained arrays
12. Protect Map Invariants — Private types, constructors, selectors, and invariants
13. Parse Commands Reliably — String slices, fixed strings, unbounded strings, and character handling
14. Contain Errors at Boundaries — Exception declarations, handlers, propagation, and cleanup
15. Load Maps from Disk — Text file input/output and resource management
16. Validate the Map Format — Parsing, validation passes, and error reporting
17. Add Vector Mathematics — Floating-point types, vectors, operators, and numeric packages
18. Turn the Camera — Ada.Numerics, trigonometry, modular angles, and precision
19. Generate One Ray per Screen Column — Interpolation, coordinate transforms, and functions over ranges
20. Find Walls with DDA — Algorithmic loops, step selection, and termination
21. Render the Pseudo-3D View — Formatting, nested loops, buffers, and separation of model/view
22. Move Through the Dungeon Safely — State transitions, collision detection, and boundary checks
23. Doors, Pickups, and Save Data — Variant records, collections, and persistence
24. Finish Dungeon Walk — AUnit, assertions, documentation, profiling, and release discipline

## Project 2 — Mission Systems Simulator

Build a deterministic avionics-style mission simulator with typed messages, scheduled components, concurrency, fault injection, networking, and tests.

Workspace: `~/Documents/src/projects/ada-mastery/mission_sim`

Final product: A deterministic multi-component simulation with contracts, tasking, protected state, serialization, external interfaces, fault scenarios, and engineering documentation.

1. Define the Simulator Architecture — Layered architecture and GPR/Alire organization
2. Create Strong Physical Units — Derived numeric types, private types, and unit-safe APIs
3. Model Bus Messages — Discriminated records and variant parts
4. Define Replaceable Components — Tagged types, interfaces, dispatching, and composition
5. Build Reusable Typed Utilities — Generic packages and formal parameters
6. Manage Components and Events — Ada.Containers vectors, maps, sets, and iteration
7. Control Dynamic Lifetime — Access types, accessibility, aliased objects, and ownership boundaries
8. Manage Resources Safely — Controlled and limited controlled types
9. State Contracts Explicitly — Preconditions, postconditions, predicates, invariants, and assertions
10. Design Error and Logging Boundaries — Exception taxonomy, logging levels, and fault containment
11. Load Typed Configuration — Configuration parsing, defaults, validation, and immutable startup state
12. Serialize Messages and State — Streams, attributes, representation, and versioned formats
13. Introduce Active Components — Tasks, task types, activation, termination, and ownership
14. Protect Shared Runtime State — Protected objects, protected functions, procedures, and entries
15. Coordinate with Entries and Select — Rendezvous, entry guards, selective accept, and asynchronous transfer concepts
16. Use Real-Time Timing Correctly — Ada.Real_Time, Time_Span, delay until, priorities, and drift
17. Build a Deterministic Scheduler — Logical time, ordering, fixed steps, and reproducibility
18. Schedule Events and Inject Faults — Priority queues, state machines, and scenario execution
19. Expose a Network Adapter — Sockets, framing, partial reads, timeouts, and adapter isolation
20. Wrap a C Interface Safely — Interfaces.C, Convention, import/export, pointers, and representation clauses
21. Test and Analyze the Simulator — AUnit, property-style tests, SPARK boundaries, and static analysis
22. Profile and Release Mission Sim — Performance measurement, diagnostics, compatibility, and release engineering

## Project 3 — Rescue Run SDL

Build a compact top-down rescue game using SDLada and the map ideas learned in Dungeon Walk.

Workspace: `~/Documents/src/projects/ada-mastery/rescue_run_sdl`

Final product: A polished top-down game with maps, camera, animation, enemies, objectives, audio, configuration, tests, and a release build.

1. Open an SDL Window — SDLada dependency and lifecycle
2. Draw Basic Shapes — Renderers, colors, coordinates, and resource wrappers
3. Process SDL Events — Event unions, polling loops, and quit behavior
4. Create an Input Abstraction — State versus events and command mapping
5. Use a Fixed Update Step — Frame time, accumulator loops, and interpolation
6. Move the Player — Vectors, velocity, acceleration, and input response
7. Reuse the Map Format — Data adapters and shared format concepts
8. Render Tile Maps — Nested iteration, clipping, and tile lookup
9. Follow the Player with a Camera — World-to-screen transforms and clamping
10. Resolve Tile Collision — Bounding boxes, swept movement, and axis separation
11. Load and Manage Textures — SDL_image, ownership, caching, and failure fallback
12. Animate the Player — Sprite sheets, frame timing, and state machines
13. Add Enemy Behavior — Finite-state machines and steering
14. Add Attacks and Projectiles — Object lifetime, collision queries, and cooldowns
15. Build Rescue Objectives — Collections, triggers, and game rules
16. Create a HUD — SDL_ttf, formatting, and view models
17. Add Sound and Music — SDL_mixer, channels, resource policy, and events
18. Organize Game States — State pattern, pause, menus, and transitions
19. Load Settings and Save Progress — Configuration, save data, and compatibility
20. Finish Rescue Run SDL — Integration tests, performance, packaging, and release polish

## Project 4 — Rescue Run ECS Conversion

Rebuild the SDL game in controlled stages as a data-oriented ECS while preserving behavior.

Workspace: `~/Documents/src/projects/ada-mastery/rescue_run_ecs`

Final product: An ECS-based version of Rescue Run with deterministic systems, data-driven entities, tests, profiling, and a documented migration.

1. Plan the ECS Migration — Architecture assessment and behavior baselines
2. Create Stable Entity IDs — Opaque identifiers, generations, and lifecycle
3. Define Plain Components — Data-oriented records and component boundaries
4. Build Component Stores — Generics, sparse/dense storage, and membership
5. Create the World API — Encapsulation, composition, and entity construction
6. Define System Phases — System interfaces, ordering, and dependencies
7. Query Matching Entities — Component signatures and iteration joins
8. Defer Structural Changes — Command buffers and safe mutation phases
9. Create an ECS Event Stream — Typed events, buffering, and decoupling
10. Migrate Movement — Pure systems and component transforms
11. Migrate Rendering — Read-only systems and adapter boundaries
12. Migrate Collision — Broad phase, narrow phase, and event generation
13. Migrate Animation — Component state and time-driven systems
14. Migrate Enemy AI — State components, decision systems, and navigation data
15. Serialize ECS Worlds — Stable IDs, component schemas, and versioning
16. Measure Data-Oriented Performance — Profiling, cache behavior, allocations, and complexity
17. Test and Debug the ECS — System isolation, world fixtures, invariants, and debug views
18. Complete the ECS Conversion — Migration completion, architecture review, and release comparison

## Project 5 — Forge Map Editor

Build a useful GtkAda map editor for the Dungeon Walk and Rescue Run map formats, inspired by proven map-editor workflows without copying a full professional editor.

Workspace: `~/Documents/src/projects/ada-mastery/forge_map_editor`

Final product: A desktop editor with a central map canvas, palette, layers, objects, properties, shortcuts, undo/redo, validation, autosave, and export.

1. Create the GtkAda Application — GtkAda dependency, initialization, application/window lifecycle
2. Build the Editor Shell — Hierarchical widget composition and containers
3. Menus, Actions, and Shortcuts — Gtk actions, menus, accelerators, and command routing
4. Separate the Document Model — Model-view separation, observable state, and domain APIs
5. Draw the Map Canvas — Gtk.Drawing_Area, Cairo, expose/draw callbacks, and coordinate transforms
6. Pan, Zoom, and Pointer Input — Signals, event masks, gestures, and viewport math
7. Create the Tile Palette — Lists, icon views, selection models, and reusable widgets
8. Implement Map Painting Tools — Mouse signals, tools, drag operations, and model updates
9. Add Layers — Tree/list models, visibility, locking, ordering, and composition
10. Place Objects and Triggers — Object models, shapes, hit testing, and custom data
11. Select and Manipulate Content — Selection models, hit testing, drag/resize, and multi-selection
12. Build the Properties Inspector — Forms, widget binding, validation, and context-sensitive panels
13. Implement Undo and Redo — Command pattern, reversible changes, stacks, and grouping
14. Open, Save, and Export — Gtk file dialogs, recent files, serialization, and atomic writes
15. Validate Maps and Show Errors — Dialogs, list views, diagnostics, and navigation to errors
16. Autosave and Background Work — Gtk main loop, tasks, synchronization, and idle callbacks
17. Custom Widgets and Visual Polish — Widget composition, Gtk.Builder, CSS themes, and reusable controls
18. Finish Forge Map Editor — End-to-end integration, usability testing, packaging, and documentation

