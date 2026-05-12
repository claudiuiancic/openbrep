---
id: wiki.generated.initaddonscope
type: wiki
category: other
commands: ["INITADDONSCOPE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### INITADDONSCOPE

INITADDONSCOPE (extension, parameter_string1, parameter_string2) Opens a channel as directed. Its return value is a positive integer that will identify the specific connection. This value, the channel number, will be the connection’s reference number in succeeding instances.

extension: string, the name of an existing extension. parameter_string1: string, its contents are interpreted by the extension. parameter_string2: string, its contents are interpreted by the extension.