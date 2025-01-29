import cv2
import numpy as np

# image_path = r"D:\DIP\messi.jpg"
image_path = r"/home/student/Desktop/melwin_pythonLab/DIP/messi.jpg"

#read image
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) 

hist_equalized = cv2.equalizeHist(img)

cv2.imshow('og_image', img)
cv2.imshow('hist_equalized_image', hist_equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()
