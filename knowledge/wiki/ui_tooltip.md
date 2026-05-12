---
id: wiki.generated.ui_tooltip
type: wiki
category: other
commands: ["UI_TOOLTIP"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### UI_TOOLTIP

UI_BUTTON type, text, x, y, width, height [, id [, url]] [ UI_TOOLTIP tooltiptext ] UI_PICT_BUTTON type, text, picture_reference,

x, y, width, height [, id [, url]] [ UI_TOOLTIP tooltiptext ] UI_INFIELD "name", x, y, width, height [, extra parameters ... ]

[ UI_TOOLTIP tooltiptext ]

UI_INFIELD{2} name, x, y, width, height [, extra parameters ... ]

[ UI_TOOLTIP tooltiptext ]

UI_INFIELD{3} name, x, y, width, height [, extra parameters ... ]

[ UI_TOOLTIP tooltiptext ]

UI_INFIELD{4} "name", x, y, width, height [, extra parameters ... ]

[ UI_TOOLTIP tooltiptext ]

UI_CUSTOM_POPUP_INFIELD "name", x, y, width, height , extra parameters ...

[ UI_TOOLTIP tooltiptext ]

UI_CUSTOM_POPUP_INFIELD{2} name, x, y, width, height , extra parameters ...

[ UI_TOOLTIP tooltiptext ] UI_RADIOBUTTON name, value, text, x, y, width, height [ UI_TOOLTIP tooltiptext ] UI_OUTFIELD expression, x, y, width, height [, flags] [ UI_TOOLTIP tooltiptext ] UI_PICT expression, x, y [, width, height [, mask]] [ UI_TOOLTIP tooltiptext ] UI_LISTFIELD fieldID, x, y, width, height [, iconFlag [, description_header [, value_header]]]

[ UI_TOOLTIP tooltiptext ]

UI_LISTITEM itemID, fieldID, "name" [, childFlag [, image [, paramDesc]]]

[ UI_TOOLTIP tooltiptext ]

UI_LISTITEM{2} itemID, fieldID, name [, childFlag [, image [, paramDesc]]]

[ UI_TOOLTIP tooltiptext ]

UI_CUSTOM_POPUP_LISTITEM itemID, fieldID, "name", childFlag , image , paramDesc, extra parameters ... [ UI_TOOLTIP tooltiptext ]

UI_CUSTOM_POPUP_LISTITEM{2} itemID, fieldID, name, childFlag , image , paramDesc, extra parameters ... [ UI_TOOLTIP tooltiptext ]

Defines the tooltip for the control on the user interface page. Tooltips are available for buttons, infields, outfields, listfields, listitems and pictures if they are not disabled by the user in the running context (e.g., in the Help menu of Archicad). The listfield's tooltip appears in all included listitems if an item has none declared. The own tooltip of the listitem will take effect over the tooltip of the listfield (if existing) inline. tooltiptext: the text to display as tooltip for the control.