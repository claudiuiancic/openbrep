---
id: wiki.generated.assoclp_parvalue_with_description
type: wiki
category: other
commands: ["ASSOCLP_PARVALUE_WITH_DESCRIPTION"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### ASSOCLP_PARVALUE_WITH_DESCRIPTION

n = REQUEST("ASSOCLP_PARVALUE_WITH_DESCRIPTION", expr, name_or_index, type,

flags, dim1, dim2, p_values_and_descriptions) Works the same as ASSOCLP_PARVALUE, except instead p_values:

p_values_and_descriptions: returns the parameter value followed by the parameter description string (as specified at the VALUES command command) or an array of these pairs. For string type parameters the description string is always empty. The array element - array element description string pairs are returned successively, row by row as a one dimensional array, independently of the dimensions of the variable specified to store it. If the variable is not a dynamic array, there are as many elements stored as there is room for (for a simple variable only one, the first element). If values is a two dimensional dynamic array, all elements are stored in the first row.