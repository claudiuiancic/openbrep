from __future__ import annotations

import base64
from typing import Callable

from ui.chat_render import render_assistant_block, render_user_bubble
from ui.chat_history_actions import (
    build_chat_record_entries,
    close_chat_record_browser,
    delete_chat_record_entry,
    sanitize_hsf_name,
    suggest_hsf_name_from_chat_record,
)
from ui.project_activity import is_project_activity_message


def render_chat_panel(
    st,
    *,
    is_generation_locked_fn: Callable[[object], bool],
    extract_gsm_name_candidate_fn: Callable[[str], str | None],
    thumb_image_bytes_fn: Callable[[str], bytes | None],
    copyable_chat_text_fn: Callable[[dict], str],
    copy_text_to_system_clipboard_fn: Callable[[str], tuple[bool, str]],
    is_bridgeable_explainer_message_fn: Callable[[dict], bool],
    extract_gdl_from_text_fn: Callable[[str], dict],
    capture_last_project_snapshot_fn: Callable[[str], None],
    apply_scripts_to_project_fn: Callable[[object, dict], tuple[int, int]],
    bump_main_editor_version_fn: Callable[[], int],
    create_project_fn: Callable[[str], object],
    validate_chat_image_size_fn: Callable[[bytes, str], str | None],
) -> dict:
    st.markdown("### AI Assistant (Generation & Debug)")
    _render_header(st)
    _render_chat_record_launcher(
        st,
        extract_gdl_from_text_fn=extract_gdl_from_text_fn,
        extract_gsm_name_candidate_fn=extract_gsm_name_candidate_fn,
        capture_last_project_snapshot_fn=capture_last_project_snapshot_fn,
        apply_scripts_to_project_fn=apply_scripts_to_project_fn,
        bump_main_editor_version_fn=bump_main_editor_version_fn,
        create_project_fn=create_project_fn,
        copy_text_to_system_clipboard_fn=copy_text_to_system_clipboard_fn,
    )
    _render_chat_history(
        st,
        thumb_image_bytes_fn=thumb_image_bytes_fn,
        copyable_chat_text_fn=copyable_chat_text_fn,
        copy_text_to_system_clipboard_fn=copy_text_to_system_clipboard_fn,
        is_bridgeable_explainer_message_fn=is_bridgeable_explainer_message_fn,
    )
    _render_adopt_dialog(
        st,
        extract_gdl_from_text_fn=extract_gdl_from_text_fn,
        capture_last_project_snapshot_fn=capture_last_project_snapshot_fn,
        apply_scripts_to_project_fn=apply_scripts_to_project_fn,
        bump_main_editor_version_fn=bump_main_editor_version_fn,
    )
    live_output = st.empty()
    active_debug_mode = _render_route_controls(st)
    payload = _read_chat_input(st, is_generation_locked_fn=is_generation_locked_fn)
    payload["live_output"] = live_output
    payload["active_debug_mode"] = active_debug_mode
    _decode_chat_attachment(st, payload, validate_chat_image_size_fn=validate_chat_image_size_fn)
    return payload


def _render_header(st) -> None:
    st.caption("Describe your requirements — the AI will automatically create a GDL object and write it to the editor.")


def _render_chat_record_launcher(
    st,
    *,
    extract_gdl_from_text_fn: Callable[[str], dict],
    extract_gsm_name_candidate_fn: Callable[[str], str | None],
    capture_last_project_snapshot_fn: Callable[[str], None],
    apply_scripts_to_project_fn: Callable[[object, dict], tuple[int, int]],
    bump_main_editor_version_fn: Callable[[], int],
    create_project_fn: Callable[[str], object],
    copy_text_to_system_clipboard_fn: Callable[[str], tuple[bool, str]],
) -> None:
    history = st.session_state.get("chat_record_history") or []
    entries = build_chat_record_entries(history, classify_code_blocks_fn=extract_gdl_from_text_fn)
    if not entries:
        return

    if st.button(f"📚 Chat History ({len(entries)})", key="chat_record_browser_button", width="stretch"):
        st.session_state.chat_record_browser_open = True
        st.rerun()

    if st.session_state.get("chat_record_browser_open") or st.session_state.get("chat_record_open_idx") is not None:
        _render_chat_record_dialog(
            st,
            extract_gdl_from_text_fn=extract_gdl_from_text_fn,
            extract_gsm_name_candidate_fn=extract_gsm_name_candidate_fn,
            capture_last_project_snapshot_fn=capture_last_project_snapshot_fn,
            apply_scripts_to_project_fn=apply_scripts_to_project_fn,
            bump_main_editor_version_fn=bump_main_editor_version_fn,
            create_project_fn=create_project_fn,
            copy_text_to_system_clipboard_fn=copy_text_to_system_clipboard_fn,
        )


