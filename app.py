"""Evidence manifest generator for lab copies; reads files and hashes their contents."""
import hashlib, json, sys
from datetime import datetime, timezone
from pathlib import Path

def build_manifest(root):
    base=Path(root).resolve()
    if not base.is_dir(): raise ValueError("Evidence path must be a directory")
    entries=[]
    for path in sorted(p for p in base.rglob("*") if p.is_file()):
        h=hashlib.sha256()
        with path.open("rb") as f:
            for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
        entries.append({"path":str(path.relative_to(base)),"size_bytes":path.stat().st_size,"sha256":h.hexdigest()})
    return {"generated_utc":datetime.now(timezone.utc).isoformat(),"algorithm":"SHA-256","files":entries}
if __name__=="__main__":
    if len(sys.argv)!=2: raise SystemExit("Usage: python app.py <evidence-directory>")
    print(json.dumps(build_manifest(sys.argv[1]),indent=2))
