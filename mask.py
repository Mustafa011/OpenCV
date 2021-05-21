import cv2 as cv
import numpy as np

img = cv.imread('bochan.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (img.shape[1]//2 +30,img.shape[0]//2 ),100,255,-1)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow("masking", masked)

cv.waitKey(0)