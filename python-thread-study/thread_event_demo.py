# coding:utf-8

import threading
import time

event = threading.Event()


def chihuoguo(name):
    # 等待事件，进入等待阻塞状态
    print('%s 已经启动' % threading.currentThread().getName())
    print('小伙伴 %s 已经进入就餐状态！' % name)
    time.sleep(1)
    event.wait()
    # 收到事件后进入运行状态
    print('%s 收到通知了.' % threading.currentThread().getName())
    print('小伙伴 %s 开始吃咯！' % name)


# 设置线程组
threads = []

# 创建新线程
thread1 = threading.Thread(target=chihuoguo, args=("a",))
thread2 = threading.Thread(target=chihuoguo, args=("b",))

# 添加到线程组
threads.append(thread1)
threads.append(thread2)

# 开启线程
for thread in threads:
    thread.start()

time.sleep(2)
# 发送事件通知
print('主线程通知小伙伴开吃咯！')
event.set()
