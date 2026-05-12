---
id: wiki.generated.poly2_b_4
type: wiki
category: 3d
commands: ["POLY2_B{4}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### POLY2_B{4} n, frame_fill, fill_pen, fill_background_pen, fillOrigoX, fillOrigoY, mxx, mxy, myx, myy, gradientInnerRadius, x1, y1, s1, ..., xn, yn, sn

- Advanced version of POLY2_ B{3}, where the inner radius of radial gradient fill can be set. gradientInnerRadius: inner radius of the gradient in case radial gradient fill is selected for the polygon.

POLY2_B{5}

POLY2_B{5} n, frame_fill, fillcategory, distortion_flags, fill_pen, fill_background_pen, fillOrigoX, fillOrigoY, mxx, mxy, myx, myy, gradientInnerRadius, x1, y1, s1, ..., xn, yn, sn

- Advanced version of POLY2_ B{4}, where fill distortion can be controlled in an enhanced way. frame_fill:


frame_fill = j1 + 2*j2 + 4*j3, where each j can be 0 or 1. j1: draw contour j2: draw fill j3: close an open polygon.

fillcategory: 0: Draft, 1: Cut, 2: Cover.

distortion_flags: distortion_flags = j1 + 2*j2 + 4*j3 + 8*j4 + 16*j5 + 32*j6 + 64*j7, where each j can be 0 or 1. The valid value for distortion_flags is between 0 and 127. Don’t use value out of this range.

- j1: the fill origin’s X coordinate is the global origin’s X coordinate, meaningful only when j4 is set. The fillOrigo is the origin (0,0) projected on the line of the (mxx, mxy) vector,
- j2: the fill origin’s Y coordinate is the global origin’s Y coordinate, meaningful only when j4 is set,
- j3: create circular distortion using the innerRadius parameter,
- j4: use local orientation, use the distortion matrix (mij parameters),
- j5: (effective for symbol fills only) reset the pattern’s X size to the defined X vector’s length (mxx, mxy),
- j6: (effective for symbol fills only) reset the pattern’s Y size to the defined Y vector’s length (myx, myy),
- j7: (effective for symbol fills only) keep proportion of symbol fill pattern; effective only if one of j5 and j6 is set.


innerRadius: radius for circular fill distortion; the origin of the base circle will be placed on the Y fill axis in the (0, -innerRadius) position.