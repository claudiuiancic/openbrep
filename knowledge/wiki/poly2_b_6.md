---
id: wiki.generated.poly2_b_6
type: wiki
category: 3d
commands: ["POLY2_B{6}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### POLY2_B{6}

- POLY2_B{6} n, frame_fill, fillcategory, distortion_flags, fill_pen, fill_background_pen, fillOrigoX, fillOrigoY, mxx, mxy, myx, myy, gradientInnerRadius, x1, y1, s1, pen1, linetype1, ..., xn, yn, sn, penn, linetypen


Advanced version of POLY2_B{5}, where contour attributes (pen and linetype) can be controlled individually for each contour segment. peni: pen index of the contour line starting from control point i. linetypei: line type index of the contour line starting from control point i. Compatibility: introduced in Archicad 21.