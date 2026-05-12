---
id: wiki.generated.project2_2
type: wiki
category: 2d
commands: ["PROJECT2{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PROJECT2{2}

- PROJECT2{2} projection_code, angle, method [, backgroundColor, fillOrigoX, fillOrigoY, filldirection]


Creates a projection of the 3D script in the same library part and adds the generated lines to the 2D parametric symbol. The 2nd version

- PROJECT2{2}, together with a previous [SET] FILL command, allows the user to control the fill background, origin and direction of the resulting drawing from the 2D script. The SET FILL 0 shortcut to get an empty fill does not work in this case, you need to reference an actual empty fill. projection_code: the type of projection.


- 3: Top view,
- 4: Side view,
- 5: Side view 2,
- 6: Frontal axonometry,
- 7: Isometric axonometry,
- 8: Monometric axonometry,
- 9: Dimetric axonometry,


- -3: Bottom view,
- -6: Frontal bottom view,
- -7: Isometric bottom view,
- -8: Monometric bottom view,
- -9: Dimetric bottom view. angle: the azimuth angle set in the 3D Projection Settings dialog box. method: the chosen imaging method. If invalid or none is set, the default is hidden lines (2).


1: wireframe, 2: hidden lines (analytic), 3: shading, 16: addition modifier: draws vectorial hatches (effective only in hidden line and shaded mode), 32: addition modifier: use current attributes instead of attributes from 3D (effective only in shading mode), 64: addition modifier: local fill orientation (effective only in shading mode), 128: addition modifier: lines are all inner lines (effective only together with 32). Default is generic, 256: addition modifier: lines are all contour lines (effective only together with 32, if 128 is not set). Default is generic, 512: addition modifier: fills are all cut (effective only together with 32). Default is drafting fills, 1024: addition modifier: fills are all cover (effective only together with 32, if 512 is not set). Default is drafting fills.

BackgroundColor: background color of the fill. fillOrigoX: X coordinate of the fill origin. fillOrigoY: Y coordinate of the fill origin. filldirection: direction angle of fill. Note: the [SET] FILL command is effective for PROJECT2{2}

Example:

- 2D PROJECT2 3, 270, 2

LINE_TYPE "DASHED" ARC2 0, 0, A-B/3, 0, E

E = 270 A = 1 B = 0.2

ROT2 E ADD2 A-B/3, 0 LINE2 0, 0, -0.05, -0.1 LINE2 0, 0, 0.05, -0.1

DEL 2

- 3D


n = 12 E = 270 D = 0.2 A = 1 B = 0.2

FOR i=1 TO n prism 4, D,

-B/3, -B/2, -B/3, B/2,

A-B/3, B/8, A-B/3, -B/8

ADDZ D ROTz E/(n-1)

NEXT i DEL n*2