---
id: wiki.generated.global
type: wiki
category: other
commands: ["GLOBAL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### GLOBAL VARIABLES

The global variables make it possible to store special values of the model. This allows you to access geometric information about the environment of the GDL macro. For example, you can access the wall parameters when defining a window which has to fit into the wall. Global variables are not stacked during macro calls.

For doors, windows, labels and property library parts there is one more possibility to communicate with Archicad through fix named, optional parameters. These parameters, if present on the library part’s parameter list, are set by Archicad. See the list of fix named parameters and more details in the section called “Fix named optional parameters”.