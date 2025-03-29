alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(original_text, shift_amount):
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

    new_string = ""

    for char in original_text:
        if char in alphabet:
            # if char.isupper():
            #     old_index = alphabet.index(char.lower())
            #     new_index = old_index + new_shift
            #     new_string += alphabet[new_index].upper()
            # else:
            old_index = alphabet.index(char)
            new_index = (old_index + shift_amount) % len(alphabet)

            new_string += alphabet[new_index]

        else:
            new_string += char

    print(new_string)
if direction == "encrypt":
    encrypt(text, shift)




