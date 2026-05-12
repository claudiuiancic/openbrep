---
id: wiki.generated.killgroup
type: wiki
category: other
commands: ["KILLGROUP"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### KILLGROUP g_expr

Clears the bodies of the specified group from the memory. After a KILLGROUP operation the group becomes empty. The names of killed groups cannot be reused in the same script. Clearing is executed automatically at the end of the interpretation or when returning from macro calls. For performance reasons this command should be used when a group is no longer needed.

Example: GROUP "box"

BRICK 1, 1, 1 ENDGROUP GROUP "sphere" ADDZ 1 SPHERE 0.45 DEL 1

ENDGROUP GROUP "semisphere"

ELLIPS 0.45, 0.45 ENDGROUP GROUP "brick"

ADD -0.35, -0.35, 0 BRICK 0.70, 0.70, 0.35 DEL 1

ENDGROUP ! Subtracting the "sphere" from the "box"

- result_1=SUBGROUP("box", "sphere") ! Intersecting the "semisphere" and the "brick"
- result_2=ISECTGROUP("semisphere", "brick") ! Adding the generated bodies
- result_3=ADDGROUP(result_1, result_2) PLACEGROUP result_3 KILLGROUP "box" KILLGROUP "sphere" KILLGROUP "semisphere" KILLGROUP "brick"