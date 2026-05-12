---
id: wiki.generated.nurbslump
type: wiki
category: other
commands: ["NURBSLUMP"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### NURBSLUMP

NURBSLUMP n, face1, face2, ..., facen Defines a solid part - a geometrically connected subset - of a solid NURBS body.

n: number of bounding faces (including optional void-separator zeros). facei: gdl-index of NURBS face bounding the lump

- • May be zero, indicating the end of shell and the beginning of another shell (void-separator).
- • Negative index means face is used in opposite direction. For positive index the backward side of the face correspond to the interior of the lump, for negative index the front side looks to the interior.


The boundary of a lump may fall to several closed shells: one outer shell which separates the lump from the infinite outer region of the space; and zero or more inner - void - shells which separate the lump from cavity regions. The faces of one shell must compose a continuous part

of the face list. These different parts for different shells must be separated by a 0 value. The first shell must be the outer shell. The faces of a shell must connect at common edges, but no ordering is assumed in the list. Note that the faces of a shell may be connected to other faces which are not in the shell or are in another shell (because edges can have more than two faces). Each face must be used in only one lump. Neither shell of a lump can be open - open bodies have no lumps and no shells.