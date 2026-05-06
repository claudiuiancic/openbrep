---
type: concept
status: stable
tags: [globals, context, project-info, view, scale, environment]
aliases: [GLOBALS, global variables, GLOB_SCALE, GLOB_VIEW_TYPE, SYMB_POS_X, WALL_THICKNESS]
source: official:gdl.graphisoft.com/reference-guide/global-variables
---

# GLOBALS

GDL global variables are built-in variables supplied by Archicad. They expose view, project, placement, host element, and environment context to a library part.

Modern GDL does not require a `GLOBALS list_of_variables` declaration before reading global variables. Use the official global variable names directly.

## Common Useful Globals

```gdl
GLOB_SCALE
GLOB_VIEW_TYPE
GLOB_PREVIEW_MODE
GLOB_FEEDBACK_MODE
GLOB_SEO_TOOL_MODE
SYMB_POS_X
SYMB_POS_Y
SYMB_ROTANGLE
WALL_THICKNESS
WALL_HEIGHT
```

## Recommended OpenBrep Use

- Use `GLOB_SCALE` in 2D script when symbol detail should change with drawing scale.
- Use `GLOB_VIEW_TYPE`, `GLOB_PREVIEW_MODE`, `GLOB_FEEDBACK_MODE`, and `GLOB_SEO_TOOL_MODE` for display context decisions.
- Use wall globals only in door/window/wall-end contexts where the host wall exists.
- Avoid view-dependent globals in parameter scripts and master scripts that run as parameter scripts.
- Prefer explicit parameters for object dimensions; globals should adapt display or host-specific behavior, not replace normal parameters.

## Examples

### Scale-sensitive 2D display

```gdl
IF GLOB_SCALE <= 50 THEN
    LINE2 0, B * 0.9, A, B * 0.9
ENDIF
```

### Feedback-mode simplification

```gdl
IF GLOB_FEEDBACK_MODE THEN
    RESOL 12
ELSE
    RESOL gs_resol
ENDIF
```

### Wall thickness fallback

```gdl
IF WALL_THICKNESS > 0 THEN
    _depth = WALL_THICKNESS
ELSE
    _depth = B
ENDIF
```

## Edge Cases & Traps

- Do not invent a `GLOBALS SYMBOL` declaration. This is not the modern way to access context.
- `GLOB_CONTEXT` is deprecated; prefer `GLOB_VIEW_TYPE` combined with preview, feedback, and SEO mode globals.
- View-dependent globals can produce warnings or dummy defaults in parameter scripts.
- Some host-element globals only contain useful values in compatible host contexts.
- Global variable availability can vary by Archicad version and script type.

## Related

- [[Object_Types]] — choosing object behavior by library part subtype and host context
- [[IF_ENDIF]] — branching on global values
- [[Paramlist_XML]] — keeping explicit dimensions parameter-driven
