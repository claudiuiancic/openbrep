---
id: wiki.generated.textblock_info
type: wiki
category: other
commands: ["TEXTBLOCK_INFO"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### TEXTBLOCK_INFO

n = REQUEST("TEXTBLOCK_INFO", textblock_name, width, height)

Returns in the given variables the sizes in x and y direction of a text block previously defined via the TEXTBLOCK command. The sizes are in mm or in m in model space depending on the fixed_height parameter value of TEXTBLOCK (millimeters if 1, meters in model space if 0 ). If width was 0, the request returns the calculated width and height, if width was specified in the text block definition, returns the calculated height corresponding to that width. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning.