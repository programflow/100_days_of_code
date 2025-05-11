# Challenge: Recursive Palindrome Check
# Requirements:
# - Use recursion to check symmetry
# - do not reverse the string or use slicing
# - only basic string ops and recursion logic


def is_clean_palindrome(s, left=0, right=None):
    """
    That resturns True if the input string is a palindrome, ignoring:
    - Case ("A" == "a")
    - Non-alphanumeric characters
    """
    if right is None:
        right = len(s) -1

    while left < right and not s[left].isalnum():
        left += 1
    while left < right and not s[right].isalnum():
        right -= 1

    if left >= right:
        return True

    if s[left].lower() != s[right].lower():
        return False

    return is_clean_palindrome(s, left+1, right-1)





x= is_clean_palindrome("Racecar")
# ➞ True
print(x)

is_clean_palindrome("A man, a plan, a canal: Panama")
# ➞ True

is_clean_palindrome("No 'x' in Nixon!")
# ➞ True

is_clean_palindrome("This is not one.")
# ➞ False
