def search_paths(data, target, mode="key", path=None, results=None):
    """
    Recursively search a nested dict/list for matching keys or values.

    Parameters:
        data: The JSON object (dict or list)
        target: The key or value to search for
        mode: 'key' or 'value' (search mode)
        path: Internal accumulator to track the current path
        results: Accumulator list to store found paths

    Returns:
        List of full paths to the matched keys/values
    """
    if results is None:
        results = []
    if path is None:
        path = []

    # Reject invalid mode
    if mode not in ("key", "value"):
        raise ValueError("Invalid mode. Use 'key' or 'value'.")

    # If the current level is a dictionary
    if isinstance(data, dict):
        for k, v in data.items():
            current_path = path + [k]  # Append current key to path

            # If searching by key and this key matches
            if mode == "key" and k == target:
                results.append(current_path)

            # If searching by value and this value matches
            if mode == "value" and v == target:
                results.append(current_path)

            # Recurse deeper if the value is a nested container
            if isinstance(v, (dict, list)):
                search_paths(v, target, mode, current_path, results)

    # If the current level is a list
    elif isinstance(data, list):
        for i, item in enumerate(data):
            current_path = path + [i]  # Track index in path
            if isinstance(item, (dict, list)):
                search_paths(item, target, mode, current_path, results)

    return results


def format_path(path):
    """
    Format a list path (e.g., ['tags', 1, 'lang']) into a string:
    tags[1].lang
    """
    formatted = ""
    for part in path:
        if isinstance(part, int):
            formatted += f"[{part}]"
        else:
            if formatted and not formatted.endswith("]"):
                formatted += "."
            formatted += str(part)
    return formatted
