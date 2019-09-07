import cv2 
import numpy as np

img = cv2.imread('images/image.jpg')

cv2.imshow('image', img)
cv2.waitKey(5000)

image_gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5, 5), np.uint8)

opening = cv2.morphologyEx(image_gray_scale, cv2.MORPH_OPEN, kernel)

top_hat_opening = cv2.subtract(image_gray_scale, opening)

closing = cv2.morphologyEx(image_gray_scale, cv2.MORPH_CLOSE, kernel)

top_hat_closing = cv2.subtract(closing, image_gray_scale)

im = cv2.add(image_gray_scale, top_hat_opening)

k = cv2.subtract(im, top_hat_closing)

(status, image) = cv2.threshold(k, 230, 255, cv2.THRESH_BINARY)

cv2.imshow('image', image)
cv2.waitKey()