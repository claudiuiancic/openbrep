---
id: wiki.generated.shadow
type: wiki
category: other
commands: ["SHADOW"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### SHADOW

SHADOW casting [, catching]

Controls the shadow casting of the elements in PhotoRendering and in vectorial shadow casting. casting: ON, AUTO or OFF

ON: all the subsequent elements will cast shadows in all circumstances, OFF: none of the subsequent elements will cast shadows in any circumstance, AUTO: shadow casting will be determined automatically

Setting SHADOW OFF for hidden parts will spare memory space and processing time. Setting SHADOW ON ensures that even tiny details will cast shadows.