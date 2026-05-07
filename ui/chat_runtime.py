from __future__ import annotations

from typing import Callable


def pop_chat_runtime_state(
    *,
    session_state,
    has_image_input: bool,
) -> dict:
    return {
        "redo_input": session_state.pop("_redo_input", None),
        "pending_bridge_idx": session_state.pop("_pending_bridge_idx", None),
        "active_debug_mode": session_state.get("_debug_mode_active"),
        "tapir_trigger": session_state.pop("tapir_test_trigger", False),
        "tapir_selection_trigger": session_state.pop("tapir_selection_trigger", False),
        "tapir_highlight_trigger": session_state.pop("tapir_highlight_trigger", False),
        "tapir_load_params_trigger": session_state.pop("tapir_load_params_trigger", False),
        "tapir_apply_params_trigger": session_state.pop("tapir_apply_params_trigger", False),
        "has_image_input": bool(has_image_input),
    }


def resolve_bridge_input(
    *,
    pending_bridge_idx,
    user_input: str | None,
    history: list[dict],
    has_project: bool,
    build_modify_bridge_prompt_fn: Callable[[dict], str],
    maybe_build_followup_bridge_input_fn: Callable[[str, list[dict], bool], str | None],
) -> str | None:
    if pending_bridge_idx is not None:
        bridge_msg = history[pending_bridge_idx]
        return build_modify_bridge_prompt_fn(bridge_msg)
    if user_input:
        return maybe_build_followup_bridge_input_fn(
            user_input=user_input,
            history=history,
            has_project=has_project,
        )
    return None


def resolve_effective_input(
    *,
    active_debug_mode,
    user_input: str | None,
    has_image_input: bool,
    auto_debug_input: str | None,
    bridge_input: str | None,
    redo_input: str | None,
) -> tuple[str | None, bool, bool]:
    if active_debug_mode and user_input:
        dbg_prefix = f"[DEBUG:{active_debug_mode}]"
        return f"{dbg_prefix} {user_input.strip()}", True, False

    if active_debug_mode and user_input == "" and not has_image_input:
        return auto_debug_input or bridge_input or redo_input, False, True

    return auto_debug_input or bridge_input or redo_input or user_input, False, False


def resolve_image_route_mode(
    *,
    route_pick: str,
    active_debug_mode,
    joined_text: str,
    vision_name: str,
    detect_image_task_mode_fn: Callable[[str, str], str],
) -> str:
    if route_pick == "强制调试":
        return "debug"
    if route_pick == "强制生成":
        return "generate"
    if active_debug_mode:
        return "debug"
    return detect_image_task_mode_fn(joined_text, vision_name)


def build_image_user_display(vision_name: str, route_mode: str, joined_text: str) -> str:
    route_tag = "🧩 Debug" if route_mode == "debug" else "🧱 生成"
    return f"🖼️ `{vision_name}` · {route_tag}" + (f"  \n{joined_text}" if joined_text else "")
