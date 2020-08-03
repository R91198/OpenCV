# Importing Images and Videos through OpenCV
import cv2
print('Package Imported')

# Reading the image from the source
#img = cv2.imread('Resources/sample.jpeg')

#cv2.imshow('Output', img)
#cv2.waitKey(0)

# Reading the video from the source
#cap = cv2.VideoCapture('Resources/presidential_debate.mp4')

#while True:
#    success, img = cap.read()
#    cv2.imshow('Video', img)
    # It adds the delay and looks for the word 'q' in order to end the video
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break

# Webcam
cap = cv2.VideoCapture(0)
# Setting params for the webcam like width, height, brightness
cap.set(3,640)     # width
cap.set(4,500)     # height
cap.set(10,150)

while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    # It adds the delay and looks for the word 'q' in order to end the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
