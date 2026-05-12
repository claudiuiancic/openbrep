---
id: wiki.generated.ui_slider_2
type: wiki
category: other
commands: ["UI_SLIDER{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### UI_SLIDER{2}

UI_SLIDER{2} name, x0, y0, width, height [, nSegments [, sliderStyle]] Generates a slider control for an integer parameter defined with a range. For integer parameters with undefined range lower and upper limit values are -32768 (minimum signed short) and 32767 (maximum signed short).

name: parameter name as string expression parameter or name with optional actual index values for UI_SLIDER{2}. x0, y0: position of the slider. width, height: slider width and height in pixels. If the width > height the slider is horizontal, in the opposite case it is vertical. nSegments: optional number of segments on the slider. If 0, no segments are displayed, if omitted or negative, the number of segments

are calculated from the range upper and lower limit values and the step defined for the parameter.

sliderStyle: optional slider style (default is 0) 0: slider points to the bottom (horizontal sliders) or to the right (vertical sliders). 1: slider points to the top (horizontal sliders) or to the left (vertical sliders).