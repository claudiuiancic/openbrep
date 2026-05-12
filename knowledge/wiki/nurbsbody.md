---
id: wiki.generated.nurbsbody
type: wiki
category: other
commands: ["NURBSBODY"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### NURBSBODY

NURBSBODY shadowStatus, smoothnessMin, smoothnessMax Composes a NURBS body defined with the above NURBS primitives. shadowStatus: status for shadow control:

shadowStatus = 32*j6 + 64*j7, where each j can be 0 or 1. j6: NURBS body always casts shadow independently from automatic preselection algorithm, j7: NURBS body never casts shadow. If neither j6 nor j7 are set, the automatic shadow preselection is performed. See the SHADOW command.

smoothnessMin, smoothnessMax: limits of automatically calculated smoothness parameter for tessellation of the surfaces and curves of body. The automatically calculated parameter will be always in the range 0 to 1 inclusive, so that smoothnessMin <= 0 means no lower limit and smoothnessMax >= 1 means no upper limit. If smoothnessMin > smoothnessMax, values will not affect the automatically calculated smoothness.

Any non-NURBS primitive statement (VERT, TEVE, EDGE, VECT, PGON, PIPG, BODY) or any compound statement (BRICK, CYLIND, PRISM, REVOLVE, etc.) causes the NURBS body under construction to be finished (implicit NURBSBODY statement). In this case smoothness limits will not be set and shadowStatus will be zero (status parameter of BODY statement will not be passed).

POINT CLOUDS