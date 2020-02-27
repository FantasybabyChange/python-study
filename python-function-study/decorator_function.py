# 装饰器
def wrapper_type(str):
    def wrapper(func):
        def inner_wrapper():
            print(func.__name__ + '--' + str)
            print('start')
            func()
            print('stop')

        return inner_wrapper

    return wrapper


@wrapper_type('hello')
def inner_function():
    print('inner_function')


@wrapper_type('hello2')
def inner_function2():
    print('inner_function2')


inner_function()
inner_function2()