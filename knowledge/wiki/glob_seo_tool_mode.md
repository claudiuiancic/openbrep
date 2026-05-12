---
id: wiki.generated.glob_seo_tool_mode
type: wiki
category: other
commands: ["GLOB_SEO_TOOL_MODE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### GLOB_SEO_TOOL_MODE = 1 generating as an operator for Solid Element Operations

The generated 3D model is used as a parameter for solid (CSG) operations. This can be useful, when the object's space demand is larger than the object itself. E.g. when you subtract a stair from a slab, you'd expect that the stair cuts a hole for the walking people, too. To achieve this, in this context the stair should generate a model containing that walking space.