# 定义函数
def func(first, *other):
    """definition a function ."""
    print(first)
    first['a'] = 'c'
    print(other[0])
    return 0


a = {'a': 'b'}
print(func(a, 2, 3))
print(a)


# 默认值定义
def default_value(p, p1=4, p2=7):
    print('%s,%s,%s' % (p, p1, p2))


default_value(1, 5)
# 1, 5, 7
# 关键字调用
default_value(p=1, p2=9)


# 1, 4, 9

# 定义字典接收参数
def dic_param(p, **name):
    print(p)
    print(name)


dic_param(1, **{'a': 'b'})


# 位置参数 和 关键字参数
def positional_keywords(a, b, /, c, d, *, e, f):
    print('%s,%s,%s,%s,%s,%s' % (a, b, c, d, e, f))


# positional_keywords(b='1',a='2',c='3',d='4',e='5',f='6')
# TypeError: positional_keywords() got some positional-only arguments passed as keyword arguments: 'a, b'
# positional_keywords('1','2','3','4','5','6')
# TypeError: positional_keywords() takes 4 positional arguments but 6 were given
def foo(name, **kwds):
    return 'name' in kwds


print(foo(1, **{'name1': 2}))


# 任意长度的函数
def any_length(*args):
    print(*args)


any_length(1, 2, 3, 4)
