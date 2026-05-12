---
id: wiki.generated.add
type: wiki
category: 3d
commands: ["ADD"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### ADD

ADD dx, dy, dz Replaces the sequence ADDX dx: ADDY dy: ADDZ dz.

Example: ADD a, b, c

Z

Y

Z

c

Y

X

b

a

X

It has only one entry in the stack, thus it can be deleted with DEL 1.