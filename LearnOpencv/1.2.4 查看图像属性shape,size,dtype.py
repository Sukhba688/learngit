# 查看图像属性 (行,列,通道,图像数据类型,像素数目)
import cv2
img = cv2.imread("LearnOpencv\lena.bmp")
# img.shape 获取图像的形状,返回一个包含行数,列数,通道数的元组
print("图像形状:", img.shape)
# img.size 返回图像的像素数目
print("像素数目", img.size)
# img.dtype 返回图像的数据类型
print("数据类型", img.dtype)