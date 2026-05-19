## Column Naming Convention

- Structural column: prefix `STR_COL_`
- Architectural column: prefix `ARC_COL_`
- Decorative column: prefix `DEC_COL_`

## Common Column Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| col_width | Length | 0.4 | Column width |
| col_depth | Length | 0.4 | Column depth |
| col_height | Length | 3.0 | Column height |
| col_offset | Length | 0.0 | Base offset |

## Column GDL Templates

```gdl
! Rectangular column
BLOCK -col_width/2, -col_depth/2, col_offset,
      col_width, col_depth, col_height
```

```gdl
! Circular column
CYLIND 0, 0, col_width/2, col_width/2, col_height
```
