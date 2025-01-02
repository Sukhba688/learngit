# 二值图像及灰度图像
# zero() 使用NumPy库生成一个元素值都是0的二维数组,用来模拟一幅黑色图像
# 并对其进行访问,修改
import cv2
import numpy as np    # 导入Numpy库(一个存储,处理矩阵的强大工具库)
img = np.zeros((512, 512),dtype=np.uint8)   # 生成矩阵(图像),数据类型为uint8
cv2.imshow("original", img)   # 显示所生成的图像
for i in range(512):
    img[256, i] = 255  # 对图像进行修改
    cv2.imshow("modified", img)   # 显示修改后的图像
cv2.waitKey(0)  #暂停程序 ps:注意!!!终止的是所有程序所以要放在外面
cv2.destroyAllWindows()   #销毁所有图像窗口