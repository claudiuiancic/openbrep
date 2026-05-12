---
id: wiki.generated.sprism_2
type: wiki
category: other
commands: ["SPRISM_{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### SPRISM_{2}

- SPRISM_{2} top_material, bottom_material, side_material, n, xtb, ytb, xte, yte, topz, tangle, xbb, ybb, xbe, ybe, bottomz, bangle, x1, y1, s1, mat1,


... xn, yn, sn, matn

Extension of the SPRISM_ command, with the possibility of having an upper and lower polygon non-parallel with the x-y plane. The definition of the planes is similar to the plane definition of the CROOF_ command. The top and bottom of the prism is defined at the reference line. Upper and lower polygon intersection is forbidden.

xtb, ytb, xte, yte: reference line (vector) of the top polygon starting and end coordinates. topz: the 'z' level of the reference line of the top polygon. tangle: rotation angle of the top polygon around the given oriented reference line in degrees (CCW). xbb, ybb, xbe, ybe: reference line (vector) of the bottom polygon starting and end coordinates. bottomz: the 'z' level of the reference line of the bottom polygon. bangle: rotation angle of the bottom polygon around the given oriented reference line in degrees (CCW). si: status code that allows you to control the visibility of polygon edges and side surfaces. You can also define holes and create segments

and arcs in the polyline using special constraints. See Status Codes for details.

mati: material reference that allows you to control the material of the side surfaces.

Example:

- SPRISM_{2} 'Grass', 'Earth', 'Earth', 11, 0, 0, 11, 0, 30, -30.0, 0, 0, 0, 11, 2, 30.0,

- 0, 0, 15, IND (MATERIAL, 'C10'), 10, 1, 15, IND (MATERIAL, 'C11'), 11, 6, 15, IND (MATERIAL, 'C12'),

- 5, 7, 15, IND (MATERIAL, 'C13'), 4, 5, 15, IND (MATERIAL, 'C14'),

1, 6, 15, IND (MATERIAL, 'C10'), 0, 0, -1, IND (MATERIAL, 'C15'),

- 9, 2, 15, IND (MATERIAL, 'C15'),
- 10, 5, 15, IND (MATERIAL, 'C15'),


- 6, 4, 15, IND (MATERIAL, 'C15'), 9, 2, -1, IND (MATERIAL, 'C15')




- SPRISM_{3}


- SPRISM_{3} top_material, bottom_material, side_material, mask, n, xtb, ytb, xte, yte, topz, tangle, xbb, ybb, xbe, ybe, bottomz, bangle, x1, y1, s1, mat1,


... xn, yn, sn, matn

Extension of the SPRISM_{2} command with the possibility of controlling the global behavior of the generated prism. mask: controls the global behavior of the generated prism.

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
- IF i = 4 THEN mask = 4


- SPRISM_{3} mat, mat, mat, mask, 5,

- 0, 0, 1, 0, 1, 0,

- 0, 0, 1, 0, 0, 0, 0, 0, 15, mat, 1, 0, 15, mat,
- 1, 1, 15, mat,


- 0, 1, 15, mat, 0, 0, -1, mat


BODY -1 DEL TOP

- IF i = 1 THEN ADDY 1
- IF i = 2 THEN ADDX -1
- IF i = 3 THEN ADDX 1


NEXT i

- SPRISM_{4}


- SPRISM_{4} top_material, bottom_material, side_material, mask, n, xtb, ytb, xte, yte, topz, tangle, xbb, ybb, xbe, ybe, bottomz, bangle, x1, y1, s1, mat1,


... xn, yn, sn, matn

- SPRISM_{4} is an extension of the SPRISM_{3} command with the possibility of using inline material definition, that means materials defined in GDL script locally also can be used next to materials defined in global material definitions.