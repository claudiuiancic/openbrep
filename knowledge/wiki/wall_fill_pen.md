---
id: wiki.generated.wall_fill_pen
type: wiki
category: 3d
commands: ["WALL_FILL_PEN"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### WALL_FILL_PEN pen of the wall fill

WALL_COMPS_NAME name of the composite or complex structure of the wall the name of the profile attribute for complex wall, the name of the composite attribute for composite walls, empty string otherwise. WALL_BMAT_NAME name of the building material of the wall

building material name of the wall, empty string for composite or complex walls.

WALL_BMAT index of the building material of the wall Compatibility: introduced in Archicad 21. building material index of the wall, 0 for composite or complex walls.

WALL_SKINS_NUMBER number of composite or complex wall skins

range of 1to 127, 0 if single fill applied

WALL_SKINS_PARAMS parameters of the composite or complex wall skins

array with 19 columns with arbitrary number of rows:

- • [1] fill
- • [2] thickness
- • [3] (old contour pen)
- • [4] pen of fill
- • [5] pen of fill background
- • [6] core status
- • [7] upper line pen
- • [8] upper line type
- • [9] lower line pen
- • [10] lower line type
- • [11] end face pen
- • [12] fill orientation
- • [13] skin type
- • [14] end face line type
- • [15] finish skin status
- • [16] oriented fill status
- • [17] trapezoid/double slanted status
- • [18] building material index
- • [19] skin edge surface index (considering wall edge surface override). Compatibility: introduced in Archicad 22. core status: 0 - not part, 1 - part, 3 - last core skin. fill orientation: 0 - global, 1 - local. skin type: 0 - cut, 1 - below cutplane, 2 - above cutplane (all skin types are 0 for simple walls). trapezoid/double slanted: 0 - this skin has parallel faces in all circumstances, 1 - this skin might have non-parallel faces to adjust for the width difference of trapezoid walls or double slanted walls. Even if the wall faces are parallel, this flag can be turned on. finish skin status: 0 - not finish skin, 1 - finish skin. oriented fill status: 0 - global or local fill orientation as set in the "fill orientation" column, 1 - fill orientation and size match with the wall skin direction and thickness. For complex walls this variable contains only the data of the skins that are cut on the floor plan (2D - regarding floor plan cut height), or cut at D/W sill / wall end bottom height (3D).


WALL_SKINS_BMAT_NAMES building material names of the composite or complex wall skins array with 1 column: building material name of the skin and with arbitrary number of rows. For D/W and wall ends in the 3D window contains the data of the skins actually cut by the D/W or wall end.

WALL_SECT_PEN pen of the contours of the wall cut surfaces

applied on contours of cut surfaces both in floor plan and section/elevation windows

WALL_VIEW_PEN pen of the contours of the wall on view

applied on all edges in 3D window and on outline edges (edges on view below cutting plane) in floor plan and section/elevation window WALL_FBGD_PEN pen of the background of the fill of the wall WALL_DIRECTION direction of the wall

straight walls: the direction of the reference line, curved walls: the direction of the chord of the arc

WALL_POSITION absolute coordinates of the wall

array with 3 columns: x, y, z, which means the position of the wall’s starting point relative to the project origin

WALL_TEXTURE_WRAP texture wrapping data of the wall to be used in VERT and COOR{2}, or COOR{3} commands. The wall texture coordinates are transformed to match the local coordinate system of the wallconnected object (no additional transformations needed).

array with 14 rows:

- • [1]: wrapping_method
- • [2]: wrap_flags
- • [3]-[4]-[5]: origin_X, origin_Y, origin_Z (nodes of vert 1)
- • [6]-[7]-[8]: endOfX_X, endOfX_Y, endOfX_Z (nodes of vert 2)
- • [9]-[10]-[11]: endOfY_X, endOfY_Y, endOfY_Z (nodes of vert 3)
- • [12]-[13]-[14]: endOfZ_X, endOfZ_Y, endOfZ_Z (nodes of vert 4)