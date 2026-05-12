---
id: wiki.generated.polyroof_2
type: wiki
category: 3d
commands: ["POLYROOF{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### POLYROOF{2}

- POLYROOF{2} defaultMat, k, m, n, offset, thickness, totalThickness, applyContourInsidePivot, z_1, ..., z_k, pivotX_1, pivotY_1, pivotMask_1, roofAngle_11, gableOverhang_11, topMat_11, bottomMat_11,

... roofAngle_1k, gableOverhang_1k, topMat_1k, bottomMat_1k,

... pivotX_m, pivotY_m, pivotMask_m, roofAngle_m1, gableOverhang_m1, topMat_m1, bottomMat_m1,

... roofAngle_mk, gableOverhang_mk, topMat_mk, bottomMat_mk, contourX_1, contourY_1, contourMask_1, edgeTrim_1, edgeAngle_1, edgeMat_1,

... contourX_n, contourY_n, contourMask_n, edgeTrim_n, edgeAngle_n, edgeMat_n

- POLYROOF{2} is an extension of the POLYROOF command with the possibility of defining the total thickness of the roof. This parameter should be considered together with offset and thickness, when the generation of a slice of the roof is desirable. In this case the thickness and the offset should be set to the thickness of the slice and to the distance between the top planes of the slice and the complete roof respectively. totalThickness: the total thickness of the roof.
- POLYROOF{3}


- POLYROOF{3} defaultMat, mask, k, m, n, offset, thickness, totalThickness, applyContourInsidePivot, z_1, ..., z_k, pivotX_1, pivotY_1, pivotMask_1, roofAngle_11, gableOverhang_11, topMat_11, bottomMat_11,


... roofAngle_1k, gableOverhang_1k, topMat_1k, bottomMat_1k,

... pivotX_m, pivotY_m, pivotMask_m, roofAngle_m1, gableOverhang_m1, topMat_m1, bottomMat_m1,

... roofAngle_mk, gableOverhang_mk, topMat_mk, bottomMat_mk, contourX_1, contourY_1, contourMask_1, edgeTrim_1, edgeAngle_1, edgeMat_1,

... contourX_n, contourY_n, contourMask_n, edgeTrim_n, edgeAngle_n, edgeMat_n

- POLYROOF{3} is an extension of the POLYROOF{2} command with the possibility of controlling the global behavior of the generated roof. mask: controls the global behavior of the generated roof.


mask = j1 + 2*j2, where each j can be 0 or 1. j1: edges participate in line elimination. j2: Make all edges invisible.

Example:

pen 1 mat = IND (MATERIAL, "Metal-Aluminium") a = -0.4242640691048 : b = 4.424264068326 c = 6.424264068326

- POLYROOF{3} mat,1, 2, 5, 5, 0, 0.3, 0.3, 1, 0, 1, a, b, 0, 45, 0, mat, mat, 90, 0, mat, mat,


- a, a, 0, 45, 0, mat, mat, 90, 0, mat, mat, c, a, 0, 45, 0, mat, mat, 90, 0, mat, mat, c, b, 0, 45, 0, mat, mat, 90, 0, mat, mat,
- a, b, -1,45, 0, mat, mat, 90, 0, mat, mat,


- -0.8, -0.8, 0, 2, 0, mat, 6.8, -0.8, 0, 2, 0, mat, 6.8, 4.8, 0, 2, 0, mat,
- -0.8, 4.8, 0, 2, 0, mat,
- -0.8, -0.8, -1, 2, 0, mat


a = 0.1514718617904 : b = 3.848528136652 c = 5.848528136652 : q = 0.5757359305057

- w = 5.424264067936 : e = 3.424264056692


- POLYROOF{3} mat,1, 1, 5, 5, 0, 0.3, 0.3, 1, 0.5757359312847, a, b, 0, 45, 0, mat, mat,


- a, a, 0, 45, 0, mat, mat, c, a, 0, 45, 0, mat, mat, c, b, 0, 45, 0, mat, mat,
- a, b, -1, 45, 0, mat, mat, q, q, 0, 0, 0, mat, w, q, 0, 0, 0, mat, w, e, 0, 0, 0, mat, q, e, 0, 0, 0, mat, q, q, -1, 0, 0, mat