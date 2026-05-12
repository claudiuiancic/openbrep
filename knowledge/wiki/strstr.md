---
id: wiki.generated.strstr
type: wiki
category: string
commands: ["STRSTR"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### STRSTR

STRSTR (string_expression1, string_expression2[, case_insensitivity]) Returns the (integer) position of the first appearance of the second string in the first string. If the first string doesn’t contain the second one, the function returns 0. Note: In case string_expression2 is an empty string, the function returns 1. case_insensitivity:

0 or not set: Case sensitive 1: Case insensitive

- Example 1:

szFormat = "" n = REQUEST ("LINEAR_DIMENSION", "", szFormat) unit = "" IF STRSTR (szFormat, "m") > 0 THEN unit = "m" IF STRSTR (szFormat, "mm") > 0 THEN unit = "mm" IF STRSTR (szFormat, "cm") > 0 THEN unit = "cm" IF STRSTR (szFormat, "dm") > 0 THEN unit = "dm" TEXT2 0, 0, STR (szFormat, a) + " " + unit !1.00 m

- Example 2:


STRSTR ("abcdefg", "BCdEf") = 0 STRSTR ("abcdefg", "BCdEf", 0) = 0 STRSTR ("abcdefg", "BCdEf", 1) = 2