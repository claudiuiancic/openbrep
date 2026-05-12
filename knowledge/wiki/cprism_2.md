---
id: wiki.generated.cprism_2
type: wiki
category: other
commands: ["CPRISM_{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### CPRISM_{2}

- CPRISM_{2} top_material, bottom_material, side_material, n, h, x1, y1, alpha1, s1, mat1,


... xn, yn, alphan, sn, matn

- CPRISM_{2} is an extension of the CPRISM_ command with the possibility of defining different angles and materials for each side of the prism. The side angle definition is similar to the one of the CROOF_ command. alphai: the angle between the face belonging to the edge i of the prism and the plane perpendicular to the base. mati: material reference that allows you to control the material of the side surfaces.
- CPRISM_{3}


- CPRISM_{3} top_material, bottom_material, side_material, mask, n, h, x1, y1, alpha1, s1, mat1,


... xn, yn, alphan, sn, matn

- CPRISM_{3} is an extension of the CPRISM_{2} command with the possibility of controlling the global behavior of the generated prism. mask: controls the global behavior of the generated prism.


mask = j1 + 2*j2 + 4*j3 + 8*j4, where each j can be 0 or 1.

- j1: top edge in line elimination.
- j2: bottom edge in line elimination.
- j3: side edge in line elimination.
- j4: side edge and surface is smooth in curved sections of the profile. Compatibility: introduced in Archicad 21.


FOR i=1 TO 4 STEP 1

- IF i = 1 THEN mask = 1+2+4
- IF i = 2 THEN mask = 1
- IF i = 3 THEN mask = 2
- IF i = 4 THEN mask = 4 CPRISM_{3} mat, mat, mat, mask,


5, 1,

- 0, 0, 0, 15, mat,
- 1, 0, 0, 15, mat, 1, 1, 0, 15, mat, 0, 1, 0, 15, mat, 0, 0, 0, -1, mat


BODY -1 DEL TOP

- IF i = 1 THEN ADDY 1
- IF i = 2 THEN ADDX -1
- IF i = 3 THEN ADDX 1


NEXT i

!visible side segment edges mask = 1 + 2 + 4 _secondStat = 15

- CPRISM_{3} mat, mat, mat, mask, 6, 1,


- 0, 0, 0, 15, mat,
- 1, 0, 0, _secondStat, mat, 0.5, 0.5, 0, 900, mat, 1, 1, 0, 3015, mat, 0, 1, 0, 15, mat,


- 0, 0, 0, -1, mat

!smooth edges using first node status copy mask = 1 + 2 + 4 _secondStat = 15 + 64

- CPRISM_{3} mat, mat, mat, mask, 6, 1, 0, 0, 0, 15, mat, 1, 0, 0, _secondStat, mat, 0.5, 0.5, 0, 900, mat,


- 1, 1, 0, 3015, mat, 0, 1, 0, 15, mat,


- 0, 0, 0, -1, mat

!smooth edges using mask, first edge is not smooth mask = 1 + 2 + 4 + 8 _secondStat = 15

- CPRISM_{3} mat, mat, mat, mask, 6, 1, 0, 0, 0, 15, mat, 1, 0, 0, _secondStat, mat, 0.5, 0.5, 0, 900, mat,


- 1, 1, 0, 3015, mat, 0, 1, 0, 15, mat, 0, 0, 0, -1, mat