from pathlib import Path

from pandas.io.sas.sas_constants import column_type_length


def walk(path: Path) -> list[Path]:
    collected_files = []
    for item in path.iterdir():
        if item.is_file() and item.suffix in [".py",".md"]:
            collected_files.append(item)
        elif item.is_dir():
            collected_files += walk(item)
    return collected_files


root = Path(".")
files = walk(root)
for f in files:
    print(f)
    print(f.resolve())
    print(f.name)