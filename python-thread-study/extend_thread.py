# 继承线程 防止主流程先结束
import threading as thread
import time
from threading import current_thread


class MyThread(thread.Thread):
    def __init__(self, a1, a2):
        thread.Thread.__init__(self)
        self.a1 = a1
        self.a2 = a2

    def run(self):
        time.sleep(1)
        print("threadName %s " % current_thread().getName(), end="")
        print('%s,%s' % (self.a1, self.a2))


for i in range(1, 6):
    my_thread = MyThread(i, i + 1)
    my_thread.start()
    my_thread.join()

print("threadName %s " % current_thread().getName())
