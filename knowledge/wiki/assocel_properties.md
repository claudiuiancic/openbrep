---
id: wiki.generated.assocel_properties
type: wiki
category: other
commands: ["ASSOCEL_PROPERTIES"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### ASSOCEL_PROPERTIES

n = REQUEST("ASSOCEL_PROPERTIES", parameter_string, nr_data, data)

Returns, in the given variables, own property data or the element properties which the library part containing this request is associated to (in labels and associative marker objects). The function return value is the number of successfully retrieved values, 0 if no property data was found or an error occurred. The function does not work in property objects during the listing process. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning.

parameter_string: a combination of keywords separated by commas representing the requested fields of the property data records. Records will be ordered accordingly. Possible values: "ISCOMP" "DBSETNAME" "KEYCODE" "KEYNAME" "CODE" "NAME" "FULLNAME" "QUANTITY" "TOTQUANTITY" "UNITCODE" "UNITNAME" "UNITFORMATSTR" "PROPOBJNAME"

nr_data: returns the number of the data items. data: returns the property data, records containing and being ordered by the fields specified in the parameter string. Values are returned as

a one dimensional array which contains the requested record fields successively, independently of the dimensions of the variable specified to

store it. If the variable is not a dynamic array, there are as many elements stored as there is room for (in case of a simple variable only one, the first element). If values is a two dimensional dynamic array, all elements are stored in the first row.

Example:

DIM DATA [] n = REQUEST ("ASSOCEL_PROPERTIES", "iscomp, code, name", nr, data) IF nr = 0 THEN

TEXT2 0, 0, "No properties" ELSE

j = 0 FOR i = 1 TO nr

IF i MOD 3 = 0 THEN TEXT2 0, -j, DATA [i] ! name j = j + 1

ENDIF NEXT i

ENDIF