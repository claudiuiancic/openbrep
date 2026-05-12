---
id: wiki.generated.newparameter
type: wiki
category: other
commands: ["NEWPARAMETER"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### NEWPARAMETER

NEWPARAMETER "name", "type" [, dim1 [, dim2]] Adds a new parameter to the parameters of a library part in the Backward Migration Script. The parameter creation happens only after the full interpretation of the script. If a parameter with the given name already exists in the parameters list, an error occurs.

name: string expression, name of the parameter to be created. type: string expression, type of the parameter. Possible values are:

Integer Length Angle RealNum LightSwitch ColorRGB Intensity LineType Material FillPattern PenColor String Boolean BuildingMaterial(Compatibility: introduced in Archicad 22.) Profile(Compatibility: introduced in Archicad 22.) Dictionary(Compatibility: introduced in Archicad 24.)

dim1, dim2: dim1 is the first dimension of the parameter, 0 if not set. dim2 is the second dimension of the parameter, 0 if not set. dim1 = 0, dim2 = 0: the parameter is a scalar parameter, dim1 > 0, dim2 = 0: the parameter is a 1 dimensional array, dim1 > 0, dim2 > 0: the parameter is a 2 dimensional array,

Restriction of parameters: If dim2 > 0, then dim1 > 0.

## EXPRESSIONS AND FUNCTIONS

All parameters of GDL shapes can be the result of calculations. For example, you can define that the height of the cylinder is five times the radius of the cylinder, or prior to defining a cube, you can move the coordinate system in each direction by half the size of the cube, in order to have the initial origin in the center of the cube rather than in its lower left corner. To define these calculations, GDL offers a large number of mathematical tools: expressions, operators and functions.