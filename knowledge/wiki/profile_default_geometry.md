---
id: wiki.generated.profile_default_geometry
type: wiki
category: other
commands: ["PROFILE_DEFAULT_GEOMETRY"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PROFILE_DEFAULT_GEOMETRY

n = REQUEST("PROFILE_DEFAULT_GEOMETRY", name_or_index, n1, n2, ..., nm, x11, y11, edgeVisible11, vertEdgeVisible11, additionalStatus11, ..., x1n1, y1n1, edgeVisible1n1, vertEdgeVisible1n1, additionalStatus1n1, x21, y21, edgeVisible21, vertEdgeVisible21, additionalStatus21, ..., x2n2, y2n2, edgeVisible2n2, vertEdgeVisible2n2, additionalStatus2n2,

..., xm1, ym1, edgeVisiblem1, vertEdgeVisiblem1, additionalStatusm1, ..., xmnm, ymnm, edgeVisiblemnm, vertEdgeVisiblemnm, additionalStatusmnm)

Returns the original geometric data of the profile identified by name or index. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning. n1...ni: then number of contour nodes in each profile component. The total number of profile components (m) can be returned by the

"PROFILE_COMPONENTS" REQUEST. edgeVisiblei: contour starting from i node is visible. vertEdgeVisiblei: vertical edge starting from i node is visible, usable in 3D (0 in case of segmented polygon). additionalStatusi: used for segments and arcs of the polyline (set centerpoint = 900, arc using centerpoint and angle = 4000, etc.),

or to mark the contour end control point (-1, this case the vertEdgeVisiblei and edgeVisiblei are set to 0 automatically). The status parameters returned in this structure support different status type definitions of poly2, cprism, tube. Each format can be calculated with the following method:

Compatibility: introduced in Archicad 21. Example:

poly2Status = edgeVisible + additionalStatus prismStatus = additionalStatus tubeStatus = additionalStatus if additionalStatus >= 0 then ! not contour end

if edgeVisible then

prismStatus = prismStatus + 15 ! j1, j2, j3, j4 endif if verticalEdgeVisible = 0 then

prismStatus = prismStatus + 64 ! j7 ! in tube, lateral edges starting from the node are used for showing the contour tubeStatus = tubeStatus + 1

endif endif