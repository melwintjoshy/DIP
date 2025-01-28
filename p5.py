import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = r"D:\DIP\messi.jpg"

#read img as grayscale
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Calculate histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Plot the histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.plot(hist, color='black')
plt.xlim([0, 256])
plt.show()