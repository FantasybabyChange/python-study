# 引用传递
def func(first, *other):
    first['a'] = 'c'


a = {'a': 'b'}
func(a, 2, 3)
print(a)
