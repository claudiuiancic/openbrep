---
id: wiki.generated.datetime
type: wiki
category: other
commands: ["DATETIME"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### DATETIME

n = REQUEST("DATETIME", format_string, datetimestring) Returns the current date and time as a formatted string in datetimestring. Uses the DateTime Add-On, opening and closing the required channel.

format_string: Format string, described at paramString parameter of the section called “Opening Channel” . datetimestring: the formatted string is returned in this variable The requests cause warning if used in parameter script.