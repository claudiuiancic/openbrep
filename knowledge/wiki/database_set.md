---
id: wiki.generated.database_set
type: wiki
category: other
commands: ["DATABASE_SET"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### DATABASE_SET

DATABASE_SET set_name [, descriptor_name, component_name, unit_name, key_name,

criteria_name, list_set_name] Database set definition or Database set selection. If this command is placed in a MASTER_GDL script, it will define a Database set containing Descriptor, Component, Unit, Key, Criteria and List Scheme files.

This Database set name can then be referenced from Properties Scripts using the same command with only the set_name parameter as a directive, by selecting the actual Database set that REF COMPONENTs and REF DESCRIPTORs refer to. The default Database set name is "Default Set", and will be used if no other set has been selected. The default Database set file names are: DESCDATA, COMPDATA, COMPUNIT, LISTKEY, LISTCRIT, LISTSET. All these names get translated in localized Archicad versions.

Scripts can include any number of DATABASE_SET selections. set_name: database set name. descriptor_name: descriptor data file name. component_name: component data file name. unit_name: unit data file name. key_name: key data file name.

criteria_name: criteria file name. list_set_name: list Scheme file name.