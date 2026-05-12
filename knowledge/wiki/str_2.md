---
id: wiki.generated.str_2
type: wiki
category: string
commands: ["STR{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### STR{2}

STR{2} (format_string, numeric_expression [, extra_accuracy_string])

This function creates a formatted string representation of the current value of the numeric expression. Formatting is specified by format_string which can either be a variable or a string literal. If the format is empty, the output is formatted as meters, with an accuracy of three decimals (displaying 0s). If the extra accuracy flags are set in the format_string, the STR{2} function will return the corresponding extra accuracy string in the 3rd parameter.

format_string: "%[0 or more flags][field_width][.precision] conv_spec" flags: (for m, mm, cm, dm, e, df, di, sqm, sqcm, sqf, sqi, dd, gr, rad, cum, l, cucm, cumm, cuf, cui, cuy, gal):

(none): right justify (default),

-: left justify,

+: explicit plus sign, (space): in place of a + sign,

- '*0': extra accuracy Off (default),
- '*1': extra accuracy .5,
- '*2': extra accuracy .25,


- '*3': extra accuracy .1,
- '*4': extra accuracy .01,
- '*5': rounding to .5 within displayed decimal range, no returned extra accuracy string, (used for area calculations),
- '*6': rounding to .25 within displayed decimal range, no returned extra accuracy string, (used for area calculations),
- '*7': fills the fractional part of numeric_expression into the extra_accuracy_string in case of fi or ffi, while the returned expression of the function does not contain the fractional parts, '#': don’t display 0s (for m, mm, cm, dm, ffi, fdi, fi, df, di, sqm, sqcm, sqf, sqi, dd, fr, rad, cum, l, cucm, cumm, cuf, cui, cuy, gal), '0': display 0 inches (for ffi, fdi, fi), '~': hide 0 decimals (effective only if the '#' flag is not specified) (for m, mm, cm, dm, fdi, df, di, sqm, sqcm, sqf, sqi, dd, fr, rad, cum, l, cucm, cumm, cuf, cui, cuy, gal), '^': do not change decimal separator and digit grouping characters (if not specified, these characters will be replaced as set in the current system). '[1*j1+2*j2+4*j3]': display 0 inches before fractions, effective if the '0' flag is not specified (for ffi, fdi, fi) j1: display 0 inches before fractions (0 3/4"), effective when value is smaller than 1 foot and not displaying 0 foot (the '#' flag is specified) j2: display 0 whole inches after feet (1'-0"), effective when value is at least 1 foot j3: display 0 inches before fractions (1'-0 3/4"), effective when value is at least 1 foot


field_width: unsigned decimal integer, the minimum number of characters to generate. precision: unsigned decimal integer, the number of fraction digits to generate. conv_spec: (conversion specifier):

e: exponential format (meter),

- m: meters, mm: millimeters, cm: centimeters,


- dm: decimeters, Compatibility: decimeters introduced in Archicad 22.

ffi: feet & fractional inches, fdi: feet & decimal inches, df: decimal feet, fi: fractional inches,

- di: decimal inches, pt: points,


for areas: sqm: square meters, sqcm: square centimeters, sqmm: square millimeters, sqf: square feet, sqi: square inches, for angles:

dd: decimal degrees, dms: degrees, minutes, seconds, gr: grads, rad: radians, surv: surveyors unit, for volumes:

cum: cubic meters, l: liters, cucm: cubic centimeters, cumm: cubic millimeters, cuf: cubic feet, cui: cubic inches, cuy: cubic yards, gal: gallons.

nr = 0.345678 TEXT2 0, 23, STR{2} ("%m", nr) !0.346 TEXT2 0, 22, STR{2} ("%#10.2m", nr) !35 TEXT2 0, 21, STR{2} ("%.4cm", nr) !34.5678 TEXT2 0, 20, STR{2} ("%12.4cm", nr) ! 34.5678 TEXT2 0, 19, STR{2} ("%.6mm", nr) !345.678000 TEXT2 0, 18, STR{2} ("%+15e", nr) !+3.456780e-01 TEXT2 0, 17, STR{2} ("%ffi", nr) !1'-2" TEXT2 0, 16, STR{2} ("%0.16ffi", nr) !1'-1 5/8" TEXT2 0, 15, STR{2} ("% .3fdi", nr) ! 1'-1.609" TEXT2 0, 14, STR{2} ("% -10.4df", nr) ! 1.1341' TEXT2 0, 13, STR{2} ("%0.64fi", nr) !13 39/64" TEXT2 0, 12, STR{2} ("%+12.4di", nr) !+13.6094" TEXT2 0, 11, STR{2} ("%#.3sqm", nr) !346 TEXT2 0, 10, STR{2} ("%+sqcm", nr) !+3,456.78 TEXT2 0, 9, STR{2} ("% .2sqmm", nr) ! 345,678.00 TEXT2 0, 8, STR{2} ("%-12sqf", nr) !3.72 TEXT2 0, 7, STR{2} ("%10sqi", nr) ! 535.80 TEXT2 0, 6, STR{2} ("%.2pt", nr) !0.35

alpha = 88.657 TEXT2 0, 5, STR{2} ("%+10.3dd", alpha) !+88.657° TEXT2 0, 4, STR{2} ("%.1dms", alpha) !88°39'

- TEXT2 0, 3, STR{2} ("%.2dms", alpha) !88°39'25"


- TEXT2 0, 2, STR{2} ("%10.4gr", alpha) ! 98.5078G


- TEXT2 0, 1, STR{2} ("%rad", alpha) !1.55R TEXT2 0, 0, STR{2} ("%.2surv", alpha) !N 1°20'35" E


- nr = 0'-0 3/4"

- TEXT2 0, -1, STR{2} ("%#[1].16ffi", nr) !0 3/4"

nr = 1'-0"

- TEXT2 0, -2, STR{2} ("%[2].16ffi", nr) !1'-0" nr = 1'-0 3/4"
- TEXT2 0, -3, STR{2} ("%[4].16ffi", nr) !1'-0 3/4"

! use system digit separators, default nr = 1234.5678

- TEXT2 0, -4, STR{2} ("%8.6m", nr) !1 234,5678 ! ignore system digit separators
- TEXT2 0, -5, STR{2} ("%^8.6m", nr) !1234.5678 nr = 0.34278
- TEXT2 0, -6, STR{2} ("%*5 .4m", nr) ! 0.3430

! split to integral and fractional parts extra_accuracy_string = "" nr = 1'-0 3/4"

- TEXT2 0, -7, STR{2}("%*7.16ffi", nr, extra_accuracy_string) !1'-
- TEXT2 0, -8, extra_accuracy_string !3/4" nr = -0.07
- TEXT2 0, -9, STR{2} ("%*1.1", nr, extra_accuracy_string) !-0,0
- TEXT2 0, -10, extra_accuracy_string !5