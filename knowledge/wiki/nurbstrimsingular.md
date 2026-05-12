---
id: wiki.generated.nurbstrimsingular
type: wiki
category: other
commands: ["NURBSTRIMSINGULAR"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### NURBSTRIMSINGULAR

NURBSTRIMSINGULAR vertex, curve, curveDomainBeg, curveDomainEnd, tolerance A bounding edge of a face. Used for trimming a face in the parameter space of the surface of the face. NURBSTRIMSINGULAR is used along singular sides of the surface (which side is contracted to one point on the surface). Connects the face to an edge (or to a vertex in singular case). edge: gdl-index of NURBS edge to which this trim is attached. Positive index, edge and trim are always oriented consistently. vertex: gdl-index of NURBS vertex to which this trim is attached (singular case). curve: gdl-index of a 2D NURBS curve. Positive index, curve and trim are always oriented consistently. It is defined on the domain (u-

v parameter space) of the surface of the face.

curveDomainBeg, curveDomainEnd: definition of the part of curve which geometrically represents the trim. The curveDomainEnd

must be greater than curveDomainBeg, they must not coincide, and both value must be in the usable domain of the curve.

tolerance: maximum geometric distance between 2D curve of NURBS trim and other entities (other NURBS trims) which are

topologically connected to it. If negative, tolerance will be some predefined default.

The curve restricted to [curveDomainBeg, curveDomainEnd] interval should completely lie within the usable domain of the surface of the face (with given tolerance). For NURBSTRIMSINGULAR the 2D curve must lie along a singular side of the usable domain (u-v parameter space) of the surface of the face.

The composition of the restricted 2D curve and the surface gives a 3D curve which should coincide with the restricted 3D curve of the edge. Therefore the 2D curve evaluated at curveDomainBeg and curveDomainEnd should coincide with the position of the appropriate vertex. In the singular case the composition of the 2D curve and the surface gives a 3D point, which should coincide with the given vertex.

Indexing of singular and non-singular trims is common. Any number of trims can refer to each edge (so indirectly any number of face can be attached to an edge). The edge can be non-2-manifold. Two trims on one edge may belong to the same face, in this case edge is called a seam edge. For example a mantle of a cylinder can be one face with a seam edge.