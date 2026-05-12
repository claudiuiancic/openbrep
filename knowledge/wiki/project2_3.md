---
id: wiki.generated.project2_3
type: wiki
category: 2d
commands: ["PROJECT2{3}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PROJECT2{3}

- PROJECT2{3} projection_code, angle, method, parts [, backgroundColor, fillOrigoX, fillOrigoY, filldirection][[,] PARAMETERS name1=value1, ..., namen=valuen]


Creates a projection of the 3D script in the same library part and adds the generated lines to the 2D parametric symbol. The third version,

- PROJECT2{3}, adds the possibility to define which parts of the projected model are required and to control separately the attributes of the cut and view part, including the line type. You can also generate the projection with actual parameters set in the command.


method: the chosen imaging method. If invalid or none is set, the default is hidden lines (2). 1: wireframe, 2: hidden lines (analytic), 3: shading, 16: addition modifier: draws vectorial hatches (effective only in hidden line and shaded mode), 32: addition modifier: use current attributes instead of attributes from 3D (effective only in shading mode), 64: addition modifier: local fill orientation (effective only in shading mode), 128: addition modifier: lines are all inner lines (effective only together with 32). Default is generic. 256: addition modifier: lines are all contour lines (effective only together with 32, if 128 is not set). Default is generic. 512: addition modifier: fills are all cut (effective only together with 32). Default is drafting fills. 1024: addition modifier: fills are all cover (effective only together with 32, if 512 is not set). Default is drafting fills. 2048: addition modifier: modifiers 16, 32, 64, 128, 256, 512, 1024 and fill attribute parameters are effective only for the view part of the projection. By default they are effective for all parts. 4096: addition modifier: modifiers 16, 32, 64, 128, 256, 512, 1024 and fill attribute parameters are effective only for the cut part of the projection. By default they are effective for all parts. 8192: addition modifier: cut fills are slanted. 16384: addition modifier: enables transparency for transparent surfaces. Note that transparency in this case means full transparency for surfaces with transmittance greater than 50, everything else is non-transparent.

Known limitation: lines of the cut part cannot be treated separately, only all lines together can be set to be inner or contour. Compatibility note: up to Archicad 19, cut polygons were generated with attributes defined by the SECT_FILL command or the SECT_ATTRS command in the 3D script. From Archicad 20 the attributes of the cut polygons are defined by the cover fill of the outer surfaces (in case the addition modifier 32 is not set). parts: defines the parts to generate. The 1+2+4+8+16+32 value means all parts.

parts = j1 + 2*j2 + 4*j3 + 8*j4 + 16*j5 + 32*j6, where each j can be 0 or 1. The j1, j2, j3, j4, j5, j6 numbers represent whether the corresponding parts of the projected model are present (1) or omitted (0):

j1: cut polygons (effective only in shading mode), j2: cut polygon edges, j3: view polygons, j4: view polygon edges, j5: project 3D hotspots as static 2D hotspots, j6: project 3D hotlines and hotarcs (including related 3D hotspots converted to static 2D hotspots).