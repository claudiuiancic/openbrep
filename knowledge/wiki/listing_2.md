---
id: wiki.generated.listing
type: wiki
category: other
commands: ["LISTING"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### LISTING OF REQUESTS

- A

n = REQUEST("ANCESTRY_INFO", expr, name [, guid, parent_name1, parent_guid1,

... parent_namen, parent_guidn)

n = REQUEST("ANGULAR_DIMENSION", "", format_string) n = REQUEST("ANGULAR_LENGTH_DIMENSION", "", format_string) n = REQUEST("AREA_DIMENSION", "", format_string) n = REQUEST("ASSOCEL_PROPERTIES", parameter_string, nr_data, data) n = REQUEST("ASSOCLP_NAME", "", name) n = REQUEST("ASSOCLP_PARVALUE", expr, name_or_index, type, flags, dim1, dim2, p_values) n = REQUEST("ASSOCLP_PARVALUE_WITH_DESCRIPTION", expr, name_or_index, type,

flags, dim1, dim2, p_values_and_descriptions) n = REQUEST("AUTOTEXT_LIST", "", autoTextListArray)

- B n = REQUEST{2}("BUILDING_MATERIAL_INFO", name_or_index, param_name, value_or_values)
- C n = REQUEST("CALC_ANGLE_UNIT", "", format_string) n = REQUEST("CALC_AREA_UNIT", "", format_string) n = REQUEST("CALC_LENGTH_UNIT", "", format_string) n = REQUEST("CALC_VOLUME_UNIT", "", format_string)


- n = REQUEST("CLASS_OF_FILL", index, class) n = REQUEST("CLEAN_INTERSECTIONS", "", state) n = REQUEST("COMPONENT_IDS_OF_PARENT", collectComponents, outputCompIds) n = REQUEST("COMPONENT_PROJECTED_AREA", idxSkin, projectedArea) n = REQUEST("COMPONENT_PROPERTIES_OF_PARENT", propertyType, parentComponentProperties) n = REQUEST("COMPONENT_PROPERTY_TREE_OF_PARENT", propTreeInput, propTreeOutput) n = REQUEST("COMPONENT_PROPERTY_VALUES_OF_PARENT", compPropInput, compPropVals) n = REQUEST("COMPONENT_VOLUME", idxSkin, skinVolume) n = REQUEST("CONFIGURATION_NUMBER", "", stConfigurationNumber) n = REQUEST("CONSTR_FILLS_DISPLAY", "", optionVal) n = REQUEST("CUSTOM_AUTO_LABEL", "", name)
- D n = REQUEST("DATETIME", format_string, datetimestring) n = REQUEST("DOOR_SHOW_DIM", "", show)
- E n = REQUEST("ELEVATION_DIMENSION", "", format_string)
- F n = REQUEST("FLOOR_PLAN_OPTION", "", storyViewpointType) n = REQUEST("FONTNAMES_LIST", "", fontnames) n = REQUEST("FULL_ID_OF_PARENT", "", id_string)


- G n = REQUEST("GSID_INFO", "", userId, organizationIds)
- H n = REQUEST("HEIGHT_OF_STYLE", name, height [, descent, leading]) n = REQUEST("HOMEDB_INFO", "", homeDBIntId, homeDBUserId, homeDBName, homeContext) n = REQUEST("HOME_STORY", "", index, story_name) n = REQUEST("HOME_STORY_OF_OPENING", "", index, story_name)
- I n = REQUEST("ID_OF_MAIN", "", id_string) n = REQUEST("INTERNAL_ID", "", id)


- K n = REQUEST("KEYNOTE_FOLDER_TREE", keynoteFolderTreeInput, keynoteFolderTreeOutput) n = REQUEST("KEYNOTE_INFO", keynoteInfoInput, keynoteInfoOutput)
- L n = REQUEST("LAYOUT_LENGTH_UNIT", "", format_string) n = REQUEST("LAYOUT_TEXT_SIZE_UNIT", "", format_string) n = REQUEST("LEVEL_DIMENSION", "", format_string) n = REQUEST("LINEAR_DIMENSION", "", format_string)
- M n = REQUEST("MATCHING_PROPERTIES", type, name1, name2, ...)


n = REQUEST{2}("MATERIAL_INFO", name_or_index, param_name, value_or_values) n = REQUEST("MEP_PIPE_FLEXIBLE_SEGMENT_GEOMETRY", InputParameters,

FlexibleSegmentGeometry) n = REQUEST("MEP_ROUTE_ATTRIBUTES", InputAttributes, MEPRouteAttributes) n = REQUEST("MODEL_LENGTH_UNIT", "", format_string) n = REQUEST("MODEL_TEXT_SIZE_UNIT", "", format_string)

- N n = REQUEST("NAME_OF_BUILDING_MATERIAL", index, name) n = REQUEST("NAME_OF_FILL", index, name) n = REQUEST("NAME_OF_LINE_TYPE", index, name) n = REQUEST("NAME_OF_LISTED", "", name) n = REQUEST("NAME_OF_MACRO", "", my_name) n = REQUEST("NAME_OF_MAIN", "", main_name) n = REQUEST("NAME_OF_MATERIAL", index, name) n = REQUEST("NAME_OF_PLAN", "", name) n = REQUEST("NAME_OF_PROFILE", index, name) n = REQUEST("NAME_OF_PROGRAM", "", program_name) n = REQUEST("NAME_OF_STYLE", index, name)