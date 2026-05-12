---
id: wiki.generated.haskey
type: wiki
category: other
commands: ["HASKEY"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### HASKEY

HASKEY (dictionary.key) Returns as a boolean whether key has been previously defined in dictionary (key can include sub-keys).

Example:

DICT myDictionary myDictionary.point[1].x = 1 myDictionary.point[1].y = 1

print HASKEY(myDictionary.point) ! true print HASKEY(myDictionary.point[2]) ! false print HASKEY(myDictionary.point[1].z) ! false