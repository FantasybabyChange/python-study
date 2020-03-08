# 线程demo
import threading as thread
import time
from threading import current_thread


def print_function(a1, a2):
    time.sleep(1)
    print("threadName %s " % current_thread().getName(),end="")
    print('%s,%s' % (a1, a2))
    print()


for i in range(1, 6):
    # print_function(i, i + 1)
    # 创建线程并 开启
    thread_thread = thread.Thread(target=print_function, args=(i, i + 1))
    thread_thread.start()
print(current_thread().getName())