from json_searcher import search_paths, format_path
import json

with open("test_data.json") as f:
    data = json.load(f)

# Search for all values "Python"
results = search_paths(data, "Python", mode="value")
for path in results:
    print("Found at:", format_path(path))
