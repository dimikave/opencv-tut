import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging Blur
average = cv.blur(img, (3,3))
cv.imshow('Average Blur',average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur (good for denoising)
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)# color sigma: more colors in the neighborhood that will be considered during bluring
# sigma space: larger values means that further pixels will affect the result.
cv.imshow('Bilateral', bilateral)





cv.waitKey(0)