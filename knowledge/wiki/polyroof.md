---
id: wiki.generated.polyroof
type: wiki
category: 3d
commands: ["POLYROOF"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### POLYROOF

POLYROOF defaultMat, k, m, n, offset, thickness, applyContourInsidePivot, z_1, ..., z_k, pivotX_1, pivotY_1, pivotMask_1, roofAngle_11, gableOverhang_11, topMat_11, bottomMat_11,

... roofAngle_1k, gableOverhang_1k, topMat_1k, bottomMat_1k,

... pivotX_m, pivotY_m, pivotMask_m, roofAngle_m1, gableOverhang_m1, topMat_m1, bottomMat_m1,

... roofAngle_mk, gableOverhang_mk, topMat_mk, bottomMat_mk, contourX_1, contourY_1, contourMask_1, edgeTrim_1, edgeAngle_1, edgeMat_1,

... contourX_n, contourY_n, contourMask_n, edgeTrim_n, edgeAngle_n, edgeMat_n

The command creates a possibly multi-level roof in which the geometry is controlled by multiple parameters, most importantly the roof angles and two polygons: a pivot polygon and a contour polygon. At the pivot polygon, the roof is slanted at the roof angle. It ascends until it either

reaches the height of the next level or until it is eliminated by its sides encountering one another. It also descends downwards, until it reaches the contour polygon, which cuts off parts of the roof outside of it. The contour polygon can also be used to cut holes in the roof. defaultMat: the numeric index of the "inner" material of the roof. This material becomes visible at gables and at cut surfaces, e.g., if

the roof is cut by a plane.

- k: the number of levels. m: the number of pivot polygon vertices. n: the number of contour polygon vertices. offset: an offset for the thickness of the roof. thickness: the thickness of the roof.


applyContourInsidePivot: if set to 0, the outer contour polygon is only applied below the pivot polygon plane. If set to 1, the outer contour polygon is applied both above and below the pivot polygon plane. The 0 setting may be used to prevent the contour polygon from cutting off gables that lean outwards.

z_i: the Z coordinate of a level. pivotX_i, pivotY_i: coordinates of the pivot polygon vertices. pivotMask_i:

0: marks a normal vertex,

-1: marks the end of the current pivot subpolygon (outer contour or hole). Data for such a vertex must be a copy of the data for the first vertex of the subpolygon. A polygon must always be closed with a mask value of -1, even if there are no holes inside it.

roofAngle_i: angle of slant for a pivot edge on a given level. If the angle >= 90, that part of the roof becomes a gable. gableOverhang_i: at the sides of a gable, the roof can extend over a lower level of itself. The amount of this can be controlled by this

parameter, which has effect only on gables (roofAngle >= 90) that are at least on the second level of the roof. topMat_i, bottomMat_i: the numeric index of the materials for the top and bottom of the roof. contourX_i, contourY_i: coordinates of the contour polygon vertices. contourMask_i:

0: marks a normal vertex,

-1: marks the end of the current contour subpolygon (outer contour or hole). Data for such a vertex must be a copy of the data for the first vertex of the subpolygon. A polygon must always be closed with a mask value of -1, even if there are no holes inside it.

edgeTrim_i: specifies the way the edge is trimmed by the contour polygon. Possible values are:

- 0: Vertical,


- 1: Perpendicular to roof plane,
- 2: Horizontal,
- 3: Custom angle to roof plane.


edgeAngle_i: the custom angle of the edge to the roof plane. It has effect only if edgeTrim is set to 3 (custom angle to roof plane). edgeMat_i: numeric index of the material at the edge the roof, where the contour cuts it

defaultEdgeMat

topMat22

bottomMat42

bottomMat41

topMat21

gableOverhang12 sideMat2

edgeMat1

topMat11

Figure 1: Materials

roofAngle22

roofAngle21 edgeAngle4

Figure 2: Angles

Example: POLYROOF "Paint-01",

2, 5, 5, 0, 0.2, 0, ! Start of z values 2.7, 3.2, ! Start of pivot polygon 2, 8, 0, 45, 0, ind(material, "Paint-01"), ind(material, "Paint-01"), 90, 0.5, ind(material, "Paint-01"), ind(material, "Paint-01"), 2, 3, 0, 45, 0, ind(material, "Paint-01"), ind(material, "Paint-01"), 65, 0, ind(material, "Paint-01"), ind(material, "Paint-01"), 10, 3, 0, 45, 0, ind(material, "Paint-01"), ind(material, "Paint-01"), 65, 0, ind(material, "Paint-01"), ind(material, "Paint-01"), 10, 8, 0, 45, 0, ind(material, "Paint-01"), ind(material, "Paint-01"), 65, 0, ind(material, "Paint-01"), ind(material, "Paint-01"), 2, 8, -1, 45, 0, ind(material, "Paint-01"), ind(material, "Paint-01"), 90, 0.5, ind(material, "Paint-01"), ind(material, "Paint-01"), ! Start of contour polygon 1.5, 8.5, 0, 0, 0, ind(material, "Paint-01"), 1.5, 2.5, 0, 0, 0, ind(material, "Paint-01"), 10.5, 2.5, 0, 0, 0, ind(material, "Paint-01"), 10.5, 8.5, 0, 0, 0, ind(material, "Paint-01"), 1.5, 8.5, -1, 0, 0, ind(material, "Paint-01")

Output: see Figure 1