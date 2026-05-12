---
id: wiki.generated.built
type: wiki
category: other
commands: ["BUILT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### BUILT-IN PROPERTY GUIDE

Built-in properties are not part of GDL itself. When requesting available properties or property values of parent object, built-in properties (a specific type of properties that are defined by Archicad) have fix, human-readable property IDs. These property IDs can be written into GDL script, allowing the script to request these specific property values. For example determine the parent object's listed height by using PROPERTY_VALUES_OF_PARENT request to get the value of Builtin.General_Height property. See the Archicad User Guide at Component Listing Parameters in the Interactive Schedule for their definitions.

Compatibility: since the main purpose of these properties is to provide listing values for elements, their actual value might depend on the localization of Archicad, and their availability and way of calculation might be developed / changed in the later Archicad versions. They can be referenced directly with a string ID in the REQUEST commands that require a property ID:

- • PROPERTY_NAME
- • PROPERTY_VALUE_OF_PARENT
- • PROPERTY_VALUES_OF_PARENT
- • COMPONENT_PROPERTY_VALUES_OF_PARENT They are also returned by these the REQUEST commands:
- • PROPERTY_TREE_OF_PARENT
- • COMPONENT_PROPERTY_TREE_OF_PARENT

Element-related built-in property IDs

- • Builtin.General_3DLength (introduced in Archicad 25)
- • Builtin.General_3DPerimeter (introduced in Archicad 25)
- • Builtin.General_Area (introduced in Archicad 25)
- • Builtin.General_BottomElevationToFirstReferenceLevel (introduced in Archicad 25)


- • Builtin.General_BottomElevationToHomeStory (introduced in Archicad 25)
- • Builtin.General_BottomElevationToProjectZero (introduced in Archicad 25)
- • Builtin.General_BottomElevationToSeaLevel (introduced in Archicad 25)
- • Builtin.General_BottomElevationToSecondReferenceLevel (introduced in Archicad 25)
- • Builtin.General_ConditionalBottomSurfaceArea (introduced in Archicad 25)
- • Builtin.General_ConditionalTopSurfaceArea (introduced in Archicad 25)
- • Builtin.General_ConditionalVolume (introduced in Archicad 25)
- • Builtin.General_CrossSectionAreaAtBeginCut (introduced in Archicad 25)
- • Builtin.General_CrossSectionAreaAtEndCut (introduced in Archicad 25)
- • Builtin.General_CrossSectionHeightAtBeginCut (introduced in Archicad 25)
- • Builtin.General_CrossSectionHeightAtBeginPerpendicular (introduced in Archicad 25)
- • Builtin.General_CrossSectionHeightAtEndCut (introduced in Archicad 25)
- • Builtin.General_CrossSectionHeightAtEndPerpendicular (introduced in Archicad 25)
- • Builtin.General_CrossSectionWidthAtBeginCut (introduced in Archicad 25)
- • Builtin.General_CrossSectionWidthAtBeginPerpendicular (introduced in Archicad 25)
- • Builtin.General_CrossSectionWidthAtEndCut (introduced in Archicad 25)
- • Builtin.General_CrossSectionWidthAtEndPerpendicular (introduced in Archicad 25)
- • Builtin.General_ElementID (introduced in Archicad 25)
- • Builtin.General_ElevationToFirstReferenceLevel (introduced in Archicad 25)
- • Builtin.General_ElevationToProjectZero (introduced in Archicad 25)
- • Builtin.General_ElevationToSeaLevel (introduced in Archicad 25)
- • Builtin.General_ElevationToSecondReferenceLevel (introduced in Archicad 25)
- • Builtin.General_ElevationToStory (introduced in Archicad 25)
- • Builtin.General_FloorPlanHolesPerimeter (introduced in Archicad 25)
- • Builtin.General_FloorPlanPerimeter (introduced in Archicad 25)
- • Builtin.General_FromZone (introduced in Archicad 25)
- • Builtin.General_FromZoneNumber (introduced in Archicad 25)
- • Builtin.General_GrossVolume (introduced in Archicad 25)
- • Builtin.General_Height (introduced in Archicad 25)
- • Builtin.General_Holes3DPerimeter (introduced in Archicad 25)
- • Builtin.General_HomeOffset (introduced in Archicad 25)
- • Builtin.General_HotlinkAndElementID (introduced in Archicad 25)
- • Builtin.General_HotlinkMasterID (introduced in Archicad 25)


- • Builtin.General_InsulationSkinThickness (introduced in Archicad 25)
- • Builtin.General_LastIssueID (introduced in Archicad 25)
- • Builtin.General_LastIssueName (introduced in Archicad 25)
- • Builtin.General_LibraryPartName (introduced in Archicad 25)
- • Builtin.General_Locked (introduced in Archicad 25)
- • Builtin.General_NetBottomSurfaceArea (introduced in Archicad 25)
- • Builtin.General_NetEdgeSurfaceArea (introduced in Archicad 25)
- • Builtin.General_NetTopSurfaceArea (introduced in Archicad 25)
- • Builtin.General_NetVolume (introduced in Archicad 25)
- • Builtin.General_OpeningNumber (introduced in Archicad 25)
- • Builtin.General_OwnerID (introduced in Archicad 25)
- • Builtin.General_RelatedZoneName (introduced in Archicad 25)
- • Builtin.General_RelatedZoneNumber (introduced in Archicad 25)
- • Builtin.General_SlantAngle (introduced in Archicad 25)
- • Builtin.General_SurfaceArea (introduced in Archicad 25)
- • Builtin.General_Thickness (introduced in Archicad 25)
- • Builtin.General_ToZone (introduced in Archicad 25)
- • Builtin.General_ToZoneNumber (introduced in Archicad 25)
- • Builtin.General_TopElevationToFirstReferenceLevel (introduced in Archicad 25)
- • Builtin.General_TopElevationToHomeStory (introduced in Archicad 25)
- • Builtin.General_TopElevationToProjectZero (introduced in Archicad 25)
- • Builtin.General_TopElevationToSeaLevel (introduced in Archicad 25)
- • Builtin.General_TopElevationToSecondReferenceLevel (introduced in Archicad 25)
- • Builtin.General_TopLinkStory (introduced in Archicad 25)
- • Builtin.General_TopOffset (introduced in Archicad 25)
- • Builtin.General_Type (introduced in Archicad 25)
- • Builtin.General_UniqueID (introduced in Archicad 25)
- • Builtin.General_Width (introduced in Archicad 25)
- • Builtin.Zone_AreaReducement (introduced in Archicad 25)
- • Builtin.Zone_CalculatedArea (introduced in Archicad 25)
- • Builtin.Zone_ExtractedColumnArea (introduced in Archicad 25)
- • Builtin.Zone_ExtractedCurtainWallArea (introduced in Archicad 25)
- • Builtin.Zone_ExtractedFillArea (introduced in Archicad 25)


- • Builtin.Zone_ExtractedLowArea (introduced in Archicad 25)
- • Builtin.Zone_ExtractedWallArea (introduced in Archicad 25)
- • Builtin.Zone_FloorThickness (introduced in Archicad 25)
- • Builtin.Zone_MeasuredArea (introduced in Archicad 25)
- • Builtin.Zone_NetArea (introduced in Archicad 25)
- • Builtin.Zone_NetPerimeter (introduced in Archicad 25)
- • Builtin.Zone_Perimeter (introduced in Archicad 25)
- • Builtin.Zone_ReducedArea (introduced in Archicad 25)
- • Builtin.Zone_TotalExtractedArea (introduced in Archicad 25)
- • Builtin.Zone_WallInsetBackSideSurfaceArea (introduced in Archicad 25)
- • Builtin.Zone_WallInsetSideSurfaceArea (introduced in Archicad 25)
- • Builtin.Zone_WallInsetTopSurfaceArea (introduced in Archicad 25)
- • Builtin.Zone_WallsPerimeter (introduced in Archicad 25)
- • Builtin.Zone_ZoneCategory (introduced in Archicad 25)
- • Builtin.Zone_ZoneCategoryCode (introduced in Archicad 25)
- • Builtin.Zone_ZoneName (introduced in Archicad 25)
- • Builtin.Zone_ZoneNumber (introduced in Archicad 25)
- • Builtin.Design_Option_Name (introduced in Archicad 27)
- • Builtin.Design_Option_ID (introduced in Archicad 27)
- • Builtin.Design_Option_Set_Name (introduced in Archicad 27)

Component-related built-in property IDs

- • Builtin.Component_ConditionalProjectedArea (introduced in Archicad 25)
- • Builtin.Component_ConditionalVolume (introduced in Archicad 25)
- • Builtin.Component_CrossSectionArea (introduced in Archicad 25)
- • Builtin.Component_CrossSectionHeight (introduced in Archicad 25)
- • Builtin.Component_CrossSectionWidth (introduced in Archicad 25)
- • Builtin.Component_GrossProjectedArea (introduced in Archicad 25)
- • Builtin.Component_GrossVolume (introduced in Archicad 25)
- • Builtin.Component_NetProjectedArea (introduced in Archicad 25)
- • Builtin.Component_NetVolume (introduced in Archicad 25)
- • Builtin.Component_Thickness (introduced in Archicad 25)


## INDEX