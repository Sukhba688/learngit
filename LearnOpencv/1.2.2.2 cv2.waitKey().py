# cv2.waitKey()的交互功能
import cv2   #导入cv包
Neko = cv2.imread("LearnOpencv\\Neko.bmp")       #读取图像
cv2.imshow("demo", Neko)                #显示图像
key = cv2.waitKey()
if key == ord("A"):       #如果按下A建,则创建PressA窗口显示图像
    cv2.imshow("pressA", Neko)
    cv2.waitKey(0)
elif key == ord("B"):     #如果按下B键,则创建PresssB窗口显示图像
    cv2.imshow("PressB", Neko)
    cv2.waitKey(0)