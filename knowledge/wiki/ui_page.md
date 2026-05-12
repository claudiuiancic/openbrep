---
id: wiki.generated.ui_page
type: wiki
category: other
commands: ["UI_PAGE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### UI_PAGE

UI_PAGE page_number [, parent_id, page_title [, image]]

Page directive, defines the page that the interface elements are placed on. Default page numbering starts at 1, but any starting number is usable. If there is no UI_PAGE command in the Interface Script, each element will be displayed on the first page by default. Moving between pages can be defined in different ways:

- • The easiest way is to let Archicad do it: in the object editor, press the "Hierarchical Pages" button in the User Interface Script window, and fill in the optional parameters of the UI_PAGE command. In this case the page_number of the page selected from the tree is passed to the library part through the "gs_ui_current_page" parameter. No need to set a value list for the paging parameter: Archicad collects and sorts all valid page ID-s from the UI_PAGE command's parameters by pre-reading the object's ui script.
- • Another method is to use two buttons created with the UI_NEXT and UI_PREV commands, placing them on every page to manipulate the value of the "gs_ui_current_page" parameter. See the UI_BUTTON command for more information.
- • In case the new hierarchical page setup is not required, to create dynamic page handling, use the the UI_INFIELD{3} command. Set a value list for "gs_ui_current_page" parameter, and place a popup using its values on every page.


page_number: the page number, a positive integer. Following interface elements are placed on this page. parent_id: positive integer, the parent id of the page. The special value -1 value means root parent. Only evaluated if "Hierarchical Pages"

is set.

page_title: title string of the page, appears on the top of the page and the tree view popup of the pages. Only evaluated if "Hierarchical

Pages" is set.

image: file name or index number of a picture stored in the library part. If specified and not empty or 0, this icon associated to the page is

displayed on the top of the page and in tree view popup of the pages, next to the title. Only evaluated if "Hierarchical Pages" is set.

Warning: In the simple way of paging, any break of continuity in the page numbering forces the insertion of a new page without buttons, and therefore there will be no possibility to go to any other page from there. This restriction can be circumvented using the UI_CURRENT_PAGE command.