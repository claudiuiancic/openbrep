---
id: wiki.generated.revolvedshellangular_2
type: wiki
category: 3d
commands: ["REVOLVEDSHELLANGULAR{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### REVOLVEDSHELLANGULAR{2}

REVOLVEDSHELLANGULAR{2} topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4, defaultMat, n, status, offset, thickness, flipped, trimmingBody, alphaOffset, alpha, segmentationType, nOfSegments, preThickenTran_11, preThickenTran_12, preThickenTran_13, preThickenTran_14, preThickenTran_21, preThickenTran_22, preThickenTran_23, preThickenTran_24, preThickenTran_31, preThickenTran_32, preThickenTran_33, preThickenTran_34, x_1, y_1, s_1,

... x_n, y_n, s_n

- REVOLVEDSHELLANGULAR{2} is an extension of the REVOLVEDSHELLANGULAR command with the possibility of hiding edges of surfaces, and edges between original and thickened surface. status: Status bits:

status = j1 + 2*j2, where each j can be 0 or 1.

- j1: Make edges invisible between original and thickened surface.
- j2: Make edges invisible on surfaces.


- REVOLVEDSHELLANGULAR{3}


REVOLVEDSHELLANGULAR{3} topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4, defaultMat, n, status, offset, thickness, flipped, trimmingBody, alphaOffset, alpha, segmentationType, nOfSegments, preThickenTran_11, preThickenTran_12, preThickenTran_13, preThickenTran_14, preThickenTran_21, preThickenTran_22, preThickenTran_23, preThickenTran_24, preThickenTran_31, preThickenTran_32, preThickenTran_33, preThickenTran_34, x_1, y_1, s_1,

... x_n, y_n, s_n

- REVOLVEDSHELLANGULAR{3} is an extension of the REVOLVEDSHELLANGULAR{2} command with the possibility of using inline material definition, that means materials defined in GDL script locally also can be used next to materials defined in global material definitions.