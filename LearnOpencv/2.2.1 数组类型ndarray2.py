# 构建多维数组,并查看其常用属性
import numpy as np
# 构建多维的数组
pylist1 = [1, 2, 3]
pylist2 = [4, 5, 6]
marray = np.array([pylist1, pylist2])
print("构建多维的数组:\n", marray)
# T: 转置数组,如果维度小于2就返回矩阵本身
print("转置 T:\n", marray.T)
# size: 数组中元素的个数
print("数组中元素个数 size:\n", marray.size)
# itemsize: 数组中单个元素的字节数
print("数组中单个元素的字节数 itemsize:\n", marray.itemsize)
# dtype: 数组元素的数据类型对象
print("数组元素的数据类型对象 dtype:\n", marray.dtype)
# ndim: 数组的维度
print("数组的维度 ndim:\n", marray.ndim)
# shape: 数组的形状
print("数组的形状 shape:\n", marray.shape)
# data:指向存放数组数据的Python buffer对象
print("指向存放数组数据的Python buffer对象 data:\n", marray.data)
# flat: 返回数组的一维迭代器
print("数组的一维迭代器: \n")
for item in marray.flat:
    print(item)
# nbytes: 数组中所有元素的字节数
print("数组中所有元素的字节数 nbytes: \n",marray.nbytes)