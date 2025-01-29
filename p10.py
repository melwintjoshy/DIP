import cv2
import numpy as np

# image_path = r"D:\DIP\messi.jpg"
image_path = r"/home/student/Desktop/melwin_pythonLab/DIP/messi.jpg"

#read image
img = cv2.imread(image_path) 

results = {'original': img}

kernels = [3, 5, 7]
for k in kernels:
        # Create normalized box kernel
        results[f'gaussian_kernel_{k}x{k}'] = cv2.GaussianBlur(img, (k,k), sigmaX=0)
for name, img in results.items():
        cv2.imshow(name, img)
cv2.waitKey(0)
cv2.destroyAllWindows()    