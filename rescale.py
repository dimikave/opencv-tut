import cv2 as cv
import numpy as np

#img = cv.imread('Photos/cat_large.jpg')

#cv.imshow('Cat',img)
#cv.waitKey(0)    # Wait for infinite amount of time


def rescaleFrame(frame, scale = 0.75):
    # Live Video, Video, Images
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    # Live Video
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue,frame = capture.read()
    frame_resized = rescaleFrame(frame,scale =.2)
    cv.imshow('Video Resized',frame_resized)
    cv.imshow('Video',frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):# it means if it ends or if you press d it stops
        break



