---
id: wiki.generated.building_material_info
type: wiki
category: other
commands: ["BUILDING_MATERIAL_INFO"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### BUILDING_MATERIAL_INFO

n = REQUEST{2}("BUILDING_MATERIAL_INFO", name_or_index, param_name, value_or_values)

Returns information in the given variable(s) on a parameter of the specified building material. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning. Possible building material parameter names corresponding to parameters of the building material definition:

param_name: "gs_bmat_id": building material id "gs_bmat_surface": building material surface index "gs_bmat_description": building material description "gs_bmat_manufacturer": building material manufacturer "gs_bmat_collisiondetection": building material participates in collision detection (0 or 1) "gs_bmat_intersectionpriority": building material intersection priority "gs_bmat_cutFill_properties": building material cut fill properties (cut fill index number, cut fill foreground pen index number, cut fill background pen index number) "gs_bmat_physical_properties": building material physical properties (thermal conductivity, density, heat capacity, embodied energy, embodied carbon)

Example:

n = REQUEST{2} ("BUILDING_MATERIAL_INFO", "Brick", "gs_bmat_id", id) n = REQUEST{2} ("BUILDING_MATERIAL_INFO", "Brick", "gs_bmat_surface", index) n = REQUEST{2} ("BUILDING_MATERIAL_INFO", "Brick", "gs_bmat_physical_properties",

thermalConductivity, density, heatCapacity, embodiedEnergy, embodiedCarbon)