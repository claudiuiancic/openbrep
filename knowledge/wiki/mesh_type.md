---
id: wiki.generated.mesh_type
type: wiki
category: 3d
commands: ["MESH_TYPE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### MESH_TYPE type of the mesh

1- closed body, 2 - top & edge, 3 - top surface only MESH_BASE_OFFSET offset of the bottom surface to the base level MESH_USEREDGE_PEN pen of the user defined ridges of the mesh MESH_TRIEDGE_PEN pen of the triangulated edges of the mesh MESH_SECT_PEN pen of the contours of the mesh in section

applied on contours of cut surfaces of walls both in floor plan and section/elevation windows

MESH_VIEW_PEN pen of the contours on view

applied on all edges in 3D window and on edges on view in section/elevation windows MESH_MAT_TOP surface attribute index of the top surface of the mesh MESH_MAT_EDGE surface attribute index of the edges of the mesh MESH_MAT_BOTT surface attribute index of the bottom surface of the mesh MESH_LINETYPE line type of the mesh

applied on the contours only in the floor plan window

MESH_FILL fill type of the mesh

MESH_BMAT_NAME building material name of the mesh MESH_BMAT building material index of the mesh

Compatibility: introduced in Archicad 21. MESH_FILL_PEN pen of the fill of the mesh MESH_FBGD_PEN pen of the background of the fill of the mesh MESH_BOTTOM_SURF bottom surface area of the mesh MESH_TOP_SURF top surface area of the mesh MESH_EDGE_SURF surface area of the edge of the mesh MESH_PERIMETER perimeter of the mesh MESH_VOLUME volume of the mesh MESH_SEGMENTS_NR number of segments of the mesh MESH_HOLES_NR number of holes in the mesh MESH_HOLES_AREA area of holes in the mesh MESH_HOLES_PRM perimeter of holes in the mesh