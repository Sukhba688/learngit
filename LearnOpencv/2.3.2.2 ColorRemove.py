# 使用NumPy生成一个三维数组,用来观察3个通道值的变化情况
import numpy as np
import cv2
img = np.zeros((300, 300, 3), dtype=np.uint8)   # 生成一个图像,数据类型为uint8
# 图像左边设为蓝色
img[:, 0:100, 0] = 255   # 255为纯蓝(0)色
# 图像中间设为绿色
img[:, 100:200, 1] = 255
# 图像右边设为红色
img[:, 200:300, 2] = 255
print("img=\n", img)    # 输出图像
cv2.imshow("img", img)    # 显示图像
cv2.waitKey()    # 暂停程序
cv2.destroyAllWindows()    #销毁所有图像