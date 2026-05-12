---
id: wiki.generated.croof_2
type: wiki
category: other
commands: ["CROOF_{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### CROOF_{2}

CROOF_{2} top_material, bottom_material, side_material, n, xb, yb, xe, ye, height, angle, thickness, x1, y1, alpha1, s1, mat1,

... xn, yn, alphan, sn, matn

Extension of the CROOF_ command with the possibility of defining different materials for the sides. mati: material reference that allows you to control the material of the side surfaces.

Extension of the CROOF_{2} command with the possibility of controlling the global behavior of the generated roof. mask: controls the global behavior of the generated roof.

mask = j1 + 2*j2 + 4*j3 + 8*j4, where each j can be 0 or 1.

- j1: top edge in line elimination.
- j2: bottom edge in line elimination.
- j3: side edge in line elimination.
- j4: side edge and surface is smooth in curved sections of the profile. Compatibility: introduced in Archicad 21.


Example:

PEN 1 mat = IND (MATERIAL, "Metal-Aluminium") FOR i=1 TO 4 STEP 1

- IF i = 1 THEN mask = 1+2+4
- IF i = 2 THEN mask = 1
- IF i = 3 THEN mask = 2
- IF i = 4 THEN mask = 4 CROOF_{3} mat, mat, mat, mask,


5, 0, 1, 2, 1, 3, -45, 0.3, 0, 0, 0, 15, mat, 1, 0, 0, 15, mat, 1, 1, 0, 15, mat, 0, 1, 0, 15, mat, 0, 0, 0, -1, mat

BODY -1 DEL TOP

- IF i = 1 THEN ADD 0,1,1
- IF i = 2 THEN ADDX -1
- IF i = 3 THEN ADDX 1


NEXT i

CROOF_{4} is an extension of the CROOF_{3} command with the possibility of using inline material definition, that means materials defined in GDL script locally also can be used next to materials defined in global material definitions.