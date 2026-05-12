---
id: wiki.generated.autotext_list
type: wiki
category: other
commands: ["AUTOTEXT_LIST"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### AUTOTEXT_LIST

n = REQUEST("AUTOTEXT_LIST", "", autoTextListArray)

Returns one AUTOTEXT array of the autotexts used in the project with the following triplets ["ID", "Category", "Name"]. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning. Can be used only in UI script. The ID is stored in the parameter via the UI_CUSTOM_POPUP... commands.

Contains all autotexts from Project Info and Autotext Dialog (Text tool - Insert Autotext).

- Compatibility: introduced in Archicad 20.


Example:

DIM autoTextListArray[] n = REQUEST ("AUTOTEXT_LIST", "", autoTextListArray) ! autoTextListArray = [ID1, CategoryName1, TextName1, ! ID2, CategoryName2, TextName2, ! ... ! IDn, CategoryNamen, TextNamen]