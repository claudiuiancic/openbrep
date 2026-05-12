---
id: wiki.generated.stair_breakmark_geometry
type: wiki
category: other
commands: ["STAIR_BREAKMARK_GEOMETRY"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### STAIR_BREAKMARK_GEOMETRY geometry of the breakmarks

|2D| |3D| |UI| |Parameter| |Property| |Default|{}|
|---|---|---|---|---|---|---|---|---|---|---|---|


Compatibility: introduced in Archicad 23.

- • .breakMarks[m]: (array) All shown breakmarks' geometry. The array size depends on the Floor Plan Display Layout of the Stair.
- • .breakMarks[m].isVisible: (boolean) Visibility attribute of the part of the stair that this break mark cuts.
- • .breakMarks[m].polyline2D{}: (dictionary) 2D polyline in the project coordinate system. Contains only the part between the stair's boundaries (without the extensions). The same data format as PolyOperations polylines, it can be sent directly to "StoreDictPolyline".
- • .breakMarks[m].polyline2D.isClosed: (boolean) 1 - closed polyline, 0 - open polyline (the last point given as an extra edge). Breakmarks are always open polylines.
- • .breakMarks[m].polyline2D.contour{}: (dictionary) contains data of the polyline
- • .breakMarks[m].polyline2D.contour.edges[n]: (array) contains an embedded dictionary for each edge of the polyline.
- • .breakMarks[m].polyline2D.contour.edges[n].type: (integer) 0 - straight, 1 - curved (circular arc)
- • .breakMarks[m].polyline2D.contour.edges[n].begPoint{}: (dictionary) an embedded dictionary for the 2D coordinates of the beginning point of the edge
- • .breakMarks[m].polyline2D.contour.edges[n].begPoint.x: (float)
- • .breakMarks[m].polyline2D.contour.edges[n].begPoint.y: (float)
- • .breakMarks[m].polyline2D.contour.edges[n].arcAngle: (angle) central angle of the edge curve, positive counter-clockwise, negative clockwise (not set for straight edges)


STAIR_VOLUME area of the stair including all 3D parts

|2D| |3D| |UI| |Parameter| |Property| |Default|0|
|---|---|---|---|---|---|---|---|---|---|---|---|


STAIR_HEIGHT difference between maximum and minimum of Z coordinates

|2D| |3D| |UI| |Parameter| |Property| |Default|0|
|---|---|---|---|---|---|---|---|---|---|---|---|


STAIR_WALKLINE_LENGTH projected 2D length of the stair's walking line

|2D| |3D| |UI| |Parameter| |Property| |Default|0|
|---|---|---|---|---|---|---|---|---|---|---|---|


STAIR_DEFAULT_WIDTH default width of stair (as set in the Stair Default Settings/Geometry and Positioning panel)

|2D| |3D| |UI| |Parameter| |Property| |Default|0|
|---|---|---|---|---|---|---|---|---|---|---|---|


STAIR_DEFAULT_GOING_DEPTH default depth of going (as set in the Stair Default Settings/Geometry and Positioning panel)

|2D| |3D| |UI| |Parameter| |Property| |Default|0|
|---|---|---|---|---|---|---|---|---|---|---|---|


STAIR_DEFAULT_RISER_HEIGHT default width of riser (as set in the Stair Default Settings/Geometry and Positioning panel)

|2D| |3D| |UI| |Parameter| |Property| |Default|0|
|---|---|---|---|---|---|---|---|---|---|---|---|


STAIR_DEFAULT_TREAD_THICKNESS default tread thickness of stair (as set in the Stair Default Settings/Geometry and Positioning panel)

|2D| |3D| |UI| |Parameter| |Property| |Default|0|
|---|---|---|---|---|---|---|---|---|---|---|---|


STAIR_NR_OF_TREADS_IN_FLIGHTS integer array with one dimension ([n]) number of treads in each flight of the stair (n = number

of flights)

|2D| |3D| |UI| |Parameter| |Property| |Default|0|
|---|---|---|---|---|---|---|---|---|---|---|---|


STAIR_NR_OF_RISERS_IN_FLIGHTS integer array with one dimension ([n]) number of risers in each flight of the stair (n = number of

flights)

|2D| |3D| |UI| |Parameter| |Property| |Default|0|
|---|---|---|---|---|---|---|---|---|---|---|---|


STAIR_NR_OF_RISERS number of risers regarding the whole stair

|2D| |3D| |UI| |Parameter| |Property| |Default|0|
|---|---|---|---|---|---|---|---|---|---|---|---|


STAIR_NR_OF_TREADS number of treads regarding the whole stair

|2D| |3D| |UI| |Parameter| |Property| |Default|0|
|---|---|---|---|---|---|---|---|---|---|---|---|


STAIR_LANDING_NUMBER number of landing sections regarding the whole stair

|2D| |3D| |UI| |Parameter| |Property| |Default|0|
|---|---|---|---|---|---|---|---|---|---|---|---|


STAIR_STAIR_GRADIENT stair inclination: the angle of the riser/going ratio in radian

|2D| |3D| |UI| |Parameter| |Property| |Default|0|
|---|---|---|---|---|---|---|---|---|---|---|---|


STAIR_RULE_LIMITS length/angle array with two dimensions ([6][2]), collection of minimum and maximum values set in

Stair Default Settings/Rules and Standards/Treads and Risers panel

|2D| |3D| |UI| |Parameter| |Property| |Default|[0]|
|---|---|---|---|---|---|---|---|---|---|---|---|


Project Preferences setting of the visibility of these values does not affect the variable.

- • [1][1] - [1][2]: Riser height (R) minimum and maximum value
- • [2][1] - [2][2]: Going (G) minimum and maximum value
- • [3][1] - [3][2]: 2 Riser + 1 Going (2*R + G) minimum and maximum value
- • [4][1] - [4][2]: Riser / Going ratio (R / G) minimum and maximum value
- • [5][1] - [5][2]: Riser + Going (R + G) minimum and maximum value
- • [6][1] - [6][2]: Stair pitch minimum and maximum value


STAIR_RULE_FLAGS boolean array with two dimensions ([6][2]), enable/disable status collection of limits in accordance with STAIR_RULE_LIMITS, set in Stair Default Settings/Rules and Standards/Treads and Risers panel

|2D| |3D| |UI| |Parameter| |Property| |Default|[0]|
|---|---|---|---|---|---|---|---|---|---|---|---|


Value indexes are parallel to STAIR_RULE_LIMITS. Possible values:

- • 0 - limit option of the same index in STAIR_RULE_LIMITS is currently not used
- • 1 - limit option of the same index in STAIR_RULE_LIMITS is currently in use