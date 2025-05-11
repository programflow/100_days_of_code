import json
import argparse
from core import search_paths, format_path

def main():
    # Setup argument parsing
    parser = argparse.ArgumentParser(description="Recursive JSON key/value searcher.")
    parser.add_argument("file", help="Path to JSON file")
    parser.add_argument("--target", required=True, help="Target key or value to search for")
    parser.add_argument("--mode", choices=["key", "value"], default="key", help="Search by 'key' or 'value'")
    args = parser.parse_args()

    # Load the JSON data from file
    try:
        with open(args.file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Failed to load JSON: {e}")
        return

    # Run the recursive search and print formatted results
    try:
        results = search_paths(data, args.target, mode=args.mode)
        if results:
            print(f"\n🔍 Found {len(results)} match(es):")
            for path in results:
                print(" -", format_path(path))
        else:
            print("❌ No matches found.")
    except ValueError as e:
        print(f"❌ Error: {e}")

# Entry point for script usage
if __name__ == "__main__":
    main()
