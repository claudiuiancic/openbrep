---
id: wiki.generated.if
type: wiki
category: control
commands: ["IF", "GOTO"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### IF - GOTO

IF condition THEN label IF condition GOTO label IF condition GOSUB label

Conditional jump statement. If the value of the condition expression is 0 (logical 'false'), the command has no effect, otherwise execution continues at the label. THEN, GOTO or THEN GOTO are equivalent in this context.

IF a THEN 28 IF i > j GOTO 200+i*j IF i > 0 GOSUB 9000

###### IF - THEN - ELSE - ENDIF

IF condition THEN statement [ELSE statement] IF condition THEN

[statement1 statement2

... statementn]

[ELSE statementn+1 statementn+2 ... statementn+m]

ENDIF If you write only one command after keywords THEN and/or ELSE in the same row, there is no need for ENDIF. A command after THEN or ELSE in the same row means a definite ENDIF.

If there is a new row after THEN, the successive commands (all of them until the keyword ELSE or ENDIF) will only be executed if the expression in the condition is true (other than zero). Otherwise, the commands following ELSE will be carried out. If the ELSE keyword is absent, the commands after ENDIF will be carried out.

IF a = b THEN height = 5 ELSE height = 7 IF needDoors THEN

CALL "door_macro" PARAMETERS ADDX a

ENDIF IF simple THEN

HOTSPOT2 0, 0 RECT2 a, 0, 0, b

ELSE PROJECT2 3, 270, 1 IF name = "Sphere" THEN

ADDY b SPHERE 1

ELSE

ROTX 90 TEXT 0.002, 0, name

ENDIF