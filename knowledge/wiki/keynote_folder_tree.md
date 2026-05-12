---
id: wiki.generated.keynote_folder_tree
type: wiki
category: other
commands: ["KEYNOTE_FOLDER_TREE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### KEYNOTE_FOLDER_TREE

n = REQUEST("KEYNOTE_FOLDER_TREE", keynoteFolderTreeInput, keynoteFolderTreeOutput) Returns the Keynote folders tree of the project. Can be used only in UI Scripts of Keynote Legends. Expression returns 0 and contains dummy return values (empty dictionary) if used in other situations, triggering a warning. Compatibility: introduced in Archicad 28. keynoteFolderTreeInput: (dictionary) should be an empty, predefined dictionary. keynoteFolderTreeOutput: (dictionary) the tree of Keynote folders keynoteFolderTreeOutput.treeDepth: (integer) the depth of the property tree keynoteFolderTreeOutput.keynoteFolderTree: (array) for each returned folder, contains treeDepth + 1 strings: the ID of

the folder, then the path to it in the tree in the form of treeDepth strings

Example:

DICT keynoteFolderTreeInput, keynoteFolderTreeOutput n = REQUEST ("KEYNOTE_FOLDER_TREE", keynoteFolderTreeInput, keynoteFolderTreeOutput) if n > 0 then

ui_custom_popup_infield "stParameterName", 10, 20, 300, 19, 1, keynoteFolderTreeOutput.treeDepth, 1, "SelectedValueDescription", keynoteFolderTreeOutput.keynoteFolderTree