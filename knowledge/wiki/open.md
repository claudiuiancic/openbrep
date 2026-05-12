---
id: wiki.generated.open
type: wiki
category: other
commands: ["OPEN"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### OPEN

OPEN (filter, filename, parameter_string)

Opens a file as directed. Its return value is a positive integer that will identify the specific file, -2 if the add-on is missing, -1 if the file is missing. If positive, this value, the channel number, will be the file’s reference number in succeeding instances. To include the referenced file in the archive project, use the FILE_DEPENDENCE command with the file name.

filter: string, the name of an existing extension. filename: string, the name of the file. parameter_string: string, it contains the specific separation characters of the operational extension and the mode of opening. Its

contents are interpreted by the extension.