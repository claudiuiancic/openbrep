---
id: wiki.generated.ancestry_info
type: wiki
category: other
commands: ["ANCESTRY_INFO"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### ANCESTRY_INFO

n = REQUEST("ANCESTRY_INFO", expr, name [, guid, parent_name1, parent_guid1,

... parent_namen, parent_guidn)

Ancestry information on a library part. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning. expr: Select queried library part

- 0: returns in the given variables the name and the globally unique identifier of the library part containing this request function. Optionally the function returns the names and globally unique identifiers of the parents of the library part (parent_namei, parent_guidi). If the parent templates are not loaded their names will be empty strings.
- 1: returns information on the library part replaced by the template containing this function. In this case if the template is not actually replacing, no values are returned.


The return value of the request is the number of successfully retrieved values.

Example:

DIM strings[] n = REQUEST ("ANCESTRY_INFO", 1, name, guid, strings) IF n > 2 THEN

! data of replaced library part TEXT2 0, -1, "replacing: " + name + ' ' + guid ! parents l = -2 FOR i = 1 TO n - 2 STEP 2

TEXT2 0, l, strings [i] l = l - 1

NEXT i ENDIF