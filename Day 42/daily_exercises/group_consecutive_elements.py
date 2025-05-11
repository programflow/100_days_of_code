# Challenge: Group Consecutive Elements
# Constraints:
# - don't use any external libraries
# - maintain original order
# - only group consecutive duplicates


# def group_consecutive(lst):
#     """take a list and groups consecutive repeating elements into sublists"""
#     result = []
#     current_group = []
#     current_value = None
#     for i in range(len(lst)):
#         if lst[i] != current_value:
#             if len(current_group) > 0:
#                 result.append(current_group)
#             current_value = lst[i]
#             current_group = []
#             current_group.append(lst[i])
#         else:
#             current_group.append(lst[i])
#
#     result.append(current_group)
#     return result

def group_consecutive(lst):
    """take a list and groups consecutive repeating elements into sublists"""
    result = []
    current_group = []
    current_value = None
    for item in lst:
        if item != current_value:
            if current_group:
                result.append(current_group)
            current_group = [item]
            current_value = item
        else:
            current_group.append(item)

    result.append(current_group)
    return result









print(group_consecutive([1, 1, 2, 2, 2, 3, 1, 1]))
# ➞ [[1, 1], [2, 2, 2], [3], [1, 1]]

print(group_consecutive(['a', 'a', 'b', 'a']))
# ➞ [['a', 'a'], ['b'], ['a']]
