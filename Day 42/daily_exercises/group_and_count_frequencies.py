# Challenge: Group and Count Frequencies
# Constraints:
# - No collections.Counter
# - Use only basic types: lists, dicts, etc.
# - Maintain original first appearance order


def count_all_duplicates(lst):
    """
    Returns a list of tuples, where each tuple contains:
    -the item
    -the total count of that item in the list
    _(in order of the first appearance)
    """
    result = []
    for item in lst:
        if not result:

            result.append((item, 1 ))
        else:
            counted = False
            for i in range(len(result)):
                if result[i][0] == item:
                    result[i] = (result[i][0], result[i][1] + 1)
                    counted = True
                    break

            if not counted:
                result.append((item, 1))

    return result


x =count_all_duplicates(['a', 'b', 'a', 'a', 'b', 'c'])
# ➞ [('a', 3), ('b', 2), ('c', 1)]
y =count_all_duplicates([1, 2, 1, 3, 2, 1])
# ➞ [(1, 3), (2, 2), (3, 1)]

print(x)
print(y)