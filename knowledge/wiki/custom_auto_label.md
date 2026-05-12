---
id: wiki.generated.custom_auto_label
type: wiki
category: other
commands: ["CUSTOM_AUTO_LABEL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### CUSTOM_AUTO_LABEL

n = REQUEST("CUSTOM_AUTO_LABEL", "", name) Returns in the name variable the name of the custom auto label of the library part or an empty string if it does not exist. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning.