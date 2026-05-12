---
id: wiki.generated.ruledshell_2
type: wiki
category: 3d
commands: ["RULEDSHELL{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### RULEDSHELL{2}

- RULEDSHELL{2} topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4, defaultMat, n, m, g, status, offset, thickness, flipped, trimmingBody, preThickenTran_11, preThickenTran_12, preThickenTran_13, preThickenTran_14, preThickenTran_21, preThickenTran_22, preThickenTran_23, preThickenTran_24, preThickenTran_31, preThickenTran_32, preThickenTran_33, preThickenTran_34, firstpolyX_1, firstpolyY_1, firstpolyS_1,


... firstpolyX_n, firstpolyY_n, firstpolyS_n, secondpolyX_1, secondpolyY_1, secondpolyS_1,

... secondpolyX_m, secondpolyY_m, secondpolyS_m, profile2Tran_11, profile2Tran_12, profile2Tran_13, profile2Tran_14 profile2Tran_21, profile2Tran_22, profile2Tran_23, profile2Tran_24 profile2Tran_31, profile2Tran_32, profile2Tran_33, profile2Tran 34 generatrixFirstIndex_1, generatrixSecondIndex_1,

... generatrixFirstIndex_g, generatrixSecondIndex_g

RULEDSHELL{2} is an extension of the RULEDSHELL command with the possibility of hiding edges of surfaces, and edges between original and thickened surface. status: Status bits:

status = j1 + 2*j2, where each j can be 0 or 1. j1: Make edges invisible between original and thickened surface. j2: Make edges invisible on surfaces.