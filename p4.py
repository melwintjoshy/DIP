import cv2

image_path = r"D:\DIP\messi.jpg"

#read image
img = cv2.imread(image_path)
img_normalized = img / 255.0
c = 1

gamma = [0.1, 0.5, 1, 2, 5, 10]
for g in gamma:
    gamma_img = c * (img_normalized ** g)
    cv2.imshow('gamma_image', gamma_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
