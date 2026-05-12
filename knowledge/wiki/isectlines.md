---
id: wiki.generated.isectlines
type: wiki
category: other
commands: ["ISECTLINES"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### ISECTLINES

ISECTLINES (g_expr1, g_expr2)

Group operations: addition, subtraction, intersection, intersection lines. The return value is a new group, which can be placed using the PLACEGROUP command, stored in a variable or used as a parameter in another group operation. Group operations can be performed between previously defined groups or groups result from any other group operation. g_expr1, g_expr2 are group type expressions. Group type expressions are either group names (string expressions) or group type variables or any combination of these in operations which result in groups. Note that the operations ADDGROUP, ISECTGROUP and ISECTLINES are symmetric in their parameterization while the order of parameter matters for SUBGROUP.