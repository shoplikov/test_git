import os
import sys
from pathlib import Path


def analyze_directory(path):
    p = Path(path)

    if not p.exists():
        print(f"Error: '{path}' does not exist.")
        sys.exit(1)

    files = list(p.rglob("*"))

    total_files = 0
    total_size = 0
    extensions = {}

    for f in files:
        if f.is_file():
            total_files += 1
            size = f.stat().st_size
            total_size += size
            ext = f.suffix.lower() or "no extension"
            extensions[ext] = extensions.get(ext, 0) + 1

    print(f"\n📁 Directory: {p.resolve()}")
    print(f"📄 Total files: {total_files}")
    print(f"💾 Total size: {total_size / 1024:.2f} KB")
    avg_size = total_size / total_files if total_files else 0
    print(f"📦 Average file size: {avg_size / 1024:.2f} KB")
    print("\n📊 Files by extension:")

    for ext, count in sorted(extensions.items(), key=lambda x: x[1], reverse=True):
        print(f"  {ext}: {count}")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    analyze_directory(path)
