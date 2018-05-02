# -*- coding: utf-8 -*-
# create array

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array((1, 2, 3, 4))
c = np.arange(5)
d = np.linspace(0, 2*np.pi, 5)

print a
print b
print c
print d

# 多维数组

a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])

print a

print a[0, 1:4]
print a[1:4, 0]
print a[::2, ::2]
print a[:, 1]

print type(a)
print a.dtype
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.ndim)
print(a.nbytes)


# 数组的一些操作符


a = np.arange(25)
a = a.reshape((5, 5))

b = np.arange(25)
b = b.reshape((5, 5))
# 基本操作符
print a + b
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
print(a < b)
print(a > b)

# 特殊操作符
# dot, sum, min, max, cumsum
print(a.dot(b))
print(a.sum())
print(a.min())
print(a.max())
print(a.cumsum())

# 高级索引

a = np.arange(0, 100, 10)
indexs = [1, 5, -1]
b = a[indexs]
c = a[:5]
d = a[a >= 50]

print(a)
print(b)
print(c)
print(d)


b = np.where(a < 50)
c = np.where(a >= 50)[0]

print(b)
print(c)
print(type(b))
print(type(c))
