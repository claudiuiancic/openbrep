---
id: wiki.generated.model
type: wiki
category: other
commands: ["MODEL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### MODEL WIRE MODEL SURFACE MODEL SOLID

Sets the representation mode in the current script. MODEL WIRE: only wireframe, no surfaces or volumes. Objects are transparent. MODEL SURFACE, MODEL SOLID: The generation of the section surfaces is based on the relation of the boundary surfaces, so that both methods generate the same 3D internal data structure. Objects are opaque. The only distinction can be seen after cutting away a part of the body: MODEL SURFACE: the inside of bodies will be visible,

MODEL SOLID: new surfaces may appear. Default: MODEL SOLID

Example: To illustrate the three modeling methods, consider the following three blocks: MODEL WIRE BLOCK 3,2,1 ADDY 4 MODEL SURFACE BLOCK 3,2,1 ADDY 4 MODEL SOLID BLOCK 3,2,1 After cutting them with a plane: