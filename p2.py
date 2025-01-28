import cv2

image_path = r"D:\DIP\messi.jpg"

#read image
img = cv2.imread(image_path)

negative_img = 255 - img

cv2.imshow('image', negative_img)
cv2.waitKey(0)
cv2.destroyAllWindows()