# Ada Dungeon Walk — Concrete Intro Path

This curriculum uses one Alire crate for the entire Intro Ada path.

## Permanent workspace

```bash
mkdir -p ~/Documents/src/projects/ada-mastery/dungeon_walk
cd ~/Documents/src/projects/ada-mastery/dungeon_walk
alr init --bin --in-place dungeon_walk
```

- **Milestones:** 22
- **Quests:** 132
- **Quest rhythm:** Orientation → Question → Build → Predict → Repair → Checkpoint
- **Final result:** playable terminal ray-caster, then an introductory package refactor

## Why this replaces the prior Intro path

Every quest now names the exact next action, the files involved, the expected result, and an answer guide. No Intro quest creates another Alire crate.

## Milestones

### 1. Create the Alire Project Correctly

**Ada focus:** Alire workspace creation and project layout

**Goal:** Create one long-lived dungeon_walk binary crate in the directory where all Intro Ada quests will be completed.

**Primary files:** `alire.toml`, `src/dungeon_walk.adb`

**Expected checkpoint:** The current directory contains alire.toml and src/dungeon_walk.adb.

**Build steps:**
1. Create the parent ada-mastery directory if it does not exist.
1. Create and enter the dungeon_walk directory.
1. Run the exact Alire initialization command.
1. List the generated files and open src/dungeon_walk.adb.

### 2. Build, Run, and Edit the Generated Program

**Ada focus:** Compilation cycle and Ada procedure structure

**Goal:** Understand the generated main procedure and complete the edit-build-run cycle.

**Primary files:** `src/dungeon_walk.adb`, `alire.toml`

**Expected checkpoint:** Dungeon Walk
You wake inside a silent ship.

**Build steps:**
1. Replace the generated message with a Dungeon Walk title.
1. Build from the crate root.
1. Run the executable.
1. Change the message once more and confirm Alire rebuilds the changed source.

### 3. Import Text I/O and Read Ada Declarations

**Ada focus:** with clauses, use clauses, declarations, and begin/end

**Goal:** Understand the basic regions of an Ada procedure and why Text_IO is visible.

**Primary files:** `src/dungeon_walk.adb`

**Expected checkpoint:** The program builds both with fully qualified calls and with the use clause.

**Build steps:**
1. Remove `use Ada.Text_IO;` temporarily.
1. Qualify both output calls with Ada.Text_IO.
1. Build and run.
1. Restore the use clause and the shorter calls.

### 4. Add Screen Settings and Player State

**Ada focus:** constants, variables, Positive, Float, Boolean, and Character

**Goal:** Declare immutable configuration separately from mutable game state.

**Primary files:** `src/dungeon_walk.adb`

**Expected checkpoint:** The program still builds, and the new declarations exist before begin.

**Build steps:**
1. Add screen width and height constants.
1. Add Player_X, Player_Y, Player_Angle, Running, and Key declarations.
1. Print the screen dimensions using the Image attribute.
1. Build before adding any game loop.

### 5. Create the Main Input Loop

**Ada focus:** while loops, immediate character input, and case statements

**Goal:** Keep the program running, read one key at a time, and exit cleanly with Q.

**Primary files:** `src/dungeon_walk.adb`

**Expected checkpoint:** The program reacts to W/A/S/D and exits when Q is pressed without requiring Enter.

**Build steps:**
1. Print a short control prompt inside the loop.
1. Read Key using Get_Immediate.
1. Add Q/q to set Running False.
1. Add W/w, A/a, S/s, and D/d branches that currently print their action.
1. Ignore all other keys.

### 6. Model the Ship Map with a Subtype and Array

**Ada focus:** String constraints, subtypes, arrays, and multidimensional indexing

**Goal:** Represent a fixed 16 by 16 map so incorrect row lengths are rejected.

**Primary files:** `src/dungeon_walk.adb`

**Expected checkpoint:** Changing any row from 16 characters to 15 causes compilation to fail; restoring it succeeds.

**Build steps:**
1. Add Map_Width and Map_Height constants.
1. Declare Map_Row and Map_Array.
1. Copy the supplied Ship_Map constant.
1. Build and intentionally shorten one row to observe the compiler error, then restore it.

### 7. Print the Top-Down Map with a Procedure

**Ada focus:** procedures, for loops, array attributes, and parameters

**Goal:** Write a reusable procedure that displays every map row.

**Primary files:** `src/dungeon_walk.adb`

**Expected checkpoint:** All 16 map rows appear in the terminal before command input begins.

**Build steps:**
1. Create a nested procedure named Draw_Map before the main begin.
1. Loop through Ship_Map'Range.
1. Print each complete row with Put_Line.
1. Call Draw_Map once before the input loop.

### 8. Create an Off-Screen Character Buffer

**Ada focus:** arrays of constrained strings and mutable aggregate state

**Goal:** Store a complete 80 by 24 terminal image before printing it.

**Primary files:** `src/dungeon_walk.adb`

**Expected checkpoint:** The terminal displays exactly Screen_Height rows, each containing Screen_Width assigned characters.

**Build steps:**
1. Declare Screen_Array using Screen_Height and Screen_Width.
1. Declare the mutable Screen object.
1. Temporarily fill every element with a single character using nested loops.
1. Print each row to verify the complete buffer.

### 9. Fill Ceiling and Floor with Nested Loops

**Ada focus:** nested iteration, conditions, and array assignment

**Goal:** Initialize every frame with blank ceiling and dotted floor.

**Primary files:** `src/dungeon_walk.adb`

**Expected checkpoint:** The upper portion of the frame is blank and the lower portion is dotted.

**Build steps:**
1. Create Fill_Background.
1. Use Screen'Range for rows and Screen(Row)'Range for columns.
1. Assign a space above the midpoint and a dot at or below it.
1. Call it before printing Screen.

### 10. Write Is_Wall Safely

**Ada focus:** functions, return values, short-circuit Boolean logic, conversion, and bounds

**Goal:** Convert world coordinates to map indexes without ever indexing outside the map.

**Primary files:** `src/dungeon_walk.adb`

**Expected checkpoint:** Wall coordinates return TRUE, floor coordinates return FALSE, and outside coordinates return TRUE without crashing.

**Build steps:**
1. Add local constants Map_X and Map_Y using Float'Floor.
1. Return True when either coordinate is outside the map.
1. Otherwise compare the selected map Character with '#'.
1. Call the function for one wall coordinate and one floor coordinate and print the Boolean results.

### 11. Use Floating-Point Player Coordinates

**Ada focus:** Float state, assignments, and tile versus world coordinates

**Goal:** Allow the player to occupy positions between map tile centers.

**Primary files:** `src/dungeon_walk.adb`

**Expected checkpoint:** Repeated W input shows fractional positions changing by approximately 0.35.

**Build steps:**
1. Initialize Player_X and Player_Y to 2.5.
1. Print the current values with Float'Image.
1. Temporarily add 0.35 to Player_X when W is pressed.
1. Confirm repeated input changes the position without whole-tile jumps.

### 12. Turn with Radians and Compute Direction

**Ada focus:** Ada.Numerics, elementary functions, radians, Sin, and Cos

**Goal:** Represent facing direction with an angle and convert it into X/Y direction components.

**Primary files:** `src/dungeon_walk.adb`

**Expected checkpoint:** A and D update the direction components smoothly and in opposite directions.

**Build steps:**
1. Add the Ada.Numerics and Elementary_Functions context clauses.
1. Declare Turn_Speed.
1. Subtract Turn_Speed for A and add it for D.
1. Print Cos(Player_Angle) and Sin(Player_Angle) after turning.

### 13. Move Forward, Backward, and Slide Along Walls

