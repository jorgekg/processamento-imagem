import cv2
import numpy as np

img = cv2.imread('img.jpg', 0)
img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 2, 300,
                           param1=30, param2=35, minRadius=130, maxRadius=0)

circles = np.uint16(np.around(circles))

for i in circles[0, :]:
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 0, 0), 2)

x, y, r = circles[0][0]
xx = x - r
yy = y - r
img = cimg[xx:(xx+2*r), yy:(yy+2*r)]

cv2.imshow('teste', img)

img = cv2.medianBlur(img, 5)

cimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT, 1, 300,
                           param1=10, param2=20, minRadius=10, maxRadius=60)

circles = np.uint16(np.around(circles))

for i in circles[0, :]:
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('teste', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
