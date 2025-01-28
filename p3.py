import cv2
import numpy as np

image_path = r"D:\DIP\messi.jpg"

#read image
img = cv2.imread(image_path)

img_normalized = img / 255.0

c = 1  # Scaling constant
log_transformed = c * np.log(1 + img_normalized)
inverse_log = np.exp(log_transformed) - 1
neg_log = 1 - log_transformed

cv2.imshow('og_image', img)
cv2.imshow('log_image', log_transformed)
cv2.imshow('inverse_log_image', inverse_log)
cv2.imshow('neg_log_image', neg_log)
cv2.waitKey(0)
cv2.destroyAllWindows()