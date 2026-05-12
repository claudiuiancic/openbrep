---
id: wiki.generated.stored_par_value
type: wiki
category: other
commands: ["STORED_PAR_VALUE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### STORED_PAR_VALUE

STORED_PAR_VALUE ("oldparname", outputvalue)

Retrieves the value of a parameter, which is present in the migrated object, and present or deleted in the new version object. This command form is suggested for those parameters present in the new object as well. To get the value of an old array Parameter, the outputvalue parameter must be initialized as an array (with the dim command).

oldparname: string expression, name of the parameter in the old parameter list. outputvalue: output variable to store the value of the parameter.

Return value: 1 on success, 0 otherwise (for example, if there is no parameter with that name in the parameter list of the old object). During checking the script the return value is always 0, because the old Parameters section is not known.