---
id: wiki.generated.profile_component_info
type: wiki
category: other
commands: ["PROFILE_COMPONENT_INFO"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PROFILE_COMPONENT_INFO

- n = REQUEST{4}("PROFILE_COMPONENT_INFO", name_or_index, component_ind, param_name, value) Returns a requested attribute value of a dedicated component (by component_ind) of the profile identified by name or index. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning. The component_ind must be in the valid range of nComponents (defined by the "PROFILE_COMPONENTS" REQUEST). param_name: addresses attribute settings of Profile Manager, returned in value


"gs_profile_bmat": building material index of the component "gs_profile_surface": override surface index of the component (in case of active override settings; returns the surface of the building material otherwise) "gs_profile_showoutline": "Show Outline" setting of the component "gs_profile_outlinetype": "Outline Type" setting of the component "gs_profile_outlinepen": "Outline Pen" setting of the component

Return attribute values can be used in any attribute related command, such as POLY2_B{6}, where contour sections of the polygon can be customized individually. Compatibility: introduced in Archicad 21. n = REQUEST{4}("PROFILE_COMPONENT_INFO", name_or_index, component_ind, param_name,

value1, value2, ..., valuen) Returns requested attributes of all edges in the dedicated component (by component_ind) of the profile identified by name or index. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning. The component_ind must be in the valid range of nComponents (defined by the "PROFILE_COMPONENTS" REQUEST). param_name: addresses attribute settings of Profile Manager, returned in value

"gs_profile_comp_surfaces": individual surface indexes of edges of the component "gs_profile_comp_pens": individual pen indexes of edges of the component "gs_profile_comp_linetypes": individual linetype indexes of edges of the component

Return attribute values can be used in any attribute related command, such as POLY2_B{6}, where contour sections of the polygon can be customized individually. Compatibility: introduced in Archicad 21.