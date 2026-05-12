---
id: wiki.generated.d
type: wiki
category: other
commands: ["D"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

##### D

D

54o

origin (C=0, D=0) RefD

origin (C=0, D=0)

RefD BaseD

BaseD

! sideX, sideY parameters RECT2 0, 0, A, B RECT2 0, 0, sideX, sideY HOTSPOT2 sideX, 0, 1, sideY, 1 HOTSPOT2 sideX, -0.1, 2, sideY, 3 HOTSPOT2 sideX, sideY, 3, sideY, 2

- HOTSPOT2 0, sideY, 4, sideX, 1 HOTSPOT2 -0.1, sideY, 5, sideX, 3 HOTSPOT2 sideX, sideY, 6, sideX, 2


- Example 3: Simple length type editing with 1 parameter


- !2D SCRIPT: HOTSPOT2 -1, 0, 1

HOTSPOT2 1, 0, 2 HOTSPOT2 0, 0, 3, corner_y, 1+128 HOTSPOT2 0, -1, 4, corner_y, 3 HOTSPOT2 0, corner_y, 5, corner_y, 2 LINE2 -1, 0, 1, 0

- LINE2 -1, 0, 0, corner_y


LINE2 1, 0, 0, corner_y

- !3D SCRIPT: HOTSPOT -1, 0, 0, 1 HOTSPOT -1, 0, 0.5, 2 HOTSPOT 1, 0, 0, 3 HOTSPOT 1, 0, 0.5, 4 HOTSPOT 0, 0, 0, 5, corner_y, 1+128 HOTSPOT 0, -1, 0, 6, corner_y, 3


- HOTSPOT 0, corner_y, 0, 7, corner_y, 2 HOTSPOT 0, 0, 0.5, 8, corner_y, 1+128


- HOTSPOT 0, -1, 0.5, 9, corner_y, 3


- HOTSPOT 0, corner_y, 0.5, 10, corner_y, 2 PRISM_ 4, 0.5,


- -1, 0, 15, 1, 0, 15, 0, corner_y, 15,
- -1, 0, -1


- Example 4: Combined length type editing with 2 parameters:


- !2D SCRIPT: HOTSPOT2 -1, 0, 1 HOTSPOT2 1, 0, 2 HOTSPOT2 corner_x, 0, 3, corner_y, 1+128 HOTSPOT2 corner_x, -1, 4, corner_y, 3 HOTSPOT2 corner_x, corner_y, 5, corner_y, 2 HOTSPOT2 0, corner_y, 6, corner_x, 1+128 HOTSPOT2 -1, corner_y, 7, corner_x, 3 HOTSPOT2 corner_x, corner_y, 8, corner_x, 2


- LINE2 -1, 0, 1, 0 LINE2 -1, 0, corner_x, corner_y LINE2 1, 0, corner_x, corner_y


- !3D SCRIPT: HOTSPOT -1, 0, 0, 1 HOTSPOT -1, 0, 0.5, 2


- HOTSPOT 1, 0, 0, 3


- HOTSPOT 1, 0, 0.5, 4 HOTSPOT corner_x, 0, 0, 5, corner_y, 1+128 HOTSPOT corner_x, -1, 0, 6, corner_y, 3 HOTSPOT corner_x, corner_y, 0, 7, corner_y, 2


- HOTSPOT 0, corner_y, 0, 8, corner_x, 1+128 HOTSPOT -1, corner_y, 0, 9, corner_x, 3 HOTSPOT corner_x, corner_y, 0, 10, corner_x, 2 HOTSPOT corner_x, 0, 0.5, 11, corner_y, 1+128 HOTSPOT corner_x, -1, 0.5, 12, corner_y, 3 HOTSPOT corner_x, corner_y, 0.5, 13, corner_y, 2 HOTSPOT 0, corner_y, 0.5, 14, corner_x, 1+128 HOTSPOT -1, corner_y, 0.5, 15, corner_x, 3 HOTSPOT corner_x, corner_y, 0.5, 16, corner_x, 2 PRISM_ 4, 0.5,


- -1, 0, 15, 1, 0, 15, corner_x, corner_y, 15,
- -1, 0, -1


- Example 5: Paper space length editing:


hotspot2 0, 0, 1, textHeight, 1 + 1024 hotspot2 0, textHeight * GLOB_SCALE, 2, textHeight, 2 hotspot2 0, -1, 3, textHeight, 3

line2 0,0, 0, textHeight * GLOB_SCALE ! model size [m] line2 0,0, 1,0

define style "text" "Arial", textHeight * 1000, 4, 0 ! paper size [mm] style "text" add2 0, textHeight * GLOB_SCALE / 2 mul2 1000 / GLOB_SCALE, 1000 / GLOB_SCALE ! scale to paper size text2 0,0, "Text height: " + str(textHeight, 5, 4) + " m"

## STATUS CODES

Status codes introduced in the following pages allow users to create segments and arcs in planar polylines using special constraints.

Planar polylines with status codes at nodes are the basis of many GDL elements: POLY2_, POLY2_A, POLY2_B, POLY2_B{2}, POLY2_B{3}, POLY2_B{4}, POLY2_B{5}, POLY_, PLANE_, PRISM_, CPRISM_, BPRISM_, FPRISM_, HPRISM_, SPRISM_, SLAB_, CSLAB_, CROOF_, EXTRUDE, PYRAMID, REVOLVE, SWEEP, TUBE, TUBEA

Status codes allow you:

- • to control the visibility of planar polyline edges
- • to define holes in the polyline
- • to control the visibility of side edges and surfaces
- • to create segments and arcs in the polyline