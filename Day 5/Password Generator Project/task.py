letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random
def easy_password_generator():
    easy_password = ""

    for i in range(0,int(nr_letters)):
        index = random.randint(0,len(letters)-1)
        easy_password += letters[index]

    for j in range(0, int(nr_symbols)):
        index = random.randint(0,len(symbols)-1)
        easy_password += symbols[index]

    for k in range(0, int(nr_numbers)):
        index = random.randint(0,len(numbers)-1)
        easy_password += numbers[index]

    return easy_password


def scrambler(characters):
    characters_list = list(characters)

    password = ""
    for l in range(0, len(characters)):
        index = random.randint(0, len(characters_list)-1)
        password += characters_list[index]
        characters_list.remove(characters_list[index])

    #could also be done with random.shuffle(character_list)
    return password




print(scrambler(easy_password_generator()))

