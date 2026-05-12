---
id: wiki.generated.ui_button
type: wiki
category: other
commands: ["UI_BUTTON"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### UI_BUTTON

UI_BUTTON type, text, x, y [, width, height, id [, url]] Button definition on current page. Buttons can be used for various purposes: moving from page to page, opening a web page or performing some parameter-script defined action. Buttons can contain text. type: type of the button as follows:

UI_PREV: if pressed, the previous page is displayed, UI_NEXT: if pressed, the next page is displayed, UI_FUNCTION: if pressed, the GLOB_UI_BUTTON_ID global variable is set to the button id specified in expression, UI_LINK: if pressed, the URL in expression is opened in the default web browser,

text: the text that should appear on the button. x, y: the position of the button. width, height: width and height of the button in pixels. If not specified (for compatibility reasons) the default values are 60 pixels

for width and 20 pixels for height. id: an integer unique identifier. url: a string containing a URL. UI_PREV and UI_NEXT buttons are disabled if the previous/next page is not present. If these buttons are pushed, the gs_ui_current_page parameter of the library part is set to the index of the page to show - if there’s a parameter with this name.

Example:

! UI script UI_CURRENT_PAGE gs_ui_current_page UI_BUTTON UI_FUNCTION, "Go to page 9", 200,150, 70,20, 3 UI_BUTTON UI_LINK, "Visit Website", 200,180, 100,20, 0,

"https://graphisoft.com" ! parameter script if GLOB_UI_BUTTON_ID = 3 then

parameters gs_ui_current_page = 9, ... endif