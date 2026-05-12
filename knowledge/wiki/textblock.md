---
id: wiki.generated.textblock
type: wiki
category: other
commands: ["TEXTBLOCK"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### TEXTBLOCK

TEXTBLOCK name width, anchor, angle, width_factor, charspace_factor, fixed_height,

'string_expr1' [, 'string_expr2', ...]

Textblock definition. GDL scripts may include textblock definitions prior to the first reference to that textblock name. The textblock defined this way can be used only in the script in which it was defined and its subsequent second generation scripts. A textblock is defined to be a sequence of an arbitrary number of strings or paragraphs which can be placed using the RICHTEXT2 command and the RICHTEXT command. Use the "TEXTBLOCK_INFO" REQUEST to obtain information on the calculated width and height of a textblock.

name: name of the textblock, string type value. width: textblock width in mm or m in model space, if 0 it is calculated automatically. anchor: code of the position point in the text.

|1 2 3<br><br>4 5 6<br><br>7 8 9|
|---|


angle: rotation angle of the textblock in degrees. width_factor: Character widths defined by the actual style will be multiplied by this number. charspace_factor: The horizontal distance between two characters will be multiplied by this number. fixed_height: Possible values:

1: the placed TEXTBLOCK will be scale-independent and all specified length type parameters will mean millimeters, 0: the placed TEXTBLOCK will be scale-dependent and all specified length type parameters will mean meters in model space. string_expri: means paragraph name if it was previously defined, simple string otherwise (with default paragraph parameters).