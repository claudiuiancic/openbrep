import tempfile
import unittest

from openbrep.hsf_project import HSFProject, ScriptType
from ui.script_application import apply_scripts_to_project, parse_paramlist_text, sanitize_script_content


class _State(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as exc:
            raise AttributeError(key) from exc

    def __setattr__(self, key, value):
        self[key] = value


class TestScriptApplication(unittest.TestCase):
    def test_parse_paramlist_text_reads_simple_parameter_lines(self):
        params = parse_paramlist_text('Length A = 1.2 ! width\nString label = "Demo"\n')

        self.assertEqual([p.name for p in params], ["A", "label"])
        self.assertEqual(params[0].type_tag, "Length")
        self.assertEqual(params[0].description, "width")
        self.assertEqual(params[1].value, "Demo")

    def test_sanitize_script_content_removes_markdown_prose(self):
        raw = """\
```gdl
说明：这里是解释
BLOCK 1, 1, 1
- 不应进入脚本
```
"""
        self.assertEqual(sanitize_script_content(raw, "scripts/3d.gdl"), "BLOCK 1, 1, 1")

    def test_apply_scripts_to_project_updates_project_and_clears_preview(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            project = HSFProject.create_new("Demo", work_dir=tmpdir)
            state = _State(
                script_revision=0,
                preview_2d_data={"old": True},
                preview_3d_data={"old": True},
                preview_warnings=["old"],
                preview_meta={"kind": "3D"},
            )
            calls = {"clear": 0}

            script_count, param_count = apply_scripts_to_project(
                project,
                {
                    "scripts/3d.gdl": "BLOCK 1, 1, 1",
                    "paramlist.xml": "Length A = 1.0 ! width",
                },
                session_state=state,
                script_entries=[(ScriptType.SCRIPT_3D, "scripts/3d.gdl", "3D")],
                stamp_script_header_fn=lambda label, code, rev: f"! {label} rev {rev}\n{code}",
                clear_pending_preview_state_fn=lambda _state: calls.__setitem__("clear", calls["clear"] + 1),
            )

            self.assertEqual((script_count, param_count), (1, 1))
            self.assertIn("BLOCK 1, 1, 1", project.get_script(ScriptType.SCRIPT_3D))
            self.assertEqual(project.parameters[0].name, "A")
            self.assertIsNone(state.preview_2d_data)
            self.assertIsNone(state.preview_3d_data)
            self.assertEqual(state.preview_warnings, [])
            self.assertEqual(state.preview_meta, {"kind": "", "timestamp": ""})
            self.assertEqual(calls["clear"], 1)


if __name__ == "__main__":
    unittest.main()
