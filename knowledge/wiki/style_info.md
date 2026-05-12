---
id: wiki.generated.style_info
type: wiki
category: other
commands: ["STYLE_INFO"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### STYLE_INFO

n = REQUEST("STYLE_INFO", name, fontname [, size, anchor, face_or_slant]) Returns information in the given variables on the previously defined style (see style parameters at the DEFINE STYLE command). Can be useful in macros to collect information on the style defined in a main script. Causes warning if used in parameter script.