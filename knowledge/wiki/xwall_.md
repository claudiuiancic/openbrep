---
id: wiki.generated.xwall_
type: wiki
category: other
commands: ["XWALL_"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### XWALL_

XWALL_ left_material, right_material, vertical_material, horizontal_material, height, x1, x2, x3, x4, y1, y2, y3, y4, t, radius, log_height, log_offset, mask1, mask2, mask3, mask4, n, x_start1, y_low1, x_end1, y_high1, frame_shown1,

... x_startn, y_lown, x_endn, y_highn, frame_shownn, m, a1, b1, c1, d1,

... am, bm, cm, dm, status

Extended wall definition based on the same data structure as the BWALL_ element. vertical_material, horizontal_material: name or index of the vertical/horizontal side materials.

- y1, y2, y3, y4: the projected endpoints of the wall lying in the x-y plane as seen below.


y

- y3

y2

y1

- y4


x

x1 x2 x3 x4

log_height, log_offset: additional parameters allowing you to compose a wall from logs. Effective only for straight walls.

logheight

logoffset

status: controls the behavior of log walls

status = j1 + 2*j2 + 4*j3 + 32*j6 + 64*j7 + 128*j8 + 256*j9, where each j can be 0 or 1.

- j1: apply right side material on horizontal edges,
- j2: apply left side material on horizontal edges,
- j3: start with half log,


- j6: align texture to wall edges,
- j7: double radius on bended side,
- j8: square log on the right side,
- j9: square log on the left side.


Example:

XWALL_ "Surf-White", "Surf-White", "Surf-White", "Surf-White", 3.0, 0.0, 4.0, 4.0, 0.0,

- 0.0, 0.0, 0.3, 1.2,
- 1.2, 0.0, 0.0, 0.0, 15, 15, 15, 15, 3, 0.25, 0.0, 1.25, 2.5, -255, 1.25, 1.5, 2.25, 2.5, -255, 2.25, 0.5, 3.25, 2.5, -255, 0