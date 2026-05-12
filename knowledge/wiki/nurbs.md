---
id: wiki.generated.nurbs
type: wiki
category: other
commands: ["NURBS"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### NURBS PRIMITIVE ELEMENTS

The primitives of 3D data structure of NURBS bodies are the NURBSCURVE2D command, the NURBSCURVE3D command, the NURBSSURFACE command, the NURBSVERT command, the NURBSEDGE command, the NURBSTRIM command, the NURBSTRIMSINGULAR command, the NURBSFACE command, the NURBSLUMP command, and the NURBSBODY command.

Solid NURBS bodies are represented by the boundary NURBS faces of the solid region(s), laminar surface NURBS bodies are represented by the NURBS faces themself, wire NURBS bodies are represented by the NURBS edges. A NURBS body can have solid, laminar and wire part at the same time, a NURBS body itself is not classified into solid/surface/wire categories.

Nurbs primitives can not be used in planar face bodies and non-NURBS primitives can not be used in NURBS bodies. A non-NURBS primitive statement causes the NURBS body under construction to be finished and a new non-NURBS body to be started (implicit BODY and NURBSBODY statements).

Similarly a NURBS primitive statement causes the non-NURBS body under construction to be finished and a new NURBS body to be started. A compound statement (BRICK, CYLIND, PRISM, etc.) or a MODEL statement causes either NURBS or non-NURBS body under construction to be finished. If a NURBSBODY statement closes a non-NURBS body or a BODY statement closes a NURBS body, the given status value will have no effect.

Indexing of NURBS primitives starts from 1. Indexing of NURBS primitives and non-NURBS primitives (VERT, TEVE, EDGE, VECT, PGON, PIPG) are handled separately. The BASE statement resets counter for NURBS body primitives also. All primitives referenced by another primitive should be defined before the referencing one (e.g. vertices and 3D curve of edge should be defined before the edge).

The NURBSCURVE2D, NURBSCURVE3D and NURBSSURFACE statements create only geometric elements in the NURBS body which will not be visible themselves. A NURBS edge defines its geometric support by referencing a 3D NURBS curve, similarly a NURBS trim references a 2D NURBS curve and a NURBS face references a NURBS surface as its geometric support (the edge, trim and face may not extend to the whole geometric support, see details at each command description).

The NURBS edge, its 3D curve, its trims, and the 2D curves of the trims are always oriented consistently. The NURBS face and its surface are always oriented consistently.

The NURBS faces may be organized into NURBS lumps. A lump defines a solid region bounded by one or more shells. A shell is a closed and connected set of faces which separates the space into two regions. A lump has an outer shell which separates the lump from the infinity and may have void shells which separate the lump from inner cavities.

Consistent orientation of faces in a shell is not necessary, two neighbouring face can refer to the same edge in the same direction. But shells of lump must have consistent orientations, the back side of a shell should look toward the interior of the lump, for this the lump can refer to the faces with negative prefix for reversed orientation.

Faces which are not part of a lump will be treated as laminar surfaces, even if the faces form a closed shell. Edges which are not part of a face will be treated as wire edges. One NURBS body can contain solid lumps, laminar faces and wire edges at the same time.

The 2-manifold property is not required for NURBS bodies, a NURBS edge may be connected to more than two faces (by more than two trims). Even a shell of a NURBS lump can have more than two faces at an edge as long as the shell still separates the space into two regions (this means even number of faces of a given shell on each edge).

The RADIUS, RESOL and TOLER statements have no effect on the smoothness of the NURBS faces and edges. The smoothness of NURBS primitives is calculated automatically and may be limited for a NURBS body by the parameters of the NURBSBODY command (see details at NURBSBODY).

For correct texture setting for NURBS, see the the COOR{3} command.

###### NURBS Face trimming

A NURBS surface is a two dimensional sheet in the three dimensional space and is defined by a geometric function mapping a rectangle to the space. The geometry of a NURBS face is always a part of a NURBS surface but may be more complex than that. This is made possible by trims. A trim defines a cut on the domain rectangle of the surface, a cut with a two dimensional NURBS curve. This implies a cut on the three dimensional sheet of the surface. This cut lies along the bounding NURBS edge of the face and the geometry of the cut along the surface sheet must be consistent with the geometry of the NURBS edge.

A NURBS face has contours just like a traditional PGON, but the contours are not lists of NURBS edges but NURBS trims because the trims have the information needed to cut the face properly. (The 2d curve of trims may be computed from the 3d curve of the edge but it may be inaccurate or even ambiguous in case of surfaces with self-intersection or singularities or in case of erroneous data.)

###### NURBS Geometry Commands

The following commands describe geometric parts of NURBS elements: curves and surface.