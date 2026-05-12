---
id: wiki.generated.label_font_style
type: wiki
category: other
commands: ["LABEL_FONT_STYLE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### LABEL_FONT_STYLE font style

0-normal, 1-bold, 2-italic, 4- underline

LABEL_FONT_STYLE2 font style in the settings dialog box

0 - normal, otherwise j1 + 2*j2 + 4*j3 + 32*j6 + 64*j7 + 128*j8, j1 - bold, j2 - italic, j3 - underline, j6 - superscript, j7 - subscript, j8 - strikethrough

Label pointer/frame handling group of globals:

LABEL_CUSTOM_ARROW use symbol arrow option on/off

1 if the Use symbol arrow checkbox is checked, 0 otherwise LABEL_ARROW_LINETYPE line type of the line of the arrow LABEL_ARROW_PEN pen of the arrow LABEL_FRAME_ON label frame on/off

1 if the label frame is checked, 0 otherwise LABEL_FRAME_OFFSET frame offset LABEL_ANCHOR_POS label anchor position

0 - middle, 1 - top, 2 - bottom, 3 - bottom right