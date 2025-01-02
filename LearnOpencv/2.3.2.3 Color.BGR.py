# 使用NumPy生成一个三维数组,用来模拟一幅 BGR 模式的彩色图像
# 使用NumPy中的 zeros()函数可以生成一个元素值都是 0 的数组,可以直接使用数行访问,修改
import numpy as np
img = np.zeros((2, 4, 3),dtype=np.uint8)   # 生成了一个2*4*3的数组,其对应一幅"2行4列3个通道"的 BGR 图像
print("img=\n", img)   # 使用print语句显示(打印)当前图像(数组)的值
print("读取像素img[0, 3]=", img[0, 3])   # img[0,3]语句会访问第0行第3列位置上的B通道,G通道,R通道的3个像素
print("读取图像img[1,2,2]=", img[1, 2, 2])   # img[1,2,2]语句会访问第1行第2列位置上的第2个通道(R通道)上的像素
img[0, 3] = 255  # img[0,3]=255语句会修改img图像中第0行第3列位置的像素值，该位置上的B通道，G通道，R通道位置的3个像素值都会被修改为255.
img[0, 0] = [66, 77, 88]   # img[0,0]=[66,77,88]语句会修改img图像中的第0行第0列位置的B通道, G通道, R通道的3个像素值, 将它们修改为[66,77,88]
img[1, 1, 1] = 3  # img[1,1,1]=3语句会修改img图像中的第1行第1列位置的第1个通道(G通道)位置的像素值, 将它修改为3
img[1, 2, 2] = 4  # img[1,2,2]=4语句会修改img图像中的第1行第2列位置的第2个通道(R通道)位置的像素值, 将它修改为4
img[0, 2, 0] = 5  # img[0,2,0]=5语句会修改img图像中的第0行第2列位置的第0个通道(B通道)位置的像素值, 将它修改为5
print("修改后img\n", img)
print("读取修改后像素 img[1,2,2]=", img[1, 2, 2])   #最后两行使用print()语句观察img和img[1,2,2]的值