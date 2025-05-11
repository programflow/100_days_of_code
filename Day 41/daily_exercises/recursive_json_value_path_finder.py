def search_value_paths(data, target_value, path=None, results=None):
    if results is None:
        results = []
    if path is None:
        path = []

    if isinstance(data, dict):
        for k, v in data.items():
            current_path = path + [k]
            if v == target_value:
                results.append(current_path)
            else:
                search_value_paths(v, target_value, current_path, results)

    elif isinstance(data, list):
        for i, item in enumerate(data):
            current_path = path + [i]
            search_value_paths(item, target_value, current_path, results)

    return results

print(search_value_paths(data, "Python"))
# Output: [['tags', 0], ['tags', 1, 'lang']]
