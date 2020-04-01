from pandas import Series, DataFrame
import pandas as pd

data = {
    "name": ["liu", "aliu1", "cliu2", "bliu3"]
    , "age": [15, 16, 17, 17]
    , "grade": [99, 100, 77, 77]
}

frame = DataFrame(data)
print(frame)
# 排序
frame2 = DataFrame(data, columns=["grade", "age", "name"])
print(frame2)
print(frame2["age"])
print(frame2.grade)
frame2["older"] = frame2.age > 16
# 交换行和列的索引
print(frame2.T)
# 重新索引
obj3 = Series(["1", "2", "4", "3"], index=["a", "b", "c", "d"])
obj4 = obj3.reindex(index=["d", "c", "e", "f", "g"], fill_value=0)
print(obj4)
obj5 = Series(["a", "b", "c"], index=[0, 3, 5])
# 使用前一个值填充
obj6 = obj5.reindex(range(6), method="ffill")
print(obj6)
# 使用后一个值填充
obj7 = obj5.reindex(range(6), method="bfill")
print(obj7)

# 过滤缺失值
from numpy import nan as NA

data = Series([1, NA, 2])
print(data)
print(data.dropna())

data = DataFrame([[1, 2, 3, NA], [1, NA, 3, NA], [NA, NA, NA]])
print(data)
# 删除整行都是缺失值的
# print(data.dropna(how="all"))
# 删除缺失的一列
print(data.dropna(axis=1, how="all"))
