---
id: wiki.generated.creategroupwithmaterial
type: wiki
category: other
commands: ["CREATEGROUPWITHMATERIAL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### CREATEGROUPWITHMATERIAL

CREATEGROUPWITHMATERIAL (g_expr, repl_directive, pen, material) Returns a group that is created by replacing all pens and/or materials in group g_expr.

g_expr: group expression identifying the base group. repl_directive:

repl_directive = j1 + 2*j2 + 4*j3 + 8*j4, where each j can be 0 or 1. j1: replace pen, j2: replace material, j4: make edges invisible.

pen: replacement pen index. material: replacement material index.

BINARY 3D