---
id: wiki.generated.ui_listitem_2
type: wiki
category: other
commands: ["UI_LISTITEM{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### UI_LISTITEM{2}

UI_LISTITEM{2} itemID, fieldID, name [, childFlag [, image [, paramDesc]]] Appends a listitem to the listfield defined by the fieldID parameter. itemID: the unique identifier of the listitem. Listitems can be scripted in an arbitrary order and are sorted by itemID. Duplicate listitem

IDs within a listfield are not allowed. fieldID: the unique identifier of the listfield containing this listitem. name: parameter name as string expression for UI_LISTITEM or parameter name with optional actual index values if array for

UI_LISTITEM{2}.

childFlag: childFlag = 0: the listitem is a groupitem (default value if not specified). childFlag = 1: the listitem is a childitem. The parent item is the first groupitem above.

image: file name or index number of the picture stored in the library part. If valid, it is displayed as an icon in the first column of the

listfield in the associated listitem's row.

paramDesc: the visible name of the listitem in the Description column. If left empty, the description is automatically filled up from the

parameter list description of the Library Part. If there is no description there, the name of the parameter is displayed instead.

If "name" string is empty, the listitem is a group with bold fonttype. If both "name" string and paramDesc are empty, the listitem is a separator. The HIDEPARAMETER command is ineffective for list items, the script should not add the item instead of using it. The LOCK command can be used and it is effective for list items.

For a listfield it is recommended to define different itemIDs for different parameters, groups and separators.

Example: ! List with header without icon column ui_listfield 1, 10, 35, 432, 220, 0, "Description Header Text", "Value Header Text"

- ui_listitem 1, 1, "", 0, "", "Group Title 1" ! Group Line
- ui_listitem 2, 1, "A", 1
- ui_listitem 3, 1, "B", 1
- ui_listitem 4, 1, "ZZYZX", 1
- ui_listitem 5, 1, "" !separator
- ui_listitem 6, 1, "AC_show2DHotspotsIn3D", 0, "", "Group Title 2" ! Group Parameter Line
- ui_listitem 7, 1, "A", 1, "", "Custom Description A"
- ui_listitem 8, 1, "B", 1, "", "Custom Description B"
- ui_listitem 9, 1, "ZZYZX", 1, "", "Custom Description ZZYZX"


![image 19](<GDL_Reference_Guide_28_images/imageFile19.png>)