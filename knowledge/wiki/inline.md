---
id: wiki.generated.inline
type: wiki
category: other
commands: ["INLINE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### INLINE ATTRIBUTE DEFINITION

Attributes in can be created using the material, fill and line type dialog boxes. These floor plan attributes can be referenced from any GDL script. Attributes can also be defined in GDL scripts. There are two different cases:

- • Attribute definition in the MASTER_GDL script. The MASTER_GDL script is interpreted when the library that contains it is loaded in the memory. The MASTER_GDL attributes are merged into the floor plan attributes; attributes with the same names are not replaced. Once the MASTER_GDL is loaded, the attributes defined in it can be referenced from any script.
- • Attribute definition in library parts. The materials and textures defined this way can be used in the script and its second generation scripts. Fills and line types defined and used in the master or 2D script have the same behavior as if they were defined in the MASTER_GDL script, but only if used by name or index (not through a parameter). Fills and line types defined in the master or 3D script cannot be accessed in the 3D script.


The Check GDL Script command in the script window helps to verify whether the material, fill, line type or style parameters are correct.

When a material, fill, line type or style is different in the 3D interpretation of the library part from the intended one, but there is no error message, this probably means that one or more of the parameter values are incorrect. The Check GDL Scripts command will help you with detailed messages to find these parameters.