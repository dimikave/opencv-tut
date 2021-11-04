import cv2 as cv



#img = cv.imread('Photos/cat_large.jpg')

#cv.imshow('Cat',img)

#cv.waitKey(0)    # Wait for infinite amount of time

# Video Reading
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):# it means if it ends or if you press d it stops
        break

capture.release()
cv.destroyAllWindows()
