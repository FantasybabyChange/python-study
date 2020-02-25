import functools as ft
# 内置函数
# filter()
arrs = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x + 1 < 4, arrs))
print(result)
# map
arrs2 = [3, 1, 2, 6, 7]
result2 = list(map(lambda x, y: x+y, arrs, arrs2))
print(result2)
# reduce
arrs3 = [1, 2, 3, 4, 5]
r3 = ft.reduce(lambda x, y: x+y, arrs3)
print(r3)  # 1+2+3+4+5
r4 = ft.reduce(lambda x, y: x+y, arrs3, 1)
print(r4)  # 1+2+3+4+5+1
# zip
a1 = [1, 2, 3]
a2 = [3, 4, 5]
r5 = list(zip(a1, a2))
print(r5)  # [(1, 3), (2, 4), (3, 5)]
d1 = {'a': 'c', 'b': 'd'}
newd = {}
r6 = dict(zip(d1.values(), d1.keys()))
print(r6)  # {'c': 'a', 'd': 'b'}

