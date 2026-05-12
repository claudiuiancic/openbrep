---
id: wiki.generated.ui_pict
type: wiki
category: other
commands: ["UI_PICT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### UI_PICT

UI_PICT picture_reference, x, y [, width, height [, mask]] Picture element in the dialog box. The picture file must be located in one of the loaded libraries. picture_reference: file name or index number of the picture stored in the library part. The index 0 refers to the preview picture

of the library part. x, y: position of the top left corner of the picture. width, height: optional width and height in pixels; by default, the picture’s original width and height values will be used. mask: alpha + distortion. See the PICTURE command for full explanation.