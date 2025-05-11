def search_json(data, target, search_by="key", found=None):
    if found is None:
        found = []

    if isinstance(data, dict):
        for k, v in data.items():
            if search_by == "key" and k == target:
                found.append(v)
            elif search_by == "value" and v == target:
                found.append(k)
            # Recurse deeper
            search_json(v, target, search_by, found)

    elif isinstance(data, list):
        for item in data:
            search_json(item, target, search_by, found)

    return found

sample = {
    "user": {
        "name": "Alice",
        "email": "alice@example.com",
        "location": {
            "city": "Wonderland",
            "postal": 12345
        }
    },
    "tags": ["python", {"lang": "Python"}]
}

# Find all values under the key "city"
print(search_json(sample, "city", search_by="key"))
# Output: ['Wonderland']

# Find all keys that have the value "Python"
print(search_json(sample, "Python", search_by="value"))
# Output: ['lang']
