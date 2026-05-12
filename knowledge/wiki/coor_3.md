---
id: wiki.generated.coor_3
type: wiki
category: 3d
commands: ["COOR{3}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### COOR{3}

- COOR{3} wrapping_method, wrap_flags, origin_X, origin_Y, origin_Z, endOfX_X, endOfX_Y, endOfX_Z, endOfY_X, endOfY_Y, endOfY_Z, endOfZ_X, endOfZ_Y, endOfZ_Z


Compatibility: introduced in Archicad 20. Similar to the COOR{2} command. Can be used with array parameter input (see WALL_TEXTURE_WRAP global in the section called “Wall parameters - available for Doors/Windows, listing and labels” for more). The coordinate system of the projection body is included in the COOR{3} command itself, no need to define additional vertexes in the current BODY. Compatible with NURBS bodies (no non-NURBS primitives are needed to set up the texture coordinate system). wrap_method: Wrapping modes are the same as described in the the COOR command supplemented by NURBS based wrapping mode.

Projection types do not apply, use wrap_flags instead. 1: planar box (deprecated), 2: box, 3: cylindrical, 4: spherical,

5: same as the cylindrical fill mapping, but in rendering the top and the bottom surface will get a circular mapping, 6: planar, 7: NURBS based, the vertices' texture coordinates are from their surface parameters, only in case of NURBS bodies.

wrap_flags: Wrapping flags wrap_flags = 4*j3 + 8*j4 + 16*j5 + 32*j6 + 64*j7 + 128*j8, where each j can be 0 or 1. j3: quadratic texture projection (recommended), j4: linear texture projection based on the average distance, j5: linear texture projection based on normal triangulation, j8: translate the origin of the texture coordinate system closest to the global origin in the direction of the X, Y or Z axis respectively. For example, j6 makes the origin translating in the direction of the X axis so that it will be the orthogonal projection of the global origin to the line of the X axis. That is, if all j6, j7 and j8 are 1, the origin is translated into the global origin (opposite effect of projection type 256 in the the COOR command).

Note: The j3, j4 and j5 flags are only effective if wrap_method is 0 and only one of them can be 1. The j6, j7 and j8 flags are only

effective if wrap_method is not 0. These can be 1 at the same time in any combination.

origin_X, origin_Y, origin_Z: node in the x-y-z space, defined by three coordinates, texture origin.

- endOfX_X, endOfX_Y, endOfX_Z: node in the x-y-z space, defined by three coordinates, texture mapping X direction.
- endOfY_X, endOfY_Y, endOfY_Z: node in the x-y-z space, defined by three coordinates, texture mapping Y direction.
- endOfZ_X, endOfZ_Y, endOfZ_Z: node in the x-y-z space, defined by three coordinates, texture mapping Z direction.


Example: COOR{3} and equivalent COOR{2} parametrisation COOR{3} wrapping_method, wrap_flags,

origin_X, origin_Y, origin_Z, endOfX_X, endOfX_Y, endOfX_Z, endOfY_X, endOfY_Y, endOfY_Z, endOfZ_X, endOfZ_Y, endOfZ_Z

! COOR{2} equivalent BASE VERT origin_X, origin_Y, origin_Z, VERT endOfX_X, endOfX_Y, endOfX_Z VERT endOfY_X, endOfY_Y, endOfY_Z VERT endOfZ_X, endOfZ_Y, endOfZ_Z COOR{2} wrapping_method, wrap_flags, -1, -2, -3, -4