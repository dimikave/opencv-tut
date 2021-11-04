import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype = 'uint8')
#cv.imshow('Blank',blank)

# 1.Paint the image a certain color
#blank[:] = 100,100,0#
#blank[200:250, 300:350] = 100,100,0#      brg
#cv.imshow('Green',blank)

# 2. Rectangle

#cv.rectangle(blank,(0,0),(250,30),(0,255,0),thickness=2)
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
#cv.imshow('Rectangle',blank)

# 3. Circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2), 40, (0,255,255), thickness = 3)
#cv.imshow('Circle',blank)


# 4. Line
cv.line(blank,(0,0),(250,250), (255,255,255),thickness=3)
cv.imshow('Line',blank)

# 5. Write text
cv.putText(blank,'Hello',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)
cv.waitKey(0)
