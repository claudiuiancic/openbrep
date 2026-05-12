---
id: wiki.generated.picture
type: wiki
category: other
commands: ["PICTURE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PICTURE

PICTURE expression, a, b, mask A picture element for photorendering.

|a numeric expression or the index of a picture|
|---|


A string type expression means a file name, stored in the library part. A 0 index is a special value that refers to the preview picture of the library part. Other pictures can only be stored in library parts when saving the project or selected elements containing pictures as GDL Objects.

Indexed picture reference cannot be used in the MASTER_GDL script when attributes are merged into the current attribute set. The image is fitted on a rectangle treated as a RECT in any other 3D projection method.

mask: alpha + distortion alpha: alpha channel control.

- 0: do not use alpha channel; picture is a rectangle,
- 1: use alpha channel; parts of the picture may be transparent.

distortion: distortion control.

0: fit the picture into the given rectangle,

- 2: fit the picture in the middle of the rectangle using the natural aspect ratio of the picture, 4: fill the rectangle with the picture in a central position using natural aspect ratio of the picture.


distortion=0 distortion=2 distortion=4

3D TEXT ELEMENTS