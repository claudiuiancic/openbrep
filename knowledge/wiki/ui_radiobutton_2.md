---
id: wiki.generated.ui_radiobutton_2
type: wiki
category: other
commands: ["UI_RADIOBUTTON{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### UI_RADIOBUTTON{2}

UI_RADIOBUTTON{2} "name", value, text, x, y, width, height Version {2} compatibility: introduced in Archicad 20.

Generates a radio button of a radio button group. Radio button groups are defined by the parameter name. Items in the same group are mutually exclusive. name: parameter name or name as string expression for UI_RADIOBUTTON and parameter name as string expression (or text array

indexed value) for UI_RADIOBUTTON{2}. value: parameter is set to this value if this radio button is set. text: this text is displayed beside the radio button. x, y: the position of the radio control. width, height: width and height in pixels.

Example:

UI_RADIOBUTTON "ceilingPlan", 0, _(`Floor Plan`), 10, 140, 100, 20 UI_RADIOBUTTON "ceilingPlan", 1, _(`Ceiling Plan`), 10, 160, 100, 20

![image 18](<GDL_Reference_Guide_28_images/imageFile18.png>)