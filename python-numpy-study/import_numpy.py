# numpy
import numpy as np

array = np.array([2, 3, 4])
print(array)
print(array.dtype)

array1 = np.array([1.2, 1.3, 1.4])
print(array1)
print(array1.dtype)

print(array + array1)

print(array * 10)

zero_array = np.zeros(10)
print(zero_array)

zero_array = np.zeros((3, 5))
print(zero_array)

ones = np.ones(3)
print(ones)

empty = np.empty((3, 2, 3))
print(empty)

arange = np.arange(10)

print(arange[2:7])

arange_copy = arange[7:10].copy()
arange_copy[:] = 1
print(arange_copy)
