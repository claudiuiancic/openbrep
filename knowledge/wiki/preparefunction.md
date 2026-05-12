---
id: wiki.generated.preparefunction
type: wiki
category: other
commands: ["PREPAREFUNCTION"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PREPAREFUNCTION

PREPAREFUNCTION channel, function_name, expression1 [, expression2, ...] Sets some values in the add-on as a preparation step for calling a later function.

function_name: the string or numeric identifier of the function to be called; its contents are interpreted by the extension. expression: parameters to be passed for the preparation step.