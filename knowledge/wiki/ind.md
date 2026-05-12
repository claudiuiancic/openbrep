---
id: wiki.generated.ind
type: wiki
category: other
commands: ["IND"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### IND

IND (MATERIAL, name_string) IND (BUILDING_MATERIAL, name_string) IND (FILL, name_string) IND (LINE_TYPE, name_string) IND (STYLE, name_string) IND (TEXTURE, name_string) IND (PROFILE_ATTR, name_string, index)

This function returns the current index of the material, building material, fill, line type or style, texture or profile attribute. The main use of the resulting number is to transfer it to a macro that requires the same attribute as the calling macro. The functions return an attribute index (integer) value. The result is negative for inline definitions (inside the script or from Master_GDL file) and positive for global definitions (from the project attributes). See also the section called “Inline Attribute Definition”.