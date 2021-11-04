import cv2 as cv
import numpy as np

img = cv.imread('Photos/group 1.jpg')
cv.imshow('Group', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Group', gray)


# Classifier
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# List with rect-coords of detected faces
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces',img)



 # Video - you do the same for each frame


cv.waitKey(0)