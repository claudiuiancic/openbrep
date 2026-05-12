---
id: wiki.generated.ui_textstyle_infield_2
type: wiki
category: other
commands: ["UI_TEXTSTYLE_INFIELD{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### UI_TEXTSTYLE_INFIELD{2}

UI_TEXTSTYLE_INFIELD{2} "name", faceCodeMask, x, y,

buttonWidth, buttonHeight [, buttonOffsetX]

- Compatibility: introduced in Archicad 22.


Generates a row of puschcheckbuttons specifically used to set font style via an integer parameter, with similar appearance as seen in the general program interface. The format of the set value matches the input parameter of the DEFINE STYLE{2} command. Both icons and tooltips are referenced from Archicad itself, according to the localized version. The enabled buttons are displayed in a single-row arrangement.

name: parameter name or name as string expression for UI_TEXTSTYLE_INFIELD and parameter name as string expression (or text

array indexed value) for UI_TEXTSTYLE_INFIELD{2}.

faceCodeMask: used bits add the matching font style option to the control: faceCodeMask = j1 + 2*j2 + 4*j3 + 32*j6 + 64*j7 + 128*j8, where each j can be 0 or 1. j1: bold, j2: italic, j3: underline, j6: superscript,

j7: subscript, j8: strikethrough.

If faceCodeMask = 0, then all possible font style buttons are displayed. In case of an invalid faceCodeMask, "Check Script" returns with warning ("Invalid mask value used").

x, y: the position of the first button (top left anchor). buttonWidth, buttonHeight: width and height of one button in pixels. Full width can be calculated by using the faceCodeMask,

the buttonWidth and the buttonOffsetX values, if necessary.

buttonOffsetX: distance between neighboring buttons in the row, in pixels. Automatic, if not set.