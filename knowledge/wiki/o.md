---
id: wiki.generated.o
type: wiki
category: other
commands: ["O"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### O

OPENING_CENTERHEIGHT_VALUES - dictionary, relative elevation of the center of the opening from specific reference levels

OPENING_HEADERHEIGHT_VALUES - dictionary, relative elevation of the header of the opening

(or topmost point if rotated) from specific reference levels OPENING_HEIGHT - length, nominal height of the opening OPENING_SILLHEIGHT_VALUES - dictionary, relative elevation of the sill of the opening (or

lowest point if rotated) from specific reference levels OPENING_SYMBOL_DISPLAY - integer, visibility of the opening symbol according to the Floor Plan Cut Plane (view dependent, do not use in parameter/property scripts) OPENING_SYMBOL_GEOMETRY - dictionary, contains the geometry of the symbol (view dependent, do not use in parameter/property scripts) OPENING_WIDTH - length, nominal width of the opening

- R RAIL2D_CUSTOMDISPLAY - contains information about the model view settings of the railing.


RAIL2D_FULL_POLYGON_FLAGS - array with two dimensions ([n][1]), where n is the number of points in the panel/rail/rail end symbol polygon. Contains visibility data of edges.

RAIL2D_FULL_POLYGON_GEOM - array with two dimensions ([n][3]), where n is the number of points in the panel/rail/rail end symbol polygon. Contains geometric data of the railing panel.

RAIL2D_FULL_POLYLINE_FLAGS - array with two dimensions ([n][1]), where n is the number of points in the panel/rail/rail end axis polyline. Contains visibility data of edges.

RAIL2D_FULL_POLYLINE_GEOM - array with two dimensions ([n][3]), where n is the number of points in the panel/rail/rail end axis polyline. Contains geometric data of the railing panel.

RAIL2D_FULL_VISIBILITY - type of the active attribute set of the current railing drawing.

RAIL2D_LOWER_POLYGON_FLAGS - array with two dimensions ([n][1]), where n is the number of points in the panel/rail/rail end symbol polygon below the first breakmark. Contains visibility data of polygon edges.

RAIL2D_LOWER_POLYGON_GEOM - array with two dimensions ([n][3]), where n is the number of points in the panel/rail/rail end symbol polygon below the first breakmark. Contains geometric data of the railing panel polygon.

RAIL2D_LOWER_POLYLINE_FLAGS - array with two dimensions ([n][1]), where n is the number of points in the panel/rail/rail end axis polyline below the first breakmark. Contains visibility data of edges.

RAIL2D_LOWER_POLYLINE_GEOM - array with two dimensions ([n][3]), where n is the number of points in the panel/rail/rail end axis polyline below the first breakmark. Contains geometric data of the railing panel polyline.

RAIL2D_LOWER_VISIBILITY - type of the active attribute set of the current railing drawing below the first breakmark.

RAIL2D_MIDDLE_POLYGON_FLAGS - array with two dimensions ([n][1]), where n is the number of points in the panel/rail/rail end symbol polygon between breakmarks. Contains visibility data of polygon edges.

RAIL2D_MIDDLE_POLYGON_GEOM - array with two dimensions ([n][3]), where n is the number of points in the panel/rail/rail end symbol polygon between breakmarks. Contains geometric data of the railing panel polygon.

RAIL2D_MIDDLE_POLYLINE_FLAGS - array with two dimensions ([n][1]), where n is the number of points in the panel/rail/rail end axis polyline between breakmarks. Contains visibility data of edges.

RAIL2D_MIDDLE_POLYLINE_GEOM - array with two dimensions ([n][3]), where n is the number of points in the panel/rail/rail end axis polyline between breakmarks. Contains geometric data of the railing panel polyline.

RAIL2D_MIDDLE_VISIBILITY - type of the active attribute set of the current railing drawing between breakmarks.

RAIL2D_UPPER_POLYGON_FLAGS - array with two dimensions ([n][1]), where n is the number of points in the panel/rail/rail end symbol polygon above the last breakmark. Contains visibility data of polygon edges.

RAIL2D_UPPER_POLYGON_GEOM - array with two dimensions ([n][3]), where n is the number of points in the panel/rail/rail end symbol polygon above the last breakmark. Contains geometric data of the railing panel polygon.

RAIL2D_UPPER_POLYLINE_FLAGS - array with two dimensions ([n][1]), where n is the number of points in the panel/rail/rail end axis polyline above the last breakmark. Contains visibility data of edges.

RAIL2D_UPPER_POLYLINE_GEOM - array with two dimensions ([n][3]), where n is the number of points in the panel/rail/rail end axis polyline above the last breakmark. Contains geometric data of the railing panel polyline.

RAIL2D_UPPER_VISIBILITY - type of the active attribute set of the current railing drawing above the last breakmark.

RAILINGEND_DIRECTION_AND_ANGLE - array with two dimensions ([n][5]), vector data pointing away from the connecting rail in a tangential direction. For two ends of a straight rail, these vectors are opponent in direction.

RAILINGPANEL_FLAGS - array with two dimensions ([n][3]), where n is the number of panel nodes (n > 3) in accordance with RAILINGPANEL_GEOMETRY. Contains geometric data of the current railing panel edges, cutting planes applied.

RAILINGPANEL_GEOMETRY - array with two dimensions ([n][5]), where n is the number of

panel nodes (n > 3). Contains geometric data of the current railing panel, cutting planes applied.

RAILINGPANEL_SIDE_OFFSETS - array with one dimension ([4]), contains the panel offsets as set in the Railing Settings dialog, distance of neihbouring element axes in a vertical plane, slanting and skewing disregarded.

RAILINGPANEL_SKEW_ANGLE - skew angle in degrees, parallel to walking direction. Vertical is 0 degrees, positive values mean backward, negative values mean forward skewing according

to walking direction (angle < 90). Curved segments: measured on the start tangential plane of the segment (before slanting).

RAILINGPANEL_SLANT_ANGLE - slant angle in degrees, perpendicular to walking direction. Vertical is 0 degrees, positive values mean left side, negative values mean right side of walking direction (angle < 90). Curved segments: measured on plane perpendicular to the start tangential plane of the segment (before skewing).

RAILINGPANEL_TYPE - generic geometry type of the panel. RAILINGPANEL_UNCUT_GEOMETRY - array with two dimensions ([n][4]), where n is the number

of panel nodes (n > 3). Contains geometric data of the current railing panel, complete raw geometry (without cuts).

RAILINGPOST_CUTS - array with two dimensions ([2][3]), defines the orientation of the end surfaces of the post

RAILINGPOST_SEGMENT_CUTS - array with two dimensions ([2][4]), contains the vector parameters of two planes used to cut inner posts and balusters at the boundary of the segment, when the railing is slanted

RAILINGPOST_TOP_COORD - array with one dimension ([3]), coordinates of the top of the

current post RAILINGPOST_TYPE - contains the subelement type the current library part is selected for. RAILING_3DLENGTH - full 3D length of the railing RAILING_HEIGHT - height of the railing segment (as set in Railing Settings Dialog /

Segment Settings) RAILING_HORIZONTAL_LENGTH - full projected 2D length of the railing RAILING_NR_OF_BALUSTERS - number of balusters in the railing RAILING_NR_OF_PANELS - number of panels in the railing RAILING_NR_OF_POSTS - number of posts in the railing RAILING_NR_OF_RAILS - number of rails in the railing

RAILING_NR_OF_SEGMENTS - number of segments in the railing RAILING_REFLINE_DISTANCE - array with one dimension ([2]), horizontal offsets of rail

element from railing reference line. RAILING_VOLUME - volume of the railing (including all subelements) RAILPOST2D_VISIBILITY - type of the active attribute set of the current post drawing. RAIL_COMPONENTS - array with one dimension ([3]), contains additional information about

the rail. RAIL_CONNECTING_POSTS - array with two dimensions ([n][2]), where n is the number of posts

or inner posts along the rail. Contains position data of these intersecting elements. RAIL_CONNECTING_POSTS_NUM - number of posts and inner posts intersecting the rail. RAIL_CUTS - array with two dimensions ([2][4]), defines the orientation of the end surfaces

of the rail RAIL_DISCONNECTED_CUTS - array with two dimensions ([2][4]), defines the orientation of the end surfaces in case of disconnected connection. RAIL_POLYLINE_GEOMETRY - array with two dimensions ([n][5]), where n is the number of railing nodes (n > 2). Contains geometric data of the current railing, all segments. RAIL_SEGMENT_FLAGS - array with one dimension ([n]), where n is the number of railing nodes (n > 2). Contains geometric data of the current railing, all segments. RAIL_SLANT_ANGLE - rail slant angle in degrees relative to vertical direction,

perpendicular to walking direction. RAIL_TYPE - contains the subelement type the current library part is selected for. RISER_BMATS - array with one dimension ([n]), building materials of the selected (current)

riser (n = number of building materials) RISER_CUT - array with two dimensions ([2][2]), contains data of starting and closing points of the ideal TUBE (modeling the riser in 3D) RISER_FRONT_AREA - front surface area of the selected (current) riser

RISER_HEIGHT - 3D height value of the selected riser RISER_SLANT_ANGLE - slant angle of the selected riser RISER_STEP_INDEX - step index of the selected (current) riser RISER_THICKNESS - 3D thickness value of the selected riser RISER_VOLUME - volume of the selected (current) riser RISER_WIDTH - polyline length of the selected (current) riser ROOF_ANGLE - slope of the roof ROOF_BMAT - building material index of the roof, 0 for composite roofs ROOF_BMAT_NAME - building material name of the roof, empty string for composite roofs ROOF_BOTTOM_SURF - bottom surface area of the roof ROOF_BOTTOM_SURF_CON - conditional bottom surface area of the roof ROOF_COMPS_NAME - name of the composite structure of the roof ROOF_CONTOUR_AREA - area covered by the roof ROOF_EAVES - roof eaves length ROOF_EDGE_SURF - surface area of the edge of the roof ROOF_END_WALL - roof end wall connection length ROOF_FBGD_PEN - pen of the background of the fill of the roof ROOF_FILL - fill of the roof ROOF_FILL_PEN - pen of the fill of the roof ROOF_GABLE - roof gables length ROOF_GROSS_BOTTOM_SURF - gross surface area of the roof bottom ROOF_GROSS_EDGE_SURF - gross surface area of the roof edges ROOF_GROSS_TOP_SURF - gross surface area of the roof top

ROOF_GROSS_VOLUME - gross volume of the roof ROOF_HIP - roof hips length ROOF_HOLES_AREA - area of holes in the roof ROOF_HOLES_NR - number of holes in the roof ROOF_HOLES_PRM - perimeter of holes in the roof ROOF_INSU_THICKNESS - roof insulation skin thickness ROOF_LINETYPE - line type of the roof ROOF_MAT_BOTT - surface attribute index of the bottom surface of the roof ROOF_MAT_EDGE - surface attribute index of the edges of the roof ROOF_MAT_TOP - surface attribute index of the top surface of the roof ROOF_PEAK - roof peaks length ROOF_PERIMETER - perimeter of the roof ROOF_RIDGE - roof ridges length ROOF_SECT_PEN - pen of the contours of the roof cut surfaces ROOF_SEGMENTS_NR - number of segments of the roof ROOF_SIDE_WALL - roof side wall connection length ROOF_SKINS_BMAT_NAMES - building material names of the composite roof skin ROOF_SKINS_NUMBER - number of composite roof skins ROOF_SKINS_PARAMS - parameters of the composite roof skin ROOF_THICKNESS - thickness of the roof ROOF_TOP_SURF - top surface area of the roof ROOF_TOP_SURF_CON - conditional surface area of the roof ROOF_TRANSITION_DOME - roof dome connection length

ROOF_TRANSITION_HOLLOW - roof hollow connection length ROOF_VALLEY - roof valleys length ROOF_VIEW_PEN - pen of the roof on view ROOF_VOLUME - volume of the roof ROOF_VOLUME_CON - conditional volume of the roof ROOM_LSIZE - real

- S SHELLBASE_BMAT - building material index of the shell/roof SHELLBASE_BMAT_NAME - building material name of the shell/roof SHELLBASE_COMPS_NAME - name of the composite structure of the shell/roof


SHELLBASE_COND_OPPOSITE_SURF - conditional surface of the opposite side to the reference

side of the shell/roof SHELLBASE_COND_REFERENCE_SURF - conditional reference side surface of the shell/roof SHELLBASE_COND_VOLUME - conditional volume of the roof shell/roof SHELLBASE_EAVES - shell/roof eaves length SHELLBASE_EDGE_SURF - surface of the edge of the shell/roof SHELLBASE_END_WALL - shell/roof end wall connection length SHELLBASE_FBGD_PEN - pen of the background of the fill of the shell/roof SHELLBASE_FILL - fill of the shell/roof SHELLBASE_FILL_PEN - pen of the fill of the roof shell/roof SHELLBASE_GABLE - shell/roof gables length SHELLBASE_GROSS_EDGE_SURF - gross surface of the shell/roof edges

SHELLBASE_GROSS_OPPOSITE_SURF - gross surface of the opposite side to the reference side

of the shell/roof SHELLBASE_GROSS_REFERENCE_SURF - gross surface of the shell/roof reference side SHELLBASE_GROSS_VOLUME - gross volume of the roof shell/roof SHELLBASE_HIP - shell/roof hips length SHELLBASE_HOLES_NR - number of holes in the shell/roof SHELLBASE_HOLES_PRM - perimeter of holes in the shell SHELLBASE_HOLES_SURF - surface of holes in the shell/roof SHELLBASE_INSU_THICKNESS - shell/roof insulation skin thickness SHELLBASE_LINETYPE - line type of the shell/roof SHELLBASE_MAT_EDGE - surface attribute index of the edges of the shell/roof SHELLBASE_MAT_OPPOSITE - surface attribute index of the top surface of the shell/roof SHELLBASE_MAT_REFERENCE - surface attribute index of the bottom surface of the shell/roof SHELLBASE_OPENINGS_NR - number of openings in the shell SHELLBASE_OPENINGS_SURF - surface of openings in the shell SHELLBASE_OPPOSITE_SURF - surface of the opposite side to the reference side of the

shell/roof SHELLBASE_PEAK - shell/roof peaks length SHELLBASE_PERIMETER - perimeter of the shell/roof SHELLBASE_REFERENCE_SURF - reference side surface of the shell/roof SHELLBASE_RIDGE - shell/roof ridges length SHELLBASE_SECT_PEN - pen of the contours of the roof cut surfaces shell/roof SHELLBASE_SIDE_WALL - shell/roof side wall connection length SHELLBASE_SKINS_BMAT_NAMES - building material names of the composite roof skin shell/roof

SHELLBASE_SKINS_NUMBER - number of composite roof skins shell/roof SHELLBASE_SKINS_PARAMS - parameters of the composite roof skin shell/roof SHELLBASE_THICKNESS - thickness of the shell/roof/slab SHELLBASE_TRANSITION_DOME - shell/roof dome connection length SHELLBASE_TRANSITION_HOLLOW - shell/roof hollow connection length SHELLBASE_VALLEY - shell/roof valleys length SHELLBASE_VIEW_PEN - pen of the roof on view shell/roof SHELLBASE_VOLUME - volume of the shell/roof SKYL_HEADER_HEIGHT - skylight header height SKYL_MARKER_TXT - skylight marker text SKYL_OPENING_HEIGHT - skylight opening height SKYL_OPENING_SURF - skylight opening surface SKYL_OPENING_VOLUME - volume of the opening cut by the skylight SKYL_OPENING_WIDTH - skylight opening width SKYL_SILL_HEIGHT - skylight sill height SLAB_BMAT - building material index of the slab, 0 for composite slabs SLAB_BMAT_NAME - building material name of the slab, empty string for composite slabs SLAB_BOT_SURF - bottom surface area of the slab without hole SLAB_BOT_SURF_CON - conditional bottom surface area of the slab SLAB_COMPS_NAME - name of the composite structure of the slab SLAB_EDGE_SURF - surface area of the edges of the slab SLAB_ELEVATION_BOTTOM - bottom elevation of the slab SLAB_ELEVATION_TOP - top elevation of the slab

SLAB_FBGD_PEN - pen of the background of the fill of the slab SLAB_FILL - fill of the slab SLAB_FILL_PEN - pen of the fill of the slab SLAB_GROSS_BOT_SURF - gross surface area of the slab bottom SLAB_GROSS_BOT_SURF_WITH_HOLES - gross surface area of the slab bottom SLAB_GROSS_EDGE_SURF - gross surface area of the slab edges without hole SLAB_GROSS_EDGE_SURF_WITH_HOLES - gross surface area of the slab edges SLAB_GROSS_TOP_SURF - gross surface area of the slab top without hole SLAB_GROSS_TOP_SURF_WITH_HOLES - gross surface area of the slab top SLAB_GROSS_VOLUME - gross volume of the slab without hole SLAB_GROSS_VOLUME_WITH_HOLES - gross volume of the slab SLAB_HOLES_AREA - area of holes in the slab SLAB_HOLES_NR - number of holes in the slab SLAB_HOLES_PRM - perimeter of holes in the slab SLAB_LINETYPE - line type of the slab SLAB_MAT_BOTT - surface attribute index of the bottom surface of the slab SLAB_MAT_EDGE - surface attribute index of the edges of the slab SLAB_MAT_TOP - surface attribute index of the top surface of the slab SLAB_PERIMETER - perimeter of the slab SLAB_SECT_PEN - pen of the contours of the slab in section SLAB_SEGMENTS_NR - number of segments of the slab SLAB_SKINS_BMAT_NAMES - building material names of the composite slab skins SLAB_SKINS_NUMBER - number of composite slab skins

SLAB_SKINS_PARAMS - parameters of the composite slab skins SLAB_THICKNESS - thickness of the slab SLAB_TOP_SURF - top surface area of the slab SLAB_TOP_SURF_CON - conditional top surface area of the slab SLAB_VIEW_PEN - pen of the slab SLAB_VOLUME - volume of the slab SLAB_VOLUME_CON - conditional volume of the slab STAIR2D_BREAKMARK_ANGLE - break mark angle in degrees (Real type value) as set in the

Stair Settings dialog. Keeps the preset value even if the break mark is edited. STAIR2D_BREAKMARK_FLAGS - integer array with two dimensions ([n][1]), additional data for breakmark polyline visibility STAIR2D_BREAKMARK_GEOM - array with two dimensions ([n][9]), data of breakmark polyline

nodes STAIR2D_CURRSTORY_LOCATION - information about the current story visibility of the stair STAIR2D_CUSTOMDISPLAY - contains information about the model view settings of the stair STAIR2D_DESCRIPTION_POSITION - array with two dimensions ([n][4]), containing information

about the position and direction of the Description text

STAIR2D_DRAIN_TPOLYGON_FLAGS - array with two dimensions ([n][4]), additional data of the drain polygons, in accordance with STAIR2D_DRAIN_TPOLYGON_GEOM. Similar structure as STAIR2D_FULL_TPOLYGON_FLAGS.

STAIR2D_DRAIN_TPOLYGON_GEOM - array with two dimensions ([n][3]), data triplets of drain polygon nodes. Similar structure as STAIR2D_FULL_TPOLYGON_GEOM.

STAIR2D_EXT_RPOLYLINE_FLAGS - array with two dimensions ([n][1]), additional data of the

riser polylines, in accordance with STAIR2D_EXT_RPOLYLINE_GEOM. Similar structure as STAIR2D_FULL_RPOLYLINE_FLAGS.

STAIR2D_EXT_RPOLYLINE_GEOM - array with two dimensions ([n][3]), data triplets

of extended riser polyline nodes (including draining). Similar structure as STAIR2D_FULL_RPOLYLINE_GEOM.

STAIR2D_EXT_TPOLYGON_FLAGS - array with two dimensions ([n][4]), additional data of the tread extended polygons, in accordance with STAIR2D_EXT_TPOLYGON_GEOM. Similar structure as STAIR2D_FULL_TPOLYGON_FLAGS.

STAIR2D_EXT_TPOLYGON_GEOM - array with two dimensions ([n][3]), data triplets

of extended tread polygon nodes (including draining). Similar structure as STAIR2D_FULL_TPOLYGON_GEOM.

STAIR2D_FULL_BOUNDARY_GEOM - array with two dimensions ([n][3]), data triplets of stair boundary polygon nodes

STAIR2D_FULL_RPOLYLINE_FLAGS - array with two dimensions ([n][1]), additional data of the riser polylines, in accordance with STAIR2D_FULL_RPOLYLINE_GEOM

STAIR2D_FULL_RPOLYLINE_GEOM - array with two dimensions ([n][3]), data triplets of riser polyline nodes

STAIR2D_FULL_SPOLYGON_FLAGS - array with two dimensions ([n][2]), where n is the number of polygon nodes.

STAIR2D_FULL_SPOLYGON_GEOM - array with two dimensions ([n][3]), containing sub-polygons of the stair 2D projection.

STAIR2D_FULL_SPOLYLINE_FLAGS - array with one dimension [n], where n is the number of nodes in STAIR2D_FULL_SPOLYLINE_GEOM.

STAIR2D_FULL_SPOLYLINE_GEOM - array with two dimensions ([n][2]), containing edges within the boundary.

STAIR2D_FULL_TPOLYGON_FLAGS - array with two dimensions ([n][4]), additional data of the tread polygons, in accordance with STAIR2D_FULL_TPOLYGON_GEOM

STAIR2D_FULL_TPOLYGON_GEOM - array with two dimensions ([n][3]), data triplets of tread polygon nodes

STAIR2D_FULL_WALKLINE_FLAGS - array with two dimensions ([n][2]), additional data of stair walking line nodes, full length

STAIR2D_FULL_WALKLINE_GEOM - array with two dimensions ([n][3]), data triplets of stair walking line nodes, full length

STAIR2D_LAYOUT_TYPES[5] - array with one dimension ([5]), information about the display layout types of the stair according to STAIR2D_CURRSTORY_LOCATION

STAIR2D_LOWER_BOUNDARY_GEOM - array with two dimensions ([n][3]), data triplets of stair boundary polygon nodes of lower part, similar to STAIR2D_FULL_BOUNDARY_GEOM

STAIR2D_LOWER_RPOLYLINE_FLAGS - array with two dimensions ([n][1]), additional data of riser polyline nodes of lower part, similar to STAIR2D_FULL_RPOLYLINE_FLAGS

STAIR2D_LOWER_RPOLYLINE_GEOM - array with two dimensions ([n][3]), data triplets of riser polyline nodes of lower part, similar to STAIR2D_FULL_RPOLYLINE_GEOM

STAIR2D_LOWER_TPOLYGON_FLAGS - array with two dimensions ([n][4]), additional data of tread polygon nodes of lower part, similar to STAIR2D_FULL_TPOLYGON_FLAGS

STAIR2D_LOWER_TPOLYGON_GEOM - array with two dimensions ([n][3]), data triplets of tread polygon nodes of lower part, similar to STAIR2D_FULL_TPOLYGON_GEOM

STAIR2D_LOWER_WALKLINE_FLAGS - integer array with two dimensions ([n][2]), additional data of stair walking line nodes, lower part

STAIR2D_LOWER_WALKLINE_GEOM - array with two dimensions ([n][3]), data triplets of stair walking line nodes, lower part (same logic as stair polygon slicing)

STAIR2D_MIDDLE_BOUNDARY_GEOM - array with two dimensions ([n][3]), data triplets of stair boundary polygon nodes of middle part, similar to STAIR2D_FULL_BOUNDARY_GEOM

STAIR2D_MIDDLE_RPOLYLINE_FLAGS - array with two dimensions ([n][1]), additional data of riser polyline nodes of middle part, similar to STAIR2D_FULL_RPOLYLINE_FLAGS

STAIR2D_MIDDLE_RPOLYLINE_GEOM - array with two dimensions ([n][3]), data triplets of riser polyline nodes of middle part, similar to STAIR2D_FULL_RPOLYLINE_GEOM

STAIR2D_MIDDLE_TPOLYGON_FLAGS - array with two dimensions ([n][4]), additional data of tread polygon nodes of middle part, similar to STAIR2D_FULL_TPOLYGON_FLAGS

STAIR2D_MIDDLE_TPOLYGON_GEOM - array with two dimensions ([n][3]), data triplets of tread polygon nodes of middle part, similar to STAIR2D_FULL_TPOLYGON_GEOM

STAIR2D_MIDDLE_WALKLINE_FLAGS - integer array with two dimensions ([n][2]), additional data of stair walking line nodes, middle part

STAIR2D_MIDDLE_WALKLINE_GEOM - array with two dimensions ([n][3]), data triplets of stair walking line nodes, middle part

STAIR2D_MONOLITH_ATTRIBUTES - array with two dimensions ([2][23]), containing attributes and visibility settings of the visible ([1][n]) and invisible ([2][n]) parts of the monolithic structure.

STAIR2D_POLYLINES_FLAGS - array with two dimensions ([n][1]), where n is the number of structure polyline nodes of the current flight/landing in 2D, contains group data of the polyline nodes.

STAIR2D_POLYLINES_GEOM - array with two dimensions ([n][3]), where n is the number of structure polyline nodes of the current flight/landing in 2D, contains geometric data of the polyline nodes derived from the stair boundary: left boundary line, right boundary line and centerline.

STAIR2D_STRUCT_ATTRIBUTES - array with two dimensions ([2][7]), containing attributes settings of the visible ([1][n]) and invisible ([2][n]) parts of the structure.

STAIR2D_UPPER_BOUNDARY_GEOM - array with two dimensions ([n][3]), data triplets of stair boundary polygon nodes of upper part, similar to STAIR2D_FULL_BOUNDARY_GEOM

STAIR2D_UPPER_RPOLYLINE_FLAGS - array with two dimensions ([n][1]), additional data of riser polyline nodes of upper part, similar to STAIR2D_FULL_RPOLYLINE_FLAGS

STAIR2D_UPPER_RPOLYLINE_GEOM - array with two dimensions ([n][3]), data triplets of riser polyline nodes of upper part, similar to STAIR2D_FULL_RPOLYLINE_GEOM

STAIR2D_UPPER_TPOLYGON_FLAGS - array with two dimensions ([n][4]), additional data of tread polygon nodes of upper part, similar to STAIR2D_FULL_TPOLYGON_FLAGS

STAIR2D_UPPER_TPOLYGON_GEOM - array with two dimensions ([n][3]), data triplets of tread polygon nodes of upper part, similar to STAIR2D_FULL_TPOLYGON_GEOM

STAIR2D_UPPER_WALKLINE_FLAGS - array with two dimensions ([n][2]), additional data of stair walking line nodes, upper part

STAIR2D_UPPER_WALKLINE_GEOM - array with two dimensions ([n][3]), data triplets of stair

walking line nodes, upper part STAIR2D_VISIBILITY - type of the active attribute set of the current drawing STAIR_AREA - projected 2D area of the stair STAIR_BREAKMARK_GEOMETRY - geometry of the breakmarks STAIR_DEFAULT_GOING_DEPTH - default depth of going (as set in the Stair Default Settings/ Geometry and Positioning panel) STAIR_DEFAULT_RISER_HEIGHT - default width of riser (as set in the Stair Default Settings/ Geometry and Positioning panel) STAIR_DEFAULT_TREAD_THICKNESS - default tread thickness of stair (as set in the Stair

Default Settings/Geometry and Positioning panel)

STAIR_DEFAULT_WIDTH - default width of stair (as set in the Stair Default Settings/ Geometry and Positioning panel)

STAIR_END_WITH_RISER - Boolean telling whether the stair ends with a riser. STAIR_HEIGHT - difference between maximum and minimum of Z coordinates STAIR_LANDING_NUMBER - number of landing sections regarding the whole stair STAIR_NOSING_EXIST - Boolean array ([2]) telling whether the stair has a Tread nosing

(length > 0) set. STAIR_NR_OF_RISERS - number of risers regarding the whole stair STAIR_NR_OF_RISERS_IN_FLIGHTS - integer array with one dimension ([n]) number of risers

in each flight of the stair (n = number of flights) STAIR_NR_OF_TREADS - number of treads regarding the whole stair

STAIR_NR_OF_TREADS_IN_FLIGHTS - integer array with one dimension ([n]) number of treads in each flight of the stair (n = number of flights)

STAIR_RISER_EXIST - Boolean array ([2]) telling whether the stair has a Riser component. STAIR_RISER_GEOMETRY - array with two dimensions ([n][3]), data triplets of stair riser

polyline path nodes STAIR_RULE_FLAGS - boolean array with two dimensions ([6][2]), enable/disable status

collection of limits in accordance with STAIR_RULE_LIMITS, set in Stair Default Settings/ Rules and Standards/Treads and Risers panel STAIR_RULE_LIMITS - length/angle array with two dimensions ([6][2]), collection of minimum

and maximum values set in Stair Default Settings/Rules and Standards/Treads and Risers panel

STAIR_STAIR_GRADIENT - stair inclination: the angle of the riser/going ratio in radian STAIR_START_WITH_RISER - Boolean telling whether the stair starts with a riser. STAIR_STRINGER_PATH_OFFSET - contains the value set in "Height above Treads" in Stair

Settings dialog. STAIR_STRUCTURE_CONN_FLAGS - array with two dimensions ([2][3]). Contains additional data of the structure connection. STAIR_STRUCTURE_CONN_OFFSETS - array with two dimensions ([2][6]). Contains data of connection offset points. STAIR_STRUCTURE_FLAGS - array with two dimensions ([n][3]), where n is the number of structure polygons points of the current flight/landing. STAIR_STRUCTURE_GEOMETRY - array with two dimensions ([n][14]), where n is the number of structure polygons points of the current flight/landing.

STAIR_TREAD_EXIST - Boolean array ([2]) telling whether the stair has a Tread component. STAIR_TREAD_FLAGS - array with two dimensions ([n][1]), additional data of the tread

polygon edges (starting from nodes), in accordance with STAIR_TREAD_GEOMETRY

STAIR_TREAD_GEOMETRY - array with two dimensions ([n][3]), data triplets of stair tread

polygon nodes STAIR_VOLUME - area of the stair including all 3D parts STAIR_WALKLINE_LENGTH - projected 2D length of the stair's walking line STRUCTURE_3DLENGTH - full 3D length of the selected (current) structure component STRUCTURE_HEIGHT - height of the selected (current) structure component (difference of

min. and max. z) STRUCTURE_THICKNESS - thickness of the selected (current) structure component STRUCTURE_VOLUME - volume of the selected (current) structure component STRUCTURE_WIDTH - width of the selected (current) structure component SYMB_A_SIZE - nominal length/width of library part SYMB_B_SIZE - nominal width/height of library parts SYMB_FBGD_PEN - pen of the background of the fill of the library part SYMB_FILL - fill type of the library part SYMB_FILL_PEN - pen of the fill of the library part SYMB_LINETYPE - line type of the library part SYMB_MAT - default surface attribute index of the library part SYMB_MIRRORED - library part mirrored SYMB_POS_FROM_SURVEY_POINT - dictionary, position of the library part transformed into

