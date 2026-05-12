---
id: wiki.generated.hideparameter
type: wiki
category: other
commands: ["HIDEPARAMETER"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### HIDEPARAMETER

HIDEPARAMETER "name1" [, "name2", ..., "namen"] Hides the named parameter(s) and its child parameters in the settings dialog box. A parameter hidden using this command in the parameter script will automatically disappear from the parameter list. namen: string expression, name of the parameter to be hidden. Compatibility: starting from Archicad 22, the locking/hiding of selected Archicad interface controls is extended. For details, see the LOCK command. HIDEPARAMETER ALL ["name1" [, "name2", ..., "namen"]] Hides all parameters and its child parameters in the settings dialog box, except those (and their children) listed after the ALL keyword.