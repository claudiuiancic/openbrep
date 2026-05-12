---
id: wiki.generated.p
type: wiki
category: other
commands: ["P"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### P

n = REQUEST("PEN_OF_RGB", "r g b", penindex) n = REQUEST("PROFILE_COMPONENTS", name_or_index, nComponents, compType1, compType2, ..., compTypen)

n = REQUEST{4}("PROFILE_COMPONENT_INFO", name_or_index, component_ind, param_name, value)

n = REQUEST("PROFILE_DEFAULT_BOUNDINGBOX", name_or_index, xmin, ymin, xmax, ymax) n = REQUEST("PROFILE_DEFAULT_GEOMETRY", name_or_index, n1, n2, ..., nm,

x11, y11, edgeVisible11, vertEdgeVisible11, additionalStatus11, ..., x1n1, y1n1, edgeVisible1n1, vertEdgeVisible1n1, additionalStatus1n1, x21, y21, edgeVisible21, vertEdgeVisible21, additionalStatus21, ..., x2n2, y2n2, edgeVisible2n2, vertEdgeVisible2n2, additionalStatus2n2,

..., xm1, ym1, edgeVisiblem1, vertEdgeVisiblem1, additionalStatusm1, ..., xmnm, ymnm, edgeVisiblemnm, vertEdgeVisiblemnm, additionalStatusmnm)

n = REQUEST("PROGRAM_INFO", "", name[, version[, keySerialNumber[, isCommercial]]]) n = REQUEST("PROPERTIES_OF_PARENT", propertyType, parentProperties) n = REQUEST("PROPERTY_NAME", "id", typeName, groupName, propertyName) n = REQUEST("PROPERTY_TREE_OF_PARENT", propTreeInput, propTreeOutput) n = REQUEST("PROPERTY_VALUES_OF_PARENT", propInputIds, propOutputVals) n = REQUEST("PROPERTY_VALUE_OF_PARENT", "id", type, dim1, dim2, propertyValues)

- R n = REQUEST("RADIAL_DIMENSION", "", format_string)

n = REQUEST("REFERENCE_LEVEL_DATA", "", name1, elev1, name2, elev2,

name3, elev3, name4, elev4) n = REQUEST("RGB_OF_MATERIAL", name, r, g, b) n = REQUEST("RGB_OF_PEN", penindex, r, g, b)

- S n = REQUEST("SILL_HEIGHT_DIMENSION", "", format_string) n = REQUEST("STORY", "", index, story_name)


n = REQUEST("STORY_INFO", expr, nStories, index1, name1, elev1, height1 [, index2, name2, ...])

n = REQUEST("STYLE_INFO", name, fontname [, size, anchor, face_or_slant]) n = REQUEST{3}("SUM_WITH_ROUNDING", req_name, addends_array, result)

- T n = REQUEST("TEXTBLOCK_INFO", textblock_name, width, height)