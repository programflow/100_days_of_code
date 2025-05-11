def search_key_paths(data, target_key, path=None, results=None):
    if results is None:
        results = []
    if path is None:
        path = []

    if isinstance(data, dict):
        for k, v in data.items():
            current_path = path + [k]
            if k == target_key:
                results.append(current_path)
            

            search_key_paths(v, target_key, current_path, results)

    elif isinstance(data,list):
        for i, item in enumerate(data):
            current_path = path + [i]
            search_key_paths(item, target_key, current_path, results)

    return results

nested = {
    "user": {
        "name": "Alice",
        "location": {
            "city": "Wonderland",
            "postal": 12345
        }
    },
    "alt": {
        "city": "Otherland"
    }
}

print(search_key_paths(nested, "city"))
# Output: [['user', 'location', 'city'], ['alt', 'city']]
