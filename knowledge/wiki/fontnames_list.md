---
id: wiki.generated.fontnames_list
type: wiki
category: other
commands: ["FONTNAMES_LIST"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### FONTNAMES_LIST

n = REQUEST("FONTNAMES_LIST", "", fontnames)

Returns in the given variables the fontnames available on the current computer (with character codes included). This list (or any part of this list) can be used in a VALUES command to set up a fontname popup. The function return value is the number of successfully retrieved values, 0 if an error occurred.

Example: dim fontnames[] n = REQUEST ("FONTNAMES_LIST", "", fontnames) VALUES "f" fontnames, CUSTOM

This form of the VALUES command assembles a fontnames pop-up for the simple string-typed parameter "f". The "fontnames" variable contains the possible fontnames (with character codes included) which can be set manually or using the "FONTNAMES_LIST" REQUEST. The CUSTOM keyword is necessary for the correct handling of missing fonts on other platforms/computers: if it is specified, a fontname set on another platform/computer missing in the current environment will be preserved in the parameter settings as a custom value (otherwise, due to the implementation of the VALUES command, a missing string popup value in the parameter settings will be replaced with the first current string value). It is recommended to include this function in the ARCHICAD_Library_Master file.