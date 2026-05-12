---
id: wiki.generated.coor_2
type: wiki
category: 3d
commands: ["COOR{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### COOR{2}

- COOR{2} wrap_method, wrap_flags, vert1, vert2, vert3, vert4 Deprecated. See the COOR{3} command. Similar to the COOR command, changing wrap to two parameters wrap_method and wrap_flags, and also extending the possibilities of it.


wrap_method: Wrapping modes are the same as described in the the COOR command. Projection types do not apply, use wrap_flags

instead.

wrap_flags: Wrapping flags wrap_flags = 4*j3 + 8*j4 + 16*j5 + 32*j6 + 64*j7 + 128*j8, where each j can be 0 or 1. j3: quadratic texture projection (recommended), j4: linear texture projection based on the average distance, j5: linear texture projection based on normal triangulation, j8: translate the origin of the texture coordinate system closest to the global origin in the direction of the X, Y or Z axis respectively. For example, j6 makes the origin translating in the direction of the X axis (along v2 - v1 vector) so that it will be the orthogonal projection of the global origin to the line of the X axis. That is, if all j6, j7 and j8 are 1, the origin is translated into the global origin (same as if projection type is 256 in the the COOR command).

Note: The j3, j4 and j5 flags are only effective if wrap_method is 0 and only one of them can be 1. The j6, j7 and j8 flags are only

effective if wrap_method is not 0. These can be 1 at the same time in any combination. vert1, vert2, vert3, vert4: like in the COOR command.