**Ada focus:** procedure parameters, local constants, collision checks, and state mutation

**Goal:** Use one movement procedure for both forward and backward travel while preventing entry into walls.

**Primary files:** `src/dungeon_walk.adb`

**Expected checkpoint:** W and S move smoothly, the player cannot cross '#', and movement can slide along an open axis.

**Build steps:**
1. Declare Move_Speed.
1. Create Attempt_Move exactly once with a Direction parameter.
1. Calculate New_X and New_Y from Sin/Cos.
1. Call Attempt_Move(1.0) for W and Attempt_Move(-1.0) for S.

### 14. Choose a Directional Minimap Symbol

**Ada focus:** functions without parameters, local constants, abs, nested conditions

**Goal:** Return >, <, v, or ^ based on the player's strongest direction component.

**Primary files:** `src/dungeon_walk.adb`

**Expected checkpoint:** Turning through a full circle eventually produces all four arrow symbols.

**Build steps:**
1. Create Player_Symbol with no parameters.
1. Store Cos and Sin in local constants.
1. Choose the dominant axis using abs.
1. Return the appropriate arrow Character.

### 15. Draw the Map into the Screen Buffer

**Ada focus:** coordinate translation, nested loops, overlays, and constant local indexes

**Goal:** Copy the hidden map into the upper-right of Screen and overlay the player arrow.

**Primary files:** `src/dungeon_walk.adb`

**Expected checkpoint:** A 16 by 16 minimap appears near the right edge with an arrow at the player's tile.

**Build steps:**
1. Choose Start_Row and Start_Column constants.
1. Loop through every map coordinate.
1. Translate each map coordinate into a screen coordinate.
1. Draw Player_Symbol at the player tile; otherwise copy Ship_Map.

### 16. Cast One Ray Until It Reaches a Wall

**Ada focus:** incremental search loops, direction vectors, and exit conditions

**Goal:** Trace one ray from the player through the map and report the wall distance.

**Primary files:** `src/dungeon_walk.adb`

**Expected checkpoint:** The reported distance changes as the player turns or moves.

**Build steps:**
1. Declare Maximum_Depth and Ray_Step.
1. Use Player_Angle as the first ray angle.
1. Compute Eye_X and Eye_Y.
1. Advance Distance_To_Wall until a wall or maximum depth, then print the distance.

### 17. Cast a Different Ray for Every Screen Column

**Ada focus:** linear interpolation, field of view, loop indexes, and Float conversion

**Goal:** Sweep rays from the left edge of the field of view to the right edge.

**Primary files:** `src/dungeon_walk.adb`

**Expected checkpoint:** The program computes 80 wall distances spanning a 60-degree field of view.

**Build steps:**
1. Declare Field_Of_View as Pi / 3.0.
1. Loop Column from 1 through Screen_Width.
1. Calculate Ray_Angle using the supplied interpolation.
1. Reuse the single-ray search for each column.

### 18. Project Wall Distance into Vertical Slices

**Ada focus:** perspective projection, numeric conversion, clamping, and ranges

**Goal:** Turn each ray distance into a wall slice between Ceiling_Row and Floor_Row.

**Primary files:** `src/dungeon_walk.adb`

**Expected checkpoint:** Vertical wall slices now form a recognizable first-person corridor.

**Build steps:**
1. Prevent corrected distance from falling below 0.1.
1. Calculate Ceiling_Row and Floor_Row.
1. Clamp both boundaries to the screen.
1. Fill the vertical range for the current Column.

### 19. Shade Walls and Correct Fish-Eye Distortion

**Ada focus:** piecewise functions and perpendicular-distance correction

**Goal:** Use distance-dependent symbols and keep flat walls visually flat.

**Primary files:** `src/dungeon_walk.adb`

**Expected checkpoint:** Nearby walls use heavy symbols, distant walls use lighter symbols, and flat walls no longer bow outward.

**Build steps:**
1. Create Wall_Character with five distance bands.
1. Calculate Corrected_Distance.
1. Clamp it to at least 0.1.
1. Use Wall_Character(Corrected_Distance) when filling the slice.

### 20. Assemble the Render Pipeline

**Ada focus:** procedure composition, deterministic ordering, and status overlays

**Goal:** Produce one complete frame in a predictable sequence.

**Primary files:** `src/dungeon_walk.adb`

**Expected checkpoint:** Each key press redraws one complete frame containing background, walls, minimap, and controls.

**Build steps:**
1. Create Draw_Status.
1. Create Clear_Terminal with ANSI escape sequences.
1. Create Render with the exact pass ordering.
1. Replace temporary printing in the loop with Render.

### 21. Complete and Verify the Monolithic Ray-Caster

**Ada focus:** integration, behavior verification, and controlled shutdown

**Goal:** Match the supplied final Dungeon Walk behavior in one source file.

**Primary files:** `src/dungeon_walk.adb`, `docs/reference/dungeon_walk/dungeon_walk_final.adb`

**Expected checkpoint:** The terminal displays a playable first-person map; W/S move, A/D turn, Q exits, and walls block movement.

**Build steps:**
1. Compare your implementation with the supplied final reference only after attempting the milestone.
1. Confirm W/S movement, A/D turning, Q shutdown, minimap, collision, and wall shading.
1. Add the final shutdown message.
1. Build with warnings enabled if available.

### 22. Refactor the Working Program into Introductory Packages

**Ada focus:** package specifications, package bodies, encapsulation, and dependency boundaries

**Goal:** Preserve behavior while separating maps, player movement, rendering, and the main loop.

**Primary files:** `src/dungeon_maps.ads`, `src/dungeon_maps.adb`, `src/dungeon_player.ads`, `src/dungeon_player.adb`, `src/dungeon_renderer.ads`, `src/dungeon_renderer.adb`, `src/dungeon_walk.adb`

**Expected checkpoint:** The refactored project behaves identically, and dungeon_walk.adb becomes a short orchestration procedure.

**Build steps:**
1. Create Dungeon_Maps with map types, Ship_Map, and Is_Wall.
1. Create Dungeon_Player with player state operations or a Player record plus movement functions.
1. Create Dungeon_Renderer with Screen and rendering procedures.
1. Reduce dungeon_walk.adb to initialization, the input loop, calls into the packages, and shutdown.
1. Build after extracting each package rather than moving everything at once.

## Complete quest list

### ADA-DW-01-01 — 1.1 — Understand the Next Milestone

- **Milestone:** 1 — Create the Alire Project Correctly
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 1: Create the Alire Project Correctly.

```ada
mkdir -p ~/Documents/src/projects/ada-mastery/dungeon_walk
cd ~/Documents/src/projects/ada-mastery/dungeon_walk
alr init --bin --in-place dungeon_walk
```


### ADA-DW-01-02 — 1.2 — Answer the Core Ada Question

- **Milestone:** 1 — Create the Alire Project Correctly
- **Kind:** Question
- **Prompt:** What do --bin and --in-place change when you run alr init, and why do we create the directory before running the command?

### ADA-DW-01-03 — 1.3 — Build the Milestone

- **Milestone:** 1 — Create the Alire Project Correctly
- **Kind:** Build
- **Prompt:** Implement milestone 1: Create the Alire Project Correctly. Work only in the existing dungeon_walk crate.

```ada
mkdir -p ~/Documents/src/projects/ada-mastery/dungeon_walk
cd ~/Documents/src/projects/ada-mastery/dungeon_walk
alr init --bin --in-place dungeon_walk
```


### ADA-DW-01-04 — 1.4 — Predict Before Running

- **Milestone:** 1 — Create the Alire Project Correctly
- **Kind:** Predict
- **Prompt:** If you run `alr init --bin dungeon_walk` while already inside an empty directory named dungeon_walk, what directory layout are you likely to create?

