---
id: wiki.generated.wallhole
type: wiki
category: other
commands: ["WALLHOLE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### WALLHOLE

WALLHOLE n, status,

x1, y1, mask1,

... xn, yn, maskn [, x, y, z]

n: the number of polygon nodes. status:

1: use the attributes of the body for the generated polygons and edges, 2: generated cut polygons will be treated as normal polygons.

xi, yi: cross-section polygon coordinates.

maski: similar to the CUTPOLYA command:

maski = j1 + 2*j2 + 4*j3 + 64*j7, where each j can be 0 or 1. x, y, z: optional direction vector (default is door/window Z axis).

z y

Z j3

x

n

i+1 j1

Y

j2

1

i

X

This command can be used in doors’/windows’ 3D script to cut custom hole(s) in the wall they are placed into. During the 3D generation of the current wall, the 3D script of all its doors/windows is interpreted without model generation to collect the WALLHOLE commands. If they exist, the current wall will be cut using an infinite tube with the polygonal cross-section and direction defined in the script. There can be any number of WALLHOLEs for any door/window, so it is possible to cut more holes for the same door/window, even intersecting ones. If at least one WALLHOLE command is interpreted in a door/window 3D script, no rectangular opening will be generated for that door/window.

Note: The 3D reveal will not be generated automatically for custom holes, you have to generate it from the script. The hole customized this way will only be visible in 3D, because WALLHOLE commands do not have any effect in 2D. A 2D representation can be scripted if needed (used with framing in plan off).

The use of convex polygonal cross-sections is recommended; using concave polygons may result in strange shadings/renderings or cut errors. Convex polygons can be combined to obtain concave ones. Mirroring transformations affect the cutting direction in an unexpected way - to get a more straightforward result, use the WALLNICHE command.

RESOL 72 l1 = 2.7: l2=1.2 h1=2.1: h2=0.3: h3=0.9 r = ((l1/2)^2+h2^2)/(2*h2) a = ATN((l1/2)/(r-h2)) WALLHOLE 5, 1,

-l1/2, h3, 15, l1/2, h3, 15, l1/2, h1-h2, 13, 0, h1-r, 915, 0, 2*a, 4015

- WALLHOLE 4, 1, l1/2-l2, 0, 15, l1/2, 0, 15, l1/2, h3, 15, l1/2-l2, h3, 15


- WALLHOLE 5, 1,


- -0.45, 0, 15, 0.45, 0, 15, 0.45, 1.5, 15, 0, 1.95, 15,
- -0.45, 1.5, 15


PRISM_ 12, 0.1,

- -0.45, 0, 15, 0.45, 0, 15, 0.45, 1.5, 15, 0, 1.95, 15,
- -0.45, 1.5, 15,
- -0.45, 0, -1,
- -0.35, 0.1, 15, 0.35, 0.1, 15, 0.35, 1.45, 15, 0, 1.80, 15,
- -0.35, 1.44, 15,
- -0.35, 0.1, -1