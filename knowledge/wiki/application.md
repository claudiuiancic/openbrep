---
id: wiki.generated.application
type: wiki
category: other
commands: ["APPLICATION"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### APPLICATION QUERY OPTIONS

n = APPLICATION_QUERY (extension_name, parameter_string, variable1, variable2, ...)

Below is a list of request functions Archicad can provide with the help of the APPLICATION_QUERY command. These request options are given in the extension_name and the parameter_string parameter of the command. Note, that the query options and return values of an APPLICATION_QUERY may vary according to the execution context.

The use of the following application query types in parameter script is not supported. These queries cause GDL warnings starting from Archicad 19, and will return either 0 or empty string starting from the next versions. The restriction applies to:

• "document_feature"