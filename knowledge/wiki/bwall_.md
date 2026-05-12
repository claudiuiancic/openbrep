---
id: wiki.generated.bwall_
type: wiki
category: other
commands: ["BWALL_"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### BWALL_

BWALL_ left_material, right_material, side_material, height, x1, x2, x3, x4, t, radius, mask1, mask2, mask3, mask4, n, x_start1, y_low1, x_end1, y_high1, frame_shown1,

... x_startn, y_lown, x_endn, y_highn, frame_shownn, m, a1, b1, c1, d1,

... am, bm, cm, dm

A smooth curved wall based on the same data structure as the straight wall CWALL_ element. The only additional parameter is radius. Derived from the corresponding CWALL_ by bending the x-z plane onto a cylinder tangential to that plane. Edges along the x axis are transformed to circular arcs, edges along the y axis will be radial in direction, and vertical edges remain vertical. The curvature is approximated by a number of segments set by the current resolution (see the RADIUS command, the RESOL command and the TOLER command).

See also the CWALL_ command for details.

- Example 1: a BWALL_ and the corresponding CWALL_


r

y

x

- Example 2:


ROTZ -60 BWALL_ 1, 1, 1,

- 4, 0, 6, 6, 0, 0.3, 2, 15, 15, 15, 15,
- 5, 1, 1, 3.8, 2.5, -255, 1.8, 0, 3, 2.5, -255, 4.1, 1, 4.5, 1.4, -255, 4.1, 1.55, 4.5, 1.95,-255, 4.1, 2.1, 4.5, 2.5, -255, 1, 0, -0.25, 1, 3