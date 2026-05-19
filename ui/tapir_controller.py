from __future__ import annotations

from typing import Callable


def reload_libraries_after_compile(*, tapir_import_ok: bool, get_bridge_fn: Callable[[], object]) -> tuple[bool, str] | None:
    """Reload Archicad libraries after a successful real GSM compile."""
    if not tapir_import_ok:
        return False, "⚪ Tapir bridge not imported — compiled successfully but Archicad library was not auto-reloaded."

    bridge = get_bridge_fn()
    if not bridge.is_available():
        return False, "⚪ Archicad is not running or Tapir is not installed — library was not auto-reloaded."

    if bridge.reload_libraries():
        return True, "🔄 Archicad notified to reload library — switch to Archicad to open the just-compiled GSM."

    return False, "⚠️ Compiled successfully, but Tapir failed to reload the Archicad library — please reload it manually in Archicad."


def tapir_sync_selection(*, tapir_import_ok: bool, get_bridge_fn: Callable[[], object], session_state, now_text_fn: Callable[[], str]) -> tuple[bool, str]:
    if not tapir_import_ok:
        return False, "Tapir bridge not imported"

    bridge = get_bridge_fn()
    if not bridge.is_available():
        session_state.tapir_last_error = "Archicad is not running or Tapir is not installed"
        return False, session_state.tapir_last_error

    guids = bridge.get_selected_elements()
    session_state.tapir_selected_guids = guids
    session_state.tapir_last_sync_at = now_text_fn()

    if not guids:
        session_state.tapir_selected_details = []
        session_state.tapir_selected_params = []
        session_state.tapir_param_edits = {}
        session_state.tapir_last_error = ""
        return True, "No objects selected"

    details = bridge.get_details_of_elements(guids)
    session_state.tapir_selected_details = details
    session_state.tapir_last_error = ""
    return True, f"Synced {len(guids)} object(s)"


def tapir_highlight_selection(*, tapir_import_ok: bool, get_bridge_fn: Callable[[], object], session_state) -> tuple[bool, str]:
    if not tapir_import_ok:
        return False, "Tapir bridge not imported"

    bridge = get_bridge_fn()
    if not bridge.is_available():
        session_state.tapir_last_error = "Archicad is not running or Tapir is not installed"
        return False, session_state.tapir_last_error

    guids = session_state.get("tapir_selected_guids") or []
    if not guids:
        return False, "Please sync selected objects first"

    ok = bridge.highlight_elements(guids)
    if not ok:
        session_state.tapir_last_error = "Highlight failed"
        return False, session_state.tapir_last_error

    session_state.tapir_last_error = ""
    return True, f"Highlighted {len(guids)} object(s)"


def tapir_load_selected_params(*, tapir_import_ok: bool, get_bridge_fn: Callable[[], object], session_state) -> tuple[bool, str]:
    if not tapir_import_ok:
        return False, "Tapir bridge not imported"

    bridge = get_bridge_fn()
    if not bridge.is_available():
        session_state.tapir_last_error = "Archicad is not running or Tapir is not installed"
        return False, session_state.tapir_last_error

    guids = session_state.get("tapir_selected_guids") or []
    if not guids:
        return False, "Please sync selected objects first"

    rows = bridge.get_gdl_parameters_of_elements(guids)
    if not rows:
        session_state.tapir_selected_params = []
        session_state.tapir_param_edits = {}
        session_state.tapir_last_error = "No editable parameters found (selection may contain non-GDL elements)"
        return False, session_state.tapir_last_error

    selected_params = []
    edit_map = {}
    skipped = 0

    for row in rows:
        if not isinstance(row, dict):
            skipped += 1
            continue
        guid = (row.get("guid") or "").strip()
        if not guid:
            element_id = row.get("elementId")
            if isinstance(element_id, dict):
                gid = element_id.get("guid")
                if isinstance(gid, str):
                    guid = gid.strip()
        if not guid:
            skipped += 1
            continue

        params = row.get("gdlParameters")
        if not isinstance(params, list):
            skipped += 1
            continue

        normalized_params = []
        for p in params:
            if not isinstance(p, dict):
                continue
            normalized_params.append(dict(p))

        if not normalized_params:
            skipped += 1
            continue

        selected_params.append({
            "guid": guid,
            "gdlParameters": normalized_params,
        })

        for p in normalized_params:
            name = p.get("name")
            if not isinstance(name, str) or not name.strip():
                continue
            key = f"{guid}::{name.strip()}"
            value = p.get("value")
            edit_map[key] = "" if value is None else str(value)

    session_state.tapir_selected_params = selected_params
    session_state.tapir_param_edits = edit_map

    if not selected_params:
        session_state.tapir_last_error = "No editable parameters found (all elements may be non-GDL)"
        return False, session_state.tapir_last_error

    if skipped > 0:
        session_state.tapir_last_error = f"Skipped {skipped} element(s) with unreadable parameters"
        return True, f"Read parameters for {len(selected_params)} object(s) (skipped {skipped})"

    session_state.tapir_last_error = ""
    return True, f"Read parameters for {len(selected_params)} object(s)"


