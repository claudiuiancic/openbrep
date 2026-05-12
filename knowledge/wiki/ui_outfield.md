---
id: wiki.generated.ui_outfield
type: wiki
category: other
commands: ["UI_OUTFIELD"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### UI_OUTFIELD

UI_OUTFIELD expression, x, y [, width, height [, flags]] Generates a static text.

expression: numerical or string expression. x, y: position of the text block’s top left corner. width, height: width and height of the text box. If omitted, the text box will wrap around the text as tight as possible for the given font. flags:

flags = j1 + 2*j2 + 4*j3, where each j can be 0 or 1.

- j1: horizontal alignment (with j2),
- j2: horizontal alignment (with j1): j1 = 0, j2 = 0: Aligns to the left edge (default), j1 = 1, j2 = 0: Aligns to the right edge, j1 = 0, j2 = 1: Aligns to the center, j1 = 1, j2 = 1: Not used,
- j3: grayed text.