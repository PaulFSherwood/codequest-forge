# Dungeon Walk Curriculum Index

One Alire project, 22 milestones, 132 quests.

| # | Milestone | Ada concept | Final checkpoint |
|---:|---|---|---|
| 1 | Create the Alire Project Correctly | Alire workspace creation and project layout | The current directory contains alire.toml and src/dungeon_walk.adb. |
| 2 | Build, Run, and Edit the Generated Program | Compilation cycle and Ada procedure structure | Dungeon Walk
You wake inside a silent ship. |
| 3 | Import Text I/O and Read Ada Declarations | with clauses, use clauses, declarations, and begin/end | The program builds both with fully qualified calls and with the use clause. |
| 4 | Add Screen Settings and Player State | constants, variables, Positive, Float, Boolean, and Character | The program still builds, and the new declarations exist before begin. |
| 5 | Create the Main Input Loop | while loops, immediate character input, and case statements | The program reacts to W/A/S/D and exits when Q is pressed without requiring Enter. |
| 6 | Model the Ship Map with a Subtype and Array | String constraints, subtypes, arrays, and multidimensional indexing | Changing any row from 16 characters to 15 causes compilation to fail; restoring it succeeds. |
| 7 | Print the Top-Down Map with a Procedure | procedures, for loops, array attributes, and parameters | All 16 map rows appear in the terminal before command input begins. |
| 8 | Create an Off-Screen Character Buffer | arrays of constrained strings and mutable aggregate state | The terminal displays exactly Screen_Height rows, each containing Screen_Width assigned characters. |
| 9 | Fill Ceiling and Floor with Nested Loops | nested iteration, conditions, and array assignment | The upper portion of the frame is blank and the lower portion is dotted. |
| 10 | Write Is_Wall Safely | functions, return values, short-circuit Boolean logic, conversion, and bounds | Wall coordinates return TRUE, floor coordinates return FALSE, and outside coordinates return TRUE without crashing. |
| 11 | Use Floating-Point Player Coordinates | Float state, assignments, and tile versus world coordinates | Repeated W input shows fractional positions changing by approximately 0.35. |
| 12 | Turn with Radians and Compute Direction | Ada.Numerics, elementary functions, radians, Sin, and Cos | A and D update the direction components smoothly and in opposite directions. |
| 13 | Move Forward, Backward, and Slide Along Walls | procedure parameters, local constants, collision checks, and state mutation | W and S move smoothly, the player cannot cross '#', and movement can slide along an open axis. |
| 14 | Choose a Directional Minimap Symbol | functions without parameters, local constants, abs, nested conditions | Turning through a full circle eventually produces all four arrow symbols. |
| 15 | Draw the Map into the Screen Buffer | coordinate translation, nested loops, overlays, and constant local indexes | A 16 by 16 minimap appears near the right edge with an arrow at the player's tile. |
| 16 | Cast One Ray Until It Reaches a Wall | incremental search loops, direction vectors, and exit conditions | The reported distance changes as the player turns or moves. |
| 17 | Cast a Different Ray for Every Screen Column | linear interpolation, field of view, loop indexes, and Float conversion | The program computes 80 wall distances spanning a 60-degree field of view. |
| 18 | Project Wall Distance into Vertical Slices | perspective projection, numeric conversion, clamping, and ranges | Vertical wall slices now form a recognizable first-person corridor. |
| 19 | Shade Walls and Correct Fish-Eye Distortion | piecewise functions and perpendicular-distance correction | Nearby walls use heavy symbols, distant walls use lighter symbols, and flat walls no longer bow outward. |
| 20 | Assemble the Render Pipeline | procedure composition, deterministic ordering, and status overlays | Each key press redraws one complete frame containing background, walls, minimap, and controls. |
| 21 | Complete and Verify the Monolithic Ray-Caster | integration, behavior verification, and controlled shutdown | The terminal displays a playable first-person map; W/S move, A/D turn, Q exits, and walls block movement. |
| 22 | Refactor the Working Program into Introductory Packages | package specifications, package bodies, encapsulation, and dependency boundaries | The refactored project behaves identically, and dungeon_walk.adb becomes a short orchestration procedure. |
