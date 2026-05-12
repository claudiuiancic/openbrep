---
id: wiki.generated.ui_listfield
type: wiki
category: other
commands: ["UI_LISTFIELD"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### UI_LISTFIELD

UI_LISTFIELD fieldID, x, y, width, height [, iconFlag [, description_header [, value_header]]] Generates a control for the parameter input as a scrollable list containing an arbitrary number of rows, with the following columns: icon, description and input field for the parameter value. Lines of the list can be defined with the UI_LISTITEM command. UI_LISTFIELD and UI_LISTITEM definitions can be scripted in an arbitrary order. Empty listfields (with no list items) are not displayed.

fieldID: the unique identifier of the listfield. This ID also used in the UI_LISTITEM commands specifies the listfield the listitems belong

to. Duplicates within a user interface script are not allowed.

x, y: position of the listfield's top left corner. width, height: width and height in pixels. iconFlag:

iconFlag = 0: icon column is not generated for this listfield. iconFlag = 1: icon column is generated for this listfield (default value if not specified).

If the Custom Settings panel has only one control and this control is a listfield, the x, y, width, height parameters have no effect. In this case the width of the listfield equals to the width of the Custom Settings panel.

description_header: the title of the Description column. value_header: the title of the Value column.

If both description_header and value_header are empty strings or not specified, the listfield is generated without a header. If the strings contain at least one space, the listfield is generated with an empty header.