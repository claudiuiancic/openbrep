---
id: wiki.generated.drawing3_2
type: wiki
category: other
commands: ["DRAWING3{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### DRAWING3{2}

- DRAWING3{2} projection_code, angle, method [, backgroundColor, fillOrigoX, fillOrigoY, filldirection]

Similarly to PROJECT2, creates a projection of the 3D script of the library part associated with the property library part containing this command. All parameters are similar to those of PROJECT2 and PROJECT2{2}.

- method: New method flags in DRAWING3{2} 3: shading, 32: use current attributes instead of attributes from 3D, 64: local fill orientation.

DRAWING3{3}

DRAWING3{3} projection_code, angle, method, parts [, backgroundColor, fillOrigoX, fillOrigoY, filldirection][[,] PARAMETERS name1=value1, ..., namen=valuen]

Similarly to PROJECT2, creates a projection of the 3D script of the library part associated with the property library part containing this command. All parameters are similar to those of PROJECT2, PROJECT2{2} and PROJECT2{3}.

- method: New method flags in DRAWING3{3} 2048: addition modifier: modifiers 16, 32, 64, 128, 256, 512, 1024 and fill attribute parameters are effective only for the view part of the projection. By default they are effective for all parts,




projection. By default they are effective for all parts, 8192: addition modifier: cut fills are slanted. 16384: addition modifier: enables transparency for transparent surfaces. Note that transparency in this case means full transparency for surfaces with transmittance greater than 50, everything else is non-transparent.

## GRAPHICAL EDITING USING HOTSPOTS

Hotspot-based interactive graphical editing of length and angle type GDL parameters.

HOTSPOT x, y, z [, unID [, paramReference [, flags [, displayParam [, "customDescription"]]]]] HOTSPOT2 x, y [, unID [, paramReference [, flags [, displayParam [, "customDescription"]]]]]

unID: unique identifier, which must be unique among the hotspots defined in the library part. paramReference: parameter that can be edited by this hotspot using the graphical hotspot based parameter editing method. displayParam: parameter to display in the information palette when editing the paramRefrence parameter. Members of arrays can be

passed as well.

customDescription: custom description string for the displayed parameter in the information palette. When using this option, displayParam must be set as well (use paramReference for default). The value set for the moving type hotspot will be displayed only. It is recommended to set the same description for all moving hotspots having the same base hotspot.

Examples of valid arguments: D, Arr[5], Arr[2*I+3][D+1], etc. flags: hotspot’s type + hotspot’s attribute: type:

- 1: length type editing, base hotspot,
- 2: length type editing, moving hotspot,
- 3: length type editing, reference hotspot (always hidden),
- 4: angle type editing, base hotspot,
- 5: angle type editing, moving hotspot,
- 6: angle type editing, center of angle (always hidden),
- 7: angle type editing, reference hotspot (always hidden).