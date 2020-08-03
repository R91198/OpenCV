import cv2
import numpy as np

img = cv2.imread('Resources/jersey.jpg')

horz = np.hstack((img,img))
ver = np.vstack((img,img))

cv2.imshow('Horizontal', horz)
cv2.imshow('Vertical', ver)
cv2.waitKey(0)

# So, there are two issues with this appraoch:-
# 1. We cannot resize or crop the images in these hstack or vstack functions
# 2. If the images that we are joining do not have the same number of channels, then it'll not work