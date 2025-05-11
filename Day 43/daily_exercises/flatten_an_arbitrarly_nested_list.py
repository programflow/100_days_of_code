# Problem Statement:
# Write a recursive function flatten(nested_list) that takes a list containing arbitrary level of nested sublists and
# returns a flat list containing all the elements in order.

# def flatten(l):
#     if len(l) >1:
#         if type(l[0]) is not list:
#             return [l[0]] + flatten(l[1:])
#         else:
#             return flatten(l[0]) + flatten(l[1:])
#     else:
#         if type(l[0]) is not list:
#             return l
#         else:
#             return flatten(l[0])


def flatten(l):
    if not l:
        return []

    head, *tail = l
    if isinstance(head, list):
        return flatten(head) + flatten(tail)
    else:
        return [head] + flatten(tail)


x= flatten([1, [2, 3], [4, [5, 6]], 7])
# Output: [1, 2, 3, 4, 5, 6, 7]

y= flatten([[1, [2]], 3, [[4, [5]], 6]])
# Output: [1, 2, 3, 4, 5, 6]

print(flatten([[[[1]]], 2, [3, [4, [5]]]]))  # [1, 2, 3, 4, 5]
print(flatten([1, [], [2, [3, []]], 4]))     # [1, 2, 3, 4]
print(flatten([]))                          # []
print(flatten([[[[]]]]))                    # []

print(x)
print(y)