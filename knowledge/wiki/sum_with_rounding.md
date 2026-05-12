---
id: wiki.generated.sum_with_rounding
type: wiki
category: other
commands: ["SUM_WITH_ROUNDING"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### SUM_WITH_ROUNDING

- n = REQUEST{3}("SUM_WITH_ROUNDING", req_name, addends_array, result) Returns the sum of the numbers in addends_array, with rounding according to the "Calculate Totals by" project preference. This preference can be found in Options > Project Preferences > Calculation Rules. Possible project preference settings:


- • "Displayed values": the request will first round the addends according to req_name, and then sum them.
- • "Exact values": the request will simply sum the addends. Causes warning if used in parameter script.

- Compatibility: introduced in Archicad 20. Return values:


- • 0, if req_name is invalid.
- • 1, if the call succeeded.


req_name: the name of the formatting request specifying how the addends have to be rounded if "Calculate Totals by" is set to "Displayed

values".

For example if req_name = "AREA_DIMENSION", and the Project Preferences > Dimensions > Area Calculations is set to "square centimeter" with 3 decimals, rounding to 0.025, then the addends will be rounded to the multiples of 0.025 cm², that is to 0.0000025 m². Valid request names:

LINEAR_DIMENSION, ANGULAR_DIMENSION, RADIAL_DIMENSION, LEVEL_DIMENSION, ELEVATION_DIMENSION, WINDOW_DOOR_DIMENSION, SILL_HEIGHT_DIMENSION, AREA_DIMENSION, CALC_LENGTH_UNIT, CALC_AREA_UNIT, CALC_VOLUME_UNIT, CALC_ANGLE_UNIT.

addends_array: the array of numbers to be added. Whether they have to be treated as m, m², m³ or degrees is determined by req_name. result: a number, on return it will be set to the sum of the addends according to the "Calculate Totals by" preference. Note that result is

in the same unit as the addends. It is not converted to the target unit specified by req_name.