import matplotlib.pyplot as plt

# 绘制一条曲线
plt.plot([1, 3, 5], [4, 8, 10])
import numpy as np

x = np.linspace(-np.pi, np.pi, 100)
plt.plot(x, np.cos(x))

x1 = np.linspace(-np.pi * 2, np.pi * 2, 100)
plt.figure(1, dpi=50)
for i in range(1, 5):
    plt.plot(x1, np.sin(x1 / i))

data = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 6, 4]
plt.hist(data)  # 直方图

x2 = np.arange(1, 10)
y2 = x2
plt.scatter(x2, y2, c='r', marker='o')  # c='r'表示红色 marker表示指定三点多形状为原型
plt.show()
