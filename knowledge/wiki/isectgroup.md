---
id: wiki.generated.isectgroup
type: wiki
category: other
commands: ["ISECTGROUP"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### ISECTGROUP

ISECTGROUP (g_expr1, g_expr2) ISECTGROUP{2} (g_expr1, g_expr2, edgeColor, materialId, materialColor [, operationStatus]) ISECTGROUP{3} (g_expr1, g_expr2, edgeColor, materialId, materialColor [, operationStatus])

g_expr1: identifier of the base group. g_expr2: identifier of the tool group. edgeColor: the color of the new edge when it differs from 0. materialId: the material of the new face when it differs from 0. materialColor: the color of the new face when the materialId is 0 and it differs from 0. operationStatus: status control of the operation.

operationStatus = j1 + 2*j2, where each j can be 0 or 1. j1: generated new edges will be invisible. j2: cut polygons of the result inherit material and texture projection from the corresponding polygons of the tool group.