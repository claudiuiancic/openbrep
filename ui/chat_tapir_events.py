from __future__ import annotations

from typing import Callable


def handle_tapir_test_trigger(
    *,
    tapir_trigger: bool,
    tapir_import_ok: bool,
    get_bridge_fn: Callable[[], object],
    errors_to_chat_message_fn: Callable[[list], str],
    session_state,
) -> tuple[bool, bool]:
    if not (tapir_trigger and tapir_import_ok):
        return False, False

    import streamlit as st

    bridge = get_bridge_fn()
    proj_for_tapir = session_state.project
    with st.spinner("🏗️ Triggering Archicad library reload, waiting for render..."):
        reload_ok, gdl_errors = bridge.reload_and_capture(
            timeout=6.0,
            project=proj_for_tapir,
        )

    if reload_ok:
        error_msg = errors_to_chat_message_fn(gdl_errors)
        session_state.chat_history.append({
            "role": "assistant",
            "content": error_msg,
        })
        if gdl_errors:
            auto_debug = "[DEBUG:editor] Please fix the script based on the Archicad errors above"
            session_state.chat_history.append({
                "role": "user",
                "content": auto_debug,
            })
            session_state["_auto_debug_input"] = auto_debug
        return True, True

    st.toast("❌ Archicad connection failed — make sure Archicad is running", icon="⚠️")
    return True, False


def handle_tapir_selection_trigger(
    *,
    tapir_selection_trigger: bool,
    tapir_import_ok: bool,
    tapir_sync_selection_fn: Callable[[], tuple[bool, str]],
    session_state,
) -> tuple[bool, bool]:
    if not (tapir_selection_trigger and tapir_import_ok):
        return False, False

    import streamlit as st

    ok, msg = tapir_sync_selection_fn()
    if ok:
        if session_state.get("tapir_selected_guids"):
            st.toast(f"✅ {msg}", icon="🧭")
        else:
            st.warning("No objects selected")
    else:
        st.error(f"❌ {msg}")
    return True, True


def handle_tapir_highlight_trigger(
    *,
    tapir_highlight_trigger: bool,
    tapir_import_ok: bool,
    tapir_highlight_selection_fn: Callable[[], tuple[bool, str]],
) -> tuple[bool, bool]:
    if not (tapir_highlight_trigger and tapir_import_ok):
        return False, False

    import streamlit as st

    ok, msg = tapir_highlight_selection_fn()
    if ok:
        st.toast(f"✅ {msg}", icon="🎯")
    else:
        st.error(f"❌ {msg}")
    return True, True


def handle_tapir_load_params_trigger(
    *,
    tapir_load_params_trigger: bool,
    tapir_import_ok: bool,
    tapir_load_selected_params_fn: Callable[[], tuple[bool, str]],
    session_state,
) -> tuple[bool, bool]:
    if not (tapir_load_params_trigger and tapir_import_ok):
        return False, False

    import streamlit as st

    ok, msg = tapir_load_selected_params_fn()
    if ok:
        if session_state.get("tapir_last_error"):
            st.warning(session_state.tapir_last_error)
        st.toast(f"✅ {msg}", icon="📥")
    else:
        st.error(f"❌ {msg}")
    return True, True


def handle_tapir_apply_params_trigger(
    *,
    tapir_apply_params_trigger: bool,
    tapir_import_ok: bool,
    tapir_apply_param_edits_fn: Callable[[], tuple[bool, str]],
) -> tuple[bool, bool]:
    if not (tapir_apply_params_trigger and tapir_import_ok):
        return False, False

    import streamlit as st

    ok, msg = tapir_apply_param_edits_fn()
    if ok:
        st.toast(f"✅ {msg}", icon="📤")
    else:
        st.error(f"❌ {msg}")
    return True, True
