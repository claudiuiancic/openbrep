---
id: wiki.generated.request
type: wiki
category: param
commands: ["REQUEST"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### REQUEST

REQUEST (question_name, name | index, variable1 [, variable2, ...])

The first parameter represents the question string while the second represents the object of the question (if it exists) and can be of either string or numeric type (for example, the question can be "RGB_OF_MATERIAL" and its object the material’s name, or "RGB_OF_PEN" and its object the index of the pen). The other parameters are variable names in which the return values (the answers) are stored.

The return value of the requests is always the number of successfully retrieved values (integer), while the type of the retrieved values is defined by each request in part. In the case of a badly formulated question or a nonexistent name, the return value will be 0. Archicad identifies the order and number of the input parameters by either the version of the command, or the exact name (as string constant) of the request option. Current accepted variations:

- • n = REQUEST - default request, with 1 input parameter of string or numeric type
- • n = REQUEST{2} - 2 input parameters: string or numeric, string type
- • n = REQUEST{3} - 2 input parameters: string, string or numeric array type
- • n = REQUEST{4} - 3 input parameters: string or numeric, numeric, string type. Compatibility: introduced in Archicad 21. For the list of available options see the section called “Listing of REQUESTs”.