#!/usr/bin/env python3
import json, os
from pathlib import Path

index_dir = Path("index")
meta_path = index_dir / "meta.json"

if not meta_path.exists():
    print("No meta.json found.")
    raise SystemExit

with open(meta_path, "r", encoding="utf-8") as f:
    meta = json.load(f)

existing = {}
for fpath, info in meta.get("files", {}).items():
    if os.path.exists(fpath):
        size = os.path.getsize(fpath)
        if size >= 10 * 1024:
            existing[fpath] = info
        else:
            print(f"Removing {fpath} ({size} bytes)")
    else:
        print(f"Missing file: {fpath} – removed")

meta["files"] = existing

with open(meta_path, "w", encoding="utf-8") as f:
    json.dump(meta, f, indent=2, ensure_ascii=False)

print(f"[✓] Cleaned metadata; {len(existing)} valid file entries remain.")
