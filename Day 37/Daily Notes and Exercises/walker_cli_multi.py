
import argparse
from pathlib import Path

def walk(path: Path, exts: list[str], max_depth: int, current_depth: int = 0) -> list[Path]:
    collected_files = []
    for item in path.iterdir():
        if item.is_file() and item.suffix in exts:
            collected_files.append(item)
        elif item.is_dir() and current_depth < max_depth:
            collected_files += walk(item, exts, max_depth, current_depth + 1)
    return collected_files

def main():
    parser = argparse.ArgumentParser(description="Recursive file walker with multiple extension support.")
    parser.add_argument("--path", type=str, required=True, help="Root directory to start search")
    parser.add_argument("--ext", type=str, nargs='+', required=True, help="File extensions to include (e.g. .py .md)")
    parser.add_argument("--max-depth", type=int, default=2, help="Maximum recursion depth")

    args = parser.parse_args()
    root = Path(args.path)

    if not root.exists():
        print(f"Path '{args.path}' does not exist.")
        return

    files = walk(root, args.ext, args.max_depth)
    for f in files:
        print(f)

if __name__ == "__main__":
    main()