def _apply_chat_record_to_editor(
    *,
    st,
    msg_idx: int,
    extracted: dict,
    hsf_name: str,
    create_project_fn: Callable[[str], object],
    capture_last_project_snapshot_fn: Callable[[str], None],
    apply_scripts_to_project_fn: Callable[[object, dict], tuple[int, int]],
    bump_main_editor_version_fn: Callable[[], int],
    save_as_hsf: bool,
) -> tuple[bool, str]:
    if not extracted:
        return False, "No injectable code blocks found"

    project = st.session_state.get("project")
    safe_name = sanitize_hsf_name(hsf_name, fallback="chat_hsf")
    if save_as_hsf or project is None:
        if project is not None:
            capture_last_project_snapshot_fn("Chat record save")
        project = create_project_fn(safe_name)
        st.session_state.project = project
        st.session_state.pending_gsm_name = safe_name
        st.session_state.script_revision = 0
    else:
        capture_last_project_snapshot_fn("Chat record inject")

    applied_scripts, applied_params = apply_scripts_to_project_fn(project, extracted)
    if save_as_hsf:
        project.save_to_disk()
    bump_main_editor_version_fn()
    st.session_state.chat_record_open_idx = None
    st.session_state.adopted_msg_index = msg_idx
    label = "Saved and injected" if save_as_hsf else "Injected into editor"
    return True, f"✅ {label}: {applied_scripts} script(s), {applied_params} parameter group(s)"


def _return_to_chat_record_list(st) -> None:
    st.session_state.chat_record_open_idx = None
    st.session_state.chat_record_delete_idx = None
    st.rerun()


def _close_chat_record_browser(st) -> None:
    close_chat_record_browser(st.session_state)
    st.rerun()


