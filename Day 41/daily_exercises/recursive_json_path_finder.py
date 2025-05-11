def search_paths(data, target, mode="key", path=None, results=None):
    if results is None:
        results = []
    if path is None:
        path = []

    if mode not in ("key", "value"):
        raise ValueError("Invalid mode. Use 'key' or 'value'.")

    # Base case: If not traversable, return
    if not isinstance(data, (dict, list)):
        return results

    if isinstance(data, dict):
        for k, v in data.items():
            current_path = path + [k]

            if mode == "key" and k == target:
                results.append(current_path)

            if mode == "value" and v == target:
                results.append(current_path)

            # Recurse only if v is a dict or list
            if isinstance(v, (dict, list)):
                search_paths(v, target, mode, current_path, results)

    elif isinstance(data, list):
        for i, item in enumerate(data):
            current_path = path + [i]
            if isinstance(item, (dict, list)):
                search_paths(item, target, mode, current_path, results)

    return results

# try:
#     search_paths({}, "x", mode="wrong")
# except ValueError as e:
#     print(e)  # Output: Invalid mode. Use 'key' or 'value'.


#
# def find_key_paths(data, "page")
#
# find_key_paths(data, "page")
# Output: ['user.history[0].page', 'user.history[1].page']



def find_key_paths(data,key):
    paths_as_string = []
    paths_as_list = search_paths(data, key, mode="key")


    for path in paths_as_list:

        string_path= ""
        for item in path:

            if isinstance(item, str):

                string_path = string_path + f".{item}"
                print(string_path)
            elif isinstance(item, int):
                string_path = string_path + f"[{item}]"
        string_path = string_path[1:]
        paths_as_string.append(string_path)

    return paths_as_string


data = {
    "user": {
        "profile": {
            "name": "Alice",
            "age": 30
        },
        "history": [
            {"page": "home"},
            {"page": "about"}
        ]
    }
}
# print(find_key_paths(data, "page"))

