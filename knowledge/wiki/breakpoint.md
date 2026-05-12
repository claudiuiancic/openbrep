---
id: wiki.generated.breakpoint
type: wiki
category: control
commands: ["BREAKPOINT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### BREAKPOINT expression

With this command, you can specify a breakpoint in the GDL script. The GDL debugger will stop at this command if the value of the parameter (a numeric expression) is true (1) and the Enable Breakpoints option of the debugger is checked. In normal execution mode, the GDL interpreter simply steps over this command.