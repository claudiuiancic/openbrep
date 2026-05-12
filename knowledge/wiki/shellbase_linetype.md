---
id: wiki.generated.shellbase_linetype
type: wiki
category: other
commands: ["SHELLBASE_LINETYPE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### SHELLBASE_LINETYPE line type of the shell/roof

applied on the contours only in the floor plan window, equal to ROOF_LINETYPE for roofs SHELLBASE_FILL fill of the shell/roof

fill index - its value is negative in case of a composite structure, equal to ROOF_FILL for roofs

SHELLBASE_FILL_PEN pen of the fill of the roof shell/roof

equal to ROOF_FILL_PEN for roofs

SHELLBASE_FBGD_PEN pen of the background of the fill of the shell/roof

equal to ROOF_FBGD_PEN for roofs

SHELLBASE_COMPS_NAME name of the composite structure of the shell/roof

equal to ROOF_COMPS_NAME for roofs

SHELLBASE_BMAT_NAME building material name of the shell/roof

equal to ROOF_BMAT_NAME for roofs

SHELLBASE_BMAT building material index of the shell/roof Compatibility: introduced in Archicad 21. equal to ROOF_BMAT for roofs

SHELLBASE_SKINS_NUMBER number of composite roof skins shell/roof

range of 1 to 8, 0 if single fill applied, equal to ROOF_SKINS_NR for roofs

SHELLBASE_SKINS_PARAMS parameters of the composite roof skin shell/roof

array with 18 columnswith arbitrary number of rows:

- • [1] fill
- • [2] thickness
- • [3] (old contour pen)
- • [4] pen of fill
- • [5] pen of fill background
- • [6] core status
- • [7] upper line pen • [8] upper line type • [9] lower line pen
- • [10] lower line type
- • [11] end face pen
- • [12] fill orientation
- • [13] skin type
- • [14] end face line type • [15] finish skin status • [16] oriented fill status • [17] core skin status (if no core skin exists, the thickest skin)
- • [18] building material index. core status: 0 - not part, 1 - part, 3 - last skin of core, fill orientation: 0 - global, 1 - local; skin type: in the current Archicad always 0 - cut, it can be used as in walls later; finish skin status: 0 not finish skin, 1: finish skin equal to ROOF_SKINS_PARAMS for roofs


SHELLBASE_SKINS_BMAT_NAMES building material names of the composite roof skin shell/roof array with 1 column: building material name of the skin and with arbitrary number of rows. equal to ROOF_SKINS_BMAT_NAMES for roofs

SHELLBASE_SECT_PEN pen of the contours of the roof cut surfaces shell/roof applied on contours of cut surfaces both in floor plan and section/elevation windows, equal to ROOF_SECT_PEN for roofs SHELLBASE_VIEW_PEN pen of the roof on view shell/roof

applied on all edges in 3D window and on outline edges (edges on view below cutting plane) in floor plan and section/elevation windows, equal to ROOF_VIEW_PEN for roofs