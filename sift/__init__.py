import numpy as np
import cv2

dataset = cv2.imread('dataset/imagem50km_1.jpg')
target = cv2.imread('target/50km.jpg')

datasetGray = cv2.cvtColor(dataset,cv2.COLOR_BGR2GRAY)
targetGray = cv2.cvtColor(target,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()

kpDataset, desDataset = sift.detectAndCompute(datasetGray, None)
kpTarget, desTarget = sift.detectAndCompute(targetGray, None)

bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=False)

matches = bf.match(desDataset, desTarget)

matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(dataset, kpDataset, target, kpTarget, matches[:10], None, flags=2)

cv2.imshow('teste', img3)
cv2.waitKey(0)
