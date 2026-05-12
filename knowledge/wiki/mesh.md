---
id: wiki.generated.mesh
type: wiki
category: 3d
commands: ["MESH"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### MESH

MESH a, b, m, n, mask, z11, z12, ..., z1m, z21, z22, ..., z2m, ... zn1, zn2, ..., znm

A simple smooth mesh based on a rectangle with an equidistant net. The sides of the base rectangle are a and b; the m and n points are along the x and y axes respectively; zij is the height of the node. Masking:

Z

Zij

Y

n

j

b

1

m

X

1

i

a

mask: mask = j1 + 4*j3 + 16*j5 + 32*j6 + 64*j7, where each j can be 0 or 1. j1: base surface is present,

j3: side surfaces are present,

- j5: base and side edges are visible,
- j6: top edges are visible,
- j7: top edges are visible, top surface is not smooth.


Restriction of parameters:

- m >= 2, n >= 2


- Example 1:

MESH 50, 30, 5, 6, 1+4+16+32+64, 2, 4, 6, 7, 8, 10, 3, 4, 5, 6, 7, 9, 5, 5, 7, 8, 10, 9, 4, 5, 6, 7, 9, 8, 2, 4, 5, 6, 8, 6

- Example 2:


MESH 90, 100, 12, 8, 1+4+16+32+64,

- 17,16,15,14,13,12,11,10,10,10,10, 9, 16,14,13,11,10, 9, 9, 9,10,10,12,10, 16,14,12,11, 5, 5, 5, 5, 5,11,12,11, 16,14,12,11, 5, 5, 5, 5, 5,11,12,12, 16,14,12,12, 5, 5, 5, 5, 5,11,12,12, 16,14,12,12, 5, 5, 5, 5, 5,11,13,14, 17,17,15,13,12,12,12,12,12,12,15,15,
- 17,17,15,13,12,12,12,12,13,13,16,16