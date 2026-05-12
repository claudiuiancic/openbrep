---
id: wiki.generated.position
type: wiki
category: other
commands: ["POSITION"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### POSITION

POSITION position_keyword Effective only in the Component List.

Changes only the type of the element the following descriptors and components are associated to. If there are no such directives in the Properties script, descriptors and components will be listed with their default element types. position_keyword: keywords are the following:

WALLS COLUMNS BEAMS DOORS WINDOWS OBJECTS CEILS PITCHED_ROOFS LIGHTS HATCHES ROOMS MESHES

A directive remains valid for all succeeding DESCRIPTORs and COMPONENTs until the next directive is ascribed. A script can include any number of directives.

Example:

DESCRIPTOR "\tPainted box.\n\t Properties:\n\ \t\t - swinging doors\n\ \t\t - adjustable height\n\ \t\t - scratchproof" REF DESCRIPTOR "0001" s = SURFACE3D () !wardrobe surface COMPONENT "glue", 1.5, "kg" COMPONENT "handle", 2*c, "nb" !c number of doors COMPONENT "paint", 0.5*s, "kg" POSITION WALLS REF COMPONENT "0002"