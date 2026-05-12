---
id: wiki.generated.xwall_3
type: wiki
category: other
commands: ["XWALL_{3}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### XWALL_{3}

- XWALL_{3} left_material, right_material, vertical_material, horizontal_material, height, x1, x2, x3, x4, y1, y2, y3, y4, t, radius, log_height, log_offset, mask1, mask2, mask3, mask4, n, x_start1, y_low1, x_end1, y_high1, sill_depth1, frame_shown1,


... x_startn, y_lown, x_endn, y_highn, sill_depthn, frame_shownn, m, a1, b1, c1, d1,

... am, bm, cm, dm, status

XWALL_{3} is an extension of XWALL_{2} command with the possibility of hiding all edges of the log wall. status: controls the behavior of log walls

status = j1 + 2*j2 + 4*j3 + 32*j6 + 64*j7 + 128*j8 + 256*j9 + 512*j10, where each j can be 0 or 1. j1: apply right side material on horizontal edges, j2: apply left side material on horizontal edges, j3: start with half log,

- j6: align texture to wall edges,
- j7: double radius on bended side,
- j8: square log on the right side,
- j9: square log on the left side,


- j10: hide all edges of log wall.


Example:

ROTZ 90 xWALL_{2} "C13", "C11", "C12", "C12",

2, 0, 4, 4, 0, 0, 0, 1, 1, 1, 0,

- 0, 0, 15, 15, 15, 15,
- 1, 1, 0.9, 3, 2.1, 0.3, -(255 + 256), 0,


- 0

DEL 1 ADDX 2 xWALL_{2} "C13", "C11", "C12", "C12",

2, 0, 2 * PI, 2 * PI, 0,

- 0, 0, 1, 1,
- 1, 2, 0, 0, 15, 15, 15, 15, 1,


- 1.6, 0.9, 4.6, 2.1, 0.3, -(255 + 256), 0,


- 0

ADDX 4 xWALL_{2} "C13", "C11", "C12", "C12",

2, 0, 2 * PI, 2 * PI, 0,

- 0, 0, 1, 1,
- 1, 2,


- 0, 0, 15, 15, 15, 15,
- 1,


- 1.6, 0.9, 4.6, 2.1, 0.3, -(255 + 256 + 512), 0, 0