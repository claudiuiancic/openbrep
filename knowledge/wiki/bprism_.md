---
id: wiki.generated.bprism_
type: wiki
category: 3d
commands: ["BPRISM_"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### BPRISM_

BPRISM_ top_material, bottom_material, side_material, n, h, radius, x1, y1, s1,

... xn, yn, sn

A smooth curved prism, based on the same data structure as the straight CPRISM_ element. The only additional parameter is radius. Derived from the corresponding CPRISM_ by bending the x-y plane onto a cylinder tangential to that plane. Edges along the x axis are transformed to circular arcs; edges along the y axis remain horizontal; edges along the z axis will be radial in direction. See the BWALL_ command for details. si: status code that allows you to control the visibility of polygon edges and side surfaces. You can also define holes and create segments

and arcs in the polyline using special constraints. See Status Codes for details. Example: Curved prisms with the corresponding straight ones

BPRISM_ "Glass - Blue", "Glass - Blue", "Glass - Blue", 3, 0.4, 1, ! radius = 1 0, 0, 15, 5, 0, 15, 1.3, 2, 15

BPRISM_ "Concrete", "Concrete", "Concrete", 17, 0.3, 5, 0, 7.35, 15, 0, 2, 15,

- 1.95, 0, 15, 8, 0, 15, 6.3, 2, 15, 2, 2, 15, 4.25, 4, 15, 8, 4, 15, 8, 10, 15,
- 2.7, 10, 15, 0, 7.35, -1, 4, 8.5, 15, 1.85, 7.05, 15,
- 3.95, 5.6, 15, 6.95, 5.6, 15, 6.95, 8.5, 15, 4, 8.5, -1