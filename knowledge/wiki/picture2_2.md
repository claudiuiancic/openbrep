---
id: wiki.generated.picture2_2
type: wiki
category: 2d
commands: ["PICTURE2{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PICTURE2{2}

PICTURE2{2} expression, a, b, mask Can be used in 2D similarly to the PICTURE command in 3D. Unlike in 3D, the mask values have no effect on 2D pictures. A string type expression means a file name, a numerical expression means an index of a picture stored in the library part. A 0 index is a special value, it refers to the preview picture of the library part. For PICTURE2{2} mask = 1 means that exact white colored pixels are transparent. Other pictures can only be stored in library parts when saving the project or selected elements containing pictures as GDL objects.

TEXT ELEMENT