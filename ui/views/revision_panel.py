from __future__ import annotations

import hashlib
from typing import Callable

from openbrep.hsf_project import HSFProject
from openbrep.revisions import get_latest_revision_id, list_revisions


def render_revision_panel(
    st,
    proj: HSFProject,
    *,
    is_generation_locked_fn: Callable[[], bool],
    save_revision_fn: Callable[[HSFProject, str, str | None], tuple[bool, str]],
    restore_revision_fn: Callable[[HSFProject, str], tuple[bool, str]],
) -> None:
    with st.expander(“🕘 Version History”, expanded=True):
        project_root_text = str(getattr(proj, “root”, “”) or “”)
        project_key = hashlib.sha1(project_root_text.encode(“utf-8”)).hexdigest()[:10]
        notice_key = f”revision_project_{project_key}_notice”
        active_hsf_source_dir = str(st.session_state.get(“active_hsf_source_dir”, “”) or “”).strip()
        if active_hsf_source_dir:
            st.caption(f”Current HSF source directory: `{active_hsf_source_dir}`”)
        st.checkbox(
            “Auto-save version on successful compile”,
            key=”revision_auto_snapshot”,
            help=”Saves a snapshot of HSF source files; compiled .gsm artifacts are not saved”,
        )
        revision_message = st.text_input(
            “Version note”,
            value=””,
            placeholder=”e.g. Adjust shelf thickness / stable version before compile”,
            key=f”revision_project_{project_key}_message_input”,
            disabled=is_generation_locked_fn(),
        )

        save_col, refresh_col = st.columns([1.2, 1.0])
        with save_col:
            if st.button(
                “Save Version”,
                key=”revision_save_button”,
                width=”stretch”,
                disabled=is_generation_locked_fn(),
            ):
                ok, msg = save_revision_fn(
                    proj,
                    revision_message,
                    st.session_state.get(“pending_gsm_name”) or proj.name,
                )
                st.session_state[notice_key] = msg
                if ok:
                    st.toast(“Version saved”, icon=”✅”)
                st.rerun()
        with refresh_col:
            if st.button(“Refresh History”, key=”revision_refresh_button”, width=”stretch”):
                st.rerun()

        notice = st.session_state.get(notice_key, “”) or st.session_state.pop(“revision_notice”, “”)
        if notice:
            if notice.startswith(“✅”):
                st.success(notice)
            else:
                st.error(notice)

        try:
            revisions = list_revisions(proj.root)
            latest_revision = get_latest_revision_id(proj.root)
        except Exception as exc:
            revisions = []
            latest_revision = None
            st.caption(f”No versions available: {exc}”)

        if not revisions:
            st.caption(“No versions yet. Click \”Save Version\” to start tracking history.”)
            return

        revision_by_label = {
            _format_revision_option(revision): revision
            for revision in reversed(revisions)
        }
        selected_revision = st.selectbox(
            “Version History”,
            options=list(revision_by_label.keys()),
            key=f”revision_project_{project_key}_restore_select”,
            help=”Select a version to view its note or restore it”,
        )
        selected_meta = revision_by_label.get(selected_revision)
        if selected_meta:
            latest_mark = “ · Latest” if selected_meta.revision_id == latest_revision else “”
            st.caption(
                f”{selected_meta.project_name} / {selected_meta.gsm_name} · “
                f”{selected_meta.created_at}{latest_mark} · “
                f”{len(selected_meta.files)} source files”
            )
            if selected_meta.message:
                st.caption(f”Note: {selected_meta.message}”)

        if st.button(
            “Restore This Version”,
            key=”revision_restore_button”,
            width=”stretch”,
            disabled=is_generation_locked_fn(),
        ):
            revision_id = selected_meta.revision_id if selected_meta else “”
            ok, msg = restore_revision_fn(proj, revision_id)
            st.session_state[notice_key] = msg
            if ok:
                st.toast(“Version restored”, icon=”✅”)
            st.rerun()


def _format_revision_option(revision) -> str:
    return f"{revision.revision_id} · {revision.gsm_name}"
