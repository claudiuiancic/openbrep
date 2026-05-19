from __future__ import annotations

from typing import Callable


def render_tapir_inspector_panel(*, session_state, caption_fn: Callable[[str], None], warning_fn: Callable[[str], None], info_fn: Callable[[str], None], markdown_fn: Callable[[str], None], code_fn: Callable[[str, str], None], json_fn: Callable[[object], None]) -> None:
    guids = session_state.get("tapir_selected_guids") or []
    details = session_state.get("tapir_selected_details") or []
    last_sync = session_state.get("tapir_last_sync_at", "")
    last_error = session_state.get("tapir_last_error", "")

    if last_sync:
        caption_fn(f"Last synced: {last_sync}")
    if last_error:
        warning_fn(last_error)

    if not guids:
        info_fn("No Archicad selection found. Click \"Read Selection\" in the Archicad Live Link section on the left first.")
        return

    markdown_fn(f"**{len(guids)} selected object(s) loaded**")
    code_fn("\n".join(guids), "text")

    markdown_fn("**Object Details**")
    if details:
        json_fn(details)
    else:
        caption_fn("No element details available.")


def render_tapir_param_workbench_panel(*, session_state, info_fn: Callable[[str], None], expander_fn: Callable[..., object], text_input_fn: Callable[..., str]) -> None:
    rows = session_state.get("tapir_selected_params") or []
    if not rows:
        info_fn("No writable parameters available. Click \"Read Params\" in the Archicad Live Link section on the left first.")
        return

    edits = session_state.get("tapir_param_edits") or {}
    object_count = len(rows)
    param_count = sum(
        len(row.get("gdlParameters") or [])
        for row in rows
        if isinstance(row.get("gdlParameters"), list)
    )
    info_fn(f"Loaded {object_count} object(s) with {param_count} parameter(s). After editing, click \"Write Params\" on the left to write back to Archicad.")
    for row in rows:
        guid = (row.get("guid") or "").strip()
        params = row.get("gdlParameters")
        if not guid or not isinstance(params, list):
            continue

        with expander_fn(f"Object {guid} · {len(params)} parameters", expanded=object_count == 1):
            for p in params:
                if not isinstance(p, dict):
                    continue
                name = p.get("name")
                if not isinstance(name, str) or not name.strip():
                    continue
                key = f"{guid}::{name.strip()}"
                current_value = edits.get(key, "")
                p_type = p.get("type", "")
                label = name.strip()
                if p_type:
                    label = f"{label} ({p_type})"
                new_val = text_input_fn(label, value=str(current_value), key=f"tapir_edit::{key}")
                edits[key] = new_val

    session_state.tapir_param_edits = edits
