# 生产消费者
from threading import Thread, current_thread
import random
import time
from queue import Queue

queue = Queue(5)


class ProducerThread(Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        while True:
            num = random.choice(nums)
            print('生产者 %s 生产了数据 %s' % (name, num))
            queue.put(num)
            queue.put(num+10)
            t = random.randint(1, 3)
            time.sleep(t)
            print('生产者 %s 休眠了 %s 秒' % (name, t))


class ConsumerThread(Thread):
    def run(self):
        name = current_thread().getName()
        while True:
            num = queue.get()
            queue.task_done()
            print('消费者 %s 消耗了数据 %s' % (name, num))
            t = random.randint(1, 5)
            time.sleep(t)
            print('消费者 %s 休眠了 %s 秒' % (name, t))


p1 = ProducerThread(name='p1')
p1.start()
c1 = ConsumerThread(name='c1')
c1.start()
c2 = ConsumerThread(name='c2')
c2.start()
