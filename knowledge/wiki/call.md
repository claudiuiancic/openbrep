---
id: wiki.generated.call
type: wiki
category: control
commands: ["CALL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### CALL

CALL macro_name_string [,] PARAMETERS [ALL][name1=value1, ..., namen=valuen][[,] RETURNED_PARAMETERS r1, r2, ...]

macro_name_string: string, the name of an existing library part

Macro names cannot be longer than 31 characters. Macro names can be string constants, string variables or parameters. String operations cannot be used with a macro call as a macro name. Warning: If string variables or parameters are used as macro names, the called macro may not be included in the archive project. To let GDL know about the dependency, use the FILE_DEPENDENCE command for each

possible macro name. The macro name must be put between quotation marks (",',`,´,”,’,“,‘), unless it matches the definition of identifiers, i.e., it begins with a letter or a '_' or '~' character and contains only letters, numbers and the '_' and '~' characters. Otherwise, the quotation marks used in the CALL command must be the same at the beginning and at the end, and should be different from any character of the macro name. Macro name itself also can be used as a command, without the CALL keyword.

PARAMETERS: the actual parameter list of the macro can follow

The parameter names of the called macro can be listed in any sequence, with both an '=' sign and an actual value for each. You can use string type expressions here, but only give a string value to string type parameters of the called macro. Array parameters have to be given full array values. If a parameter name in the parameter list cannot be found in the called macro, you will get an error message. Parameters of the called macro that are not listed in the macro call will be given their original default values as defined in the library part called as a macro.

ALL: all parameters of the caller are passed to the macro

If this keyword is present, there is no need to specify the parameters one by one. For a parameter of the macro which cannot be found in the caller, the default value will be used. If parameter values are specified one by one, they will override the values coming from the caller or parameters of the called macro left to be default.

RETURNED_PARAMETERS: a variable list can follow to collect the returned parameters of the macro

At the caller’s side, returned values can be collected using the RETURNED_PARAMETERS keyword followed by a variable list. The returned values will be stored in these variables in the order they are returned in the called macro. The number and the type of the variables specified in the caller and those returned in the macro must match. If there are more variables specified in the caller, they will be set to 0 integers. Type compatibility is not checked: the type of the variables specified in the caller will be set to the type of the returned values. If one of the variables in the caller is a dynamic array, all subsequent values will be stored in it. Note: the number of possible returned elements is limited at 32767 items. See the syntax of returning parameters at the END / EXIT command.

CALL macro_name_string [,]PARAMETERS

value1 or DEFAULT [, ..., valuen or DEFAULT]

This form of macro call can be used for compatibility with previous versions. Using this syntax the actual parameter values have to be specified one by one in the order they are present in the called library part, no value can be missed, except from the end of the list. Using the DEFAULT keyword in place of a parameter actual value means that the actual value will be the default value stored in the library part. For the missing values defaults will be used automatically (the number of actual values n can be smaller than the number of parameters). When interpreting this kind of macro call there is no need to find the parameters by name to assign them the actual value, so even though it is more uncomfortable to use than the previous ones, a better performance can be achieved.

CALL macro_name_string [, parameter_list]

This form of macro call can be used for compatibility with previous versions. Can be used with simple GDL text files as well as any library part, on the condition that its parameter list contains only single-letter numerical parameters (A ... Z). No string type expressions or arrays are allowed with this method. The parameter list is a list of simple numerical values: the value of parameter A will be the first value in the list, the value of parameter B will be the second value, and so on. If there are less than A ... Z values specified in the parameter list, for the missing values 0 will be used automatically. If the (library part) macro does not have a single-letter parameter corresponding to the value, interpretation will continue by skipping this value, but you will get a warning from the program.

Example:

CALL "leg" 2, , 5 ! A = 2, B = 0, C = 5 leg 2, , 5 CALL "door-1" PARAMETERS height = 2, a = 25.5,

name = "Director" CALL "door-1" PARAMETERS ! use parameter default values

OUTPUT IN AN ALERT BOX OR REPORT WINDOW