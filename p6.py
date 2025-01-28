import cv2
import numpy as np

img_path = r"D:\DIP\messi.jpg"

#read img as grayscale
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Find the minimum and maximum intensity values
r_min = np.min(image)
r_max = np.max(image)

# Define the desired output range (0 to 255 for 8-bit images)
L = 255

# Apply contrast stretching
contrast_stretched = ((image - r_min) / (r_max - r_min)) * L

# Convert the result to uint8 type
contrast_stretched = contrast_stretched.astype(np.uint8)

# Display the result
cv2.imshow('Original Image', image)
cv2.imshow('Contrast Stretched Image', contrast_stretched)
cv2.waitKey(0)
cv2.destroyAllWindows()