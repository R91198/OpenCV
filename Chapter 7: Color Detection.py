import cv2

def empty(a):
    pass

path = "Resources/jersey.jpg"
cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640,240)
cv2.createTrackbar('Hue min', 'TrackBars', 0, 179, empty)
cv2.createTrackbar('Hue max', 'TrackBars', 179, 179, empty)
cv2.createTrackbar('Saturation min', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('Saturation max', 'TrackBars', 255, 255, empty)
cv2.createTrackbar('Value min', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('Value max', 'TrackBars', 255, 255, empty)


while True:
    img = cv2.imread(path)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue min', 'TrackBars')
    print(h_min)

    cv2.imshow("Image", img)
    cv2.imshow('HSV', img_hsv)
    cv2.waitKey(1)