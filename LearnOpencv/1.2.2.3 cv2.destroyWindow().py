# cv2.destroyWindow(winname) 释放(销毁)指定窗口 ps:winname是指窗口名字
import cv2   # 调用cv函数
Lena = cv2.imread("LearnOpencv\lena.bmp")    # 读取图像
cv2.imshow("demo", Lena)   # 显示图像
cv2.waitKey()   # 返回值,停止
cv2.destroyWindow("demo")   # 按下任意键毁坏demo窗口