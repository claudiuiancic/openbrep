---
id: wiki.generated.fragment2
type: wiki
category: 2d
commands: ["FRAGMENT2"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### FRAGMENT2

FRAGMENT2 fragment_index, use_current_attributes_flag FRAGMENT2 ALL, use_current_attributes_flag

The fragment with the given index is inserted into the 2D Full View with the current transformations. If ALL is specified, all fragments are inserted. use_current_attributes_flag: defines whether or not the current attributes will be used.

0: the fragment appears with the color, line type and fill type defined for it, 1: the current settings of the script are used instead of the color, line type and fill type of the fragment.

3D PROJECTIONS IN 2D