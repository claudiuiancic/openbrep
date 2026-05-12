---
id: wiki.generated.story_info
type: wiki
category: other
commands: ["STORY_INFO"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### STORY_INFO

n = REQUEST("STORY_INFO", expr, nStories, index1, name1, elev1, height1 [, index2, name2, ...])

Returns the story information in the given variables: number of stories and story index, name, elevation, height to next successively. expr: Selects which stories to request

a story index: only the number of stories and the information on the specified story is returned. "": information on all stories is requested.

The return value of the function is the number of successfully retrieved values.

Example:

DIM t[] n = REQUEST ("STORY_INFO", "", nr, t) FOR i = 1 TO nr

nr = STR ("%.0m", t [4 * (i - 1) + 1]) name = t [4 * (i - 1) + 2] elevation = STR ("%m", t [4 * (i - 1) + 3]) height = STR ("%m", t [4 * (i - 1) + 4]) TEXT2 0, -i, nr + "," + name + "," + elevation + "," + height

NEXT i