import cv2
import numpy as np

face_cascase = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

img = cv2.imread('Resources/rish.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = face_cascase.detectMultiScale(img_gray,1.1, 4)

# creating the bounding box
for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h), (255,255,255), 2)
    cv2.putText(img,text='Rishabh',org = (x+18,y-23), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale= 1, color= (0,0,0),thickness=2)



cv2.imshow('Rishabh', img)
cv2.waitKey(0)