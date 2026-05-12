---
id: wiki.generated.scripting
type: wiki
category: other
commands: ["SCRIPTING"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### SCRIPTING

Library Part Structure Every library part described with GDL has scripts, which are lists of the actual GDL commands that construct the 3D shape and the 2D symbol. Library parts also have a description for quantity calculations. Master script commands will be executed before each script.

- The 2D script contains parametric 2D drawing description. The binary 2D data of the library part (content of the 2D symbol window) can be referenced using the FRAGMENT2 command. If the 2D script is empty, the binary 2D data will be used to display the library part on the floor plan.
- The 3D script contains a parametric 3D model description. The binary 3D data (which is generated during an import or export operation) can be referenced using the BINARY command.


The Properties script contains components and descriptors used in element, component and zone lists. The binary properties data described in the components and descriptors section of the library part can be referenced using the BINARYPROP command. If the properties script and the master script are empty, the binary properties data will be used during the list process.

The User Interface script allows the user to define input pages that can be used to edit the parameter values in place of the normal parameter list. In the Parameter script, sets of possible values can be defined for the library part parameters. The parameter set in the Parameters section are used as defaults in the library part settings when placing the library part on the plan. In the Forward Migration script you can define the conversion logic which can convert placed instances of older elements. In the Backward Migration script you can define a backward conversion to an older version of an element. The Preview picture is displayed in the library part settings dialog box when browsing the active library. It can be referenced by the PICTURE and PICTURE2 commands from the 3D and 2D script. Archicad provides a helpful environment to write GDL scripts, with on-the-fly visualization, syntax and error checking. Analyze, Deconstruct and Simplify

No matter how complex, most objects you wish to create can be broken down into building blocks of simple geometric shapes. Always start with a simple analysis of the desired object and define all the geometric units that compose it. These building blocks can then be translated into the vocabulary of the GDL scripting language. If your analysis was accurate, the combination of these entities will form the desired object. To make the analysis, you need to have a good perception of space and at least a basic knowledge of descriptive geometry.

Window representations with different levels of sophistication

To avoid getting discouraged early on in the learning process, start with objects of defined dimensions and take them to their simplest but still recognizable form. As you become familiar with basic modeling, you can increase the level of sophistication and get closer to the ideal form. Ideal does not necessarily mean complicated. Depending on the nature of the architectural project, the ideal library part could vary from basic to refined. The window on the left in the above illustration fits the style of a design visualization perfectly. The window on the right gives a touch of realism and detail which can be used later in the construction documents phase of the project.