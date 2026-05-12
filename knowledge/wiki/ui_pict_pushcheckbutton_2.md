---
id: wiki.generated.ui_pict_pushcheckbutton_2
type: wiki
category: other
commands: ["UI_PICT_PUSHCHECKBUTTON{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### UI_PICT_PUSHCHECKBUTTON{2}

UI_PICT_PUSHCHECKBUTTON{2} "name", text, picture_reference,

frameFlag, x, y, width, height [UI_TOOLTIP tooltip] Compatibility: introduced in Archicad 22.

Generates one pushcheck button with icon for a boolean parameter. Similar to the UI_INFIELD{3} command with method 6, with additional option to control the visibility of the button frame. name: parameter name or name as string expression for UI_PICT_PUSHCHECKBUTTON and parameter name as string expression (or

text array indexed value) for UI_PICT_PUSHCHECKBUTTON{2}. text: this text is displayed on the button if no image is declared. picture_reference: file name or index number of the picture stored in the library part. The index 0 refers to the preview picture of

the library part. Pixel transparency is allowed in the picture. frameFlag: 1 - frame is displayed, 0 - frame is not visible. Use this option to match the control to other User Interface items in style. x, y: the position of the button (top left anchor). width, height: width and height of the button in pixels. Image size is not declared individually: it should fit the button, as image is not

stretched automatically to fit, and is centered on the button.