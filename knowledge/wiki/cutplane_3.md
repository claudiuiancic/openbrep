---
id: wiki.generated.cutplane_3
type: wiki
category: 3d
commands: ["CUTPLANE{3}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### CUTPLANE{3} [x [, y [, z [, side [, status]]]]] [statement1 ... statementn] CUTEND Creates a cutting plane and removes the cut parts of enclosed shapes. CUTPLANE may have a different number of parameters. If CUTPLANE has the following number of parameters:

- 0: x-y plane;
- 1: cutting plane goes across x axis, angle is between cutting plane and x-y plane;
- 2: cutting plane is parallel to z axis, crosses x axis and y axis at the given values;
- 3: cutting plane crosses the x, y and z axes at the given values;
- 4: the first three parameters are as above, with the addition of the side value as follows:


side: definition of the side to cut. 0: removes parts above cutting plane (default), 1: removes parts below cutting plane; in case of x-y, x-z, y-z, removes the parts in the negative direction of the axis.

status: status control of the cut surfaces. If the status is not given the status is set to 1+2 automatically. status = j1 + 2*j2 + 4*j3 + 256*j9, where each j can be 0 or 1. j1: use the attributes of the body for the generated polygons and edges. j2: generated cut polygons will be treated as normal polygons. j3: generated cut edges will be invisible. j9: vertices on the cutting plane are treated as removed.

The cut (without the side parameter) removes parts above the cutting plane. If the first three parameters define the x-y, x-z or y-z plane (for example, 1.0, 1.0, 0.0 defines the x-y plane), the parts in the positive direction of the third axis are removed. Any number of statements can be added between CUTPLANE and CUTEND. It is also possible to include CUTPLANEs in macros. CUTPLANE parameters refer to the current coordinate system.

Transformations between CUTPLANE and CUTEND have no effect on this very cutting plane, but any successive CUTPLANEs will be transformed. Therefore, it is recommended to use as many transformations to set up the CUTPLANE as necessary, then delete these transformations before you define the shapes to cut.

If transformations used only to position the CUTPLANE are not removed, you may think that the CUTPLANE is at a wrong position when, in reality, it is the shapes that have moved away. Pairs of CUTPLANE-CUTEND commands can be nested, even within loops. If the final CUTEND is missing, its corresponding CUTPLANE will be effective on all shapes until the end of the script.

- Note 1: If CUTPLANE is not closed with CUTEND, all shapes may be entirely removed. That’s why you always get a warning message about missing CUTENDs.

CUTPLANEs in macros affect shapes in the macro only, even if CUTEND is missing. If a macro is called between CUTPLANE and CUTEND, the shapes in the macro will be cut.

- Note 2: If you use CUTPLANE{2} with more than two parameters, then this will act like CUTPLANE.
- Note 3: Prefer using CUTPLANE{3} instead of CUTPLANE. If you use CUTPLANE with 5 parameters, then the 4th parameter will be omitted. For CUTPLANE{3}, this parameter has effect independently from the 5th parameter.


- Example 1:

CUTPLANE 2, 2, 4 CUTPLANE -2, 2, 4 CUTPLANE -2, -2, 4 CUTPLANE 2, -2, 4 ADD -1, -1, 0 BRICK 2, 2, 4 DEL 1 CUTEND CUTEND CUTEND CUTEND

- Example 2:


CUTPLANE SPHERE 2 CUTEND

CUTPLANE 1, 1, 0, 1 SPHERE 2 CUTEND

- Example 3:

CUTPLANE 1.8, 1.8, 1.8 SPHERE 2 CUTEND

CUTPLANE 1.8, 1.8, 1.8, 1 SPHERE 2 CUTEND

- Example 4:


CUTPLANE 60 BRICK 2, 2, 2 CUTEND

CUTPLANE -120 BRICK 2, 2, 2 CUTEND