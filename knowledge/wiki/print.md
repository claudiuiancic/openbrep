---
id: wiki.generated.print
type: wiki
category: control
commands: ["PRINT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PRINT

PRINT expression [, expression, ...] Writes all of its arguments in a dialog box or the Report Window, depending on Work Environment (see the section called “GDL warnings”). Arguments can be strings or numeric expressions of any number in any sequence, separated by commas.

Example:

PRINT "loop-variable:", i PRINT j, k-3*l PRINT "Beginning of interpretation" PRINT a * SIN (alpha) + b * COS (alpha) PRINT "Parameter values: ", "a = ", a, ", b = ", b PRINT name + STR ("%m", i) + "." + ext