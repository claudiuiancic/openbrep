from __future__ import annotations

from typing import Callable

from ui.project_activity import project_activity_entries
from ui.proposed_preview_controller import clear_pending_preview_state

from openbrep.hsf_project import HSFProject


PROJECT_ACTIVITY_MAX_HEIGHT = 180


SCRIPT_HELP = {
    "scripts/3d.gdl": (
        "**3D Script** — Defines three-dimensional geometry; the solid bodies displayed in ArchiCAD's 3D window.\n\n"
        "- Use commands such as `PRISM_`, `BLOCK`, `SPHERE`, `CONE`, `REVOLVE` to model geometry\n"
        "- `ADD` / `DEL` manage coordinate-system transformations and must appear in matched pairs\n"
        "- `FOR` / `NEXT` loops are used for repeated elements (e.g. gratings, shelves)\n"
        "- **The last line must be `END`**, otherwise compilation will fail"
    ),
    "scripts/2d.gdl": (
        "**2D Script** — Floor-plan symbols; the lines displayed in ArchiCAD's floor-plan view.\n\n"
        "- **Must contain** `PROJECT2 3, 270, 2` (minimal projection) or custom 2D linework\n"
        "- Omitting it or leaving it empty will make the object invisible in floor plans"
    ),
    "scripts/1d.gdl": (
        "**Master Script** — The master control script; runs first before all other scripts.\n\n"
        "- Global variable initialization, parameter coupling logic\n"
        "- Simple objects usually do not need this script"
    ),
    "scripts/vl.gdl": (
        "**Param Script** — Parameter validation script; triggered when parameter values change.\n\n"
        "- Parameter range constraints, derived parameter calculations\n"
        "- Simple objects usually do not need this script"
    ),
    "scripts/ui.gdl": (
        "**UI Script** — Custom parameter interface; defines the control layout in ArchiCAD's Object Settings dialog.\n\n"
        "- If omitted, ArchiCAD automatically generates a default parameter list interface"
    ),
    "scripts/pr.gdl": (
        "**Properties Script** — BIM attribute output; defines IFC property sets and element attributes.\n\n"
        "- Can be left empty if no BIM data output is required"
    ),
}


def render_script_editor_panel(
    st,
    proj: HSFProject,
    *,
    script_map: list[tuple[object, str, str]],
    editor_version: int,
    ace_available: bool,
    st_ace_fn,
    main_editor_state_key_fn: Callable[[str, int], str],
    fullscreen_editor_dialog_fn: Callable[[object, str, str], None],
    editor_height: int = 420,
) -> None:
    st.markdown("### GDL Script Editor")
    script_tabs = st.tabs([label for _, _, label in script_map])

    for tab, (script_type, fpath, label) in zip(script_tabs, script_map):
        with tab:
            help_col, fullscreen_col = st.columns([6, 1])
            with help_col:
                with st.expander(f"ℹ️ {label} Script Info"):
                    st.markdown(SCRIPT_HELP.get(fpath, ""))
            with fullscreen_col:
                if st.button("⛶", key=f"fs_{fpath}_v{editor_version}", help="Fullscreen edit", width="stretch"):
                    fullscreen_editor_dialog_fn(script_type, fpath, label)

            current_code = proj.get_script(script_type) or ""
            editor_key = main_editor_state_key_fn(fpath, editor_version)

            if ace_available:
                raw_ace = st_ace_fn(
                    value=current_code,
                    language="fortran",
                    theme="monokai",
                    height=editor_height,
                    font_size=13,
                    tab_size=2,
                    show_gutter=True,
                    show_print_margin=False,
                    wrap=False,
                    key=editor_key,
                )
                pending_keys = st.session_state.get("_ace_pending_main_editor_keys", set())
                if editor_key in pending_keys and current_code and raw_ace in (None, ""):
                    new_code = current_code
                else:
                    if editor_key in pending_keys and (raw_ace is not None or not current_code):
                        pending_keys.discard(editor_key)
                        st.session_state._ace_pending_main_editor_keys = pending_keys
                    new_code = raw_ace if raw_ace is not None else current_code
            else:
                new_code = st.text_area(
                    label,
                    value=current_code,
                    height=editor_height,
                    key=editor_key,
                    label_visibility="collapsed",
                ) or ""

            if new_code != current_code:
                proj.set_script(script_type, new_code)
                _clear_preview_state(st.session_state)

    _render_project_activity_log(st)


def _clear_preview_state(session_state) -> None:
    session_state.preview_2d_data = None
    session_state.preview_3d_data = None
    session_state.preview_warnings = []
    session_state.preview_meta = {"kind": "", "timestamp": ""}
    clear_pending_preview_state(session_state)


def _render_project_activity_log(st) -> None:
    entries = project_activity_entries(st.session_state)
    if not entries:
        return

    st.divider()
    with st.expander(f"Import / Load Log ({len(entries)})", expanded=False):
        with st.container(height=PROJECT_ACTIVITY_MAX_HEIGHT, border=True):
            for idx, entry in enumerate(reversed(entries)):
                timestamp = str(entry.get("timestamp", "")).strip()
                message = str(entry.get("message", "")).strip()
                if timestamp:
                    st.caption(timestamp)
                st.markdown(message)
                if idx < len(entries) - 1:
                    st.divider()
