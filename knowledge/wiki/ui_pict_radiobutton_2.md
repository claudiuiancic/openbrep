---
id: wiki.generated.ui_pict_radiobutton_2
type: wiki
category: other
commands: ["UI_PICT_RADIOBUTTON{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### UI_PICT_RADIOBUTTON{2}

###### UI_PICT_RADIOBUTTON{2} "name", value, text,

picture_reference, x, y, width, height [UI_TOOLTIP tooltip]

Compatibility: introduced in Archicad 22. Generates one radio button with icon of a radio button group. Radio button groups are defined by the parameter name. Items in the same group are mutually exclusive. name: parameter name or name as string expression for UI_PICT_RADIOBUTTON and parameter name as string expression (or text array

indexed value) for UI_PICT_RADIOBUTTON{2}. value: parameter is set to this value if this radio button is set. text: this text is displayed on the button if no image is declared. picture_reference: file name or index number of the picture stored in the library part. The index 0 refers to the preview picture of

the library part. Pixel transparency is allowed in the picture. x, y: the position of the radio control (top left anchor). width, height: width and height of the button in pixels. Image size is not declared individually: it should fit the button, as image is not

stretched automatically to fit, and is centered on the button.