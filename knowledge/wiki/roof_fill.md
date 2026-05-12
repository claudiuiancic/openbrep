---
id: wiki.generated.roof_fill
type: wiki
category: other
commands: ["ROOF_FILL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### ROOF_FILL fill of the roof

fill index - its value is negative in case of a composite structure ROOF_FILL_PEN pen of the fill of the roof ROOF_FBGD_PEN pen of the background of the fill of the roof ROOF_COMPS_NAME name of the composite structure of the roof ROOF_BMAT_NAME building material name of the roof, empty string for composite roofs ROOF_BMAT building material index of the roof, 0 for composite roofs

Compatibility: introduced in Archicad 21.

ROOF_SKINS_NUMBER number of composite roof skins

range of 1 to 8, 0 if single fill applied

ROOF_SKINS_PARAMS parameters of the composite roof skin

array with 18 columns with arbitrary number of rows:

- • [1] fill
- • [2] thickness
- • [3] (old contour pen)
- • [4] pen of fill
- • [5] pen of fill background
- • [6] core status
- • [7] upper line pen
- • [8] upper line type
- • [9] lower line pen
- • [10] lower line type
- • [11] end face pen
- • [12] fill orientation
- • [13] skin type
- • [14] end face line type
- • [15] finish skin status
- • [16] oriented fill status
- • [17] core skin status (if no core skin exists, the thickest skin)
- • [18] building material index. core status: 0 - not part, 1 - part, 3 - last skin of core, fill orientation: 0 - global, 1 - local; skin type: in the current Archicad always 0 - cut, it can be used as in walls later; finish skin status: 0 not finish skin, 1: finish skin


ROOF_SKINS_BMAT_NAMES building material names of the composite roof skin

array with 1 column: building material name of the skin and with arbitrary number of rows.

ROOF_SECT_PEN pen of the contours of the roof cut surfaces

applied on contours of cut surfaces both in floor plan and section/elevation windows