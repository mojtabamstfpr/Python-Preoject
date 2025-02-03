import cv2
import numpy as np
image = cv2.imread("input.jpg")
blurred = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imwrite("output.jpg", blurred)