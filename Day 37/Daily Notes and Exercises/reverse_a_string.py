
def reverse_a_string(s):
    """This function takes a string and returns the reversed string
    through recursive calls"""
    if len(s) == 1:
        return s
    else:
        return reverse_a_string(s[1:]) + s[0]


# print(reverse_a_string("hello")) #Expect output: olleh
#
