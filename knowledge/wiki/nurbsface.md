---
id: wiki.generated.nurbsface
type: wiki
category: other
commands: ["NURBSFACE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### NURBSFACE

NURBSFACE n, surface, tolerance,

trim1, trim2, ..., trimn Face of a NURBS body. Different from any polygon created by the PGON command, indexed separately from those. Can be used in NURBS bodies only, excluding planar-face bodies.

n: number of bounding edges (including optional hole-separator zeros). surface: gdl-index of a NURBS surface supporting the face. Positive index, orientation of face is always identical to the orientation of

surface.

trimi: gdl-index of NURBS trim bounding the face.

- • The trims are listed in a counter-clocwise (mathematical positive) order on the surface for the outer contour loop and clockwise (negative) for hole contour loop(s).
- • May be zero, which indicates end of contour (hole-separator).
- • Negative index means trim and the contour (of face) have opposite orientation.


tolerance: if negative, tolerance will be some predefined default. The trims must connect at common vertices: the end vertex of a trim is the same as the begin vertex of the next trim in the face. (The vertices of a trim are the vertices of the edge of the trim for a non-singular trim.)

The consecutive trims - as 2D curves - also connect in the domain (parameter space) of the face, defining one or more closed contour loops on it. The first loop is always an outer loop which separates an infinite outer and a finite inner region on the plane. The potential subsequent loops are hole contours.

The 2D curve of each trim should completely lie inside the usable domain of the surface of the face and should not intersect itself or curves of other trims of the face. Each trim must be used in only one face.

The material and section attributes of a face are determined by the last MATERIAL and SECT_ATTRS (or SECT_FILL) statements respectively. The color of the edges inside the face created for polygonal segmentations is defined by the last PEN statement. This is practically visible on silhouettes coming from the internal of this face.