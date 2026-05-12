---
id: wiki.generated.primitive
type: wiki
category: other
commands: ["PRIMITIVE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### PRIMITIVE ELEMENTS

The primitives of the 3D data structure are VERT, VECT, EDGE, PGON and BODY. The bodies are represented by their surfaces and the connections between them. The information to execute a 3D cutaway comes from the connection information. Indexing starts with 1, and a BASE statement or any new body (implicit BASE statement) resets indices to 1. For each edge, the indices of the adjacent polygons (maximum 2) are stored. Edges’ orientations are defined by the two vertices determined first and second.

Polygons are lists of edges with an orientation including the indices of the edges. These numbers can have a negative prefix. This means that the given edge is used in the opposite direction. Polygons can include holes. In the list of edges, a zero index indicates a new hole. Holes must

not include other holes. One edge may belong to 0 to 2 polygons. In the case of closed bodies, the polygon’s orientation is correct if the edge has different prefixes in the edge list of the two polygons.

The normal vectors of the polygons are stored separately. In the case of closed bodies, they point from the inside to the outside of the body. The orientation of the edge list is counterclockwise (mathematical positive), if you are looking at it from the outside. The orientation of the holes is opposite to that of the parent polygon. Normal vectors of an open body must point to the same side of the body.

To determine the inside and outside of bodies they must be closed. A simple definition for a closed body is the following: each edge has exactly two adjacent polygons. The efficiency of the cutting, hidden line removal or rendering algorithms is lower for open bodies. Each compound three-dimensional element with regular parameters is a closed body in the internal 3D data structure. Contour line searching is based on the status bits of edges and on their adjacent polygons. This is automatically set for compound curved elements but it is up to you to specify these bits correctly in the case of primitive elements. In the case of a simplified definition (vect = 0 or status < 0 in a PGON) the primitives that are referred to by others must precede their reference. In this case, the recommended order is:

VERT (TEVE) EDGE (VECT) PGON (PIPG) COOR BODY

Searching for adjacent polygons by the edges is done during the execution of the BODY command. The numbering of VERTs, EDGEs, VECTs and PGONs is relative to the last (explicit or implicit) BASE statement. Status values are used to store special information about primitives. Each single bit usually has an independent meaning in the status, but there are some exceptions. Given values can be added together. Other bit combinations than the ones given below are strictly reserved for internal use. The default for each status is zero.