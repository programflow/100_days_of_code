#
# def depth(l,c):
#     if len(l) > 1:
#         if type(l[0]) is not list:
#             return depth(l[1:],c)
#         else:
#             return max(depth(l[0],c+1), depth(l[1:],c))
#     elif len(l) == 1:
#         if type(l[0]) is not list:
#             print("got to here")
#             return c+1
#         else:
#             return depth(l[0],c+1)
#     else:
#         return c+1

def depth(lst: list) -> int:
    if not isinstance(lst, list):
        return 0
    if not lst:
        return 1
    return 1 + max(depth(i) for i in lst if isinstance(i, list))

a = [1,[2],[3], 4, [3,[3,[4,[5]]]],1,2,3,[4]]
g = [1, [2,[3,4]], 5,[5,6,[7,[8]]]]
print(depth(a, 0))