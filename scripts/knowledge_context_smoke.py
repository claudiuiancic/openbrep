#!/usr/bin/env python3
"""Smoke-test GDL knowledge selection for representative generation goals."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from openbrep.knowledge import KnowledgeBase  # noqa: E402
from openbrep.knowledge_selector import select_gdl_knowledge  # noqa: E402


@dataclass(frozen=True)
class SmokeCase:
    name: str
    instruction: str
    expected_sources: tuple[str, ...]


CASES = (
    SmokeCase("bookshelf", "做一个专业一点的参数化书架", ("archetype.bookshelf", "wiki.BLOCK")),
    SmokeCase("cabinet", "生成一个带门板和层板的收纳柜", ("archetype.cabinet", "wiki.BLOCK")),
    SmokeCase("table", "做一个会议桌", ("archetype.table", "wiki.BLOCK")),
    SmokeCase("door", "生成一个带门框的门", ("archetype.door", "wiki.Object_Types")),
    SmokeCase("window", "生成一个三分格窗户", ("archetype.window", "wiki.Object_Types")),
    SmokeCase("profile", "做一个旋转体花瓶", ("archetype.profile_object", "wiki.REVOLVE")),
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--knowledge-dir", default=str(ROOT / "knowledge"))
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    args = parser.parse_args(argv)

    knowledge_dir = Path(args.knowledge_dir).expanduser()
    kb = KnowledgeBase(str(knowledge_dir))
    kb.load()
    base_context = kb.get_by_task_type("all")

    rows = []
    failures = []
    for case in CASES:
        selection = select_gdl_knowledge(
            instruction=case.instruction,
            intent="CREATE",
            knowledge_dir=knowledge_dir,
            base_context=base_context,
        )
        missing = [source for source in case.expected_sources if source not in selection.source_ids]
        row = {
            "name": case.name,
            "instruction": case.instruction,
            "expected_sources": list(case.expected_sources),
            "source_ids": selection.source_ids,
            "planner_context_chars": len(selection.planner_context),
            "generation_context_chars": len(selection.generation_context),
            "ok": not missing,
            "missing": missing,
        }
        rows.append(row)
        if missing:
            failures.append(row)

    payload = {"ok": not failures, "cases": rows}
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for row in rows:
            status = "OK" if row["ok"] else "FAIL"
            print(f"{status} {row['name']}: {', '.join(row['source_ids'])}")
            if row["missing"]:
                print(f"  missing: {', '.join(row['missing'])}")

    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
