---
id: wiki.generated.component_ids_of_parent
type: wiki
category: other
commands: ["COMPONENT_IDS_OF_PARENT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### COMPONENT_IDS_OF_PARENT

n = REQUEST("COMPONENT_IDS_OF_PARENT", collectComponents, outputCompIds) Returns the building material component IDs of the parent object in a dictionary form. Can be used only in labels. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning. Compatibility: introduced in Archicad 23.

collectComponents: (dictionary) defining the method of collecting the building material components of the parent object. collectComponents.collectMode: (integer) the method of collecting the building material components. This key is optional, if it

does not exist, the request uses a default collectMode of 1. 1: (default) returns all the building material component IDs of the parent 2: returns the same building material component IDs in the same order as in WALL_SKINS_PARAMS, SHELLBASE_SKINS_PARAMS, SLAB_SKINS_PARAMS or ROOF_SKINS_PARAMS - depending on the element type of the parent.

outputCompIds: (dictionary) the building material component IDs of the parent object. outputCompIds.componentIds[n]: (array) contains dictionaries for each building material component ID. outputCompIds.componentIds[n].id: (integer) the building material component ID of the parent element.

Example: dict collectComponents

collectComponents.collectMode = 1 dict outputCompIds n = REQUEST ("COMPONENT_IDS_OF_PARENT", collectComponents, outputCompIds) ! outputCompIds ! .componentIds[1].id ! .componentIds[2].id ! ... ! .componentIds[n].id