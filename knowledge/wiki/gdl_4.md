---
id: wiki.generated.gdl
type: wiki
category: other
commands: ["GDL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### GDL CREATED FROM THE FLOOR PLAN

Saving the floor plan as a GDL script or library part will result GDL elements. You can use these GDL scripts as templates for your custom library parts.

#### GDL DATA I/O ADD-ON

The GDL Data In/Out Add-On allows you to access a simple kind of database by using GDL commands. Otherwise this Add-On is similar to the GDL Text In/Out Add-On.

#### GDL DATETIME ADD-ON

The DateTime extension allows you to set various formats for the current date and time set on your computer. The Add-On works the same way the GDL file operations. You have to open a channel, read the information and close the channel. This Add-On is also available by using the REQUEST GDL command, in which case the sequence of commands OPEN, INPUT and CLOSE is called internally. This is the simplest way to obtain the date/time information, with just a single GDL command line: REQUEST ("DATETIME", format_string, datetimestring) The second parameter of the Request function is the same as that described in the OPEN function paramstring parameter.

#### GDL FILE MANAGER I/O ADD-ON

The GDL File Manager In-Out Add-On allows you to scan a folder for the contained files/subfolders from a GDL script. Specify the folder you would like to scan by using the OPEN command. Get the first/next file/folder name in the specified folder by using the INPUT command. Finish folder scanning by using the CLOSE command.

#### GDL TEXT I/O ADD-ON

The GDL Text In/Out Add-On allows you to open external text files for reading/writing and to manipulate them by putting/getting values from/to GDL scripts. This Add-On interprets the strings on the parameter list of the OPEN, INPUT, OUTPUT commands from the GDL script. The created files are placed in a subfolder of the application data folder if it is given by a relative path. The folder can contain subfolders where the extension will look for existing files. It can read and write TEXT type files.