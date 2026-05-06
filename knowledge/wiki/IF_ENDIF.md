---
type: concept
status: stable
tags: [control-flow, conditional, branch, if, endif, elsif, else]
aliases: [IF, ENDIF, ELSIF, ELSE, conditional, branch, gdl if]
source: official:gdl.graphisoft.com/reference-guide/flow-control-statements
---

# IF_ENDIF

`IF`/`ENDIF` is GDL's conditional branching construct. It evaluates a condition and executes the corresponding block when the result is true.

## Why Conditionals?

Parametric objects need to adapt. A window might have 2 or 3 panels depending on a parameter. A chair might or might not have armrests. `IF`/`ENDIF` lets a single GDL object produce multiple variants from one set of parameters.

GDL conditions are expression-based. Comparison and logical operators are valid in conditions, and the generated branch is chosen from the expression result.

## Official Syntax

```gdl
IF expression THEN
    ! code to execute when expression ≠ 0
ENDIF
```

With alternatives:

```gdl
IF expression THEN
    ! expression ≠ 0
ELSE
    ! expression = 0
ENDIF
```

Chained:

```gdl
IF expr1 THEN
    ! expr1 ≠ 0
ELSIF expr2 THEN
    ! expr1 = 0 and expr2 ≠ 0
ELSE
    ! both = 0
ENDIF
```

## Examples

### Parameter-based visibility

```gdl
! Show armrests only when the parameter says so
IF hasArms THEN
    ADD 0, 0, seatH
    BLOCK A, 0.05, 0.15
    DEL 1
ENDIF
```

### Multiple cases

```gdl
IF nPanels = 1 THEN
    GOSUB "DrawSinglePanel"
ELSIF nPanels = 2 THEN
    GOSUB "DrawDoublePanel"
ELSE
    GOSUB "DrawTriplePanel"
ENDIF
```

### Numeric comparison idiom

```gdl
! Comparison operators are valid in GDL conditions
IF A > B THEN
    BLOCK 1, 1, 1
ENDIF
```

### Combined conditions

```gdl
! Logical operators are valid in GDL conditions
IF hasArms AND hasBack THEN
    ! both conditions are true
ENDIF
```

## Edge Cases & Traps

- **True/false behavior**: conditions still behave like numeric truth values in practice; zero is false and non-zero is true.
- **Comparison operators**: use the normal comparison operators in the condition.
- **Logical operators**: use `AND`, `OR`, and `EXOR` when combining conditions.
- **ELSIF vs ELSEIF**: the keyword is `ELSIF` (one word), not `ELSEIF`.
- **ENDIF, not END IF**: it's a single keyword.
- **THEN is required** on the `IF` line.
- **Performance**: conditionals in the 3D script are evaluated every time the view refreshes. Keep heavy computation in the Master script or Parameter script.
- **Nesting**: GDL supports nesting IF/ENDIF up to reasonable depths (tested to ~50 levels). Use indentation to maintain readability:

```gdl
IF cond1 THEN
    IF cond2 THEN
        IF cond3 THEN
            ! deep conditional
        ENDIF
    ENDIF
ENDIF
```

## Related

- [[FOR_NEXT]] — iteration (the loop counterpart)
- [[ADD_DEL]] — conditional geometry positioning
- [[PRISM_]] — typically wrapped in conditionals
