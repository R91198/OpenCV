# Resizing and Cropping

import cv2
import numpy as np

img = cv2.imread('Resources/jersey.jpg')
print(img.shape)

# Resizing the image
img_resize = cv2.resize(img,(200,150))       # width X height
print(img_resize.shape)

# Cropping the image
img_crop = img[0:200,200:500]               # height X width

cv2.imshow('Image',img)
#cv2.imshow('Resized Image', img_resize)
cv2.imshow('Cropped Image', img_crop)
cv2.waitKey(10000)                         # 10000 milliseconds i.e 10 sec otherwise 'O' for infinte time