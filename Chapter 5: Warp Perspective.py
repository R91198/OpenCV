import cv2

img = cv2.imread('Resources/stadium.jpg')
print(img.shape)

pt1 = np.float([])

cv2.imshow('Stadium Image',img)

cv2.waitKey(0)