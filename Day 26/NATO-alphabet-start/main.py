# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_phonetic_alphabet.iterrows()}
print(nato_alphabet_dict)
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

running = True
def generate_code():
    word = input("Enter a word: ").strip()
    try:
        output = [nato_alphabet_dict[letter.upper()] for letter in word]
    except KeyError as e:
        print(f"Invalid character: {e}. Please enter letters only.")
        generate_code()
    else:
        print(output)
        running = False

generate_code()