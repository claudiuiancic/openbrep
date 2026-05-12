---
id: wiki.generated.polyroof_4
type: wiki
category: 3d
commands: ["POLYROOF{4}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### POLYROOF{4}

- POLYROOF{4} defaultMat, mask, k, m, n, offset, thickness, totalThickness, applyContourInsidePivot, z_1, ..., z_k, pivotX_1, pivotY_1, pivotMask_1, roofAngle_11, gableOverhang_11, topMat_11, bottomMat_11,


... roofAngle_1k, gableOverhang_1k, topMat_1k, bottomMat_1k,

... pivotX_m, pivotY_m, pivotMask_m, roofAngle_m1, gableOverhang_m1, topMat_m1, bottomMat_m1,

... roofAngle_mk, gableOverhang_mk, topMat_mk, bottomMat_mk, contourX_1, contourY_1, contourMask_1, edgeTrim_1, edgeAngle_1, edgeMat_1,

... contourX_n, contourY_n, contourMask_n, edgeTrim_n, edgeAngle_n, edgeMat_n

- POLYROOF{4} is an extension of the POLYROOF{3} command with the possibility of using inline material definition, that means materials defined in GDL script locally also can be used next to materials defined in global material definitions.