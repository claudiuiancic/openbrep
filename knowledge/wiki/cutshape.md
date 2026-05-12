---
id: wiki.generated.cutshape
type: wiki
category: other
commands: ["CUTSHAPE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### CUTSHAPE

CUTSHAPE d [, status] [statement1 statement2 ... statementn] CUTEND Cuts a block with "d" thickness, infinite length (both sides of the y axis) and semi-infinite height (above the xy plane). status: controls the treatment of the generated cut polygons. If not specified (for compatibility reasons) the default value is 3.

status = j1 + 2*j2, where each j can be 0 or 1. j1: use the attributes of the body for the generated polygons and edges, j2: generated cut polygons will be treated as normal polygons.

Example: FOR i = 1 TO 5

ADDX 0.4 * i ADDZ 2.5 CUTSHAPE 0.4 DEL 2 ADDX 0.4

NEXT i DEL TOP BRICK 4.4, 0.5, 4 FOR i = 1 TO 5 CUTEND NEXT i