```ada
mkdir -p ~/Documents/src/projects/ada-mastery/dungeon_walk
cd ~/Documents/src/projects/ada-mastery/dungeon_walk
alr init --bin --in-place dungeon_walk
```


### ADA-DW-01-05 — 1.5 — Repair a Focused Defect

- **Milestone:** 1 — Create the Alire Project Correctly
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
alr init --lib --in-place dungeon_walk
```


### ADA-DW-01-06 — 1.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 1 — Create the Alire Project Correctly
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 1. Then explain, without reading the source line by line, how Alire workspace creation and project layout makes the new behavior work.

### ADA-DW-02-01 — 2.1 — Understand the Next Milestone

- **Milestone:** 2 — Build, Run, and Edit the Generated Program
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 2: Build, Run, and Edit the Generated Program.

### ADA-DW-02-02 — 2.2 — Answer the Core Ada Question

- **Milestone:** 2 — Build, Run, and Edit the Generated Program
- **Kind:** Question
- **Prompt:** Why is the file named dungeon_walk.adb and the outer procedure named Dungeon_Walk?

### ADA-DW-02-03 — 2.3 — Build the Milestone

- **Milestone:** 2 — Build, Run, and Edit the Generated Program
- **Kind:** Build
- **Prompt:** Implement milestone 2: Build, Run, and Edit the Generated Program. Work only in the existing dungeon_walk crate.

```ada
with Ada.Text_IO; use Ada.Text_IO;

procedure Dungeon_Walk is
begin
   Put_Line ("Dungeon Walk");
   Put_Line ("You wake inside a silent ship.");
end Dungeon_Walk;
```


### ADA-DW-02-04 — 2.4 — Predict Before Running

- **Milestone:** 2 — Build, Run, and Edit the Generated Program
- **Kind:** Predict
- **Prompt:** What happens if the final line says `end Other_Name;` instead of `end Dungeon_Walk;`?

```ada
with Ada.Text_IO; use Ada.Text_IO;

procedure Dungeon_Walk is
begin
   Put_Line ("Dungeon Walk");
   Put_Line ("You wake inside a silent ship.");
end Dungeon_Walk;
```


### ADA-DW-02-05 — 2.5 — Repair a Focused Defect

- **Milestone:** 2 — Build, Run, and Edit the Generated Program
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
procedure Dungeon_Walk is
begin
   Put_Line ("Dungeon Walk")
end Dungeon_Walk;
```


### ADA-DW-02-06 — 2.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 2 — Build, Run, and Edit the Generated Program
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 2. Then explain, without reading the source line by line, how Compilation cycle and Ada procedure structure makes the new behavior work.

### ADA-DW-03-01 — 3.1 — Understand the Next Milestone

- **Milestone:** 3 — Import Text I/O and Read Ada Declarations
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 3: Import Text I/O and Read Ada Declarations.

### ADA-DW-03-02 — 3.2 — Answer the Core Ada Question

- **Milestone:** 3 — Import Text I/O and Read Ada Declarations
- **Kind:** Question
- **Prompt:** What is the difference between `with Ada.Text_IO;` and `use Ada.Text_IO;`?

### ADA-DW-03-03 — 3.3 — Build the Milestone

- **Milestone:** 3 — Import Text I/O and Read Ada Declarations
- **Kind:** Build
- **Prompt:** Implement milestone 3: Import Text I/O and Read Ada Declarations. Work only in the existing dungeon_walk crate.

```ada
with Ada.Text_IO;

procedure Dungeon_Walk is
begin
   Ada.Text_IO.Put_Line ("Dungeon Walk");
end Dungeon_Walk;
```


### ADA-DW-03-04 — 3.4 — Predict Before Running

- **Milestone:** 3 — Import Text I/O and Read Ada Declarations
- **Kind:** Predict
- **Prompt:** Can a variable declaration be placed after `begin` beside Put_Line?

```ada
with Ada.Text_IO;

procedure Dungeon_Walk is
begin
   Ada.Text_IO.Put_Line ("Dungeon Walk");
end Dungeon_Walk;
```


### ADA-DW-03-05 — 3.5 — Repair a Focused Defect

- **Milestone:** 3 — Import Text I/O and Read Ada Declarations
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
procedure Dungeon_Walk is
   Put_Line ("Dungeon Walk");
begin
   null;
end Dungeon_Walk;
```


### ADA-DW-03-06 — 3.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 3 — Import Text I/O and Read Ada Declarations
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 3. Then explain, without reading the source line by line, how with clauses, use clauses, declarations, and begin/end makes the new behavior work.

### ADA-DW-04-01 — 4.1 — Understand the Next Milestone

- **Milestone:** 4 — Add Screen Settings and Player State
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 4: Add Screen Settings and Player State.

### ADA-DW-04-02 — 4.2 — Answer the Core Ada Question

- **Milestone:** 4 — Add Screen Settings and Player State
- **Kind:** Question
- **Prompt:** Why should Screen_Width be constant while Player_X remains a variable?

### ADA-DW-04-03 — 4.3 — Build the Milestone

- **Milestone:** 4 — Add Screen Settings and Player State
- **Kind:** Build
- **Prompt:** Implement milestone 4: Add Screen Settings and Player State. Work only in the existing dungeon_walk crate.

```ada
   Screen_Width  : constant Positive := 80;
   Screen_Height : constant Positive := 24;

   Player_X     : Float := 2.5;
   Player_Y     : Float := 2.5;
   Player_Angle : Float := 0.0;
   Running      : Boolean := True;
   Key          : Character;
```


### ADA-DW-04-04 — 4.4 — Predict Before Running

- **Milestone:** 4 — Add Screen Settings and Player State
- **Kind:** Predict
- **Prompt:** Would `Screen_Width : constant Positive := 0;` compile and run successfully?

```ada
   Screen_Width  : constant Positive := 80;
   Screen_Height : constant Positive := 24;

   Player_X     : Float := 2.5;
   Player_Y     : Float := 2.5;
   Player_Angle : Float := 0.0;
   Running      : Boolean := True;
   Key          : Character;
```


### ADA-DW-04-05 — 4.5 — Repair a Focused Defect

- **Milestone:** 4 — Add Screen Settings and Player State
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
Player_X : constant Float := 2.5;
...
Player_X := Player_X + 1.0;
```


### ADA-DW-04-06 — 4.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 4 — Add Screen Settings and Player State
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 4. Then explain, without reading the source line by line, how constants, variables, Positive, Float, Boolean, and Character makes the new behavior work.

### ADA-DW-05-01 — 5.1 — Understand the Next Milestone

- **Milestone:** 5 — Create the Main Input Loop
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 5: Create the Main Input Loop.

### ADA-DW-05-02 — 5.2 — Answer the Core Ada Question

- **Milestone:** 5 — Create the Main Input Loop
- **Kind:** Question
- **Prompt:** Why does the case statement need `when others => null;`?

### ADA-DW-05-03 — 5.3 — Build the Milestone

- **Milestone:** 5 — Create the Main Input Loop
- **Kind:** Build
- **Prompt:** Implement milestone 5: Create the Main Input Loop. Work only in the existing dungeon_walk crate.

```ada
   while Running loop
      Put_Line ("W/S move  A/D turn  Q quit");
      Get_Immediate (Key);

      case Key is
         when 'w' | 'W' => Put_Line ("Forward");
         when 's' | 'S' => Put_Line ("Backward");
         when 'a' | 'A' => Put_Line ("Turn left");
         when 'd' | 'D' => Put_Line ("Turn right");
         when 'q' | 'Q' => Running := False;
         when others    => null;
      end case;
   end loop;
```


### ADA-DW-05-04 — 5.4 — Predict Before Running

