---
id: wiki.generated.polygon
type: wiki
category: 3d
commands: ["POLYGON"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### POLYGON OPERATIONS EXTENSION

This add-on calculates result polygons based on the input polygons and the operation that is carried out on them. Compatibility: introduced in Archicad 21: There are operations for polylines as well. Input polygons are identified by a name when passed to the add-on and are stored in a previously defined container. Result polygons are automatically named by the add-on and are stored in a second, target container. Input and result polygons are thus stored in different containers. Multiple polygons, possibly with an even greater number of contours, can be created by a single operation. These will be administered as individual polygons in the target container. As a result, these polygons can be accessed in subsequent polygon operations. The principle is the same as with the Solid Geometry Commands (see in the section called “Solid Geometry Commands”). Input polygons must be contiguous. A polygon is defined by several contours, each of which is an uninterrupted sequence of connected vertices. The first contour is the outer boundary. The subsequent contours must all be inside the first, they may not overlap, and they create cutouts of the first polygon. Polylines do not have to be closed, but cannot have multiple contours.