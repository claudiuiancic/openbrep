---
id: wiki.generated.light
type: wiki
category: other
commands: ["LIGHT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### LIGHT

LIGHT red, green, blue, shadow, radius, alpha, beta, angle_falloff, distance1, distance2, distance_falloff [[,] ADDITIONAL_DATA name1 = value1, name2 = value2, ...]

A light source radiates [red, green, blue] colored light from the local origin along the local x axis. The light is projected parallel to the x axis from a point or circle source. It has its maximum intensity within the alpha-angle frustum of a cone and falls to zero at the beta-angle frustum of a cone. This falloff is controlled by the angle_falloff parameter. (Zero gives the light a sharp edge, higher values mean that the transition is smoother.) The effect of the light is limited along the axis by the distance1 and distance2 clipping values. The distance_falloff parameter controls the decrease in intensity depending on the distance. (Zero value means a constant intensity; bigger values are used for stronger falloff.)

GDL transformations affect only the starting point and the direction of the light. shadow: controls the light’s shadow casting.

0: light casts no shadows, 1: light casts shadows.

| | |
|---|---|
| | |
| | |
| | |
| | |


beta

alpha

radius

intensity

dist1

dist2

Restriction of parameters:

alpha <= beta <= 80° The following parameter combinations have special meanings: radius = 0, alpha = 0, beta = 0: A point light, it radiates light in every direction and does not cast any shadows. The shadow and angle_falloff parameters are ignored, the values shadow = 0, angle_falloff = 0 are supposed. radius > 0, alpha = 0, beta = 0: A directional light with parallel beams.

r = 0, alpha > 0, beta > 0: A directional light with conic beams.

r > 0, alpha = 0, beta > 0: A directional light with parallel beam and conic falloff.

Light definitions can contain optional additional data definitions after the ADDITIONAL_DATA keyword. Additional data has a name (namei) and a value (valuei), which can be an expression of any type, even an array. If a string parameter name ends with the substring "_file", its value is considered to be a file name and will be included in the archive project.

Different meanings of additional data can be defined and used by the executing application.

- Example 1:

LIGHT 1.0,0.2,0.3, ! RGB 1, ! shadow on 1.0, ! radius 45.0, 60.0, ! angle1, angle2 0.3, ! angle_falloff 1.0, 10.0, ! distance1, distance2 0.2 ! distance_falloff

- Example 2: The library part dialog box for lights in Archicad:


![image 1](<GDL_Reference_Guide_28_images/imageFile1.png>)

Part of the corresponding GDL script: if gs_light_switch > 0 then

LIGHT gs_light_intensity/100*gs_color_red, \ gs_light_intensity/100*gs_color_green, \ gs_light_intensity/100*gs_color_blue, ! RGB

... endif