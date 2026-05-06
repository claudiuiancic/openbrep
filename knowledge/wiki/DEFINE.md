---
type: concept
status: stable
tags: [attribute, define, material, fill, line-type, style, texture]
aliases: [DEFINE, DEFINE MATERIAL, DEFINE FILL, DEFINE LINE_TYPE, DEFINE STYLE, inline attribute definition]
source: official:gdl.graphisoft.com/reference-guide/inline-attribute-definition
---

# DEFINE

`DEFINE` is not a GDL subroutine mechanism. In official GDL syntax, `DEFINE` belongs to inline attribute definition: surfaces, fills, line types, styles, textures, and related attributes.

For reusable script blocks, use labels with `GOSUB` / `RETURN`, not `DEFINE name ... END`.

## Official DEFINE Family

Common commands include:

```gdl
DEFINE MATERIAL name type, surface_red, surface_green, surface_blue
DEFINE MATERIAL name [,] BASED_ON orig_name [,] PARAMETERS name1 = expr1 [, ...]
DEFINE FILL name [[,] FILLTYPES_MASK fill_types,] ...
DEFINE LINE_TYPE name spacing, n, length1, ..., lengthn
DEFINE STYLE name font_family, size, anchor, face_code
DEFINE TEXTURE name expression, x, y, mask, angle
```

## Reusable GDL Code Pattern

Use labels and `GOSUB`:

```gdl
GOSUB "draw_leg"
ADD A - leg_w, 0, 0
GOSUB "draw_leg"
DEL 1
END

"draw_leg":
    BLOCK leg_w, leg_d, leg_h
RETURN
```

## Recommended OpenBrep Use

- Do not generate `DEFINE name [param] ... END` for reusable geometry.
- Prefer `GOSUB` labels for small repeated code blocks.
- Prefer parameters in `paramlist.xml` for user-editable materials instead of defining new project attributes.
- Use `DEFINE MATERIAL` only when the generated object intentionally needs an inline surface definition.
- Keep inline attribute definitions before the first use of the defined attribute.

## Edge Cases & Traps

- `DEFINE` is an attribute keyword, not a function or class declaration.
- `END` ends script execution or blocks in specific contexts; it is not the closing keyword for a `DEFINE` subroutine.
- `GOSUB` blocks should end with `RETURN`.
- Inline attributes can be local to the script context and may not behave like project attributes in every script.
- Hard-coded inline attributes reduce project portability; material parameters are usually safer for OpenBrep-generated objects.

## Related

- [[MATERIAL]] — applying a surface to following 3D geometry
- [[Paramlist_XML]] — defining editable material parameters
- [[Transformation_Stack]] — positioning repeated geometry blocks
