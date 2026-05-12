---
id: wiki.generated.strings
type: wiki
category: string
commands: ["STRINGS"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### STRINGS

Any string of Unicode characters that is placed between quotation marks (", ', “, ’, `, ´), or any string of characters without quotation marks that does not figure in the script as an identifier with a given value (macro call, attribute name, file name). Strings without quotation marks will be converted to all caps, so using quotation marks is recommended. The maximum length allowed in a string is 255 characters.

The '\' character has special control values. Its meaning depends on the next character.

\\ '\' char itself \n new line \t tabulator \new line continue string in next line without a new line \others not correct, results in warning

- Example 1:

"This is a string" `washbasin 1'-6"*1'-2` 'Do not use different delimiters’

Localized strings use special syntax. They start with _( characters and end with ). Compatibility: introduced in Archicad 25.

- Example 2:


_("This is a localized string") _('This is another localized string')