---
id: wiki.generated.revolvedshellangular
type: wiki
category: 3d
commands: ["REVOLVEDSHELLANGULAR"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### REVOLVEDSHELLANGULAR

REVOLVEDSHELLANGULAR topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4, defaultMat, n, offset, thickness, flipped, trimmingBody, alphaOffset, alpha, segmentationType, nOfSegments, preThickenTran_11, preThickenTran_12, preThickenTran_13, preThickenTran_14, preThickenTran_21, preThickenTran_22, preThickenTran_23, preThickenTran_24, preThickenTran_31, preThickenTran_32, preThickenTran_33, preThickenTran_34, x_1, y_1, s_1,

... x_n, y_n, s_n

An angular variant of the REVOLVEDSHELL command. Parameters are the same with the addition of the following extra parameters: segmentationType: Must be either 1 or 2.

1: means that 360 degrees of revolution is split into nOfSegments segments, 2: means that the actual revolution angle (given by the alpha parameter) is split into nOfSegments segments.

nOfSegments: Number of segments, see segmentationType parameter above.