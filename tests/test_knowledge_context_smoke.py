import importlib.util
import sys
import unittest
from pathlib import Path


def _load_smoke_module():
    script = Path(__file__).parent.parent / "scripts" / "knowledge_context_smoke.py"
    spec = importlib.util.spec_from_file_location("knowledge_context_smoke", script)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class TestKnowledgeContextSmoke(unittest.TestCase):
    def test_builtin_smoke_cases_pass(self):
        smoke = _load_smoke_module()

        self.assertEqual(smoke.main(["--json"]), 0)


if __name__ == "__main__":
    unittest.main()
