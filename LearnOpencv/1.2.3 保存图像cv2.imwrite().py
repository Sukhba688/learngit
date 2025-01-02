# 保存图像 ps:保存成功返回True,保存失败返回Flash
# cv2.imwrite(filename,img[,params])
import cv2  # 调用函数
lena = cv2.imread("LearnOpencv\lena.bmp")  # 读取图像
cv2.imwrite("result.bmp", lena)  #以"result.bmp"为名生成一个lena.bmp的副本
#在当前目录