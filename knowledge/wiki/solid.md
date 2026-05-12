---
id: wiki.generated.solid
type: wiki
category: other
commands: ["SOLID"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### SOLID GEOMETRY COMMANDS

GDL is capable of performing specialized 3D operations between solids represented by groups. These operations can be one of the following:

ADDGROUP forming the Boolean union of two solids

SUBGROUP forming the Boolean difference of two solids

ISECTGROUP forming the Boolean intersection of two solids

ISECTLINES calculating the intersection lines of two solids

SWEEPGROUP sweeping a solid along a vector

A GDL solid is composed of one or more lumps that appear as separated bodies in the model. A lump has exactly one outer shell and may contain voids. (Voids can be described as "negative" inner shells inside a lump.) The solid in the drawing below is composed of two lumps in such a way that one of them contains a void.

GDL bodies such as BLOCK, SPHERE, etc., appear as outer shells in groups. By means of the following construction the user is capable of putting more than one shell in a solid (note the BODY -1 statement): GROUP "myGroup"

BLOCK 1,1,1 BODY -1 ADDX 1 BLOCK 1,1,1

ENDGROUP The above solid contains two lumps; each of them is composed of one shell. Voids can be defined by means of primitives, or can occur as a result of a Boolean difference (e.g. subtracting a small cube from the middle of a big one). See also the section called “Primitive Elements”.

Although group operations are intended to work with solid objects, they can be applied to surfaces, wireframes or hybrid models, too. (Hybrid models are basically surfaces that may contain edges without neighboring faces.) The result of the operations on such models are summarized in the following tables: