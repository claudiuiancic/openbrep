---
id: wiki.generated.lock
type: wiki
category: param
commands: ["LOCK"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### LOCK

LOCK "name1" [, "name2", ..., "namen"] Locks the named parameter(s) in the settings dialog box. A locked parameter will appear grayed in the dialog box and its value cannot be modified by the user.

namen: string expression, name of the parameter to be locked. Compatibility: starting from Archicad 22, the locking/hiding of selected Archicad interface controls is extended.

The extended feature can be activated with "Enable hide/lock of specific fix named optional parameters" setting (see "Details/Compatibility Options" dialog of the object in the Library Part Editor). The extended selection contains fix named optional parameters corresponding to:

- • standard text handling controls of "Text Style" settings dialog panel - see the section called “Parameters for Text Handling”,
- • extended label styling controls of "Text Style" settings dialog panel in Label tool - see the section called “Parameters for Labels”,
- • and selected label pointer controls of "Pointer" settings dialog panel - see the section called “Parameters for Labels”. LOCK ALL ["name1" [, "name2", ..., "namen"]] Locks all parameters in the settings dialog box, except those listed after the ALL keyword.