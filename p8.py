import cv2
import numpy as np

# img_path = r"D:\DIP\messi.jpg"
img_path = r"/home/student/Desktop/melwin_pythonLab/DIP/messi.jpg"

#read img
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) 

# Box blur kernel
box_kernel = np.ones((3, 3), np.float32) / 9

# Gaussian blur kernel (3x3)
gaussian_kernel = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
], dtype=np.float32) / 16
    
# Apply correlation (filter2D)
corr_box_kernel = cv2.filter2D(img, -1, box_kernel)
corr_gaussian_kernel = cv2.filter2D(img, -1, gaussian_kernel)

# Apply convolution (flip kernel and apply correlation)
conv_box_kernel = cv2.filter2D(img, -1, np.flip(box_kernel))
conv_gaussian_kernel = cv2.filter2D(img, -1, np.flip(gaussian_kernel))

cv2.imshow('og_img', img)
cv2.imshow('corr_box_kernel', corr_box_kernel)
cv2.imshow('corr_gaussian_kernel', corr_gaussian_kernel)
cv2.imshow('conv_box_kernel', conv_box_kernel)
cv2.imshow('conv_gaussian_kernel', conv_gaussian_kernel)


cv2.waitKey(0)
cv2.destroyAllWindows()