def _render_chat_record_dialog(
    st,
    *,
    extract_gdl_from_text_fn: Callable[[str], dict],
    extract_gsm_name_candidate_fn: Callable[[str], str | None],
    capture_last_project_snapshot_fn: Callable[[str], None],
    apply_scripts_to_project_fn: Callable[[object, dict], tuple[int, int]],
    bump_main_editor_version_fn: Callable[[], int],
    create_project_fn: Callable[[str], object],
    copy_text_to_system_clipboard_fn: Callable[[str], tuple[bool, str]],
) -> None:
    idx = st.session_state.get("chat_record_open_idx")
    history = st.session_state.get("chat_record_history") or []
    entries = build_chat_record_entries(history, classify_code_blocks_fn=extract_gdl_from_text_fn)
    if not entries:
        st.session_state.chat_record_browser_open = False
        st.session_state.chat_record_open_idx = None
        st.session_state.chat_record_delete_idx = None
        return

    if idx is not None and not (0 <= idx < len(history)):
        st.session_state.chat_record_open_idx = None
        idx = None

    @st.dialog("📚 Chat History")
    def _dialog() -> None:
        delete_idx = st.session_state.get("chat_record_delete_idx")
        if delete_idx is not None:
            _render_chat_record_delete_confirm(
                st,
                delete_idx=delete_idx,
                history=history,
            )
            return

        selected_idx = st.session_state.get("chat_record_open_idx")
        if selected_idx is None:
            st.caption("Browse and open any chat record to copy it, inject it into the editor, or save it as HSF.")
            with st.container(height=420, border=True):
                for entry in reversed(entries):
                    row_idx = entry["index"]
                    cols = st.columns([5, 1, 1])
                    with cols[0]:
                        st.caption(f"{entry['role_label']} · {entry['summary']}")
                    with cols[1]:
                        if st.button("Open", key=f"chat_record_browser_open_{row_idx}", width="stretch"):
                            st.session_state.chat_record_open_idx = row_idx
                            st.rerun()
                    with cols[2]:
                        if st.button("Delete", key=f"chat_record_browser_delete_{row_idx}", width="stretch"):
                            st.session_state.chat_record_delete_idx = row_idx
                            st.rerun()
                    if row_idx > 0:
                        st.divider()
            if st.button("Close", width="stretch"):
                _close_chat_record_browser(st)
            return

        msg = history[selected_idx]
        record_role = "User" if msg.get("role") == "user" else "Assistant"
        record_text = st.session_state.get(f"chat_record_text_{selected_idx}") or str(msg.get("content") or "")
        extracted = extract_gdl_from_text_fn(record_text)
        suggested_name = suggest_hsf_name_from_chat_record(
            history,
            selected_idx,
            extract_gsm_name_candidate_fn=extract_gsm_name_candidate_fn,
        )
        name_key = f"chat_record_hsf_name_{selected_idx}"
        if not st.session_state.get(name_key):
            st.session_state[name_key] = suggested_name

        st.caption(f"Record role: {record_role}")
        edited_text = st.text_area(
            "Record Content",
            value=record_text,
            height=220,
            key=f"chat_record_text_{selected_idx}",
            label_visibility="visible",
        )
        edited_extracted = extract_gdl_from_text_fn(edited_text)
        st.text_input(
            "HSF Name",
            value=sanitize_hsf_name(st.session_state.get(name_key, suggested_name)),
            key=name_key,
            help="Name used when saving to an HSF folder",
        )
        st.caption("Code Block Extraction")
        if edited_extracted:
            for path, code in edited_extracted.items():
                st.text_area(
                    path,
                    value=code,
                    height=180,
                    key=f"chat_record_code_{selected_idx}_{path}",
                )
        else:
            st.info("No recognizable code blocks found in this record")

        action_cols = st.columns([1, 1, 1, 1])
        with action_cols[0]:
            if st.button("📋 Copy All", width="stretch"):
                ok, copy_msg = copy_text_to_system_clipboard_fn(edited_text)
                if ok:
                    st.toast(copy_msg, icon="✅")
                else:
                    st.warning(copy_msg)
        with action_cols[1]:
            if st.button("📥 Inject into Editor", type="primary", width="stretch"):
                ok, msg_text = _apply_chat_record_to_editor(
                    st=st,
                    msg_idx=selected_idx,
                    extracted=edited_extracted,
                    hsf_name=st.session_state.get(name_key, suggested_name),
                    create_project_fn=create_project_fn,
                    capture_last_project_snapshot_fn=capture_last_project_snapshot_fn,
                    apply_scripts_to_project_fn=apply_scripts_to_project_fn,
                    bump_main_editor_version_fn=bump_main_editor_version_fn,
                    save_as_hsf=False,
                )
                if ok:
                    st.toast(msg_text, icon="📥")
                    st.rerun()
                else:
                    st.error(msg_text)
        with action_cols[2]:
            if st.button("💾 Save as HSF", width="stretch"):
                ok, msg_text = _apply_chat_record_to_editor(
                    st=st,
                    msg_idx=selected_idx,
                    extracted=edited_extracted,
                    hsf_name=st.session_state.get(name_key, suggested_name),
                    create_project_fn=create_project_fn,
                    capture_last_project_snapshot_fn=capture_last_project_snapshot_fn,
                    apply_scripts_to_project_fn=apply_scripts_to_project_fn,
                    bump_main_editor_version_fn=bump_main_editor_version_fn,
                    save_as_hsf=True,
                )
                if ok:
                    st.toast(msg_text, icon="💾")
                    st.rerun()
                else:
                    st.error(msg_text)
        with action_cols[3]:
            if st.button("Delete", width="stretch"):
                st.session_state.chat_record_delete_idx = selected_idx
                st.rerun()

        if st.button("Back to List", width="stretch"):
            _return_to_chat_record_list(st)

    _dialog()


