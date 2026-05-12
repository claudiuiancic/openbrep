---
id: wiki.generated.repeat
type: wiki
category: other
commands: ["REPEAT", "UNTIL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### REPEAT - UNTIL

REPEAT [statement1 statement2

... statementn]

UNTIL condition The statements between the keywords are executed until the condition becomes true. The condition is checked after each execution of the statements.

Example: The following four sequences of GDL commands are equivalent

! 1st FOR i = 1 TO 5 STEP 1

BRICK 0.5, 0.5, 0.1 ADDZ 0.3

NEXT i

! 2nd i = 1 DO

BRICK 0.5, 0.5, 0.1 ADDZ 0.3 i = i + 1

WHILE i <= 5

! 3rd i = 1 WHILE i <= 5 DO

BRICK 0.5, 0.5, 0.1 ADDZ 0.3 i = i + 1

ENDWHILE

! 4th i = 1 REPEAT

BRICK 0.5, 0.5, 0.1 ADDZ 0.3 i = i + 1

UNTIL i > 5