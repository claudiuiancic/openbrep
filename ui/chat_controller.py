from __future__ import annotations

from typing import Callable

from openbrep.elicitation_agent import ElicitationState
from openbrep.learning import ErrorLearningStore, looks_like_error_report

from ui.chat_paths import run_normal_text_path, run_vision_path
from ui.chat_runtime import (
    build_image_user_display,
    pop_chat_runtime_state,
    resolve_bridge_input,
    resolve_effective_input,
    resolve_image_route_mode,
)
from ui.chat_tapir_events import (
    handle_tapir_apply_params_trigger,
    handle_tapir_highlight_trigger,
    handle_tapir_load_params_trigger,
    handle_tapir_selection_trigger,
    handle_tapir_test_trigger,
)


def maybe_record_conversation_error_learning(session_state, text: str | None) -> bool:
    if not text or not looks_like_error_report(text):
        return False
    try:
        project = session_state.get("project")
        project_name = getattr(project, "name", "") if project is not None else ""
        work_dir = session_state.get("work_dir", "./workdir")
        ErrorLearningStore(work_dir).record_error(
            text,
            source="conversation_error_fragment",
            project_name=project_name,
            instruction="用户在聊天中提供的脚本错误提示，后续生成需避免同类问题。",
        )
        session_state["learning_notice"] = "已加入错题本"
        return True
    except Exception:
        return False


def persist_new_chat_messages(session_state, start_index: int) -> int:
    try:
        messages = list(session_state.get("chat_history", []))[start_index:]
        if not messages:
            return 0
        project = session_state.get("project")
        project_name = getattr(project, "name", "") if project is not None else ""
        work_dir = session_state.get("work_dir", "./workdir")
        stored = ErrorLearningStore(work_dir).append_chat_messages(
            messages,
            project_name=project_name,
            source="ui_chat",
        )
        if stored:
            record_history = list(session_state.get("chat_record_history") or [])
            record_history.extend(messages)
            session_state.chat_record_history = record_history
            session_state.chat_record_history_loaded_work_dir = work_dir
        return stored
    except Exception:
        return 0


def is_learning_summary_request(text: str | None) -> bool:
    raw = (text or "").strip()
    if not raw:
        return False
    compact = raw.replace(" ", "")
    has_learning_target = any(term in compact for term in ("整理错题本", "生成错题本", "整理学习", "整理记忆"))
    has_action = any(term in compact for term in ("整理", "生成", "更新", "刷新"))
    return has_learning_target and has_action


def summarize_learning_from_chat_request(session_state, text: str, llm_refiner=None) -> str:
    project = session_state.get("project")
    project_name = getattr(project, "name", "") if project is not None else ""
    work_dir = session_state.get("work_dir", "./workdir")
    result = ErrorLearningStore(work_dir).summarize_to_skill(
        project_name=project_name,
        llm_refiner=llm_refiner,
    )
    if result.ok:
        session_state["learning_notice"] = result.message
        return (
            f"{result.message}\n\n"
            f"已写入：`{result.path}`\n\n"
            "说明：整理链路先用确定性规则扫描聊天记录和已有编译/报错记录，"
            "再把可验证事实压缩成后续生成会自动注入的本地 Skill；"
            "如果可用，会额外调用 LLM 做二阶段专业化改写，失败则回退到规则整理。"
        )
    session_state["learning_notice"] = result.message
    return (
        f"{result.message}\n\n"
        "我已经检查当前工作区的聊天记录和错题记录，但没有发现可整理的 GDL 报错线索。"
    )


def handle_elicitation_route(
    *,
    user_input: str,
    gdl_obj_name: str,
    session_state,
    ensure_elicitation_agent_fn: Callable[[], object],
    make_generation_project_fn: Callable[[str], object],
    run_agent_generate_fn: Callable[[str, object, object, str, bool], str],
    container_fn: Callable[[], object],
    info_fn: Callable[[str], None],
    is_positive_confirmation_fn: Callable[[str], bool],
    is_negative_confirmation_fn: Callable[[str], bool],
    should_start_elicitation_fn: Callable[[str], bool],
) -> tuple[str, bool]:
    agent = ensure_elicitation_agent_fn()

    if agent.state == ElicitationState.HANDOFF and agent.spec is not None:
        spec = agent.spec
        instruction = spec.to_instruction()
        object_name = spec.object_name
        agent.reset()
        session_state.elicitation_state = agent.state.value
        if not session_state.project:
            make_generation_project_fn(gdl_obj_name or object_name or "elicited_object")
            info_fn(f"📁 已初始化项目 `{session_state.pending_gsm_name}`")
        project = session_state.project
        effective_gsm = session_state.pending_gsm_name or project.name
        return run_agent_generate_fn(
            instruction,
            project,
            container_fn(),
            effective_gsm,
            True,
        ), False

    if agent.state == ElicitationState.SPEC_READY:
        if is_positive_confirmation_fn(user_input):
            spec = agent.confirm(True)
            session_state.elicitation_state = agent.state.value
            if spec is None:
                return "❌ 规格确认失败，请重试。", True
            return handle_elicitation_route(
                user_input=user_input,
                gdl_obj_name=spec.object_name,
                session_state=session_state,
                ensure_elicitation_agent_fn=ensure_elicitation_agent_fn,
                make_generation_project_fn=make_generation_project_fn,
                run_agent_generate_fn=run_agent_generate_fn,
                container_fn=container_fn,
                info_fn=info_fn,
                is_positive_confirmation_fn=is_positive_confirmation_fn,
                is_negative_confirmation_fn=is_negative_confirmation_fn,
                should_start_elicitation_fn=should_start_elicitation_fn,
            )
        if is_negative_confirmation_fn(user_input):
            agent.confirm(False)
            session_state.elicitation_state = agent.state.value
            reply, _ = agent.respond(user_input)
            session_state.elicitation_state = agent.state.value
            return reply, True
        return agent._format_spec_summary(), True

    if agent.state == ElicitationState.ELICITING:
        reply, _ = agent.respond(user_input)
        session_state.elicitation_state = agent.state.value
        return reply, True

    if should_start_elicitation_fn(user_input):
        reply = agent.start(user_input)
        session_state.elicitation_state = agent.state.value
        return reply, True

    return "", False


