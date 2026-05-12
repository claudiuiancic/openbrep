---
id: wiki.generated.shapes
type: wiki
category: other
commands: ["SHAPES"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### SHAPES GENERATED FROM POLYLINES

These elements let you create complex 3D shapes using a polyline and a built-in rule. You can rotate, project or translate the given polyline. The resulting bodies are a generalization of some previously described elements like PRISM_ and CYLIND. Shapes generated from a single polyline:

- • EXTRUDE
- • PYRAMID
- • REVOLVE Shapes generated from two polylines:
- • RULED
- • SWEEP
- • TUBE
- • TUBE{2}
- • TUBEA The first polyline is always in the x-y plane. Points are determined by two coordinates; the third value is the status (see below). The second polyline (for RULED, SWEEP, TUBE and TUBEA) is a space curve. Apices are determined by three coordinate values. Shape generated from four polylines:
- • COONS
- • COONS{2} Shape generated from any number of polylines:
- • MASS General restrictions for polylines
- • Adjacent vertices must not be coincident (except RULED).
- • The polyline must not intersect itself (this is not checked by the program, but hidden line removal and rendering will be incorrect).
- • The polylines may be either open or closed. In the latter case, the first node must be repeated after the last one of the contour. Masking Mask values are used to show or hide characteristic surfaces and/or edges of the 3D shape. The mask values are specific to each element and you can find a more detailed description in their corresponding sections/chapters. mask:


mask = j1 + 2*j2 + 4*j3 + 8*j4 + 16*j5 + 32*j6 + 64*j7, where each j can be 0 or 1. j1, j2, j3, j4 represent whether the surfaces are present (1) or omitted (0). j5, j6, j7 represent whether the edges are visible (1) or invisible (0).

- j1: base surface.
- j2: top surface.
- j3: side surface.
- j4: other side surface.


- j5: base edges.
- j6: top edges.
- j7: cross-section/surface edges are visible, surface is not smooth. To enable all faces and edges, set mask value to 127.


Status Status values are used to state whether a given point of the polyline will leave a sharp trace of its rotation path behind. 0: latitudinal arcs/lateral edges starting from the node are all visible. 1: latitudinal arcs/lateral edges starting from the node are used only for showing the contour.

-1: for EXTRUDE only: it marks the end of the enclosing polygon or a hole, and means that the next node will be the first node of another hole. Additional status codes allow you to create segments and arcs in the polyline using special constraints. See the section called “Additional Status Codes” for details. To create a smooth 3D shape, set all status values to 1. Use status = 0 to create a ridge. Other values are reserved for future enhancements.