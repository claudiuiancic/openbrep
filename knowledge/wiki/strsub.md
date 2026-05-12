---
id: wiki.generated.strsub
type: wiki
category: string
commands: ["STRSUB"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### STRSUB

STRSUB (string_expression, start_position, characters_number) Returns a substring of the string parameter that begins at the position given by the start_position parameter and its length is characters_number characters.

Example:

string = "Flowers.jpeg" len = STRLEN (string) iDotPos = STRSTR (string, ".")

- TEXT2 0, -1, STRSUB (string, 1, iDotPos - 1) !Flowers
- TEXT2 0, -2, STRSUB (string, len - 4, 5) !.jpeg