def process_chat_turn(
    *,
    st,
    session_state,
    chat_payload: dict,
    api_key: str,
    model_name: str,
    resolve_bridge_input_fn: Callable[[object, str | None, list[dict], bool], str | None],
    resolve_effective_input_fn: Callable[[object, str | None, bool, str | None, str | None, str | None], tuple[str | None, bool, bool]],
    detect_gsm_name_candidate_fn: Callable[[str], str | None],
    handle_tapir_test_trigger_fn: Callable[[bool], tuple[bool, bool]],
    handle_tapir_selection_trigger_fn: Callable[[bool], tuple[bool, bool]],
    handle_tapir_highlight_trigger_fn: Callable[[bool], tuple[bool, bool]],
    handle_tapir_load_params_trigger_fn: Callable[[bool], tuple[bool, bool]],
    handle_tapir_apply_params_trigger_fn: Callable[[bool], tuple[bool, bool]],
    run_vision_path_fn: Callable[..., tuple[bool, bool, str | None]],
    run_normal_text_path_fn: Callable[..., tuple[bool, bool, str | None]],
    learning_refine_fn: Callable[[str], str] | None = None,
) -> None:
    runtime = pop_chat_runtime_state(session_state=session_state, has_image_input=bool(chat_payload.get("vision_b64")))
    user_input = chat_payload.get("user_input")
    live_output = chat_payload["live_output"]
    chat_start_index = len(session_state.get("chat_history", []))
    maybe_record_conversation_error_learning(session_state, user_input)

    _handled, _should_rerun = handle_tapir_test_trigger_fn(runtime["tapir_trigger"])
    if _handled and _should_rerun:
        st.rerun()

    _handled, _should_rerun = handle_tapir_selection_trigger_fn(runtime["tapir_selection_trigger"])
    if _handled and _should_rerun:
        st.rerun()

    _handled, _should_rerun = handle_tapir_highlight_trigger_fn(runtime["tapir_highlight_trigger"])
    if _handled and _should_rerun:
        st.rerun()

    _handled, _should_rerun = handle_tapir_load_params_trigger_fn(runtime["tapir_load_params_trigger"])
    if _handled and _should_rerun:
        st.rerun()

    _handled, _should_rerun = handle_tapir_apply_params_trigger_fn(runtime["tapir_apply_params_trigger"])
    if _handled and _should_rerun:
        st.rerun()

    auto_debug_input = session_state.pop("_auto_debug_input", None)
    bridge_input = resolve_bridge_input_fn(
        runtime["pending_bridge_idx"],
        user_input,
        session_state.get("chat_history", []),
        bool(session_state.get("project")),
    )
    effective_input, clear_debug_mode, toast_missing_debug_text = resolve_effective_input_fn(
        runtime["active_debug_mode"],
        user_input,
        runtime["has_image_input"],
        auto_debug_input,
        bridge_input,
        runtime["redo_input"],
    )
    if clear_debug_mode:
        session_state["_debug_mode_active"] = None
    if toast_missing_debug_text:
        st.toast("请输入问题描述后再发送，或直接描述你看到的现象", icon="💬")

    if user_input and not (session_state.pending_gsm_name or "").strip():
        gsm_candidate = detect_gsm_name_candidate_fn(user_input)
        if gsm_candidate:
            session_state.pending_gsm_name = gsm_candidate

    if runtime["has_image_input"]:
        handled, should_rerun, err_msg = run_vision_path_fn(
            runtime["has_image_input"],
            chat_payload["vision_mime"],
            chat_payload["vision_name"],
            user_input,
            runtime["active_debug_mode"],
            chat_payload["vision_b64"],
            live_output,
            api_key,
            model_name,
        )
        if err_msg:
            st.error(err_msg)
        persist_new_chat_messages(session_state, chat_start_index)
        if handled and should_rerun:
            st.rerun()
    elif effective_input:
        if is_learning_summary_request(effective_input):
            session_state.chat_history.append({"role": "user", "content": effective_input})
            try:
                msg = summarize_learning_from_chat_request(
                    session_state,
                    effective_input,
                    llm_refiner=learning_refine_fn,
                )
            except Exception as exc:
                msg = f"整理错题本失败：{exc}"
                session_state["learning_notice"] = msg
            session_state.chat_history.append({"role": "assistant", "content": msg})
            persist_new_chat_messages(session_state, chat_start_index)
            st.toast("错题本整理完成" if "失败" not in msg else "错题本整理失败", icon="🧠")
            st.rerun()
            return

        handled, should_rerun, err_msg = run_normal_text_path_fn(
            effective_input,
            runtime["redo_input"],
            bridge_input,
            live_output,
            api_key,
            model_name,
        )
        if err_msg:
            st.error(err_msg)
        persist_new_chat_messages(session_state, chat_start_index)
        if handled and should_rerun:
            st.rerun()
