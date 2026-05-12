---
id: wiki.generated.revolvedshell_2
type: wiki
category: 3d
commands: ["REVOLVEDSHELL{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### REVOLVEDSHELL{2}

- REVOLVEDSHELL{2} topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4, defaultMat, n, status, offset, thickness, flipped, trimmingBody, alphaOffset, alpha, preThickenTran_11, preThickenTran_12, preThickenTran_13, preThickenTran_14, preThickenTran_21, preThickenTran_22, preThickenTran_23, preThickenTran_24, preThickenTran_31, preThickenTran_32, preThickenTran_33, preThickenTran_34, x_1, y_1, s_1,


... x_n, y_n, s_n

REVOLVEDSHELL{2} is an extension of the REVOLVEDSHELL command with the possibility of hiding edges of surfaces, and edges between original and thickened surface. status: Status bits:

status = j1 + 2*j2, where each j can be 0 or 1. j1: Make edges invisible between original and thickened surface. j2: Make edges invisible on surfaces.

Example: REVOLVEDSHELL "Paint-02", "Surf-Stucco Yellow",

"Surf-Stucco Yellow", "Surf-Stucco Yellow", "Surf-Stucco Yellow", "Surf-Stucco Yellow", "Surf-Stucco Yellow", 2, 0.00, 0.30, 0, 0, 0.00, 270.00, ! transformation matrix 0.00, 0.00, -1.00, 0.00, 0.00, 1.00, 0.00, 0.00, 1.00, 0.00, 0.00, 0.00, ! profile polyline 4.00, 0.00, 2, 0.00, 4.00, 2