- **Milestone:** 5 — Create the Main Input Loop
- **Kind:** Predict
- **Prompt:** What is the difference between assigning `Running := False` and writing `exit` in the Q branch?

```ada
   while Running loop
      Put_Line ("W/S move  A/D turn  Q quit");
      Get_Immediate (Key);

      case Key is
         when 'w' | 'W' => Put_Line ("Forward");
         when 's' | 'S' => Put_Line ("Backward");
         when 'a' | 'A' => Put_Line ("Turn left");
         when 'd' | 'D' => Put_Line ("Turn right");
         when 'q' | 'Q' => Running := False;
         when others    => null;
      end case;
   end loop;
```


### ADA-DW-05-05 — 5.5 — Repair a Focused Defect

- **Milestone:** 5 — Create the Main Input Loop
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
case Key is
   when 'q' => Running := False;
end case;
```


### ADA-DW-05-06 — 5.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 5 — Create the Main Input Loop
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 5. Then explain, without reading the source line by line, how while loops, immediate character input, and case statements makes the new behavior work.

### ADA-DW-06-01 — 6.1 — Understand the Next Milestone

- **Milestone:** 6 — Model the Ship Map with a Subtype and Array
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 6: Model the Ship Map with a Subtype and Array.

### ADA-DW-06-02 — 6.2 — Answer the Core Ada Question

- **Milestone:** 6 — Model the Ship Map with a Subtype and Array
- **Kind:** Question
- **Prompt:** Why use `Map_Row` instead of declaring Ship_Map as a loose collection of ordinary Strings?

### ADA-DW-06-03 — 6.3 — Build the Milestone

- **Milestone:** 6 — Model the Ship Map with a Subtype and Array
- **Kind:** Build
- **Prompt:** Implement milestone 6: Model the Ship Map with a Subtype and Array. Work only in the existing dungeon_walk crate.

```ada
   Map_Width  : constant Positive := 16;
   Map_Height : constant Positive := 16;

   subtype Map_Row is String (1 .. Map_Width);
   type Map_Array is array (1 .. Map_Height) of Map_Row;

   Ship_Map : constant Map_Array :=
     ("################",
      "#..............#",
      "#..####........#",
      "#..#..#........#",
      "#..#..######...#",
      "#..#...........#",
      "#..######..#####",
      "#..............#",
      "#####..####....#",
      "#......#.......#",
      "#......#..###..#",
      "#.........#....#",
      "#..########....#",
      "#..............#",
      "#..............#",
      "################");
```


### ADA-DW-06-04 — 6.4 — Predict Before Running

- **Milestone:** 6 — Model the Ship Map with a Subtype and Array
- **Kind:** Predict
- **Prompt:** Which expression selects column 5 from row 3: `Ship_Map (5) (3)` or `Ship_Map (3) (5)`?

```ada
   Map_Width  : constant Positive := 16;
   Map_Height : constant Positive := 16;

   subtype Map_Row is String (1 .. Map_Width);
   type Map_Array is array (1 .. Map_Height) of Map_Row;

   Ship_Map : constant Map_Array :=
     ("################",
      "#..............#",
      "#..####........#",
      "#..#..#........#",
      "#..#..######...#",
      "#..#...........#",
      "#..######..#####",
      "#..............#",
      "#####..####....#",
      "#......#.......#",
      "#......#..###..#",
      "#.........#....#",
      "#..########....#",
      "#..............#",
      "#..............#",
      "################");
```


### ADA-DW-06-05 — 6.5 — Repair a Focused Defect

- **Milestone:** 6 — Model the Ship Map with a Subtype and Array
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
Ship_Map : constant Map_Array := ("#####", "#####");
```


### ADA-DW-06-06 — 6.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 6 — Model the Ship Map with a Subtype and Array
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 6. Then explain, without reading the source line by line, how String constraints, subtypes, arrays, and multidimensional indexing makes the new behavior work.

### ADA-DW-07-01 — 7.1 — Understand the Next Milestone

- **Milestone:** 7 — Print the Top-Down Map with a Procedure
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 7: Print the Top-Down Map with a Procedure.

### ADA-DW-07-02 — 7.2 — Answer the Core Ada Question

- **Milestone:** 7 — Print the Top-Down Map with a Procedure
- **Kind:** Question
- **Prompt:** Why is `for Row in Ship_Map'Range loop` preferable to hard-coding `for Row in 1 .. 16 loop`?

### ADA-DW-07-03 — 7.3 — Build the Milestone

- **Milestone:** 7 — Print the Top-Down Map with a Procedure
- **Kind:** Build
- **Prompt:** Implement milestone 7: Print the Top-Down Map with a Procedure. Work only in the existing dungeon_walk crate.

```ada
   procedure Draw_Map is
   begin
      for Row in Ship_Map'Range loop
         Put_Line (Ship_Map (Row));
      end loop;
   end Draw_Map;
```


### ADA-DW-07-04 — 7.4 — Predict Before Running

- **Milestone:** 7 — Print the Top-Down Map with a Procedure
- **Kind:** Predict
- **Prompt:** Does Draw_Map need Ship_Map as a parameter while it is nested inside Dungeon_Walk?

```ada
   procedure Draw_Map is
   begin
      for Row in Ship_Map'Range loop
         Put_Line (Ship_Map (Row));
      end loop;
   end Draw_Map;
```


### ADA-DW-07-05 — 7.5 — Repair a Focused Defect

- **Milestone:** 7 — Print the Top-Down Map with a Procedure
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
procedure Draw_Map is
begin
   for Row in Ship_Map loop
      Put_Line (Row);
   end loop;
end Draw_Map;
```


### ADA-DW-07-06 — 7.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 7 — Print the Top-Down Map with a Procedure
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 7. Then explain, without reading the source line by line, how procedures, for loops, array attributes, and parameters makes the new behavior work.

### ADA-DW-08-01 — 8.1 — Understand the Next Milestone

- **Milestone:** 8 — Create an Off-Screen Character Buffer
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 8: Create an Off-Screen Character Buffer.

### ADA-DW-08-02 — 8.2 — Answer the Core Ada Question

- **Milestone:** 8 — Create an Off-Screen Character Buffer
- **Kind:** Question
- **Prompt:** What does `Screen (Row) (Column)` mean?

### ADA-DW-08-03 — 8.3 — Build the Milestone

- **Milestone:** 8 — Create an Off-Screen Character Buffer
- **Kind:** Build
- **Prompt:** Implement milestone 8: Create an Off-Screen Character Buffer. Work only in the existing dungeon_walk crate.

```ada
   type Screen_Array is
     array (1 .. Screen_Height) of String (1 .. Screen_Width);

   Screen : Screen_Array;
```


### ADA-DW-08-04 — 8.4 — Predict Before Running

- **Milestone:** 8 — Create an Off-Screen Character Buffer
- **Kind:** Predict
- **Prompt:** Why is an uninitialized Screen unsafe to print immediately?

```ada
   type Screen_Array is
     array (1 .. Screen_Height) of String (1 .. Screen_Width);

   Screen : Screen_Array;
```


### ADA-DW-08-05 — 8.5 — Repair a Focused Defect

- **Milestone:** 8 — Create an Off-Screen Character Buffer
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
type Screen_Array is array (1 .. Screen_Height) of String;
```


### ADA-DW-08-06 — 8.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 8 — Create an Off-Screen Character Buffer
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 8. Then explain, without reading the source line by line, how arrays of constrained strings and mutable aggregate state makes the new behavior work.

### ADA-DW-09-01 — 9.1 — Understand the Next Milestone

- **Milestone:** 9 — Fill Ceiling and Floor with Nested Loops
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 9: Fill Ceiling and Floor with Nested Loops.

