# 使用NumPy生成三维数组,用来观察3个通道值的变化情况
import cv2   # 调用cv2
import numpy as np  # 调用NumPy库
# ---------蓝色通道值--
blue = np.zeros((300,300,3), dtype=np.uint8)    
# 生成彩色图像,图像数据属性为uint8   ↑↑
blue[:, :, 0] = 255   # 填充为蓝色 前一个(:)指代宽的阈值为从头至尾,后者等同,0为蓝色
print("blue=\n", blue)   # 输出图像
cv2.imshow("blue", blue)   # 显示图像
# ---------绿色通道值--
green = np.zeros((300,300,3), dtype=np.uint8)
green[:, :, 1] = 255
print("green=\n", green)
cv2.imshow("green", green)
# ---------红色通道值--
red = np.zeros((300,300,3), dtype=np.uint8)
red[:, :, 2] = 255
print("red=\n",red)
cv2.imshow("red", red)
# ---------释放窗口--
cv2.waitKey()  #暂停程序
cv2.destroyAllWindows()   # 销毁所有窗口