---
id: wiki.generated.class_of_fill
type: wiki
category: other
commands: ["CLASS_OF_FILL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### CLASS_OF_FILL

n = REQUEST("CLASS_OF_FILL", index, class) Returns class of the fill identified by index in the class variable. Causes warning if used in parameter script.

class: Possible values:

- 1: vector fill
- 2: symbol fill
- 3: translucent fill
- 4: linear gradient fill
- 5: radial gradient fill
- 6: image fill