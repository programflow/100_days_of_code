# new_list = [new_item for item in list]

name = "Kevin"
new_list = [letter for letter in name]
print(new_list)

# Conditional List Comprehension
# new_list = [new_item for item in list if test]

# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}

student_dict = {
    "student" :["Angela", "James", "Lily"],
    "score" : [56, 79, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value )

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)