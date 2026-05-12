---
id: wiki.generated.removekey
type: wiki
category: other
commands: ["REMOVEKEY"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### REMOVEKEY

REMOVEKEY (dictionary.key) The function removes the referred key from the dictionary, along with the assigned value(s). If the removal was successful, the return value is 1, othervise 0 (in case the key is non-existent or already deleted).

Example:

DICT myDictionary myDictionary.myText[1] = "hello" myDictionary.myOtherText[1] = "world"

print myDictionary _dummy = REMOVEKEY(myDictionary.myOtherText) print myDictionary, _dummy _dummy2 = REMOVEKEY(myDictionary.myNonExistentText) print myDictionary, _dummy2