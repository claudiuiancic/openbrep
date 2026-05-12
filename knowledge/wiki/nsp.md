---
id: wiki.generated.nsp
type: wiki
category: other
commands: ["NSP"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### NSP

NSP Returns the number of stored parameters in the internal buffer.

Example: Using the parameter buffer:

- r=2: b=6: c=4: d=10 n=12
- s=180/n FOR t=0 TO 180 STEP s


PUT r+r*COS(T), c-r*SIN(t), 1 NEXT t FOR i=1 TO 2

EXTRUDE 3+NSP/3, 0,0,d, 1+16, 0, b, 0, 2*r, b, 0, USE(NSP), 0, b, 0

MULY -1 NEXT i DEL 1 ADDZ d REVOLVE 3+NSP/3, 180, 0, 0, b, 0, 2*r, b, 0, GET(NSP), 0, b, 0

The full description:

r=2: b=6: c=4: d=10 FOR i=1 TO 2

EXTRUDE 16, 0,0,d, 1+16,

- 0, b, 0, 2*r, b, 0, 2*r, c, 1, r+r*COS(15), c-r*SIN(15), 1, r+r*COS(30), c-r*SIN(30), 1, r+r*COS(45), c-r*SIN(45), 1, r+r*COS(60), c-r*SIN(50), 1, r+r*COS(75), c-r*SIN(75), 1, r+r*COS(90), c-r*SIN(90), 1, r+r*COS(105), c-r*SIN(105), 1, r+r*COS(120), c-r*SIN(120), 1, r+r*COS(135), c-r*SIN(135), 1, r+r*COS(150), c-r*SIN(150), 1, R+R*COS(165), c-r*SIN(165), 1,
- 0, b, 1, 0, b, 0


MULY -1 NEXT i DEL 1

ADDZ d REVOLVE 16, 180, 0,

- 0, b, 0, 2*r, b, 0, 2*r, c, 1, r+r*COS(15), c-r*SIN(15), 1, r+r*COS(30), c-r*SIN(30), 1, r+r*COS(45), c-r*SIN(45), 1, r+r*COS(60), c-r*SIN(50), 1, r+r*COS(75), c-r*SIN(75), 1, r+r*COS(90), c-r*SIN(90), 1, r+r*COS(105), c-r*SIN(105), 1, r+r*COS(120), c-r*SIN(120), 1, r+r*COS(135), c-r*SIN(135), 1, r+r*COS(150), c-r*SIN(150), 1, r+r*COS(165), c-r*SIN(165), 1,
- 0, b, 1, 0, b, 0