---
id: wiki.generated.extrudedshell_3
type: wiki
category: 3d
commands: ["EXTRUDEDSHELL{3}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### EXTRUDEDSHELL{3}

EXTRUDEDSHELL{3} topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4, defaultMat, n, status, offset, thickness, flipped, trimmingBody, x_tb, y_tb, x_te, y_te, topz, tangle, x_bb, y_bb, x_be, y_be, bottomz, bangle, preThickenTran_11, preThickenTran_12, preThickenTran_13, preThickenTran_14, preThickenTran_21, preThickenTran_22, preThickenTran_23, preThickenTran_24, preThicakenTran_31, preThickenTran_32, preThickenTran_33, preThickenTran_34, x_1, y_1, s_1,

... x_n, y_n, s_n

- EXTRUDEDSHELL{3} is an extension of the EXTRUDEDSHELL{2} command with the possibility of using inline material definition, that means materials defined in GDL script locally also can be used next to materials defined in global material definitions.