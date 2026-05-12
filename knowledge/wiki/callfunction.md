---
id: wiki.generated.callfunction
type: wiki
category: control
commands: ["CALLFUNCTION"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### CALLFUNCTION

CALLFUNCTION (channel, function_name, parameter, variable1 [, variable2, ...]) The function named function_name in the add-on specified by channel is called. The parameter list must contain at least one value. This function puts the returned values into the parameters as ordered. The return value is the number of the successfully set values. channel: channel value, used to identify the connection.

function_name: the string or numeric identifier of the function to be called; its contents are interpreted by the extension. parameter: input parameter; its contents are interpreted by the extension. variablei: output parameter.