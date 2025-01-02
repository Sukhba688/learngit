import cv2   # 调用cv函数
Lena = cv2.imread("LearnOpencv\lena.bmp")    # 读取图像
cv2.imshow("demo1", Lena)   # 显示图像
cv2.imshow("demo2", Lena)   # 显示第二个图像
cv2.waitKey()   # 返回值,停止
cv2.destroyALLWindow("demo")   #按下任意键毁坏所有的窗口