### ADA-DW-09-02 — 9.2 — Answer the Core Ada Question

- **Milestone:** 9 — Fill Ceiling and Floor with Nested Loops
- **Kind:** Question
- **Prompt:** Why must Fill_Background assign every character on every frame?

### ADA-DW-09-03 — 9.3 — Build the Milestone

- **Milestone:** 9 — Fill Ceiling and Floor with Nested Loops
- **Kind:** Build
- **Prompt:** Implement milestone 9: Fill Ceiling and Floor with Nested Loops. Work only in the existing dungeon_walk crate.

```ada
   procedure Fill_Background is
   begin
      for Row in Screen'Range loop
         for Column in Screen (Row)'Range loop
            if Row < Screen_Height / 2 then
               Screen (Row) (Column) := ' ';
            else
               Screen (Row) (Column) := '.';
            end if;
         end loop;
      end loop;
   end Fill_Background;
```


### ADA-DW-09-04 — 9.4 — Predict Before Running

- **Milestone:** 9 — Fill Ceiling and Floor with Nested Loops
- **Kind:** Predict
- **Prompt:** With Screen_Height = 24, which branch handles row 12?

```ada
   procedure Fill_Background is
   begin
      for Row in Screen'Range loop
         for Column in Screen (Row)'Range loop
            if Row < Screen_Height / 2 then
               Screen (Row) (Column) := ' ';
            else
               Screen (Row) (Column) := '.';
            end if;
         end loop;
      end loop;
   end Fill_Background;
```


### ADA-DW-09-05 — 9.5 — Repair a Focused Defect

- **Milestone:** 9 — Fill Ceiling and Floor with Nested Loops
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
for Column in Screen'Range loop
   Screen (Row) (Column) := '.';
