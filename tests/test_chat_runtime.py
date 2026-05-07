import unittest

from ui.chat_runtime import (
    build_image_user_display,
    pop_chat_runtime_state,
    resolve_bridge_input,
    resolve_effective_input,
    resolve_image_route_mode,
)


class _State(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as exc:
            raise AttributeError(key) from exc

    def __setattr__(self, key, value):
        self[key] = value


class TestChatRuntime(unittest.TestCase):
    def test_pop_chat_runtime_state_consumes_transient_flags(self):
        state = _State(
            _redo_input="redo",
            _pending_bridge_idx=2,
            _debug_mode_active="editor",
            tapir_test_trigger=True,
            tapir_selection_trigger=True,
            tapir_highlight_trigger=False,
            tapir_load_params_trigger=True,
            tapir_apply_params_trigger=False,
        )

        runtime = pop_chat_runtime_state(session_state=state, has_image_input=True)

        self.assertEqual(runtime["redo_input"], "redo")
        self.assertEqual(runtime["pending_bridge_idx"], 2)
        self.assertEqual(runtime["active_debug_mode"], "editor")
        self.assertTrue(runtime["tapir_trigger"])
        self.assertTrue(runtime["tapir_selection_trigger"])
        self.assertTrue(runtime["tapir_load_params_trigger"])
        self.assertTrue(runtime["has_image_input"])
        self.assertNotIn("_redo_input", state)
        self.assertNotIn("_pending_bridge_idx", state)
        self.assertNotIn("tapir_test_trigger", state)

    def test_resolve_bridge_input_prefers_explicit_pending_message(self):
        history = [{"content": "old"}, {"content": "解释结果"}]
        out = resolve_bridge_input(
            pending_bridge_idx=1,
            user_input="继续改",
            history=history,
            has_project=True,
            build_modify_bridge_prompt_fn=lambda msg: f"bridge:{msg['content']}",
            maybe_build_followup_bridge_input_fn=lambda **_kwargs: "followup",
        )

        self.assertEqual(out, "bridge:解释结果")

    def test_resolve_effective_input_prefixes_active_debug_text(self):
        effective, clear_debug, toast = resolve_effective_input(
            active_debug_mode="editor",
            user_input="修复报错",
            has_image_input=False,
            auto_debug_input=None,
            bridge_input=None,
            redo_input=None,
        )

        self.assertEqual(effective, "[DEBUG:editor] 修复报错")
        self.assertTrue(clear_debug)
        self.assertFalse(toast)

    def test_resolve_effective_input_uses_auto_debug_when_debug_submit_is_empty(self):
        effective, clear_debug, toast = resolve_effective_input(
            active_debug_mode="editor",
            user_input="",
            has_image_input=False,
            auto_debug_input="[DEBUG:editor] 自动修复",
            bridge_input="bridge",
            redo_input="redo",
        )

        self.assertEqual(effective, "[DEBUG:editor] 自动修复")
        self.assertFalse(clear_debug)
        self.assertTrue(toast)

    def test_resolve_image_route_mode_honors_forced_modes(self):
        self.assertEqual(
            resolve_image_route_mode(
                route_pick="强制调试",
                active_debug_mode=None,
                joined_text="生成",
                vision_name="a.png",
                detect_image_task_mode_fn=lambda *_args: "generate",
            ),
            "debug",
        )
        self.assertEqual(
            resolve_image_route_mode(
                route_pick="强制生成",
                active_debug_mode="editor",
                joined_text="修复",
                vision_name="a.png",
                detect_image_task_mode_fn=lambda *_args: "debug",
            ),
            "generate",
        )

    def test_build_image_user_display_keeps_name_route_and_text(self):
        out = build_image_user_display("demo.png", "debug", "请修复")

        self.assertIn("demo.png", out)
        self.assertIn("Debug", out)
        self.assertIn("请修复", out)


if __name__ == "__main__":
    unittest.main()
