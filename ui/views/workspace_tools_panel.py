from __future__ import annotations

import re
from typing import Callable

from openbrep.hsf_project import HSFProject
from openbrep.learning import ErrorLearningStore
from ui.chat_history_actions import close_chat_record_browser


def render_workspace_tools_panel(
    st,
    proj: HSFProject,
    *,
    tapir_import_ok: bool,
    get_bridge_fn: Callable[[], object],
) -> None:
    _render_project_action_buttons(st, proj)
    _render_memory_privacy_panel(st)


def render_preview_workbench(
    st,
    proj: HSFProject,
    *,
    run_preview_fn: Callable[[HSFProject, str], tuple[bool, str]],
    render_preview_2d_fn: Callable[[object], None],
    render_preview_3d_fn: Callable[[object], None],
) -> None:
    st.markdown("### Preview")
    preview_2d, preview_3d = st.columns(2)
    with preview_2d:
        if st.button("👁️ Preview 2D", width="stretch", help="Run 2D subset interpreter and display the result"):
            close_chat_record_browser(st.session_state)
            ok, msg = run_preview_fn(proj, "2d")
            if ok:
                st.toast(msg, icon="✅")
            else:
                st.error(msg)

    with preview_3d:
        if st.button("🧊 Preview 3D", width="stretch", help="Run 3D subset interpreter and display the result"):
            close_chat_record_browser(st.session_state)
            ok, msg = run_preview_fn(proj, "3d")
            if ok:
                st.toast(msg, icon="✅")
            else:
                st.error(msg)

    _render_preview_panel(st, render_preview_2d_fn=render_preview_2d_fn, render_preview_3d_fn=render_preview_3d_fn)


def _render_tapir_controls(st, *, tapir_import_ok: bool, get_bridge_fn: Callable[[], object]) -> None:
    st.divider()
    st.markdown("#### Archicad Live Link")
    if not tapir_import_ok:
        st.caption("Tapir Python dependency not installed; live link is unavailable.")
        return

    bridge = get_bridge_fn()
    tapir_ok = bridge.is_available()
    if not tapir_ok:
        st.caption("⚪ Archicad is not running or Tapir is not installed; skipping live test")
        return

    ac_col1, ac_col2 = st.columns([2, 3])
    with ac_col1:
        if st.button(
            "🏗️ Test in Archicad",
            width="stretch",
            help="Trigger Archicad to reload the library and capture GDL runtime errors back into chat",
        ):
            st.session_state.tapir_test_trigger = True
            st.rerun()
    with ac_col2:
        st.caption("✅ Archicad + Tapir connected")

    p0_b1, p0_b2, p0_b3, p0_b4 = st.columns(4)
    with p0_b1:
        if st.button("Read Selection", width="stretch", help="Sync the currently selected library object from Archicad"):
            st.session_state.tapir_selection_trigger = True
            st.rerun()
    with p0_b2:
        if st.button("Highlight Object", width="stretch", help="Highlight the current object in Archicad"):
            st.session_state.tapir_highlight_trigger = True
            st.rerun()
    with p0_b3:
        if st.button("Read Params", width="stretch", help="Read current object parameters from Archicad"):
            st.session_state.tapir_load_params_trigger = True
            st.rerun()
    with p0_b4:
        can_apply = bool(st.session_state.get("tapir_selected_params"))
        if st.button("Write Params", width="stretch", disabled=not can_apply, help="Write the values from the parameter workbench back to Archicad"):
            st.session_state.tapir_apply_params_trigger = True
            st.rerun()


def _render_project_action_buttons(st, proj: HSFProject) -> None:
    if st.button(
        "🧠 Consolidate Error Notes",
        width="stretch",
        help="Consolidate the current workspace error notes into a self-hint that will be injected into future generation runs",
    ):
        result = ErrorLearningStore(st.session_state.work_dir).summarize_to_skill(
            project_name=proj.name,
        )
        if result.ok:
            st.success(result.message)
            st.caption(str(result.path))
        else:
            st.info(result.message)


def _render_memory_privacy_panel(st) -> None:
    st.divider()
    st.markdown("#### Memory & Privacy")

    store = ErrorLearningStore(st.session_state.work_dir)
    status = store.memory_status()
    st.caption(
        "OpenBrep saves chat records, error notes, and consolidated Skills in the current workspace "
        "to help avoid previously encountered issues in future generation runs."
    )
    st.caption(f"Storage location: `{status.memory_root}`")

    metric_1, metric_2, metric_3 = st.columns(3)
    metric_1.metric("Chats", status.chat_count)
    metric_2.metric("Error Notes", status.lesson_count)
    metric_3.metric("Skill", "Generated" if status.has_learned_skill else "Not generated")

    if st.session_state.get("confirm_clear_memory"):
        st.warning("Confirm clearing the current workspace memory? HSF projects, compiled outputs, and version snapshots will not be deleted.")
        ok_col, cancel_col, _ = st.columns([1, 1, 3])
        with ok_col:
            if st.button("Confirm Clear Memory", type="primary", key="clear_memory_confirm_button"):
                before = store.clear_memory()
                st.session_state.confirm_clear_memory = False
                st.toast(
                    f"Memory cleared: {before.chat_count} chats, {before.lesson_count} error notes",
                    icon="✅",
                )
                st.rerun()
        with cancel_col:
            if st.button("Cancel", key="clear_memory_cancel_button"):
                st.session_state.confirm_clear_memory = False
                st.rerun()
        return

    disabled = (
        status.chat_count == 0
        and status.lesson_count == 0
        and not status.has_learned_skill
        and status.total_bytes == 0
    )
    if st.button(
        "Clear Workspace Memory",
        width="stretch",
        disabled=disabled,
        help="Delete persistent chats, error notes, and consolidated Skills in the current workspace without affecting project source files.",
    ):
        st.session_state.confirm_clear_memory = True
        st.rerun()


def _render_preview_panel(
    st,
    *,
    render_preview_2d_fn: Callable[[object], None],
    render_preview_3d_fn: Callable[[object], None],
) -> None:
    preview_meta = st.session_state.get("preview_meta") or {}
    preview_kind = preview_meta.get("kind", "")
    preview_time = preview_meta.get("timestamp", "")
    title = f"Latest Preview: {preview_kind} · {preview_time}" if preview_kind else "Preview Panel (2D / 3D)"
    has_preview = bool(
        st.session_state.get("preview_2d_data")
        or st.session_state.get("preview_3d_data")
        or st.session_state.get("preview_warnings")
    )

    with st.expander(title, expanded=has_preview):
        tab_specs = ["2D", "3D", "Warnings"]
        if str(preview_kind).upper() == "3D":
            tab_specs = ["3D", "2D", "Warnings"]
        tabs = dict(zip(tab_specs, st.tabs(tab_specs)))
        with tabs["2D"]:
            render_preview_2d_fn(st.session_state.get("preview_2d_data"))
        with tabs["3D"]:
            render_preview_3d_fn(st.session_state.get("preview_3d_data"))
        with tabs["Warnings"]:
            _render_preview_warnings(st)


def _render_preview_warnings(st) -> None:
    warnings = st.session_state.get("preview_warnings") or []
    if not warnings:
        st.caption("No warnings.")
        return

    for warning in warnings:
        text = re.sub(r"^line\s+(\d+):", r"3d.gdl:L\1", str(warning))
        st.warning(text)
