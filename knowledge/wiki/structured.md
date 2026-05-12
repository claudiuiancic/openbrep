---
id: wiki.generated.structured
type: wiki
category: string
commands: ["STRUCTURED"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### STRUCTURED TYPES

Variables and parameters can also be dictionaries. Compatibility: introduced in Archicad 23. Dictionaries are a hierarchical collection of key and value pairs. Keys can contain other dictionary, array, integer, string or floating-point type values. Keys are considered identifiers (the section called “Identifiers”) - same syntax rules apply, except the '~' character is not allowed. It is not allowed to use dictionary keys (even if they are simple type) in the following places:

- • as FOR - TO - NEXT loop variable.
- • as HOTSPOT2 or HOTSPOT edited or displayed parameter.
- • as UI_... input parameter where the input parameter is given as an expression. (UI_INFIELD{2}, UI_INFIELD{3}, UI_CUSTOM_POPUP_INFIELD{2}, UI_RADIOBUTTON, UI_PICT_RADIOBUTTON, UI_PICT_PUSHCHECKBUTTON, UI_TEXTSTYLE_INFIELD, UI_LISTITEM{2}, UI_CUSTOM_POPUP_LISTITEM{2}, UI_COLORPICKER{2}, UI_SLIDER{2})
- • as UI_... input parameter where the input parameter is given as a string, if the string evaluates to a dictionary type parameter.
- • as VALUES or VALUES{2} parameter - value lists cannot be applied.
- • as REQUEST returned values - only root level of a dictionary is allowed in requests that support it.
- • as APPLICATION_QUERY, SPLIT, INPUT, LIBRARYGLOBAL or CALLFUNCTION returned values.
- • as STR{2} returned extra_accuracy_string.
- • as RETURNED_PARAMETERS of a CALL - only returned dictionaries can be stored only at the root level of a dictionary.