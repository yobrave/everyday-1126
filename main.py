from __future__ import annotations

import json
import os
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.txt"


def read_two_lines() -> str:
    text = SOURCE.read_text(encoding="utf-8").strip()
    if not text:
        raise SystemExit("entry.txt is empty")
    if len(text) > 400:
        raise SystemExit(f"entry too long for the gate: {len(text)} chars")
    return text


def publish(text: str) -> Path:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(text + "\n", encoding="utf-8", newline="\n")
    return target


def main() -> None:
    lines = read_two_lines()
    where = publish(lines)
    print(json.dumps({"ok": True, "chars": len(lines), "written": str(where)}))


if __name__ == "__main__":
    main()
