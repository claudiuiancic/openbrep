---
id: wiki.generated.window_door_show_dim
type: wiki
category: other
commands: ["WINDOW_DOOR_SHOW_DIM"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### WINDOW_DOOR_SHOW_DIM

n = REQUEST("WINDOW_DOOR_SHOW_DIM", "", show)

Before 9.0 returns 1 in the show variable if Options > Display Options > Doors & Windows is set to "Show with Dimensions", 0 otherwise. Since 9.0 display options were split to separate Door and Window display options, so for compatibility reasons Archicad checks if the request is used in a Window (or marker of a Window) or a Door (or marker of a Door) and automatically returns the corresponding display option. In other cases (symbol, lamp, label) the Window option is returned. Can be used to hide/show custom dimensions according to the current Display Options. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning.

Since 9.0 the "WINDOW_SHOW_DIM", and the "DOOR_SHOW_DIM" separate requests are available.