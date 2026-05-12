---
id: wiki.generated.keynote_info
type: wiki
category: other
commands: ["KEYNOTE_INFO"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### KEYNOTE_INFO

n = REQUEST("KEYNOTE_INFO", keynoteInfoInput, keynoteInfoOutput) Returns requested information about Keynotes as defined by the input parameter. Can be used only in 2D Scripts of Keynote Legends placed on layouts. Expression returns 0 and contains dummy return values (empty dictionary) if used in other situations, triggering a warning.

keynoteInfoInput: (dictionary) defines the parameters for collecting Keynote information. keynoteInfoInput.source: (string) keyword defining the source of the requested Keynotes. This key is optional. If it does not exist,

the request collects the visible Keynotes. Possible values: "ALLKEYNOTES" "VISIBLEKEYNOTES"

keynoteInfoInput.filterToFolders: (array) contains a dictionary for each folder. It may contain at most one element. This key

is optional. If it does not exist, the request collects Keynote folders and items in all folders of the source.

keynoteInfoInput.filterToFolders[n].folderId: (string) id of the folder to filter to, as returned by

KEYNOTE_FOLDER_TREE

keynoteInfoInput.dataTypeToGet: (dictionary) defines the data type of the keynote items and folders which the request should

return. keynoteInfoInput.dataTypeToGet.folderKey: (boolean) defines if Keynote folder keys are required. keynoteInfoInput.dataTypeToGet.folderTitle: (boolean) defines if Keynote folder titles are required. keynoteInfoInput.dataTypeToGet.folderReference: (boolean) defines if Keynote folder references are required. keynoteInfoInput.dataTypeToGet.itemKey: (boolean) defines if Keynote item keys are required. keynoteInfoInput.dataTypeToGet.itemTitle: (boolean) defines if Keynote item titles are required. keynoteInfoInput.dataTypeToGet.itemDescription: (boolean) defines if Keynote item descriptions are required. keynoteInfoInput.dataTypeToGet.itemReference: (boolean) defines if Keynote item references are required. keynoteInfoInput.includeAncestry: (string) keyword defining the part of ancestry to be returned. This key is optional. If it

does not exist, ParentOnly option is the default value. Possible values: "PARENTONLY" "FILTEREDANCESTRY": Filters ancestry based on the value of filterToFolders. "FULLANCESTRY"

keynoteInfoInput.omitConflict: (boolean) defines if conflicting Keynote item or folder fields should be omitted, or a placeholder

text returned instead. This key is optional. If it does not exist, placeholder text is returned.

keynoteInfoInput.sortingType: (string) defines the sorting type used on Keynote items and folders in the Keynote Legend. This key is optional. If it does not exist, the Keynote items and folders will be sorted alphabetically. "ALPHABETICAL": Alphabetical sorting is based on the selected column order. "HIERARCHICAL": Hierarchical sorting gives back the Keynotes palette order, except that Keynote items without folders always appear at the top of the list.

keynoteInfoInput.activeKeynoteColumns: (array) contains dictionaries corresponding to each selected Keynote item column. It may contain at least one and at most four elements. This key is optional. If it does not exist, the request sorts items based on the default [KEYNOTE_KEY, KEYNOTE_TITLE] active column order.

keynoteInfoInput.activeKeynoteColumns[n].keynoteField: (string) selected field of the nth active Keynote item column. "NONE" "KEYNOTE_KEY" "KEYNOTE_TITLE" "KEYNOTE_DESCRIPTION" "KEYNOTE_REFERENCE"