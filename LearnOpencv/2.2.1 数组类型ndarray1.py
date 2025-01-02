# 数组类型 ndarray
import numpy as np   #导入Numpy库
# 通过元组tuple构建数组
pytuple = (1, 2, 3)
array1 = np.array(pytuple)
print("通过元组tuple构建数组:\n", array1)
# 通过列表list构建数组
pylist = [4, 5, 6]
array2 = np.array(pylist)
print("通过列表list构建数组:\n", array2)
# 构建多维的数组
pylist1 = [1, 2, 3]
pylist2 = [4, 5, 6]
marray = np.array([pylist1, pylist2])
print("构建多维的数组:\n", marray)