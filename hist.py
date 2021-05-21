import cv2 as cv


img =cv.imread('bochan.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

threshold , thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)

cv.imshow('Thresh',thresh)
cv.waitKey(0)