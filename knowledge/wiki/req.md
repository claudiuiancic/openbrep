---
id: wiki.generated.req
type: wiki
category: other
commands: ["REQ"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### REQ

REQ (parameter_string) Asks the current state of the program. Its parameter - the question - is a string. The GDL interpreter answers with a numeric value. If it does not understand the question, the answer is negative. parameter_string: question string, one of the following:

"GDL_version": version number of the GDL compiler/interpreter. Warning: it is not the same as the Archicad version. "Program": code of the program (e.g., 1: Archicad), "Serial_number": the serial number of the keyplug, "Model_size": size of the current 3D data structure in bytes, "Red_of_material name" "Green_of_material name" "Blue_of_material name": Defines the given material’s color components in RGB values between 0 and 1,

"Red_of_pen index" "Green_of_pen index" "Blue_of_pen index": Defines the given pen’s color components in RGB values between 0 and 1, "Pen_of_RGB r g b": Defines the index of the pen closest to the given color. The r, g and b constants’ values are between 0 and 1.