def find_key_paths(data, target_key, current_path=""):
    paths = []

    # Your logic here...

    return paths

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

find_key_paths(data, "page")
# Output: ['user.history[0].page', 'user.history[1].page']
