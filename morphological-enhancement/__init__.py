import cv2 
import numpy as np

# read image of disk
img = cv2.imread('images/image.jpg')

# transform imagem to gray scale
image_gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# generate kernel
kernel = np.ones((5, 5), np.uint8)

# generate erosion
image_erosion = cv2.erode(image_gray_scale, kernel, iterations=1)

# generate opening
opening = cv2.dilate(image_erosion, kernel, iterations=1)

# generate top hat
tap_hat_opening = cv2.subtract(img, opening)

# generate dilatetion
image_dilated = cv2.dilate(image_gray_scale, kernel, iterations=1)

# generate closing
closing = cv2.erode(image, kernel, iterations=1)

# generate top hat closing
tap_hat_closing = cv2.subtract(img, closing)

k = cv2.subtract(cv2.add(img,tap_hat_opening), tap_hat_closing)

(status, image) = cv2.threshold(k, 100, 255, cv2.THRESH_BINARY)

cv2.imshow('image', image)