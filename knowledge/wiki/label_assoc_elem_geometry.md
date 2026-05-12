---
id: wiki.generated.label_assoc_elem_geometry
type: wiki
category: other
commands: ["LABEL_ASSOC_ELEM_GEOMETRY"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### LABEL_ASSOC_ELEM_GEOMETRY reference line of the of the associated element

|2D| |3D| |UI| |Parameter| |Property| |Default|{}|
|---|---|---|---|---|---|---|---|---|---|---|---|


Compatibility: introduced in Archicad 23. Only valid when the associated element is a wall.

- • .referenceLine2D{}: (dictionary) 2D reference line in the project coordinate system. Basic walls with Polygonal Geometry Method can have multiple edges. The same data format as PolyOperations polylines, it can be sent directly to "StoreDictPolyline".
- • .referenceLine2D.isClosed: (boolean) 1 - closed polyline, 0 - open polyline (the last point given as an extra edge). Reference lines are always open polylines.
- • .referenceLine2D.contour{}: (dictionary) contains data of the polyline
- • .referenceLine2D.contour.edges[n]: (array) contains an embedded dictionary for each edge of the polyline.
- • .referenceLine2D.contour.edges[n].type: (integer) 0 - straight, 1 - curved (circular arc)
- • .referenceLine2D.contour.edges[n].begPoint{}: (dictionary) an embedded dictionary for the 2D coordinates of the beginning point of the edge
- • .referenceLine2D.contour.edges[n].begPoint.x: (float)
- • .referenceLine2D.contour.edges[n].begPoint.y: (float)
- • .referenceLine2D.contour.edges[n].arcAngle: (angle) central angle of the edge curve, positive counter-clockwise, negative clockwise (not set for straight edges)


LABEL_ROTANGLE absolute rotation angle data for GDL symbol type labels

|2D| |3D| |UI| |Parameter| |Property| |Default|0|
|---|---|---|---|---|---|---|---|---|---|---|---|


The angle is calculated according to Label Orientation, Fixed Angle, and readability settings. Compatibility: parameter and property script restrictions are introduced in Archicad 22. View-dependent value in case of "Fixed Angle" ON. Project-dependent in case "Label Orientation" is set to "Parallel" or "Perpendicular": the parent element can be moved, thus changing the value of the variable.

LABEL_ARROWHEAD_PEN pen of the arrowhead LABEL_HAS_POINTER Boolean

1 - "Add/Remove Pointer" is checked on "Label Settings/Pointer" panel, 0 otherwise. Compatibility: introduced in Archicad 22. The similar, reverse-working global variable "LABEL_CUSTOM_ARROW" is considered deprecated since Archicad 22.