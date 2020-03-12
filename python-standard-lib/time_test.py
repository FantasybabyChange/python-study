# 时间模块
import time
import datetime

# 1970 1 1
print(time.time())

print(time.localtime())

print(time.strftime('%y-%m-%d %H:%M:%S'))

print(datetime.datetime.now())
new_time = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + new_time)

one_day = datetime.datetime(2019, 11, 10)
new_time = datetime.timedelta(days=10)

print(one_day + new_time)
