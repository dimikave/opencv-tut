import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel Kernel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
sobelxy = cv.Sobel(gray, cv.CV_64F, 1, 1)
cv.imshow('SobelX', sobelx)
cv.imshow('SobelY', sobely)
cv.imshow('Combined Sobel', combined_sobel)
cv.imshow('Sobel XY', sobelxy)

# Canny 
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)



cv.waitKey(0)