from reverse_a_string import reverse_a_string

def is_palindrome(s):
    if s.lower() == reverse_a_string(s).lower():
        return True
    else:
        return False

print(is_palindrome("raCecar"))
print(is_palindrome("python"))
