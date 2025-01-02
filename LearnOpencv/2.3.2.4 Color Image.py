# 读取一幅彩色图像, 并对其像素进行访问, 修改
import cv2
img = cv2.imread("LearnOpencv\lena.bmp")
cv2.imshow("before", img)
print("访问igm[0,0]=", img[0, 0])
print("访问img[0,0,0]=", img[0, 0, 0])
print("访问img[0,0,1]=", img[0, 0, 1])
print("访问img[0,0,2]=", img[0, 0, 2])
print("访问igm[50,0]=", img[50, 0])
print("访问igm[100,0]=", img[100, 0])
for i in range(0, 50):
    for j in range(0, 100):
        for k in range(0, 3):
            img[i, j, k] = 255  # 白色
for i in range(50, 100):
    for j in range(0, 100):
        img[i, j] = [128, 128, 128]  # 灰色
for i in range(100, 150):
    for j in range(0, 100):
        img[i, j] = 0  # 黑色
        cv2.imshow("after", img)
print("修改后img[0,0]=", img[0, 0])
print("修改后img[0,0,0]=", img[0, 0, 1])
print("修改后img[0,0,1]=", img[0, 0, 2])
print("修改后img[0,0,2]=", img[0, 0, 0])
print("修改后img[50,0]=", img[50, 0])
print("修改后img[100,0]=", img[100, 0])
cv2.waitKey()
cv2.destroyAllWindows()