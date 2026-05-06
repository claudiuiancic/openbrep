import importlib.util
import tempfile
import unittest
from pathlib import Path


def _load_lint_module():
    script = Path(__file__).parent.parent / "knowledge" / "scripts" / "lint-knowledge.py"
    spec = importlib.util.spec_from_file_location("lint_knowledge", script)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class TestKnowledgeLint(unittest.TestCase):
    def test_builtin_knowledge_lint_passes(self):
        lint_knowledge = _load_lint_module()
        root = Path(__file__).parent.parent / "knowledge"

        self.assertEqual(lint_knowledge.lint(str(root)), 0)

    def test_lint_fails_for_missing_archetype_field(self):
        lint_knowledge = _load_lint_module()
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "wiki").mkdir()
            (root / "wiki" / "BLOCK.md").write_text("---\ntype: reference\n---\n# BLOCK\n", encoding="utf-8")
            (root / "archetypes").mkdir()
            (root / "archetypes" / "bad.md").write_text(
                "---\n"
                "id: archetype.bad\n"
                "title: Bad\n"
                "type: archetype\n"
                "commands: [BLOCK]\n"
                "---\n"
                "# Bad\n",
                encoding="utf-8",
            )

            result = lint_knowledge.lint(str(root))

        self.assertEqual(result, 1)

    def test_officially_verified_wiki_pages_do_not_reintroduce_pseudo_syntax(self):
        root = Path(__file__).parent.parent / "knowledge" / "wiki"

        revolve = (root / "REVOLVE.md").read_text(encoding="utf-8")
        sweep = (root / "SWEEP.md").read_text(encoding="utf-8")
        project2 = (root / "PROJECT2.md").read_text(encoding="utf-8")
        hotspot2 = (root / "HOTSPOT2.md").read_text(encoding="utf-8")
        block = (root / "BLOCK.md").read_text(encoding="utf-8")

        self.assertIn("REVOLVE n, alpha, mask", revolve)
        self.assertNotIn("```gdl\nREVOLVE id, angle", revolve)
        self.assertIn("SWEEP n, m, alpha, scale, mask", sweep)
        self.assertNotIn("```gdl\nSWEEP path_id, sections_id", sweep)
        self.assertIn("PROJECT2 projection_code, angle, method", project2)
        self.assertNotIn("PROJECT2 [options]", project2)
        self.assertIn("HOTSPOT2 x, y [, unID", hotspot2)
        self.assertNotIn('HOTSPOT2 x, y, paramName', hotspot2)
        self.assertIn("a >= 0, b >= 0, c >= 0", block)


if __name__ == "__main__":
    unittest.main()
