---
id: wiki.generated.endparagraph
type: wiki
category: control
commands: ["ENDPARAGRAPH"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### ENDPARAGRAPH

GDL scripts may include paragraph definitions prior to the first reference to that paragraph name. The paragraph defined this way can be used only in the script in which it was defined and its subsequent second generation scripts. A paragraph is defined to be a sequence of an arbitrary number of strings (max 256 characters long each) with different attributes: style, pen and material (3D). If no attributes are specified inside the paragraph definition, actual (or default) attributes are used. The new lines included in a paragraph string (using the special character '\n') will automatically split the string into identical paragraphs, each containing one line. Paragraph definitions can be referenced by name in the TEXTBLOCK command. All length type parameters (firstline_indent, left_indent, right_indent, tab_position) meaning millimeters or meters depends on the fixed_height parameter of the TEXTBLOCK definition.

name: name of the paragraph. Can be either string or integer. Integer identifiers works only with the TEXTBLOCK_ command alignment: alignment of the paragraph strings. Possible values:

- 1: left aligned,
- 2: center aligned,


- 3: right aligned,
- 4: full justified.


firstline_indent: first line indentation, in mm or m in model space. left_indent: left indentation, in mm or m in model space. right_indent: right indentation, in mm or m in model space. line_spacing: line spacing factor. The default distance between the lines (character size + distance to the next line) defined by the

actual style will be multiplied by this number.

tab_positioni: consecutive tabulator positions (each relative to the beginning of the paragraph), in mm or m in model space. Tabulators in the paragraph strings will snap to these positions. If no tabulator positions are specified, default values are used (12.7 mm). Works only with '\t' special character.

stringi: part of the text. Can be either constant string or string type parameter.