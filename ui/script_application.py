from __future__ import annotations

import re
from typing import Callable

from openbrep.gdl_sanitizer import sanitize_llm_script_output
from openbrep.hsf_project import GDLParameter, HSFProject


def parse_paramlist_text(text: str) -> list[GDLParameter]:
    """Parse simplified `Type Name = Value ! Description` parameter lines."""
    valid_types = {
        "Length", "Angle", "RealNum", "Integer", "Boolean",
        "String", "PenColor", "FillPattern", "LineType", "Material",
    }
    params: list[GDLParameter] = []
    for line in (text or "").splitlines():
        line = line.strip()
        if not line or line.startswith("!") or line.startswith("#"):
            continue
        match = re.match(r'(\w+)\s+(\w+)\s*=\s*(.+?)(?:\s*!\s*(.*))?$', line)
        if not match:
            continue
        ptype, pname, pval, pdesc = match.groups()
        if ptype in valid_types:
            params.append(GDLParameter(
                pname,
                ptype,
                (pdesc or "").strip(),
                pval.strip().strip('"'),
            ))
    return params


def sanitize_script_content(raw: str, fpath: str) -> str:
    """Best-effort sanitize to avoid narrative text leaking into script editors."""
    text = (raw or "").strip()
    if not text:
        return ""

    text = sanitize_llm_script_output(text, fpath)

    next_header = re.search(r"(?m)^\s*\[FILE:\s*.+?\]\s*$", text)
    if next_header:
        text = text[:next_header.start()].rstrip()

    if fpath.startswith("scripts/"):
        kept: list[str] = []
        prose_prefix = re.compile(r"^(分析|说明|原因|修复|结论|总结)\s*[:：]")
        numbered_md = re.compile(r"^\d+\.\s+")
        for line in text.splitlines():
            stripped = line.strip()
            if not stripped:
                kept.append(line)
                continue
            if stripped.startswith(("#", "##", "###", "- ", "* ", ">")):
                continue
            if numbered_md.match(stripped):
                continue
            if prose_prefix.match(stripped):
                continue
            kept.append(line)
        text = "\n".join(kept).strip()

    return text


def apply_scripts_to_project(
    proj: HSFProject,
    script_map: dict,
    *,
    session_state,
    script_entries: list[tuple[object, str, str]],
    stamp_script_header_fn: Callable[[str, str, int], str],
    parse_paramlist_text_fn: Callable[[str], list[GDLParameter]] = parse_paramlist_text,
    sanitize_script_content_fn: Callable[[str, str], str] = sanitize_script_content,
    clear_pending_preview_state_fn: Callable[[object], None] | None = None,
) -> tuple[int, int]:
    """Apply parsed LLM file changes to an HSF project and clear stale preview state."""
    label_map = {
        "scripts/3d.gdl": "3D",
        "scripts/2d.gdl": "2D",
        "scripts/1d.gdl": "Master",
        "scripts/vl.gdl": "Param",
        "scripts/ui.gdl": "UI",
        "scripts/pr.gdl": "Properties",
    }

    has_script_update = any(fpath in script_map for _, fpath, _ in script_entries)
    if has_script_update:
        session_state.script_revision = int(session_state.get("script_revision", 0)) + 1
    revision = int(session_state.get("script_revision", 0))

    script_count = 0
    for script_type, fpath, fallback_label in script_entries:
        if fpath not in script_map:
            continue
        cleaned = sanitize_script_content_fn(script_map[fpath], fpath)
        script_label = label_map.get(fpath, fallback_label)
        final = stamp_script_header_fn(script_label, cleaned, revision) if cleaned else ""
        proj.set_script(script_type, final)
        script_count += 1

    param_count = 0
    if "paramlist.xml" in script_map:
        new_params = parse_paramlist_text_fn(script_map["paramlist.xml"])
        if new_params:
            proj.parameters = new_params
            param_count = len(new_params)

    if script_count > 0 or param_count > 0:
        session_state.preview_2d_data = None
        session_state.preview_3d_data = None
        session_state.preview_warnings = []
        session_state.preview_meta = {"kind": "", "timestamp": ""}
        if clear_pending_preview_state_fn is not None:
            clear_pending_preview_state_fn(session_state)
        proj.save_to_disk()

    return script_count, param_count
