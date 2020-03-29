from pandas import Series, DataFrame
import pandas as pd

obj = Series([4, 5, 6, -7])
print(obj)
print(obj.index)
print(obj.values)

obj2 = Series([2, 3, 5, 6], index=["a", "b", "c", "d"])
print(obj2)
obj2["c"] = 12
print(obj2)
print("d" in obj2)
