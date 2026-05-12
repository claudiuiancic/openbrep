---
id: wiki.generated.libraryglobal
type: wiki
category: other
commands: ["LIBRARYGLOBAL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### LIBRARYGLOBAL

LIBRARYGLOBAL (object_name, parameter, value)

Fills value with the current model view option parameter value of the library global object defined by object_name if available. A library global setting is available if the global object is currently loaded in the library, or was loaded earlier and its setting was saved in the current model view option combination.

Visible placed objects whose 2d or 3d scripts contain LIBRARYGLOBAL commands are refreshed when the library global object's parameters change at Model View Options. Parameter and migration scripts should not use LIBRARYGLOBAL values, the current view should not have any effect on other views.

Returns 1 if successful, 0 otherwise. object_name: name of library global object. Must be a string constant. Warning: If string variables or parameters are used as object names,

then the 2d and 3d view of objects querying this library global object will not refresh automatically. parameter: name of requested parameter. value: filled with the requested parameter value.

Example:

success = LIBRARYGLOBAL ("MyGlobalOptions", "detLevel2D", det) if success > 0 then

text2 0, 0, det else

text2 0, 0, "Not available" endif