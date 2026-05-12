---
id: wiki.generated.ui_infield_4
type: wiki
category: other
commands: ["UI_INFIELD{4}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### UI_INFIELD{4} "name", x, y, width, height [, method, picture_name, images_number, rows_number, cell_x, cell_y, image_x, image_y, expression_image1, text1, value_definition1,

... [picIdxArray, textArray, valuesArray,

...] expression_imagen, textn, value_definitionn]

Generates an edit text or a pop-up menu for the parameter input. A pop-up is generated if the parameter type is value list, material, fill, line type or pencolor.

If the optional parameters of the command are present, value lists can be alternatively displayed as thumbnail view fields. Different thumbnail control types are available. They display the specified images and associated texts and allow the selection of one single item at a time, just like in a pop-up menu.

In the version 1 and 2 infield, the thumbnail items and the value list items are associated by indices.

The version 3 and version 4 infield defines value association which binds the thumbnail items to value list items of the associated parameter. If a value defined in a thumbnail item isn’t present in the parameter’s value list, it won’t be displayed in the control. Identical sized arrays can be used for lines of definition as well.

The Interface Script is rebuilt with the new value after any parameter is modified. name: parameter name as string expression (all 4 command versions), with parameter name option for UI_INFIELD{2} and

- UI_INFIELD{3}, and parameter name as text array value option for UI_INFIELD{4}.


x, y: the position of the edit text, pop-up or control. width, height: width and height in pixels. method: the type of the control.

- 1: List view control.

![image 4](<GDL_Reference_Guide_28_images/imageFile4.png>)

- 2: Popup menu control.

![image 5](<GDL_Reference_Guide_28_images/imageFile5.png>)

- 3: Popup icon radio control (arrow on picture).

![image 6](<GDL_Reference_Guide_28_images/imageFile6.png>)

- 4: Push icon radio control.


![image 7](<GDL_Reference_Guide_28_images/imageFile7.png>)

- 5: Pushbutton with text.

![image 8](<GDL_Reference_Guide_28_images/imageFile8.png>)

- 6: Pushbutton with picture.

![image 9](<GDL_Reference_Guide_28_images/imageFile9.png>)

- 7: Checkbox with text.

![image 10](<GDL_Reference_Guide_28_images/imageFile10.png>)

- 8: Popup list with text.

![image 11](<GDL_Reference_Guide_28_images/imageFile11.png>)

- 9: Popup icon radio control (arrow next to picture).


![image 12](<GDL_Reference_Guide_28_images/imageFile12.png>)

picture_name: name of the common image file containing a matrix of concatenated images, or empty string. images_number: number of images in the matrix, for boolean parameters it can be 0 or 2. rows_number: number of rows of the matrix. cell_x, cell_y: width and height of a cell within the thumbnail view field, including image and text. image_x, image_y: width and height of the image in the cell.

expression_imagei: index of image number i in the matrix, or individual file name. If a common image file name was specified, indices

must be used here. Combination of indices and individual file names does not work. texti: text in cell number i. value_definitioni: value definition which matches the cell with a value list item by value:

expression: numerical or string expression, or CUSTOM: keyword, meaning that any custom value can be entered.

picIdxArray: Dynamic array of picture names (strings) or indexes (integers) in cells. Do not use mixed types in array textArray: Dynamic array of texts in cells valueArray: Dynamic array of parameter values in cells

IF c THEN UI_DIALOG "Hole definition parameters" UI_OUTFIELD "Type of hole:",15,40,180,20 UI_INFIELD "D",190,40,105,20 IF d="Rectangular" THEN

UI_PICT "rect.pict",110,33,60,30 UI_OUTFIELD "Width of hole",15,70,180,20

- UI_INFIELD "E", 190,70,105,20 UI_OUTFIELD "Height of hole",15,100,180,20
- UI_INFIELD "F", 190,100,105,20 UI_OUTFIELD "Distance between holes",15,130,180,20
- UI_INFIELD "G", 190,130,105,20


ELSE

UI_PICT "circle.pict",110,33,60,30 UI_OUTFIELD "Diameter of hole circle",15,70,180,20

- UI_INFIELD "J", 190,70,105,20 UI_OUTFIELD "Distance of hole centers", 15,100,180,20
- UI_INFIELD "K", 190,100,105,20 UI_OUTFIELD "Resolution of hole circle", 15,130,180,20 UI_INFIELD "M", 190,130,105,20


ENDIF UI_OUTFIELD "Number of holes",15,160,180,20 UI_INFIELD "I", 190,160,105,20

ENDIF UI_SEPARATOR 50,195,250,195 UI_OUTFIELD "Material of beam", 15,210,180,20 UI_INFIELD "MAT", 190,210,105,20 UI_OUTFIELD "Pen of beam", 15,240,180,20 UI_INFIELD "P", 190,240,105,20

![image 13](<GDL_Reference_Guide_28_images/imageFile13.png>)

![image 14](<GDL_Reference_Guide_28_images/imageFile14.png>)

Example 2:

! Parameter Script: VALUES "myParameter" "Two", "Three", "Five", CUSTOM

! Interface Script: px = 80 py = 60 cx = px + 3 cy = py + 25

- UI_INFIELD{3} "myParameter", 10, 10, 4 * cx + 21, cy + 5, 1, "myPicture", 6, 1, cx, cy, px, py,


- 1, "1 - one", "One",
- 2, "2 - two", "Two",
- 3, "3 - three", "Three",
- 4, "4 - four", "Four",
- 5, "5 - five", "Five",
- 6, "custom value", CUSTOM


! Parameter Script: VALUES "myParameter" "Two", "Three", "Five", CUSTOM

! Interface Script: px = 80 py = 60 cx = px + 3 cy = py + 25

paramNameVar = "myParameter"

- UI_INFIELD{4} paramNameVar, 10, 10, 4 * cx + 21, cy + 5, 1, "myPicture", 6, 1, cx, cy, px, py,


- 1, "1 - one", "One",
- 2, "2 - two", "Two",
- 3, "3 - three", "Three",
- 4, "4 - four", "Four",
- 5, "5 - five", "Five",
- 6, "custom value", CUSTOM


! Master Script dim picIdxValuesUI[] dim textValuesUI[] dim parameterValues[]

if myTypeParameter = 1 then

picIdxValuesUI[1] = 6 picIdxValuesUI[2] = 7 picIdxValuesUI[3] = 8

textValuesUI[1] = "6 - six" textValuesUI[2] = "7 - seven" textValuesUI[3] = "8 - eight"

parameterValues[1] = "Six" parameterValues[2] = "Seven" parameterValues[3] = "Eight"

else

picIdxValuesUI[1] = 6 picIdxValuesUI[2] = 7

textValuesUI[1] = "6 - six" textValuesUI[2] = "7 - seven"

parameterValues[1] = "Six" parameterValues[2] = "Seven"

endif

! Parameter Script: VALUES "myTypeParameter" 1, 2 VALUES "myStringParameter" "Two", "Three", "Five", parameterValues, CUSTOM

! Interface Script: px = 80 py = 60 cx = px + 3 cy = py + 25

paramNameVar = "myStringParameter"

- UI_INFIELD{4} paramNameVar, 10, 10, 4 * cx + 21, cy + 5, 1, "myPicture", 6, 1, cx, cy, px, py, 1, "1 - one", "One", 2, "2 - two", "Two", 3, "3 - three", "Three", 4, "4 - four", "Four", 5, "5 - five", "Five", picIdxValuesUI, textValuesUI, parameterValues, 9, "custom value", CUSTOM