the Survey Point's coordinate system

SYMB_POS_X - position of the library part (x) SYMB_POS_Y - position of the library part (y) SYMB_POS_Z - position of the library part (z) SYMB_ROTANGLE - rotation angle of the library part

SYMB_SECT_PEN - pen of the library part in section SYMB_VIEW_PEN - default pen of the library part SYMB_Z_SIZE - nominal height/length of the library part

- T TO_GUID - Main GUID of the library part to which the migration is performed TREAD_AREA - projected 2D area of the selected (current) tread


TREAD_BMATS - array with one dimension ([n]), building materials of the selected (current)

tread (n = number of building materials) TREAD_ELEVATION - elevation to Project Zero of the selected (current) tread TREAD_FRONT_AREA - front surface area of the selected (current) tread TREAD_GOING - going length of the selected (current) tread TREAD_LOWER_RISER_HEIGHT - height of the riser below the current tread (measured between

the bottom plane of the current tread and the upper plane of the previous tread) TREAD_LOWER_RISER_SLANT_ANGLE - slant angle of the riser below the current tread in degrees (is Slanting = 0, the value is 90 degrees) TREAD_LOWER_RISER_THICKNESS - thickness of the riser below the current tread (measured between grid and structure)

TREAD_NOSING - contains tread nosing depth value of the selected tread (horizontal offset, as set on the Stair Settings dialog), in case TREAD_NOSING_METHOD = 1 (nosing by value length)

TREAD_NOSING_BY_SLANTING - contains tread nosing length value (vertical offset to

control riser intersection point, as set on the Stair Settings dialog), in case TREAD_NOSING_METHOD = 2 (nosing by slanting length)

TREAD_NOSING_METHOD - information about the nosing method of the current tread, as set on the Stair Settings dialog

TREAD_STEP_INDEX - step index of the selected (current) tread TREAD_THICKNESS - 3D thickness value of the selected tread TREAD_UPPER_RISER_HEIGHT - height of the riser above the current tread (measured between

the top plane of the current tread and the bottom plane of the following tread) TREAD_UPPER_RISER_SLANT_ANGLE - slant angle of the riser above the current tread in degrees (is Slanting = 0, the value is 90 degrees) TREAD_UPPER_RISER_THICKNESS - thickness of the riser above the current tread (measured between grid and structure) TREAD_VOLUME - volume of the selected (current) tread