from pathlib import Path

def walk1(path: Path, max_depth: int, current_depth: int = 0) -> list[Path]:
    collected_files = []
    for item in path.iterdir():
        if item.is_file() and item.suffix in [".py", ".md"]:
            collected_files.append(item)
        elif item.is_dir() and current_depth < max_depth:
            collected_files += walk1(item, max_depth, current_depth + 1)
    return collected_files

# Usage
root = Path(".")
files = walk1(root, max_depth=2)

for f in files:
    print(f)



def walk2(path: Path, depth=0, max_depth=2) -> list[Path]:
    collected_files = []
    if depth > max_depth:
        return collected_files

    for item in path.iterdir():
        if item.is_file() and item.suffix in [".py", ".md"]:
            collected_files.append(item)
        elif item.is_dir():
            collected_files += walk2(item, depth + 1, max_depth)
    return collected_files

# Usage
root = Path(".")
files = walk2(root, max_depth=2)  # Limit to 2 levels deep
for f in files:
    print(f)
