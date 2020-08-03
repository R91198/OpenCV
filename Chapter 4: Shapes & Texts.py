import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)       # 'zero' always means black in Computer Vision

# color the image
#img[:] = 255,0,0

# Creating a line in the image
cv2.line(img, (0,256),(300,250),(0,145,156), thickness=5)
# Creating the full line
cv2.line(img, (0,256),(img.shape[1],img.shape[0]),(0,145,156), thickness=5)
# Creating a rectangle
cv2.rectangle(img,(0,0),(250,350),(0,0,255),thickness=2)
# Creating a circle
cv2.circle(img,(300,300),30,(255,255,0),5)
# Adding Text
cv2.putText(img,' RISHABH ', (100,400), cv2.FONT_ITALIC, 2,(0,150,0), 3)


cv2.imshow('Image', img)
print(img.shape)
cv2.waitKey(0)