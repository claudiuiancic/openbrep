---
id: wiki.generated.file_dependence
type: wiki
category: other
commands: ["FILE_DEPENDENCE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### FILE_DEPENDENCE

FILE_DEPENDENCE "name1" [, "name2", ...] You can give a list of external files on which your GDL script depends on. File names should be constant strings.

All files specified here will be included in the archive project (like constant macro names used in CALL statements and constant picture names used in various GDL commands). The command works on this level only: if the specified files are library parts, their called macro files will not be included.

The command can be useful in cases when external files are referenced at custom places in the GDL script, for example: ADDITIONAL_DATA file parameters, data files in file operations.

## NON-GEOMETRIC SCRIPTS

In addition to the 3D and 2D script windows that define the appearance of the GDL Object, further scripts are available for adding complementary information to it. These are the Properties Script used for quantity calculations, the Parameter Script that includes the list of possible values for different parameters, and the User Interface Script for creating a custom interface for parameter entry, Forward Migration Script and Backward Migration Scripts to define how to migrate an old instance forward to the actual element or how to migrate the element backward to an older one. The commands available for all these script types are detailed on the following pages.