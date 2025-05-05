import os


def search_py_files(p):
    collected_files = []
    if os.path.isdir(p):
        for file in os.listdir(p):
            file_path = os.path.join(p, file)
            if os.path.isfile(file_path) and file_path.endswith(".py"):
                collected_files.append(file_path)
            else:
                collected_files += search_py_files(file_path)
    return collected_files

print("\n".join(search_py_files(".")))




# for name in os.listdir('.'):
#     if os.path.isfile(name):

# from pathlib import Path
# path = Path("myfolder")
# for item in path.iterdir():
#     if item.is_dir():
#         # recurse in it
#     elif item.name.endswith(".py"):
#         # collect it


# def search_py_files(p):
#     # LOOK AT A FOLDER
#     list = os.listdir(p)
#     if os.path.isfile(list[0]) and list[0].endswith(".py"):
#         return [list[0]]
#     else:
#         return search_py_files(p + "/" + list[0])

# def walk_directory(p):
#     for itme in path:
#         if item is a file and endswith(".py"):
#             do something
#         elif item is a directory:
#             c
#







# start_point = "test_root"
#
#
# search_py_files(start_point)