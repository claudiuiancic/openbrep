---
id: wiki.generated.binary
type: wiki
category: other
commands: ["BINARY"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### BINARY

BINARY mode [, section, elementID]

Special command to include inline binary objects into a GDL macro. A set of vertices, vectors, edges, polygons, bodies and materials is read from a special section of the library part file. These are transformed according to the current transformations and merged into the 3D model. The data contained in the binary section is not editable by the user.

mode: defines pencolor and material attribute definition usage.

- 0: the current PEN and MATERIAL settings are in effect,
- 1: the current PEN and MATERIAL settings have no effect. The library part will be shown with the stored colors and material definitions. Surface appearance is constant,
- 2: the stored PEN and MATERIAL settings are used, non-defined materials are replaced by current settings,
- 3: the stored PEN and MATERIAL settings are used, non-defined materials are replaced by the stored default attributes.


section: index of the binary part, from 1 to 16. 0: you can refer simultaneously to all the existing binary parts, 1: Only these sections can be saved from within GDL, BINARY commands without the section argument will also refer to this, 2-16: can be used by third party tools.

elementID: ID of an element of this binary part. This parameter is generated during the import process.

If you open files with a different data structure (e.g., DXF or ZOOM) their 3D description will be converted into binary format. You can save a library part in binary format from the main Library Part editing window through the Save as... command. If the Save in binary format checkbox is marked in the Save as... dialog box, the GDL text of the current library part will be replaced with a binary description. Hint: Saving the 3D model after a 3D cutaway operation in binary format will save the truncated model. This way, you can create cut shapes. You can only save your library part in binary format if you have already generated its 3D model. By replacing the GDL description of your library part with a binary description you can considerably reduce the 3D conversion time of the item. On the other hand, the binary 3D description is not parametric and takes more disk space than an algorithmic GDL script.

## 2D SHAPES

This chapter presents the commands used for generating shapes in 2D from simple forms such as lines and arcs to complex polygons and splines, and the definition of text elements in 2D. It also covers the way binary data is handled in 2D and the projection of the shape created by a 3D script into the 2D view, thereby ensuring coherence between the 3D and 2D appearance of objects. Further commands allow users to place graphic elements into element lists created for calculations.

DRAWING ELEMENTS