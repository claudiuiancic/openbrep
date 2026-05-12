---
id: wiki.generated.split
type: wiki
category: string
commands: ["SPLIT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### SPLIT

SPLIT (string, format, variable1 [, variable2, ..., variablen]) Splits the string parameter according to the format in one or more numeric or string parts. The split process stops when the first non-matching part is encountered. Returns the number of successfully read values (integer).

string: the string to be split. format: any combination of constant strings, %s, %n and %^n -s. Parts in the string must fit the constant strings, %s denotes any string

value delimited by spaces or tabs, while %n or %^n denotes any numeric value. If the '^' flag is present, current system settings for decimal separator and digit grouping characters are taken into consideration when matching the actual numerical value.

variablei: names of the variables to store the split string parts.

ss = "3 pieces 2x5 beam"

- n = SPLIT (ss, "%n pieces %nx%n %s", num, ss1, size1, ss2, size2, name) IF n = 6 THEN


PRINT num, ss1, size1, ss2, size2, name ! 3 pieces 2 x 5 beam ELSE

PRINT "ERROR" ENDIF