---
id: wiki.generated.constr_fills_display
type: wiki
category: other
commands: ["CONSTR_FILLS_DISPLAY"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### CONSTR_FILLS_DISPLAY

n = REQUEST("CONSTR_FILLS_DISPLAY", "", optionVal) Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning. Compatibility up till Archicad 19: returns in the given variable the value of the Cut Fills Display option as set in the Document > Set Model View > Model View Options. (previous Construction Fills). Compatibility starting from Archicad 20: the returned value is always 6 by default (Cut fill patterns: as in Settings).

optionVal: cut fill display code. 1: Show cut fill contours only (previous Empty) 2: Show cut fill contours only with separator lines (previous No Fills) 4: Cut fill patterns: Solid (previous Solid) 6: Cut fill patterns: as in Settings (previous Vectorial Hatching)