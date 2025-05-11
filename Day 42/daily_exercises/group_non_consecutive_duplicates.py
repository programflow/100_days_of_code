#Challenge: Group Non-Consecutive Duplicates
#Constraints:
# keep sublists in order of ifrst appearance in the input list
# don't use collections.Counter or similar helpers
# stick with basic python types

# def group_all_duplicates(lst):
#     """Groups all items with the same value into sublists, regardless of position, while preserving the order of first appearance."""
#     result = []
#
#     for item in lst:
#         if len(result) < 1:
#             result.append([item])
#         else:
#             in_a_group = False
#             for group in result:
#                 if item in group:
#                     in_a_group = True
#                     group.append(item)
#             if not in_a_group:
#                 result.append([item])
#
#     return result

def group_all_duplicates(lst):
    """Groups all items with the same value into sublists, regardless of position, while preserving the order of first appearance."""
    result = []

    for item in lst:
        if not result:
            result.append([item])

        else:
            in_a_group = False
            for group in result:
                if item in group:
                    in_a_group = True
                    group.append(item)
                    break # Stop searching after we found the match
            if not in_a_group:
                result.append([item])


    return result





x= group_all_duplicates([1, 1, 2, 2, 2, 3, 1, 1])
print(x)
# ➞ [[1, 1, 1, 1], [2, 2, 2], [3]]


y = group_all_duplicates(['a', 'a', 'b', 'a'])
print(y)
# ➞ [['a', 'a', 'a'], ['b']]
