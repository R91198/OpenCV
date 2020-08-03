# Basic Functions

import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)
img = cv2.imread('Resources/jersey.jpg')

# Converting the image into grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image
img_blur = cv2.GaussianBlur(img, (15,15), 0)
# Edge Detection in the image
img_canny = cv2.Canny(img, 150, 200)
# Increasing the thickness of the edge
img_dilation = cv2.dilate(img_canny, kernel, iterations=1)
# Erosion i.e opposite of Dilation
img_erosion = cv2.erode(img_dilation, kernel, iterations=1)

#cv2.imshow('Original Image', img)
#cv2.imshow('Gray Image', img_gray)
#cv2.imshow('Blur Image', img_blur)
cv2.imshow('Canny Image', img_canny)
cv2.imshow('Dilation Image', img_dilation)
cv2.imshow('Erosion Image', img_erosion)
cv2.waitKey(0)
