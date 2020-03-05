# with关键字使用
class AClassWithWith():
    def __init__(self):
        pass

    def __enter__(self):
        print("1.现在进入了，所以马上到这里，执行 __enter__ 这里的代码")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print("2.结束使用这个 class 时，会执行这里面的代码，用打印内容代替")
        else:
            print('------ %s' % exc_tb)


with AClassWithWith():
    print("3.这里的内容是class之外的操作，是在开始确认使用类AClassWithWith、执行 __enter__ 后才执行的，")
    print("4.执行完之后，就自动执行结束的 __exit__ 里面的内容，什么呢？如下：")
    raise IndexError('越界了')

AClassWithWith()
