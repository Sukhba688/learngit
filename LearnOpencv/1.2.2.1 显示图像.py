# 显示图像
# cv2.imshow(Windowname,img)
import cv2
lena = cv2.imread("LearnOpencv\lena.bmp")     # 读取图像 ps:注意括号内是填写图像的指定途径
cv2.namedWindow("image")    # 创建指定窗口来显示图像
cv2.imshow("image", lena)   # 显示图像
cv2.waitKey(0)    # 暂停程序