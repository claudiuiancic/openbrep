from __future__ import annotations

import re


def check_gdl_script(content: str, script_type: str = "") -> list:
    issues = []
    if not content.strip():
        if script_type == "2d":
            issues.append("⚠️ 2D script is empty — must contain at least PROJECT2 3, 270, 2")
        return issues

    lines = content.splitlines()

    if_multi = sum(
        1 for line in lines
        if re.search(r"\bIF\b", line, re.I)
        and re.search(r"\bTHEN\s*$", line.strip(), re.I)
    )
    endif_count = sum(1 for line in lines if re.match(r"\s*ENDIF\b", line, re.I))
    if if_multi != endif_count:
        issues.append(f"⚠️ IF/ENDIF mismatch: {if_multi} multi-line IF(s), {endif_count} ENDIF(s)")

    for_count = sum(1 for line in lines if re.match(r"\s*FOR\b", line, re.I))
    next_count = sum(1 for line in lines if re.match(r"\s*NEXT\b", line, re.I))
    if for_count != next_count:
        issues.append(f"⚠️ FOR/NEXT mismatch: {for_count} FOR(s), {next_count} NEXT(s)")

    add_count = sum(1 for line in lines if re.match(r"\s*ADD(X|Y|Z)?\b", line, re.I))
    del_count = sum(1 for line in lines if re.match(r"\s*DEL\b", line, re.I))
    if add_count != del_count:
        issues.append(f"⚠️ ADD/DEL mismatch: {add_count} ADD/ADDX/ADDY/ADDZ, {del_count} DEL(s)")

    if any(line.strip().startswith("```") for line in lines):
        issues.append("⚠️ Script contains ``` markers — AI formatting artifact; please remove all backtick lines")

    if script_type == "3d":
        _check_3d_termination(lines, issues)

    if script_type == "2d":
        has_proj = any(
            re.search(r"\bPROJECT2\b|\bRECT2\b|\bPOLY2\b", line, re.I)
            for line in lines
        )
        if not has_proj:
            issues.append("⚠️ 2D script is missing a floor-plan projection statement (PROJECT2 / RECT2)")

    assigned = set(re.findall(r"\b(_[A-Za-z]\w*)\s*=", content))
    used = set(re.findall(r"\b(_[A-Za-z]\w*)\b", content))
    undefined = used - assigned
    if undefined:
        issues.append(
            f"ℹ️ Variable(s) {', '.join(sorted(undefined))} are not assigned in this script — "
            "safe to ignore if defined in the Master script, otherwise ArchiCAD may not render the object at runtime"
        )

    if not issues:
        issues = ["✅ Checks passed"]
    return issues


def _check_3d_termination(lines: list[str], issues: list[str]) -> None:
    sub_label_pat = re.compile(r'^\s*"[^"]+"\s*:')
    has_subs = any(sub_label_pat.match(line) for line in lines)

    if not has_subs:
        last_non_empty = next((line.strip() for line in reversed(lines) if line.strip()), "")
        if not re.match(r"^END\s*$", last_non_empty, re.I):
            issues.append("⚠️ The last line of the 3D script must be END")
        return

    main_body = []
    for line in lines:
        if sub_label_pat.match(line):
            break
        main_body.append(line)
    last_main = next((line.strip() for line in reversed(main_body) if line.strip()), "")
    if not re.match(r"^END\s*$", last_main, re.I):
        issues.append("⚠️ The last line of the 3D main body (before the first subroutine) must be END")

    current_sub = None
    sub_lines: list[str] = []
    for line in lines:
        if sub_label_pat.match(line):
            if current_sub and sub_lines:
                last_sub = next((item.strip() for item in reversed(sub_lines) if item.strip()), "")
                if not re.match(r"^RETURN\s*$", last_sub, re.I):
                    issues.append(f"⚠️ Subroutine {current_sub} should end with RETURN, not END")
            current_sub = line.strip()
            sub_lines = []
        else:
            sub_lines.append(line)

    if current_sub and sub_lines:
        last_sub = next((item.strip() for item in reversed(sub_lines) if item.strip()), "")
        if not re.match(r"^RETURN\s*$", last_sub, re.I):
            issues.append(f"⚠️ Subroutine {current_sub} should end with RETURN")
