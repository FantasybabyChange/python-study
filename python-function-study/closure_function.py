# 闭包
def cl_function(a):
    def inner_function(b):
        return a + b

    return inner_function


inner = cl_function(1)
print(inner(3))


# 实现一个计数器
def create_counter():
    i = 0

    def counter():
        nonlocal i
        i += 1
        return i

    return counter


counterA = create_counter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = create_counter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
