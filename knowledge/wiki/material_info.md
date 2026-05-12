---
id: wiki.generated.material_info
type: wiki
category: other
commands: ["MATERIAL_INFO"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### MATERIAL_INFO

n = REQUEST{2}("MATERIAL_INFO", name_or_index, param_name, value_or_values)

Returns information in the given variable(s) on a parameter (or extra parameter, see the section called “Additional Data”) of the specified material. RGB information is returned in three separate variables, texture information is returned in the following variables: file_name, width, height, mask, rotation_angle corresponding to the texture definition. All other parameter information is returned in single variables. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning. Possible material parameter names corresponding to parameters of the material definition:

param_name: "gs_mat_surface_rgb": surface R, G, B [0.0..1.0] "gs_mat_surface_r": surface R [0.0..1.0] "gs_mat_surface_g": surface G [0.0..1.0] "gs_mat_surface_b": surface B [0.0..1.0] "gs_mat_ambient": ambient coefficient [0.0..1.0] "gs_mat_diffuse": diffuse coefficient [0.0..1.0] "gs_mat_specular": specular coefficient [0.0..1.0] "gs_mat_transparent": transparent coefficient [0.0..1.0] "gs_mat_shining": shininess [0.0..100.0] "gs_mat_transp_att": transparency attenuation [0.0..4.0] "gs_mat_specular_rgb": specular color R, G, B [0.0..1.0] "gs_mat_specular_r": specular color R [0.0..1.0] "gs_mat_specular_g": specular color G [0.0..1.0] "gs_mat_specular_b": specular color B [0.0..1.0] "gs_mat_emission_rgb": emission color R, G, B [0.0..1.0] "gs_mat_emission_r": emission color R [0.0..1.0]

"gs_mat_emission_g": emission color G [0.0..1.0] "gs_mat_emission_b": emission color B [0.0..1.0] "gs_mat_emission_att": emission attenuation [0.0..65.5] "gs_mat_fill_ind": fill index "gs_mat_fillcolor_ind": fill color index "gs_mat_texture": texture index

Example:

n = REQUEST{2} ("MATERIAL_INFO", "Brick-Face", "gs_mat_ambient", a) n = REQUEST{2} ("MATERIAL_INFO", 1, "gs_mat_surface_rgb", r, g, b) n = REQUEST{2} ("MATERIAL_INFO", "Brick-Face", "gs_mat_texture",

file_name, w, h, mask, alpha) n = REQUEST{2} ("MATERIAL_INFO", "My-Material", "my_extra_parameter", e)