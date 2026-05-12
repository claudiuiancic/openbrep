---
id: wiki.generated.teve
type: wiki
category: 3d
commands: ["TEVE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### TEVE

TEVE x, y, z, u, v Extension of the VERT command including a texture coordinate definition. Can be used instead of the VERT command if user-defined texture coordinates are required instead of the automatic texture wrapping (see the COOR command).

x, y, z: coordinates of a node. u, v: texture coordinates of the node (u, v) coordinates for each vertex of the current body must be specified and each vertex should have

only one texture coordinate. If VERT and TEVE statements are mixed inside a body definition, (u, v) coordinates are ineffective. Note: The (u, v) texture coordinates are only effective in photorenderings, and not for vectorial fill mapping.