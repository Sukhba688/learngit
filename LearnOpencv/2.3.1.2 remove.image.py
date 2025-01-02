# 读取一幅灰度图像,并对其像素进行访问,修改
import cv2   # 调用cv2
img = cv2.imread("LearnOpencv\lena.bmp",0)  # 读取图像且修改为灰度图像
cv2.imshow("original", img)   # 显示图像
for i in range(40, 200):   # 扫描 40至200 的像素
    for j in range(160, 200):   # 扫描 160至200 的像素
        img[i, j] = 255   # i * j 的像素被修改成白色(255)
cv2.imshow("modified", img)   # 显示修改后的图像
cv2.waitKey()   # 暂停程序
cv2.destroyAllWindows()   # 销毁所有窗口