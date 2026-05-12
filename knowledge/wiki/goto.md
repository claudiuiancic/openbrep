---
id: wiki.generated.goto
type: wiki
category: control
commands: ["GOTO"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### GOTO

GOTO label Unconditional jump statement. The program executes a branch to the statement denoted by the value of the label (numerical or string). Variable label expressions can slow down interpretation due to runtime jumping address determination.

Example: GOTO K+2