end loop;
```


### ADA-DW-09-06 — 9.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 9 — Fill Ceiling and Floor with Nested Loops
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 9. Then explain, without reading the source line by line, how nested iteration, conditions, and array assignment makes the new behavior work.

### ADA-DW-10-01 — 10.1 — Understand the Next Milestone

- **Milestone:** 10 — Write Is_Wall Safely
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 10: Write Is_Wall Safely.

### ADA-DW-10-02 — 10.2 — Answer the Core Ada Question

- **Milestone:** 10 — Write Is_Wall Safely
- **Kind:** Question
- **Prompt:** Why does Is_Wall check bounds before evaluating Ship_Map(Map_Y)(Map_X)?

### ADA-DW-10-03 — 10.3 — Build the Milestone

- **Milestone:** 10 — Write Is_Wall Safely
- **Kind:** Build
- **Prompt:** Implement milestone 10: Write Is_Wall Safely. Work only in the existing dungeon_walk crate.

```ada
   function Is_Wall (X : Float; Y : Float) return Boolean is
      Map_X : constant Integer := Integer (Float'Floor (X));
      Map_Y : constant Integer := Integer (Float'Floor (Y));
   begin
      if Map_X < 1
        or else Map_X > Map_Width
        or else Map_Y < 1
        or else Map_Y > Map_Height
      then
         return True;
      end if;

      return Ship_Map (Map_Y) (Map_X) = '#';
   end Is_Wall;
```


### ADA-DW-10-04 — 10.4 — Predict Before Running

- **Milestone:** 10 — Write Is_Wall Safely
- **Kind:** Predict
- **Prompt:** What map tile is tested for X = 2.9 and Y = 4.1?

```ada
   function Is_Wall (X : Float; Y : Float) return Boolean is
      Map_X : constant Integer := Integer (Float'Floor (X));
      Map_Y : constant Integer := Integer (Float'Floor (Y));
   begin
      if Map_X < 1
        or else Map_X > Map_Width
        or else Map_Y < 1
        or else Map_Y > Map_Height
      then
         return True;
      end if;

      return Ship_Map (Map_Y) (Map_X) = '#';
   end Is_Wall;
```


### ADA-DW-10-05 — 10.5 — Repair a Focused Defect

- **Milestone:** 10 — Write Is_Wall Safely
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
return Ship_Map (Map_Y) (Map_X) = '#';
-- bounds check placed after this line
```


### ADA-DW-10-06 — 10.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 10 — Write Is_Wall Safely
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 10. Then explain, without reading the source line by line, how functions, return values, short-circuit Boolean logic, conversion, and bounds makes the new behavior work.

### ADA-DW-11-01 — 11.1 — Understand the Next Milestone

- **Milestone:** 11 — Use Floating-Point Player Coordinates
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 11: Use Floating-Point Player Coordinates.

### ADA-DW-11-02 — 11.2 — Answer the Core Ada Question

- **Milestone:** 11 — Use Floating-Point Player Coordinates
- **Kind:** Question
- **Prompt:** Why are Player_X and Player_Y Float instead of Integer?

### ADA-DW-11-03 — 11.3 — Build the Milestone

- **Milestone:** 11 — Use Floating-Point Player Coordinates
- **Kind:** Build
- **Prompt:** Implement milestone 11: Use Floating-Point Player Coordinates. Work only in the existing dungeon_walk crate.

```ada
Put_Line
  ("X=" & Float'Image (Player_X)
   & " Y=" & Float'Image (Player_Y));
```


### ADA-DW-11-04 — 11.4 — Predict Before Running

- **Milestone:** 11 — Use Floating-Point Player Coordinates
- **Kind:** Predict
- **Prompt:** After starting at 2.5 and adding Move_Speed 0.35 twice, what is Player_X mathematically?

```ada
Put_Line
  ("X=" & Float'Image (Player_X)
   & " Y=" & Float'Image (Player_Y));
```


### ADA-DW-11-05 — 11.5 — Repair a Focused Defect

- **Milestone:** 11 — Use Floating-Point Player Coordinates
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
Player_X : Integer := 2.5;
```


### ADA-DW-11-06 — 11.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 11 — Use Floating-Point Player Coordinates
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 11. Then explain, without reading the source line by line, how Float state, assignments, and tile versus world coordinates makes the new behavior work.

### ADA-DW-12-01 — 12.1 — Understand the Next Milestone

- **Milestone:** 12 — Turn with Radians and Compute Direction
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 12: Turn with Radians and Compute Direction.

### ADA-DW-12-02 — 12.2 — Answer the Core Ada Question

- **Milestone:** 12 — Turn with Radians and Compute Direction
- **Kind:** Question
- **Prompt:** At Player_Angle = 0.0, what are the approximate X and Y direction components?

### ADA-DW-12-03 — 12.3 — Build the Milestone

- **Milestone:** 12 — Turn with Radians and Compute Direction
- **Kind:** Build
- **Prompt:** Implement milestone 12: Turn with Radians and Compute Direction. Work only in the existing dungeon_walk crate.

```ada
with Ada.Numerics;
with Ada.Numerics.Elementary_Functions;
use Ada.Numerics.Elementary_Functions;

...
Turn_Speed : constant Float := 0.20;
```


### ADA-DW-12-04 — 12.4 — Predict Before Running

- **Milestone:** 12 — Turn with Radians and Compute Direction
- **Kind:** Predict
- **Prompt:** Approximately what direction is represented by Ada.Numerics.Pi / 2.0?

```ada
with Ada.Numerics;
with Ada.Numerics.Elementary_Functions;
use Ada.Numerics.Elementary_Functions;

...
Turn_Speed : constant Float := 0.20;
```


### ADA-DW-12-05 — 12.5 — Repair a Focused Defect

- **Milestone:** 12 — Turn with Radians and Compute Direction
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
Player_Angle := Player_Angle + 20.0; -- intended as 20 degrees
```


### ADA-DW-12-06 — 12.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 12 — Turn with Radians and Compute Direction
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 12. Then explain, without reading the source line by line, how Ada.Numerics, elementary functions, radians, Sin, and Cos makes the new behavior work.

### ADA-DW-13-01 — 13.1 — Understand the Next Milestone

- **Milestone:** 13 — Move Forward, Backward, and Slide Along Walls
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 13: Move Forward, Backward, and Slide Along Walls.

### ADA-DW-13-02 — 13.2 — Answer the Core Ada Question

- **Milestone:** 13 — Move Forward, Backward, and Slide Along Walls
- **Kind:** Question
- **Prompt:** Why does Attempt_Move test `(New_X, Player_Y)` separately from `(Player_X, New_Y)`?

### ADA-DW-13-03 — 13.3 — Build the Milestone

- **Milestone:** 13 — Move Forward, Backward, and Slide Along Walls
- **Kind:** Build
- **Prompt:** Implement milestone 13: Move Forward, Backward, and Slide Along Walls. Work only in the existing dungeon_walk crate.

```ada
   procedure Attempt_Move (Direction : Float) is
      New_X : constant Float :=
        Player_X + Cos (Player_Angle) * Move_Speed * Direction;
      New_Y : constant Float :=
        Player_Y + Sin (Player_Angle) * Move_Speed * Direction;
   begin
      if not Is_Wall (New_X, Player_Y) then
         Player_X := New_X;
      end if;

      if not Is_Wall (Player_X, New_Y) then
         Player_Y := New_Y;
      end if;
   end Attempt_Move;
```


### ADA-DW-13-04 — 13.4 — Predict Before Running

- **Milestone:** 13 — Move Forward, Backward, and Slide Along Walls
- **Kind:** Predict
- **Prompt:** What changes when Attempt_Move receives -1.0?

```ada
   procedure Attempt_Move (Direction : Float) is
      New_X : constant Float :=
        Player_X + Cos (Player_Angle) * Move_Speed * Direction;
      New_Y : constant Float :=
        Player_Y + Sin (Player_Angle) * Move_Speed * Direction;
   begin
      if not Is_Wall (New_X, Player_Y) then
         Player_X := New_X;
      end if;

      if not Is_Wall (Player_X, New_Y) then
         Player_Y := New_Y;
      end if;
   end Attempt_Move;
```


### ADA-DW-13-05 — 13.5 — Repair a Focused Defect

- **Milestone:** 13 — Move Forward, Backward, and Slide Along Walls
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
if not Is_Wall (New_X, New_Y) then
   Player_X := New_X;
   Player_Y := New_Y;
end if;
```


### ADA-DW-13-06 — 13.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 13 — Move Forward, Backward, and Slide Along Walls
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 13. Then explain, without reading the source line by line, how procedure parameters, local constants, collision checks, and state mutation makes the new behavior work.

### ADA-DW-14-01 — 14.1 — Understand the Next Milestone

- **Milestone:** 14 — Choose a Directional Minimap Symbol
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 14: Choose a Directional Minimap Symbol.

### ADA-DW-14-02 — 14.2 — Answer the Core Ada Question

- **Milestone:** 14 — Choose a Directional Minimap Symbol
- **Kind:** Question
- **Prompt:** Why compare `abs Horizontal` with `abs Vertical` before checking their signs?

### ADA-DW-14-03 — 14.3 — Build the Milestone

- **Milestone:** 14 — Choose a Directional Minimap Symbol
- **Kind:** Build
- **Prompt:** Implement milestone 14: Choose a Directional Minimap Symbol. Work only in the existing dungeon_walk crate.

```ada
   function Player_Symbol return Character is
      Horizontal : constant Float := Cos (Player_Angle);
      Vertical   : constant Float := Sin (Player_Angle);
   begin
      if abs Horizontal > abs Vertical then
         if Horizontal > 0.0 then
            return '>';
         else
            return '<';
         end if;
      else
         if Vertical > 0.0 then
            return 'v';
         else
            return '^';
         end if;
      end if;
   end Player_Symbol;
```


### ADA-DW-14-04 — 14.4 — Predict Before Running

- **Milestone:** 14 — Choose a Directional Minimap Symbol
- **Kind:** Predict
- **Prompt:** What symbol is returned near angle 0.0?

```ada
   function Player_Symbol return Character is
      Horizontal : constant Float := Cos (Player_Angle);
      Vertical   : constant Float := Sin (Player_Angle);
   begin
      if abs Horizontal > abs Vertical then
         if Horizontal > 0.0 then
            return '>';
         else
            return '<';
         end if;
      else
         if Vertical > 0.0 then
            return 'v';
         else
            return '^';
         end if;
      end if;
   end Player_Symbol;
```


### ADA-DW-14-05 — 14.5 — Repair a Focused Defect

- **Milestone:** 14 — Choose a Directional Minimap Symbol
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
if Horizontal > Vertical then return '>'; else return 'v'; end if;
```


### ADA-DW-14-06 — 14.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 14 — Choose a Directional Minimap Symbol
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 14. Then explain, without reading the source line by line, how functions without parameters, local constants, abs, nested conditions makes the new behavior work.

### ADA-DW-15-01 — 15.1 — Understand the Next Milestone

- **Milestone:** 15 — Draw the Map into the Screen Buffer
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 15: Draw the Map into the Screen Buffer.

### ADA-DW-15-02 — 15.2 — Answer the Core Ada Question

- **Milestone:** 15 — Draw the Map into the Screen Buffer
- **Kind:** Question
- **Prompt:** Why are Player_Map_X and Player_Map_Y calculated with Float'Floor?

### ADA-DW-15-03 — 15.3 — Build the Milestone

- **Milestone:** 15 — Draw the Map into the Screen Buffer
- **Kind:** Build
- **Prompt:** Implement milestone 15: Draw the Map into the Screen Buffer. Work only in the existing dungeon_walk crate.

```ada
   procedure Draw_Minimap is
      Start_Row : constant Positive := 2;
      Start_Column : constant Positive := Screen_Width - Map_Width - 1;
      Player_Map_X : constant Integer :=
        Integer (Float'Floor (Player_X));
      Player_Map_Y : constant Integer :=
        Integer (Float'Floor (Player_Y));
      Screen_Row    : Integer;
      Screen_Column : Integer;
   begin
      for Map_Y in 1 .. Map_Height loop
         for Map_X in 1 .. Map_Width loop
            Screen_Row := Start_Row + Map_Y - 1;
            Screen_Column := Start_Column + Map_X - 1;
            if Map_X = Player_Map_X and then Map_Y = Player_Map_Y then
               Screen (Screen_Row) (Screen_Column) := Player_Symbol;
            else
               Screen (Screen_Row) (Screen_Column) :=
                 Ship_Map (Map_Y) (Map_X);
            end if;
         end loop;
      end loop;
   end Draw_Minimap;
```


### ADA-DW-15-04 — 15.4 — Predict Before Running

- **Milestone:** 15 — Draw the Map into the Screen Buffer
- **Kind:** Predict
- **Prompt:** With Screen_Width 80 and Map_Width 16, what is Start_Column?

```ada
   procedure Draw_Minimap is
      Start_Row : constant Positive := 2;
      Start_Column : constant Positive := Screen_Width - Map_Width - 1;
      Player_Map_X : constant Integer :=
        Integer (Float'Floor (Player_X));
      Player_Map_Y : constant Integer :=
        Integer (Float'Floor (Player_Y));
      Screen_Row    : Integer;
      Screen_Column : Integer;
   begin
      for Map_Y in 1 .. Map_Height loop
         for Map_X in 1 .. Map_Width loop
            Screen_Row := Start_Row + Map_Y - 1;
            Screen_Column := Start_Column + Map_X - 1;
            if Map_X = Player_Map_X and then Map_Y = Player_Map_Y then
               Screen (Screen_Row) (Screen_Column) := Player_Symbol;
            else
               Screen (Screen_Row) (Screen_Column) :=
                 Ship_Map (Map_Y) (Map_X);
            end if;
         end loop;
      end loop;
   end Draw_Minimap;
```


### ADA-DW-15-05 — 15.5 — Repair a Focused Defect

- **Milestone:** 15 — Draw the Map into the Screen Buffer
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
Screen (Map_Y) (Map_X) := Ship_Map (Map_X) (Map_Y);
```


### ADA-DW-15-06 — 15.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 15 — Draw the Map into the Screen Buffer
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 15. Then explain, without reading the source line by line, how coordinate translation, nested loops, overlays, and constant local indexes makes the new behavior work.

### ADA-DW-16-01 — 16.1 — Understand the Next Milestone

- **Milestone:** 16 — Cast One Ray Until It Reaches a Wall
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 16: Cast One Ray Until It Reaches a Wall.

### ADA-DW-16-02 — 16.2 — Answer the Core Ada Question

- **Milestone:** 16 — Cast One Ray Until It Reaches a Wall
- **Kind:** Question
- **Prompt:** What tradeoff does Ray_Step control?

### ADA-DW-16-03 — 16.3 — Build the Milestone

- **Milestone:** 16 — Cast One Ray Until It Reaches a Wall
- **Kind:** Build
- **Prompt:** Implement milestone 16: Cast One Ray Until It Reaches a Wall. Work only in the existing dungeon_walk crate.

```ada
Distance_To_Wall := 0.0;
loop
   Distance_To_Wall := Distance_To_Wall + Ray_Step;
   Test_X := Player_X + Eye_X * Distance_To_Wall;
   Test_Y := Player_Y + Eye_Y * Distance_To_Wall;
   exit when Is_Wall (Test_X, Test_Y);
   exit when Distance_To_Wall >= Maximum_Depth;
end loop;
```


### ADA-DW-16-04 — 16.4 — Predict Before Running

- **Milestone:** 16 — Cast One Ray Until It Reaches a Wall
- **Kind:** Predict
- **Prompt:** If Ray_Step is 0.05, approximately how many iterations are needed to reach distance 5.0?

```ada
Distance_To_Wall := 0.0;
loop
   Distance_To_Wall := Distance_To_Wall + Ray_Step;
   Test_X := Player_X + Eye_X * Distance_To_Wall;
   Test_Y := Player_Y + Eye_Y * Distance_To_Wall;
   exit when Is_Wall (Test_X, Test_Y);
   exit when Distance_To_Wall >= Maximum_Depth;
end loop;
```


### ADA-DW-16-05 — 16.5 — Repair a Focused Defect

- **Milestone:** 16 — Cast One Ray Until It Reaches a Wall
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
loop
   Test_X := Player_X + Eye_X * Distance_To_Wall;
   exit when Is_Wall (Test_X, Test_Y);
end loop;
```


### ADA-DW-16-06 — 16.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 16 — Cast One Ray Until It Reaches a Wall
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 16. Then explain, without reading the source line by line, how incremental search loops, direction vectors, and exit conditions makes the new behavior work.

### ADA-DW-17-01 — 17.1 — Understand the Next Milestone

- **Milestone:** 17 — Cast a Different Ray for Every Screen Column
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 17: Cast a Different Ray for Every Screen Column.

### ADA-DW-17-02 — 17.2 — Answer the Core Ada Question

- **Milestone:** 17 — Cast a Different Ray for Every Screen Column
- **Kind:** Question
- **Prompt:** Why convert Column and Screen_Width to Float in the ray-angle expression?

### ADA-DW-17-03 — 17.3 — Build the Milestone

- **Milestone:** 17 — Cast a Different Ray for Every Screen Column
- **Kind:** Build
- **Prompt:** Implement milestone 17: Cast a Different Ray for Every Screen Column. Work only in the existing dungeon_walk crate.

```ada
Ray_Angle :=
  Player_Angle
  - Field_Of_View / 2.0
  + Float (Column - 1)
    / Float (Screen_Width - 1)
    * Field_Of_View;
```


### ADA-DW-17-04 — 17.4 — Predict Before Running

- **Milestone:** 17 — Cast a Different Ray for Every Screen Column
- **Kind:** Predict
- **Prompt:** What ray angle is used by the leftmost column?

```ada
Ray_Angle :=
  Player_Angle
  - Field_Of_View / 2.0
  + Float (Column - 1)
    / Float (Screen_Width - 1)
    * Field_Of_View;
```


### ADA-DW-17-05 — 17.5 — Repair a Focused Defect

- **Milestone:** 17 — Cast a Different Ray for Every Screen Column
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
Float (Column - 1 / Screen_Width - 1) * Field_Of_View
```


### ADA-DW-17-06 — 17.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 17 — Cast a Different Ray for Every Screen Column
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 17. Then explain, without reading the source line by line, how linear interpolation, field of view, loop indexes, and Float conversion makes the new behavior work.

### ADA-DW-18-01 — 18.1 — Understand the Next Milestone

- **Milestone:** 18 — Project Wall Distance into Vertical Slices
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 18: Project Wall Distance into Vertical Slices.

### ADA-DW-18-02 — 18.2 — Answer the Core Ada Question

- **Milestone:** 18 — Project Wall Distance into Vertical Slices
- **Kind:** Question
- **Prompt:** Why does a smaller distance produce a taller wall slice?

### ADA-DW-18-03 — 18.3 — Build the Milestone

- **Milestone:** 18 — Project Wall Distance into Vertical Slices
- **Kind:** Build
- **Prompt:** Implement milestone 18: Project Wall Distance into Vertical Slices. Work only in the existing dungeon_walk crate.

```ada
Ceiling_Row :=
  Integer
    (Float (Screen_Height) / 2.0
     - Float (Screen_Height) / Corrected_Distance);

Floor_Row := Screen_Height - Ceiling_Row;

Ceiling_Row := Integer'Max (1, Ceiling_Row);
Floor_Row := Integer'Min (Screen_Height, Floor_Row);
```


### ADA-DW-18-04 — 18.4 — Predict Before Running

- **Milestone:** 18 — Project Wall Distance into Vertical Slices
- **Kind:** Predict
- **Prompt:** Which wall appears taller: one at distance 2.0 or one at distance 8.0?

```ada
Ceiling_Row :=
  Integer
    (Float (Screen_Height) / 2.0
     - Float (Screen_Height) / Corrected_Distance);

Floor_Row := Screen_Height - Ceiling_Row;

Ceiling_Row := Integer'Max (1, Ceiling_Row);
Floor_Row := Integer'Min (Screen_Height, Floor_Row);
```


### ADA-DW-18-05 — 18.5 — Repair a Focused Defect

- **Milestone:** 18 — Project Wall Distance into Vertical Slices
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
for Row in 0 .. Floor_Row loop
   Screen (Row) (Column) := '#';
end loop;
```


### ADA-DW-18-06 — 18.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 18 — Project Wall Distance into Vertical Slices
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 18. Then explain, without reading the source line by line, how perspective projection, numeric conversion, clamping, and ranges makes the new behavior work.

### ADA-DW-19-01 — 19.1 — Understand the Next Milestone

- **Milestone:** 19 — Shade Walls and Correct Fish-Eye Distortion
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 19: Shade Walls and Correct Fish-Eye Distortion.

### ADA-DW-19-02 — 19.2 — Answer the Core Ada Question

- **Milestone:** 19 — Shade Walls and Correct Fish-Eye Distortion
- **Kind:** Question
- **Prompt:** Why is raw Distance_To_Wall not used directly for wall height?

### ADA-DW-19-03 — 19.3 — Build the Milestone

- **Milestone:** 19 — Shade Walls and Correct Fish-Eye Distortion
- **Kind:** Build
- **Prompt:** Implement milestone 19: Shade Walls and Correct Fish-Eye Distortion. Work only in the existing dungeon_walk crate.

```ada
Corrected_Distance :=
  Distance_To_Wall * Cos (Ray_Angle - Player_Angle);

if Corrected_Distance < 0.1 then
   Corrected_Distance := 0.1;
end if;
```


### ADA-DW-19-04 — 19.4 — Predict Before Running

- **Milestone:** 19 — Shade Walls and Correct Fish-Eye Distortion
- **Kind:** Predict
- **Prompt:** At the center column, what is approximately `Cos(Ray_Angle - Player_Angle)`?

```ada
Corrected_Distance :=
  Distance_To_Wall * Cos (Ray_Angle - Player_Angle);

if Corrected_Distance < 0.1 then
   Corrected_Distance := 0.1;
end if;
```


### ADA-DW-19-05 — 19.5 — Repair a Focused Defect

- **Milestone:** 19 — Shade Walls and Correct Fish-Eye Distortion
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
Corrected_Distance := Distance_To_Wall / Cos (Ray_Angle - Player_Angle);
```


### ADA-DW-19-06 — 19.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 19 — Shade Walls and Correct Fish-Eye Distortion
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 19. Then explain, without reading the source line by line, how piecewise functions and perpendicular-distance correction makes the new behavior work.

### ADA-DW-20-01 — 20.1 — Understand the Next Milestone

- **Milestone:** 20 — Assemble the Render Pipeline
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 20: Assemble the Render Pipeline.

### ADA-DW-20-02 — 20.2 — Answer the Core Ada Question

- **Milestone:** 20 — Assemble the Render Pipeline
- **Kind:** Question
- **Prompt:** What visual bug occurs if Fill_Background runs after Cast_Rays?

### ADA-DW-20-03 — 20.3 — Build the Milestone

- **Milestone:** 20 — Assemble the Render Pipeline
- **Kind:** Build
- **Prompt:** Implement milestone 20: Assemble the Render Pipeline. Work only in the existing dungeon_walk crate.

```ada
   procedure Render is
   begin
      Fill_Background;
      Cast_Rays;
      Draw_Minimap;
      Draw_Status;
      Clear_Terminal;

      for Row in Screen'Range loop
         Put_Line (Screen (Row));
      end loop;
   end Render;
```


### ADA-DW-20-04 — 20.4 — Predict Before Running

- **Milestone:** 20 — Assemble the Render Pipeline
- **Kind:** Predict
- **Prompt:** Why print the Screen only after every drawing procedure finishes?

```ada
   procedure Render is
   begin
      Fill_Background;
      Cast_Rays;
      Draw_Minimap;
      Draw_Status;
      Clear_Terminal;

      for Row in Screen'Range loop
         Put_Line (Screen (Row));
      end loop;
   end Render;
```


### ADA-DW-20-05 — 20.5 — Repair a Focused Defect

- **Milestone:** 20 — Assemble the Render Pipeline
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
Cast_Rays;
Fill_Background;
Draw_Minimap;
```


### ADA-DW-20-06 — 20.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 20 — Assemble the Render Pipeline
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 20. Then explain, without reading the source line by line, how procedure composition, deterministic ordering, and status overlays makes the new behavior work.

### ADA-DW-21-01 — 21.1 — Understand the Next Milestone

- **Milestone:** 21 — Complete and Verify the Monolithic Ray-Caster
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 21: Complete and Verify the Monolithic Ray-Caster.

### ADA-DW-21-02 — 21.2 — Answer the Core Ada Question

- **Milestone:** 21 — Complete and Verify the Monolithic Ray-Caster
- **Kind:** Question
- **Prompt:** Why does the main loop render before calling Get_Immediate?

### ADA-DW-21-03 — 21.3 — Build the Milestone

- **Milestone:** 21 — Complete and Verify the Monolithic Ray-Caster
- **Kind:** Build
- **Prompt:** Implement milestone 21: Complete and Verify the Monolithic Ray-Caster. Work only in the existing dungeon_walk crate.

```ada
Final reference installed at:
~/Documents/src/projects/codequest-forge/docs/reference/dungeon_walk/dungeon_walk_final.adb
```


### ADA-DW-21-04 — 21.4 — Predict Before Running

- **Milestone:** 21 — Complete and Verify the Monolithic Ray-Caster
- **Kind:** Predict
- **Prompt:** What happens if Running is initialized to False?

```ada
Final reference installed at:
~/Documents/src/projects/codequest-forge/docs/reference/dungeon_walk/dungeon_walk_final.adb
```


### ADA-DW-21-05 — 21.5 — Repair a Focused Defect

- **Milestone:** 21 — Complete and Verify the Monolithic Ray-Caster
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
Get_Immediate (Key);
Render;
```


### ADA-DW-21-06 — 21.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 21 — Complete and Verify the Monolithic Ray-Caster
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 21. Then explain, without reading the source line by line, how integration, behavior verification, and controlled shutdown makes the new behavior work.

### ADA-DW-22-01 — 22.1 — Understand the Next Milestone

- **Milestone:** 22 — Refactor the Working Program into Introductory Packages
- **Kind:** Orientation
- **Prompt:** Read the lesson, inspect the listed files, and state what the program will be able to do after completing milestone 22: Refactor the Working Program into Introductory Packages.

### ADA-DW-22-02 — 22.2 — Answer the Core Ada Question

- **Milestone:** 22 — Refactor the Working Program into Introductory Packages
- **Kind:** Question
- **Prompt:** Which declarations should remain private to Dungeon_Renderer rather than appear in its specification?

### ADA-DW-22-03 — 22.3 — Build the Milestone

- **Milestone:** 22 — Refactor the Working Program into Introductory Packages
- **Kind:** Build
- **Prompt:** Implement milestone 22: Refactor the Working Program into Introductory Packages. Work only in the existing dungeon_walk crate.

```ada
package Dungeon_Maps is
   Map_Width  : constant Positive := 16;
   Map_Height : constant Positive := 16;

   function Is_Wall (X : Float; Y : Float) return Boolean;
end Dungeon_Maps;
```


### ADA-DW-22-04 — 22.4 — Predict Before Running

- **Milestone:** 22 — Refactor the Working Program into Introductory Packages
- **Kind:** Predict
- **Prompt:** If Ship_Map is declared only in Dungeon_Maps' body, can Dungeon_Renderer index it directly?

```ada
package Dungeon_Maps is
   Map_Width  : constant Positive := 16;
   Map_Height : constant Positive := 16;

   function Is_Wall (X : Float; Y : Float) return Boolean;
end Dungeon_Maps;
```


### ADA-DW-22-05 — 22.5 — Repair a Focused Defect

- **Milestone:** 22 — Refactor the Working Program into Introductory Packages
- **Kind:** Repair
- **Prompt:** The following code or command is wrong. Identify the defect, explain the likely compiler/runtime/behavioral result, and repair it.

```ada
package Dungeon_Maps is
   procedure Cast_Rays;
   procedure Read_Key;
end Dungeon_Maps;
```


### ADA-DW-22-06 — 22.6 — Demonstrate and Explain the Checkpoint

- **Milestone:** 22 — Refactor the Working Program into Introductory Packages
- **Kind:** Checkpoint
- **Prompt:** Build and demonstrate milestone 22. Then explain, without reading the source line by line, how package specifications, package bodies, encapsulation, and dependency boundaries makes the new behavior work.
