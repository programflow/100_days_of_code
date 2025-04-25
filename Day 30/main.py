#FileNotFound
# with oepn("a_file.txt") as file:
#     file.read()


# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sdfsdf"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
# except KeyError:
#     print("That key does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is a made up error.")


height = float(input("Height: "))
weight = int(input("Weight: "))
if height > 3:
    raise ValueError("Height should not be greater than 3 meters.")
bmi = weight / (height ** 2)
print(bmi)





#Key Error
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

#IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text +5)