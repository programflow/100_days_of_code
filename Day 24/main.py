# This is practice using the open function

# file= open("my_file.txt","r", encoding="utf-8" )
# contents = file.read()
# print(contents)
#
# file.close()

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode='a') as file:
    file.write("\nNew Line")

with open("../../../new_file.txt", mode='a') as file:
    file.write("This a new file.")

