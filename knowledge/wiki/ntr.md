---
id: wiki.generated.ntr
type: wiki
category: other
commands: ["NTR"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### NTR

NTR () Returns the actual number of transformations.

BLOCK 1, 1, 1

- ADDX 2 ADDY 2.5 ADDZ 1.5 ROTX -60 ADDX 1.5 BLOCK 1, 0.5, 2 DEL 1, 1 ! Deletes the ADDX 2 transformation


- BLOCK 1, 0.5, 1 DEL 1, NTR() - 2 ! Deletes the ADDZ 1.5 transformation
- BLOCK 1, 0.5, 2 DEL -2, 3 ! Deletes the ROTX -60 and ADDY 2.5 transformations BLOCK 1, 0.5, 2


## 3D SHAPES

This chapter covers all the 3D shape creation commands available in GDL, from the most basic ones to the generation of complex shapes from polylines. Elements for visualization (light sources, pictures) are also presented here, as well as the definition of text to be displayed in 3D. Furthermore, the primitives of the internal 3D data structure consisting of nodes, vectors, edges and bodies are discussed in detail, followed by the interpretation of binary data and guidelines for using cutting planes.

BASIC SHAPES