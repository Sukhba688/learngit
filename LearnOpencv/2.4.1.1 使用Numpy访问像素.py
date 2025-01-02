# 使用Numpy访问像素
# item()函数能够访问图像的像素,其语法格式为:
# item((row, column),value)  其中(row, column)为像素索引,value为新值

# 使用NumPy生成一个二维随机数组,用来模拟一幅灰度图像,并对其像素进行访问修改

import numpy as np
img = np.random.randint(10, 99, size =[8, 8],dtype=np.uint8)
print("img=\n", img)
print("读取像素img.item(4,4)=", img.item(3,2))
img[3, 2] = 255
print("修改后img=\n", img)
print("修改后的像素img.item(4, 4)=", img.item(3,2))