import cv2
import numpy as np

path = "Resources/different-shapes.png"
img = cv2.imread(path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(7,7), 1)

cv2.imshow('Image', img)
cv2.imshow("Gray", img_gray)
cv2.imshow('Blur', img_blur)
cv2.waitKey(0)
