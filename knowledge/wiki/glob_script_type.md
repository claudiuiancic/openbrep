---
id: wiki.generated.glob_script_type
type: wiki
category: other
commands: ["GLOB_SCRIPT_TYPE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### GLOB_SCRIPT_TYPE type of current script

- • 1 - properties script
- • 2 - 2D script
- • 3 - 3D script
- • 4 - user interface script
- • 5 - parameter script
- • 6 - master script
- • 7 - forward migration script
- • 8 - backward migration script


GLOB_VIEW_TYPE type of current view (view dependent, do not use in parameter/property scripts).

|2D| |3D| |UI| |Parameter| |Property| |Default|-|
|---|---|---|---|---|---|---|---|---|---|---|---|


- • 2 - 2D (Floor Plan)
- • 3 - 3D
- • 4 - Section
- • 5 - Elevation
- • 6 - 3D Document
- • 7 - Detail
- • 8 - Layout
- • 9 - Calculation Use the exact needed values. Using ranges are not recommended due to possible future value extensions.


GLOB_PREVIEW_MODE type of current preview (view dependent, do not use in parameter/property scripts)

- • 0 - None
- • 1 - Dialog
- • 2 - Listing
- • 3 - Favorite saving Use the exact needed values. Using ranges are not recommended due to possible future value extensions.


GLOB_FEEDBACK_MODE indicates editing in progress (view dependent, do not use in parameter/property scripts)

0 - off, 1 - editing feedback mode

GLOB_SEO_TOOL_MODE indicates solid element operations in progress (view dependent, do not use in parameter/property

scripts) 0 - off, 1 - solid element operations mode

GLOB_DIAGNOSTICS_MODE Library Developer (59) menu command for GDL diagnostics Compatibility: introduced in Archicad 23. 0 - off, 1 - on Use in scripts as a conditional statement to visualize debug content of library parts.

GLOB_SCALE drawing scale (view dependent, do not use in parameter/property scripts)

|2D| |3D| |UI| |Parameter| |Property| |Default|100|
|---|---|---|---|---|---|---|---|---|---|---|---|


according to the current window

GLOB_DRAWING_BGD_PEN pen of the drawing background color (view dependent, do not use in parameter/property scripts)

|2D| |3D| |UI| |Parameter| |Property| |Default|19|
|---|---|---|---|---|---|---|---|---|---|---|---|


the best matching (printable) pen from the current palette to the background color of the current window

GLOB_FILL_INDEX_SOLID index of fill type "Solid" according to the template (project dependent, do not use in parameter

script)

|2D| |3D| |UI| |Parameter| |Property| |Default|16|
|---|---|---|---|---|---|---|---|---|---|---|---|


contains the applied index of the fill type "Solid" Compatibility: introduced in Archicad 22.

GLOB_FILL_INDEX_BACKGROUND index of fill type "Background" according to the template (project dependent, do not use in

parameter script)

|2D| |3D| |UI| |Parameter| |Property| |Default|16|
|---|---|---|---|---|---|---|---|---|---|---|---|


contains the applied index of the fill type "Background" Compatibility: introduced in Archicad 22.

GLOB_NORTH_DIR project North direction (project dependent, do not use in parameter script)

|2D| |3D| |UI| |Parameter| |Property| |Default|90|
|---|---|---|---|---|---|---|---|---|---|---|---|


relative to the default project coordinate system according to the settings made in the Project Location dialog

GLOB_PROJECT_LONGITUDE project longitude (project dependent, do not use in parameter script) GLOB_PROJECT_LATITUDE project latitude (project dependent, do not use in parameter script) GLOB_PROJECT_ALTITUDE project altitude (project dependent, do not use in parameter script)

|2D| |3D| |UI| |Parameter| |Property| |Default|0|
|---|---|---|---|---|---|---|---|---|---|---|---|


the geographical coordinates of the project origin according to the settings specified in the Project Location dialog

GLOB_PROJECT_DATE project date (project dependent, do not use in parameter script)

|2D| |3D| |UI| |Parameter| |Property| |Default|[0, 0, 0, 0, 0, 0]|
|---|---|---|---|---|---|---|---|---|---|---|---|


array of the following six values: 1 - year, 2 - month, 3 - day, 4 - hour, 5 - minute, 6 - second. This variable contains the project's current date and is only set in the EcoDesigner STAR® add-on (in other cases all values are set to 0). The value of this variable is modified by the add-on when running the solar analysis routines to allow certain GDL objects (for example deciduous trees) to be represented differently at different times of the year.

GLOB_WORLD_ORIGO_OFFSET_X (project dependent, do not use in parameter script) GLOB_WORLD_ORIGO_OFFSET_Y (project dependent, do not use in parameter script)

|2D| |3D| |UI| |Parameter| |Property| |Default|0|
|---|---|---|---|---|---|---|---|---|---|---|---|


Position of the project origin relative to the world origin. See Illustrating the usage of the GLOB_WORLD_ORIGO_... globals. GLOB_MODPAR_NAME name of the last modified parameter

in the settings dialog or library part editor, including parameters modified through editable hotspots.

GLOB_UI_BUTTON_ID id of the button pushed on the UI page

or 0, if the last action was not the push of a button with id.

GLOB_CUTPLANES_INFO (project dependent, do not use in parameter script)

|2D| |3D| |UI| |Parameter| |Property| |Default|[1.,, 3.0, -0.1, -0.1]|
|---|---|---|---|---|---|---|---|---|---|---|---|


array of 4 length values: 1 - cutplane height, 2 - cutplane top level, 3 - cutplane bottom level, 4 - absolute display limit, in the library part’s local coordinate system. See details in Archicad Set Floor Plan Cutplane dialog.

GLOB_STRUCTURE_DISPLAY structure display detail (project dependent, do not use in parameter script)

|2D| |3D| |UI| |Parameter| |Property| |Default|0|
|---|---|---|---|---|---|---|---|---|---|---|---|


informs about the partial structure display option settings (integer): 0 - entire structure, 1 - core only, 2 - without finishes

GLOB_ISSUE_SCHEME list of custom data defined in the Issue Scheme

|2D| |3D| |UI| |Parameter| |Property| |Default|-|
|---|---|---|---|---|---|---|---|---|---|---|---|


Available in all context. 2-row string array, containing the names of fields defined in the Issue Scheme (first row), with the corresponding GUIDs (second row). The first five columns are fixed: Revision ID, Issue ID, Issue Name, Issue Date, Issued by. For example:

|Revision ID|Issue ID|Issue Name|Issue Date|Issued By|Recipient|Status|...|
|---|---|---|---|---|---|---|---|
|{RevIdGUID}|{IssueIdGUID}|{IssueNameGUID}|{IssueDateGUID}|{IssuedByGUID}|{Custom1GUID}|{Custom2GUID}| |


LAYOUT_REVISION_HISTORY list of the current Layout's Revision History

|2D| |3D| |UI| |Parameter| |Property| |Default|-|
|---|---|---|---|---|---|---|---|---|---|---|---|


Available in Layout context only. String array, containing 1 row per Revision, in the same structure as GLOB_ISSUE_SCHEME. The first five columns are fixed: Revision ID, Issue ID, Issue Name, Issue Date, Issued by. For example:

|01|1|First Issue|2013-06-30|user1|Everyone|SD|...|
|---|---|---|---|---|---|---|---|
|02|3|General Update|2013-07-31|user2|Mechanical|DD| |
|03|5|Structural Update|2013-08-31|user1|Structural|DD| |
|...| | | | | | | |


GLOB_CHANGE_SCHEME list of custom data defined in the Change Scheme

|2D| |3D| |UI| |Parameter| |Property| |Default|-|
|---|---|---|---|---|---|---|---|---|---|---|---|


Available in all context. 2-row string array, containing the names of fields defined in the Change Scheme (first row), with the corresponding GUIDs (second row). The first five columns are fixed: Revision ID, Change ID, Change Name, Last Modified Date, Last Modified by. For example:

|Revision ID|Change ID|Change Description|Last Modified|Last Modified By|Created by|Approved by|...|
|---|---|---|---|---|---|---|---|
|{RevIdGUID}|{ChIdGUID}|{ChDescGUID}|{ModiTimeGUID}|{ModiByGUID}|{Custom1GUID}|{Custom2GUID}| |


LAYOUT_CHANGE_HISTORY list of all the Changes appearing in the current Layout's Revision History

|2D| |3D| |UI| |Parameter| |Property| |Default|-|
|---|---|---|---|---|---|---|---|---|---|---|---|


Available in Layout context only. String array, containing 1 row per Change, in the same structure as GLOB_CHANGE_SCHEME. The first five columns are fixed: Revision ID, Change ID, Change Name, Last Modified Date, Last Modified by. For example:

|2|Ch-13|Kitchen|2013-07-13|user1|Architect 1|Lead Architect 1|...|
|---|---|---|---|---|---|---|---|
|2|Ch-15|Ventillation|2013-07-16|user2|Architect 2|Lead Architect 1| |
|3|Ch-18|Structural Col.|2013-08-03|user2|Architect 1|Lead Architect 2| |
|3|Ch-19|Truss Sections|2013-08-12|user1|Architect 3|Lead Architect 2| |
|B|Ch-23|Door Numbering|2013-10-01|user3|Architect 2|Lead Architect 1| |
|...| | | | | | | |


LAYOUT_CURRENTREVISION_OPEN Work in Progress state of the current Layout (project dependent, do not use in parameter script)

|2D| |3D| |UI| |Parameter| |Property| |Default|0|
|---|---|---|---|---|---|---|---|---|---|---|---|


Available in Layout context only. 0 - current Layout has no open Revision, 1 - current Layout has an open Revision (it is a Work in Progress Layout)