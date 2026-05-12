---
id: wiki.generated.ui_style
type: wiki
category: other
commands: ["UI_STYLE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### UI_STYLE

UI_STYLE fontsize, face_code All the UI_OUTFIELDs and UI_INFIELDs generated after this keyword will represent this style until the next UI_STYLE statement. fontsize: one of the following font size values:

- 0: small,
- 1: extra small,
- 2: large.


face_code: similar to the DEFINE STYLE command, but the values cannot be used in combination. 0: normal, 1: bold, 2: italic, 4: underline.