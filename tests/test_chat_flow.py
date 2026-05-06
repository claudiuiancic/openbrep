import unittest
import tempfile

from openbrep.learning import ErrorLearningStore
from ui.chat_controller import process_chat_turn


class _State(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as exc:
            raise AttributeError(key) from exc

    def __setattr__(self, key, value):
        self[key] = value


class _DummyStreamlit:
    def __init__(self):
        self.rerun_called = 0
        self.toasts = []
        self.errors = []

    def rerun(self):
        self.rerun_called += 1

    def toast(self, msg, icon=None):
        self.toasts.append((msg, icon))

    def error(self, msg):
        self.errors.append(msg)


class TestChatFlowDispatch(unittest.TestCase):
    def test_process_chat_turn_routes_text_input(self):
        st = _DummyStreamlit()
        session_state = _State(
            chat_history=[],
            project=object(),
            pending_gsm_name="",
            agent_running=False,
        )
        calls = {"normal": 0, "vision": 0}

        def run_normal_text_path_fn(*args, **kwargs):
            calls["normal"] += 1
            return True, True, None

        def run_vision_path_fn(*args, **kwargs):
            calls["vision"] += 1
            return False, False, None

        process_chat_turn(
            st=st,
            session_state=session_state,
            chat_payload={
                "user_input": "请修复这个对象",
                "live_output": object(),
                "vision_b64": None,
                "vision_mime": None,
                "vision_name": None,
            },
            api_key="k",
            model_name="glm-4-flash",
            resolve_bridge_input_fn=lambda *_args, **_kwargs: None,
            resolve_effective_input_fn=lambda *args, **kwargs: ("请修复这个对象", False, False),
            detect_gsm_name_candidate_fn=lambda text: "demo-gsm" if text else None,
            handle_tapir_test_trigger_fn=lambda *_args: (False, False),
            handle_tapir_selection_trigger_fn=lambda *_args: (False, False),
            handle_tapir_highlight_trigger_fn=lambda *_args: (False, False),
            handle_tapir_load_params_trigger_fn=lambda *_args: (False, False),
            handle_tapir_apply_params_trigger_fn=lambda *_args: (False, False),
            run_vision_path_fn=run_vision_path_fn,
            run_normal_text_path_fn=run_normal_text_path_fn,
        )

        self.assertEqual(calls["normal"], 1)
        self.assertEqual(calls["vision"], 0)
        self.assertEqual(session_state.pending_gsm_name, "demo-gsm")
        self.assertEqual(st.errors, [])

    def test_process_chat_turn_records_script_error_fragment_before_routing(self):
        st = _DummyStreamlit()
        with tempfile.TemporaryDirectory() as tmpdir:
            session_state = _State(
                chat_history=[],
                project=type("Project", (), {"name": "钢结构旋转楼梯"})(),
                pending_gsm_name="",
                agent_running=False,
                work_dir=tmpdir,
            )
            user_text = "3d 脚本有错误提示：Not enough parameters\nat line 27 in the 3D script of file 钢结构旋转楼梯_v1.gsm"

            process_chat_turn(
                st=st,
                session_state=session_state,
                chat_payload={
                    "user_input": user_text,
                    "live_output": object(),
                    "vision_b64": None,
                    "vision_mime": None,
                    "vision_name": None,
                },
                api_key="k",
                model_name="glm-4-flash",
                resolve_bridge_input_fn=lambda *_args, **_kwargs: None,
                resolve_effective_input_fn=lambda *args, **kwargs: (user_text, False, False),
                detect_gsm_name_candidate_fn=lambda _text: None,
                handle_tapir_test_trigger_fn=lambda *_args: (False, False),
                handle_tapir_selection_trigger_fn=lambda *_args: (False, False),
                handle_tapir_highlight_trigger_fn=lambda *_args: (False, False),
                handle_tapir_load_params_trigger_fn=lambda *_args: (False, False),
                handle_tapir_apply_params_trigger_fn=lambda *_args: (False, False),
                run_vision_path_fn=lambda *args, **kwargs: (False, False, None),
                run_normal_text_path_fn=lambda *args, **kwargs: (True, True, None),
            )

            lessons = ErrorLearningStore(tmpdir).list_error_lessons()
            self.assertEqual(len(lessons), 1)
            self.assertEqual(lessons[0].category, "command_arguments")
            self.assertEqual(lessons[0].project_name, "钢结构旋转楼梯")
            self.assertEqual(session_state.learning_notice, "已加入错题本")

    def test_process_chat_turn_persists_new_chat_messages(self):
        st = _DummyStreamlit()
        with tempfile.TemporaryDirectory() as tmpdir:
            session_state = _State(
                chat_history=[],
                project=type("Project", (), {"name": "Demo"})(),
                pending_gsm_name="",
                agent_running=False,
                work_dir=tmpdir,
            )

            def run_normal_text_path_fn(*args, **kwargs):
                session_state.chat_history.append({"role": "user", "content": "请生成楼梯"})
                session_state.chat_history.append({"role": "assistant", "content": "已生成"})
                return True, True, None

            process_chat_turn(
                st=st,
                session_state=session_state,
                chat_payload={
                    "user_input": "请生成楼梯",
                    "live_output": object(),
                    "vision_b64": None,
                    "vision_mime": None,
                    "vision_name": None,
                },
                api_key="k",
                model_name="glm-4-flash",
                resolve_bridge_input_fn=lambda *_args, **_kwargs: None,
                resolve_effective_input_fn=lambda *args, **kwargs: ("请生成楼梯", False, False),
                detect_gsm_name_candidate_fn=lambda _text: None,
                handle_tapir_test_trigger_fn=lambda *_args: (False, False),
                handle_tapir_selection_trigger_fn=lambda *_args: (False, False),
                handle_tapir_highlight_trigger_fn=lambda *_args: (False, False),
                handle_tapir_load_params_trigger_fn=lambda *_args: (False, False),
                handle_tapir_apply_params_trigger_fn=lambda *_args: (False, False),
                run_vision_path_fn=lambda *args, **kwargs: (False, False, None),
                run_normal_text_path_fn=run_normal_text_path_fn,
            )

            transcript = ErrorLearningStore(tmpdir).list_chat_transcript()
            self.assertEqual([entry.role for entry in transcript], ["user", "assistant"])
            self.assertEqual(transcript[0].project_name, "Demo")

    def test_process_chat_turn_handles_learning_summary_request_without_llm_route(self):
        st = _DummyStreamlit()
        with tempfile.TemporaryDirectory() as tmpdir:
            store = ErrorLearningStore(tmpdir)
            store.append_chat_messages(
                [
                    {
                        "role": "user",
                        "content": (
                            "3d 脚本有错误提示：Not enough parameters\n"
                            "at line 27 in the 3D script of file 钢结构旋转楼梯_v1.gsm"
                        ),
                    }
                ],
                project_name="钢结构旋转楼梯",
            )
            session_state = _State(
                chat_history=[],
                project=type("Project", (), {"name": "钢结构旋转楼梯"})(),
                pending_gsm_name="",
                agent_running=False,
                work_dir=tmpdir,
            )
            calls = {"normal": 0}

            def run_normal_text_path_fn(*args, **kwargs):
                calls["normal"] += 1
                return True, True, None

            process_chat_turn(
                st=st,
                session_state=session_state,
                chat_payload={
                    "user_input": "整理错题本",
                    "live_output": object(),
                    "vision_b64": None,
                    "vision_mime": None,
                    "vision_name": None,
                },
                api_key="k",
                model_name="glm-4-flash",
                resolve_bridge_input_fn=lambda *_args, **_kwargs: None,
                resolve_effective_input_fn=lambda *args, **kwargs: ("整理错题本", False, False),
                detect_gsm_name_candidate_fn=lambda _text: None,
                handle_tapir_test_trigger_fn=lambda *_args: (False, False),
                handle_tapir_selection_trigger_fn=lambda *_args: (False, False),
                handle_tapir_highlight_trigger_fn=lambda *_args: (False, False),
                handle_tapir_load_params_trigger_fn=lambda *_args: (False, False),
                handle_tapir_apply_params_trigger_fn=lambda *_args: (False, False),
                run_vision_path_fn=lambda *args, **kwargs: (False, False, None),
                run_normal_text_path_fn=run_normal_text_path_fn,
            )

            self.assertEqual(calls["normal"], 0)
            self.assertTrue(store.learned_skill_path.exists())
            self.assertIn("扫描聊天命中 1 条", session_state.chat_history[-1]["content"])
            self.assertEqual(st.rerun_called, 1)
            transcript = ErrorLearningStore(tmpdir).list_chat_transcript()
            self.assertEqual([entry.role for entry in transcript[-2:]], ["user", "assistant"])

    def test_process_chat_turn_passes_learning_refiner_to_summary_request(self):
        st = _DummyStreamlit()
        with tempfile.TemporaryDirectory() as tmpdir:
            store = ErrorLearningStore(tmpdir)
            store.record_error(
                "Error in 3D script, line 12: Undefined variable width",
                source="compile",
                project_name="Chair",
            )
            session_state = _State(
                chat_history=[],
                project=type("Project", (), {"name": "Chair"})(),
                pending_gsm_name="",
                agent_running=False,
                work_dir=tmpdir,
            )
            calls = {"refine": 0, "normal": 0}

            def refine(_prompt: str) -> str:
                calls["refine"] += 1
                return """\
# Skill: learned_gdl_error_avoidance_compacted

## Success Criteria

- 生成前做变量来源检查。

## Hard Constraints

- 变量必须来自参数表或脚本内赋值。

## Representative Lessons

1. width 未定义导致脚本失败。
"""

            process_chat_turn(
                st=st,
                session_state=session_state,
                chat_payload={
                    "user_input": "请更新整理错题本",
                    "live_output": object(),
                    "vision_b64": None,
                    "vision_mime": None,
                    "vision_name": None,
                },
                api_key="k",
                model_name="glm-4-flash",
                resolve_bridge_input_fn=lambda *_args, **_kwargs: None,
                resolve_effective_input_fn=lambda *args, **kwargs: ("请更新整理错题本", False, False),
                detect_gsm_name_candidate_fn=lambda _text: None,
                handle_tapir_test_trigger_fn=lambda *_args: (False, False),
                handle_tapir_selection_trigger_fn=lambda *_args: (False, False),
                handle_tapir_highlight_trigger_fn=lambda *_args: (False, False),
                handle_tapir_load_params_trigger_fn=lambda *_args: (False, False),
                handle_tapir_apply_params_trigger_fn=lambda *_args: (False, False),
                run_vision_path_fn=lambda *args, **kwargs: (False, False, None),
                run_normal_text_path_fn=lambda *args, **kwargs: calls.__setitem__("normal", calls["normal"] + 1) or (True, True, None),
                learning_refine_fn=refine,
            )

            self.assertEqual(calls, {"refine": 1, "normal": 0})
            self.assertIn("方式：LLM 二阶段整理", session_state.chat_history[-1]["content"])
            compacted = store.learned_skill_path.read_text(encoding="utf-8")
            self.assertIn("变量必须来自参数表或脚本内赋值", compacted)

    def test_process_chat_turn_routes_image_input(self):
        st = _DummyStreamlit()
        session_state = _State(
            chat_history=[],
            project=object(),
            pending_gsm_name="",
            agent_running=False,
        )
        calls = {"normal": 0, "vision": 0}

        def run_normal_text_path_fn(*args, **kwargs):
            calls["normal"] += 1
            return False, False, None

        def run_vision_path_fn(*args, **kwargs):
            calls["vision"] += 1
            return True, True, None

        process_chat_turn(
            st=st,
            session_state=session_state,
            chat_payload={
                "user_input": "请生成",
                "live_output": object(),
                "vision_b64": "ZmFrZQ==",
                "vision_mime": "image/png",
                "vision_name": "shot.png",
            },
            api_key="k",
            model_name="glm-4-flash",
            resolve_bridge_input_fn=lambda *_args, **_kwargs: None,
            resolve_effective_input_fn=lambda *args, **kwargs: ("请生成", False, False),
            detect_gsm_name_candidate_fn=lambda text: "demo-gsm" if text else None,
            handle_tapir_test_trigger_fn=lambda *_args: (False, False),
            handle_tapir_selection_trigger_fn=lambda *_args: (False, False),
            handle_tapir_highlight_trigger_fn=lambda *_args: (False, False),
            handle_tapir_load_params_trigger_fn=lambda *_args: (False, False),
            handle_tapir_apply_params_trigger_fn=lambda *_args: (False, False),
            run_vision_path_fn=run_vision_path_fn,
            run_normal_text_path_fn=run_normal_text_path_fn,
        )

        self.assertEqual(calls["normal"], 0)
        self.assertEqual(calls["vision"], 1)
        self.assertEqual(st.errors, [])


if __name__ == "__main__":
    unittest.main()
