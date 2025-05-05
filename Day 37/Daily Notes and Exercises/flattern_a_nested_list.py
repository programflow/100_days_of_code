
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
    result = []
    for i in lst:
        if isinstance(i, list):
            result = flatten(i)
        else:
            result.append(i)
    return result



print(flatten([1, [2,[3,4]], 5])) # expected output: [1,2,3,4,5]