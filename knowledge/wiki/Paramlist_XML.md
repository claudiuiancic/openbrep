---
type: concept
status: stable
tags: [parameters, xml, types, configuration, paramlist, hsf]
aliases: [paramlist, parameters xml, paramlist.xml, gdl parameters, HSF parameters]
source: openbrep:paramlist_builder.py
---

# Paramlist_XML

`paramlist.xml` is the HSF parameter definition file for a GDL library part. OpenBrep treats it as part of source state together with `scripts/*.gdl`.

Generated GDL must keep script variable names and `paramlist.xml` parameter names exactly aligned.

## OpenBrep HSF Format

OpenBrep writes the LP_XMLConverter-style HSF format:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ParamSection>
    <ParamSectHeader>
        ...
    </ParamSectHeader>
    <Parameters SectVersion="27" SectionFlags="0" SubIdent="0">
        <Length Name="A">
            <Description><![CDATA["Width"]]></Description>
            <Fix/>
            <Value>1</Value>
        </Length>
    </Parameters>
</ParamSection>
```

Do not generate simplified `<PARAMETERS>` / `<PARAMETER>` XML for OpenBrep HSF projects.

## Supported Type Tags

Use the exact HSF type tags supported by OpenBrep:

```text
Length
Angle
RealNum
Integer
Boolean
String
PenColor
FillPattern
LineType
Material
Title
Separator
```

Common aliases in user-facing text must be normalized before writing XML:

| User-facing name | HSF type tag |
|---|---|
| Real | `RealNum` |
| Pen | `PenColor` |
| Fill | `FillPattern` |
| Line | `LineType` |

## Recommended OpenBrep Use

- Use `Length A`, `Length B`, and `Length ZZYZX` for primary dimensions.
- Keep `A`, `B`, and `ZZYZX` fixed with `<Fix/>`.
- Store `Length` values in meters.
- Store `Angle` values in degrees.
- Store `Boolean` values as `0` or `1`.
- Store `Material`, `FillPattern`, and `LineType` as integer attribute indices, not string names.
- Put user-facing labels in `<Description><![CDATA["..."]]></Description>`.

## LLM Output Format

When an LLM returns a `paramlist.xml` block to OpenBrep, prefer the compact line format that OpenBrep parses:

```text
Length A = 1.2 ! Width
Length B = 0.4 ! Depth
Length ZZYZX = 2.1 ! Height
Material mat_body = 0 ! Body surface
Boolean has_back_panel = 1 ! Back panel
```

OpenBrep converts that line format into HSF XML.

## Edge Cases & Traps

- `Float` and `Text` are not valid OpenBrep HSF type tags; use `RealNum` and `String`.
- `Material`, `FillPattern`, and `LineType` values must be numeric indices in HSF XML.
- Duplicate parameter names are invalid for reliable generation.
- A script reference that is missing from `paramlist.xml` is an undefined variable risk.
- Do not include units like `mm` in parameter names; convert dimensions to meters in values.
- Do not generate standalone XML unless the caller explicitly asks for raw HSF XML.

## Related

- [[MATERIAL]] — using material parameters
- [[HOTSPOT2]] — linking graphical editing to parameters
- [[IF_ENDIF]] — branching on Boolean parameters
