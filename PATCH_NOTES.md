# CodeQuest Forge v0.5.2

Map overlay fix.

## Changed

- `/map` now treats `data/images/overworld-map.png` as a true background/image layer.
- Zone labels are positioned on top of the blank label plaques using percentage coordinates from `data/seed.json`.
- Player name, level, XP, progress stats, current location, and recent events are dynamic overlays.
- The CSS file is cache-busted with `?v=0.5.2` so Firefox/Chrome should pick up the map overlay styles immediately.
- The map page gets a wider layout with no artificial 16:9 crop.
- Added `map` metadata and `label_x`, `label_y`, `label_width` fields for zones in the seed file.

## Edit zone positions

Open `data/seed.json` and edit these values per zone:

```json
"label_x": 28.6,
"label_y": 16.1,
"label_width": 12.5
```

Values are percentages of the image width/height.

## v0.5.3

- Fixed dashboard crash when no zone has `Current` status, such as after completing the final quest.
- Dashboard now uses `state.current_zone` fallback instead of assuming a current zone always exists.
- Dashboard Start Here panel is now a Next Step panel and stops pointing at Quest 001 after it is completed.
- Added `/admin` Developer Controls for prototype testing.
- Added Set Level, Level +/- 1, XP +/- controls, and Clear Dev Level Override.
- Dev level override changes only effective level/XP for testing screens. It does not complete quests or award gear.