def _render_chat_record_delete_confirm(st, *, delete_idx: int, history: list[dict]) -> None:
    if not (0 <= delete_idx < len(history)):
        st.warning("This chat record no longer exists.")
        if st.button("Back", width="stretch"):
            st.session_state.chat_record_delete_idx = None
            st.rerun()
        return

    entry = build_chat_record_entries(history)[delete_idx]
    st.warning(f"Confirm deletion of this chat record?\n\n{entry['role_label']} · {entry['summary']}")
    confirm_col, cancel_col = st.columns(2)
    with confirm_col:
        if st.button("Confirm Delete", type="primary", width="stretch"):
            ok, msg = delete_chat_record_entry(
                st.session_state,
                delete_idx,
                st.session_state.get("work_dir", ""),
            )
            if ok:
                st.toast(msg, icon="🗑️")
                st.rerun()
            else:
                st.error(msg)
    with cancel_col:
        if st.button("Cancel", width="stretch"):
            st.session_state.chat_record_delete_idx = None
            st.rerun()


def _render_chat_history(
    st,
    *,
    thumb_image_bytes_fn: Callable[[str], bytes | None],
    copyable_chat_text_fn: Callable[[dict], str],
    copy_text_to_system_clipboard_fn: Callable[[str], tuple[bool, str]],
    is_bridgeable_explainer_message_fn: Callable[[dict], bool],
) -> None:
    for idx, msg in enumerate(st.session_state.chat_history):
        role = msg.get("role", "assistant")
        if role == "assistant" and is_project_activity_message(msg.get("content", "")):
            continue

        is_user = role == "user"
        left, right = st.columns([1, 5]) if is_user else st.columns([5, 1])
        target = right if is_user else left

        with target:
            if is_user:
                img_bytes = None
                if msg.get("image_b64"):
                    img_bytes = thumb_image_bytes_fn(msg.get("image_b64", ""))
                render_user_bubble(st, msg.get("content", ""), image_bytes=img_bytes)
            else:
                render_assistant_block(st, msg.get("content", ""))

            if role == "assistant":
                _render_assistant_message_actions(
                    st,
                    idx,
                    msg,
                    copyable_chat_text_fn=copyable_chat_text_fn,
                    copy_text_to_system_clipboard_fn=copy_text_to_system_clipboard_fn,
                    is_bridgeable_explainer_message_fn=is_bridgeable_explainer_message_fn,
                )
            else:
                if st.button("Open", key=f"chat_record_inline_open_{idx}", help="View and replay this record"):
                    st.session_state.chat_record_browser_open = True
                    st.session_state.chat_record_open_idx = idx


def _render_assistant_message_actions(
    st,
    idx: int,
    msg: dict,
    *,
    copyable_chat_text_fn: Callable[[dict], str],
    copy_text_to_system_clipboard_fn: Callable[[str], tuple[bool, str]],
    is_bridgeable_explainer_message_fn: Callable[[dict], bool],
) -> None:
    copy_col, redo_col, open_col, action_col = st.columns([1, 1, 1, 9])
    with copy_col:
        if st.button("📋", key=f"copy_{idx}", help="Copy this reply"):
            copy_text = copyable_chat_text_fn(msg)
            ok, copy_msg = copy_text_to_system_clipboard_fn(copy_text)
            if ok:
                st.toast(copy_msg, icon="✅")
            else:
                st.warning(copy_msg)
    with redo_col:
        prev_user = next(
            (
                st.session_state.chat_history[j]["content"]
                for j in range(idx - 1, -1, -1)
                if st.session_state.chat_history[j]["role"] == "user"
            ),
            None,
        )
        if prev_user and st.button("🔄", key=f"redo_{idx}", help="Regenerate"):
            st.session_state.chat_history = st.session_state.chat_history[:idx]
            st.session_state["_redo_input"] = prev_user
            st.rerun()
    with open_col:
        if st.button("📂", key=f"open_{idx}", help="Open chat record"):
            st.session_state.chat_record_browser_open = True
            st.session_state.chat_record_open_idx = idx
    with action_col:
        _render_assistant_primary_action(
            st,
            idx,
            msg,
            is_bridgeable_explainer_message_fn=is_bridgeable_explainer_message_fn,
        )


