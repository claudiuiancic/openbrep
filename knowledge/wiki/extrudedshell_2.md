---
id: wiki.generated.extrudedshell_2
type: wiki
category: 3d
commands: ["EXTRUDEDSHELL{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### EXTRUDEDSHELL{2}

EXTRUDEDSHELL{2} topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4, defaultMat, n, status, offset, thickness, flipped, trimmingBody, x_tb, y_tb, x_te, y_te, topz, tangle, x_bb, y_bb, x_be, y_be, bottomz, bangle, preThickenTran_11, preThickenTran_12, preThickenTran_13, preThickenTran_14, preThickenTran_21, preThickenTran_22, preThickenTran_23, preThickenTran_24, preThicakenTran_31, preThickenTran_32, preThickenTran_33, preThickenTran_34, x_1, y_1, s_1,

... x_n, y_n, s_n

- EXTRUDEDSHELL{2} is an extension of the EXTRUDEDSHELL command with the possibility of hiding edges between original and thickened surface. status: Status bits:


status = j1, where each j can be 0 or 1. j1: Make edges invisible between original and thickened surface.

Example:

EXTRUDEDSHELL "Paint-02", "Surf-Stucco Yellow", "Surf-Stucco Yellow", "Surf-Stucco Yellow", "Surf-Stucco Yellow", "Surf-Stucco Yellow", "Surf-Stucco Yellow", 3, 0.00, 0.30, 0, 0, ! 2 slant planes

- 0.00, 0.00, 0.00, 1.00, 0.00, 0.00,

- 0.00, 0.00, 0.00, 1.00, -10.00, 0.00, ! transformation matrix
- 0.00, 0.00, 1.00, 0.00,


- 1.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.00, 0.00, ! profile polyline
- 2.00, 0.00, 15, 0.00, 2.00, 15,


-2.00, 0.00, 15