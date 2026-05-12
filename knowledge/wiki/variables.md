---
id: wiki.generated.variables
type: wiki
category: other
commands: ["VARIABLES"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### VARIABLES

GDL programs can handle numeric and string variables (defined by their identifiers), numbers and character strings. There are two sets of variables: local and global.

All identifiers that are not keywords, global variables, attribute names, macro names or file names are considered local variables. If left uninitialized (undefined), their value will be 0 (integer). Local variables are stacked with macro calls. When returning from a macro call, the interpreter restores their values.

Global variables have reserved names (for the list of global variables see the section called “Global Variables”). They are not stacked during macro calls, enabling the user to store special values of the modeling and to simulate return codes from macros. The user global variables can be set in any script but they will only be effective in subsequent scripts. If you want to make sure that the desired script is analyzed first, set these variables in the MASTER_GDL library part. All elements will always read these values set by the Master GDL first, unless their own scripts (caller object or called macro) modify those values. There is no user global data exchange between the different interpretation instances. The other global variables can be used in your scripts to communicate with the program. By using the "=" command, you can assign a numeric or string value to local and global variables.