def _render_assistant_primary_action(
    st,
    idx: int,
    msg: dict,
    *,
    is_bridgeable_explainer_message_fn: Callable[[dict], bool],
) -> None:
    has_code = "```" in msg.get("content", "")
    is_bridgeable = is_bridgeable_explainer_message_fn(msg)
    if has_code:
        msg_raw = msg.get("content", "")
        has_full_suite = "scripts/3d.gdl" in msg_raw and "paramlist.xml" in msg_raw
        if has_full_suite:
            is_adopted = st.session_state.adopted_msg_index == idx
            adopt_label = "✅ Adopted" if is_adopted else "📥 Adopt This"
            if st.button(adopt_label, key=f"adopt_{idx}", width="stretch"):
                st.session_state["_pending_adopt_idx"] = idx
    elif is_bridgeable:
        if st.button("🪄 Modify Based on This", key=f"bridge_modify_{idx}", width="stretch"):
            st.session_state["_pending_bridge_idx"] = idx
            st.rerun()


def _render_adopt_dialog(
    st,
    *,
    extract_gdl_from_text_fn: Callable[[str], dict],
    capture_last_project_snapshot_fn: Callable[[str], None],
    apply_scripts_to_project_fn: Callable[[object, dict], tuple[int, int]],
    bump_main_editor_version_fn: Callable[[], int],
) -> None:
    @st.dialog("📥 Apply This Code")
    def adopt_confirm_dialog(msg_idx):
        st.warning("This will overwrite based on the returned files: matched scripts/parameters will be fully overwritten, unmatched parts will remain unchanged. Confirm?")
        confirm_col, cancel_col = st.columns(2)
        with confirm_col:
            if st.button("✅ Confirm Overwrite", type="primary", width="stretch"):
                msg_content = st.session_state.chat_history[msg_idx]["content"]
                extracted = extract_gdl_from_text_fn(msg_content)
                if extracted:
                    if st.session_state.project:
                        capture_last_project_snapshot_fn("Chat code adoption")
                        apply_scripts_to_project_fn(st.session_state.project, extracted)
                    bump_main_editor_version_fn()
                    st.session_state.adopted_msg_index = msg_idx
                    st.session_state["_pending_adopt_idx"] = None
                    st.toast("✅ Written to editor", icon="📥")
                    st.rerun()
                else:
                    st.error("No extractable code blocks found")
        with cancel_col:
            if st.button("❌ Cancel", width="stretch"):
                st.session_state["_pending_adopt_idx"] = None
                st.rerun()

    if st.session_state.get("_pending_adopt_idx") is not None:
        adopt_confirm_dialog(st.session_state["_pending_adopt_idx"])


def _render_route_controls(st) -> str | None:
    st.session_state["_debug_mode_active"] = None
    st.radio(
        "AI Mode",
        ["Auto", "Force Generate", "Force Debug"],
        horizontal=True,
        key="chat_route_mode",
    )
    return None


def _read_chat_input(st, *, is_generation_locked_fn: Callable[[object], bool]) -> dict:
    if st.session_state.agent_running:
        st.info("⏳ AI is generating, please wait...")
    chat_payload = st.chat_input(
        "Describe your requirements, ask a question, or attach an image for additional context…",
        key="chat_main_input",
        accept_file=True,
        file_type=["jpg", "jpeg", "png", "webp", "gif"],
        disabled=is_generation_locked_fn(st.session_state),
    )
    return {
        "chat_payload": chat_payload,
        "user_input": chat_payload if isinstance(chat_payload, str) else None,
        "vision_b64": None,
        "vision_mime": None,
        "vision_name": None,
    }


def _decode_chat_attachment(
    st,
    payload: dict,
    *,
    validate_chat_image_size_fn: Callable[[bytes, str], str | None],
) -> None:
    chat_payload = payload["chat_payload"]
    if isinstance(chat_payload, str) or chat_payload is None:
        return

    payload["user_input"] = chat_payload.get("text", "") or ""
    chat_files = chat_payload.get("files", []) or []
    if not chat_files:
        return

    img = chat_files[0]
    raw_bytes = img.read()
    if not raw_bytes:
        return

    image_name = getattr(img, "name", "image") or "image"
    size_error = validate_chat_image_size_fn(raw_bytes, image_name)
    if size_error:
        st.session_state.chat_history.append({"role": "assistant", "content": f"❌ {size_error}"})
        st.error(size_error)
        st.rerun()

    payload["vision_b64"] = base64.b64encode(raw_bytes).decode()
    payload["vision_mime"] = getattr(img, "type", "") or "image/jpeg"
    payload["vision_name"] = image_name
