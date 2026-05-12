---
id: wiki.generated.dict
type: wiki
category: other
commands: ["DICT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### DICT

DICT variableName1[, variableName2...]

- Compatibility: introduced in Archicad 23.


GDL supports dictionaries. A variable is declared as a dictionary after the above declaration statement (and cannot be changed to array or simple type or vice versa). Library part parameters can also be dictionaries, by selecting Dictionary type in the parameter list.

After the DICT keyword there can be any number of variable names separated by commas. Each variable will contain hierarchical key and value pairs. A key of the dictionary can be referenced with dot notation. The full path of a key cannot be longer than 255 characters (counting array indices as one character).

Dictionaries and simple type values:

- • simple type (string, integer, floating-point) values can be assigned to dictionary keys,
- • no declaration is necessary, the value type for the key is set by the current value:


myDictionary.element1 = 1 myDictionary.element1 = "hello"

print myDictionary Dictionaries and derived type values:

- • a dictionary can nest array type (with one dimension only) and dictionary type keys,
- • an array inside a dictionary can contain unnamed dictionary or simple types (referenced by the index),
- • however, a standalone array type parameter/variable cannot contain dictionary type elements,
- • a nested array key can be initialized by referencing it right away, no need to declare with DIM in this case, DICT myDictionary myDictionary.myArray[1] = 1 myDictionary.myArray[2] = 5 print myDictionary
- • unreferenced indexes of a nested array are automatically initialized according to the type of the first referenced element of the array (string keys to "", numerical keys to 0, dictionary keys to {}), DICT myDictionary DICT dictForNesting dictForNesting.elem1 = "hello" dictForNesting.elem2 = "world" myDictionary.myArray[2] = dictForNesting print myDictionary

DICT myDictionary2 myDictionary2.myArray[3] = 33 myDictionary2.myArray[4] = 44

print myDictionary2

- • the values of a nested array has to be of the same type (all string, all integer, all floating-point or all dictionary types), this is contrary to how arrays work, so extra caution is needed! DICT myDictionary2 myDictionary2.myArray[1] = 1 myDictionary2.myArray[2] = 1.0 ! GDL error


- • to change the value types of a nested array, it needs to be reset first: create an empty array, and overwrite the nested array with this new empty array. The type of the next referenced value will set the type for the array after the reset automatically: DICT myDictionary myDictionary.myArray[1] = "hello" print myDictionary

DIM arrayForReset[] myDictionary.myArray = arrayForReset print myDictionary

myDictionary.myArray[1] = 10000 print myDictionary

- • changing the type of the first value of a nested array containing that value only, will not change the type of the array! DICT myDictionary myDictionary.myArray[1] = "hello" print myDictionary


myDictionary.myArray[1] = 10000 ! GDL error print myDictionary

Initialization and copying:

- • the first reference of the dictionary has to be DICT dictName, a subroutine containing the name of the dictionary can not precede it (same as with DIM arrays),
- • initialization is required before the first use of a key, either explicitly with assignment to the key, or implicitly with assigning a dictionary that contains the key at the right depth. DICT myDictionary

myDictionary.level1.a = 1 myDictionary.level1.b = 2 myDictionary.level2 = myDictionary.level1

print myDictionary.level2.b

- • writing the dictionary name without actual inner keys references the whole dictionary structure, which is accepted in some cases (CALL, PRINT, LET statements),
- • writing part of the structure references the subtree below that key as a dictionary


myDictionary.point1.x = 1 myDictionary.point1.y = 1 myDictionary.point1.type = 0 print myDictionary

DICT myPoint myPoint = myDictionary.point1 print myPoint

myDictionary.point2 = myDictionary.point1 print myDictionary

- • assigning all or part of a dictionary makes a deep copy of the right-hand side on the left-hand side DICT myDictionary, tempPoint tempPoint.x = 1 tempPoint.y = 1


- myDictionary.line.point1 = tempPoint

tempPoint.x = 2 tempPoint.y = 2

- myDictionary.line.point2 = tempPoint


DICT myLine myLine = myDictionary.line myDictionary.line.point2.x = 0 print myLine

Macro calls and requests:

- • in macro calls, dictionary type values can be sent to the macro if there is a dictionary type parameter on the receiving end,
- • RETURNED_PARAMETERS can work with dictionaries: an empty DICT has to be declared on the receiving end (caller object). In the following code myDictionary is a dict type parameter in the macro, _myDictionary is a dict type variable on the caller object side:


! caller object Master script DICT _myDictionary

_myDictionary.element1 = 1 _myDictionary.element2 = 2

DICT _dictForReceivedData call "macroname" parameters all myDictionary = _myDictionary,

returned_parameters _dictForReceivedData print _dictForReceivedData ! in the macro object Master script myDictionary.element1 = myDictionary.element1 * 2 myDictionary.element2 = myDictionary.element2 * 2 end myDictionary

- • in REQUEST options currently there is no request supporting dictionaries. However, the possibility is open for the future.
- • LIBRARYGLOBAL requests cannot return dictionary type values. Visualization and functions:
- • dictionary type parameters are not visible on "All Parameters" page in the "Settings" dialog,
- • dictionary type parameters are not available for Listing display or IFC mappings,
- • text-like visualization works only with the PRINT command ("Check Script" warning and printed to Report window in JSON format),
- • general text handling commands like TEXT2, RICHTEXT2, etc. are not supporting the complete dictionary,
- • however, nested non-dictionary type values can be displayed with them, DICT myDictionary myDictionary.myArray[1] = "hello" myDictionary.myArray[2] = "world"

text2 0, 0, myDictionary.myArray[1] + " " + myDictionary.myArray[2] print myDictionary

- • values for a dictionary type parameter can only be set via the Parameter script (no direct user input is available through Parameter list or UI controls), the VALUES command is disabled for this type,


- • however, using non-dictionary parameters for user input can work. In the following code, myDictionary is a dictionary type parameter, stTextInput is a string type parameter (which can be used in User Interface, displayed on the "All Parameters" page, and works together with GLOB_MODPAR_NAME): ! in Parameter Script myDictionary.text1 = stTextInput parameters myDictionary = myDictionary

! in Master Script print myDictionary

! in 2D script

- TEXT2 0, 0, myDictionary.text1


- • value replacement using the LP_XMLConverter tool is currently unavailable for dictionary type parameters.