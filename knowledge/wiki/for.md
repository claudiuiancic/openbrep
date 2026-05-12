---
id: wiki.generated.for
type: wiki
category: control
commands: ["FOR", "TO", "NEXT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### FOR - TO - NEXT

FOR variable_name = initial_value TO end_value [ STEP step_value ] NEXT variable_name FOR is the first statement of a FOR loop. NEXT is the last statement of a FOR loop.

The loop variable varies from the initial_value to the end_value by the step_value increment (or decrement) in each execution of the body of the loop (statements between the FOR and NEXT statements). If the loop variable exceeds the value of the end_value, the program executes the statement following the NEXT statement.

If the STEP keyword and the step_value are missing, the step is assumed to be 1. Note: Changing the step_value during the execution of the loop has no effect. A global variable is not allowed as a loop control variable.

- Example 1:


FOR i=1 TO 10 STEP 2

PRINT i NEXT i

- Example 2: ! The two program fragments below are equivalent:


! 1st a = b

- 1: IF c > 0 AND a > d OR c < 0 AND a < d THEN 2 PRINT a a = a + c GOTO 1 ! 2nd
- 2: FOR a = b TO d STEP c


PRINT a NEXT a The above example shows that step_value = 0 causes an infinite loop. Only one NEXT statement is allowed after a FOR statement. You can exit the loop with the GOTO command and to return after leaving, but you cannot enter a loop skipping the FOR statement.