def tapir_apply_param_edits(*, tapir_import_ok: bool, get_bridge_fn: Callable[[], object], session_state) -> tuple[bool, str]:
    if not tapir_import_ok:
        return False, "Tapir bridge not imported"

    bridge = get_bridge_fn()
    if not bridge.is_available():
        session_state.tapir_last_error = "Archicad is not running or Tapir is not installed"
        return False, session_state.tapir_last_error

    rows = session_state.get("tapir_selected_params") or []
    if not rows:
        return False, "No parameters to apply — please read parameters first"

    edits = session_state.get("tapir_param_edits") or {}
    payload_rows = []
    conversion_errors = []

    for row in rows:
        guid = (row.get("guid") or "").strip()
        params = row.get("gdlParameters")
        if not guid or not isinstance(params, list):
            continue

        out_params = []
        for p in params:
            if not isinstance(p, dict):
                continue
            name = p.get("name")
            if not isinstance(name, str) or not name.strip():
                continue
            key = f"{guid}::{name.strip()}"
            raw_new = edits.get(key, "")
            old_val = p.get("value")

            parsed_value = raw_new
            if isinstance(old_val, bool):
                txt = str(raw_new).strip().lower()
                if txt in {"1", "true", "yes", "on"}:
                    parsed_value = True
                elif txt in {"0", "false", "no", "off"}:
                    parsed_value = False
                else:
                    conversion_errors.append(f"{guid}::{name}（Boolean）")
                    continue
            elif isinstance(old_val, int) and not isinstance(old_val, bool):
                try:
                    parsed_value = int(str(raw_new).strip())
                except Exception:
                    conversion_errors.append(f"{guid}::{name}（Integer）")
                    continue
            elif isinstance(old_val, float):
                try:
                    parsed_value = float(str(raw_new).strip())
                except Exception:
                    conversion_errors.append(f"{guid}::{name}（RealNum）")
                    continue
            else:
                parsed_value = str(raw_new)

            out_params.append({"name": name.strip(), "value": parsed_value})

        if out_params:
            payload_rows.append({"guid": guid, "gdlParameters": out_params})

    if not payload_rows:
        if conversion_errors:
            session_state.tapir_last_error = f"Parameter conversion failed: {', '.join(conversion_errors[:6])}"
            return False, session_state.tapir_last_error
        return False, "No parameters to write back"

    result = bridge.set_gdl_parameters_of_elements(payload_rows)
    execution_results = []
    if isinstance(result, dict):
        maybe = result.get("executionResults")
        if isinstance(maybe, list):
            execution_results = [r for r in maybe if isinstance(r, dict)]

    if not execution_results:
        session_state.tapir_last_error = "Tapir returned no execution results"
        return False, session_state.tapir_last_error

    fail_idx = [i for i, r in enumerate(execution_results) if r.get("success") is not True]
    if fail_idx:
        fail_guids = []
        for idx in fail_idx:
            if idx < len(payload_rows):
                fail_guids.append(payload_rows[idx].get("guid", ""))
        fail_text = ", ".join([g for g in fail_guids if g]) or "unknown object"
        session_state.tapir_last_error = f"Partial write-back failed: {fail_text}"
        suffix = f"; {len(conversion_errors)} parameter conversion error(s)" if conversion_errors else ""
        return False, session_state.tapir_last_error + suffix

    session_state.tapir_last_error = ""
    suffix = f" ({len(conversion_errors)} conversion error(s) skipped)" if conversion_errors else ""
    return True, f"Parameters applied to {len(payload_rows)} object(s){suffix}"
