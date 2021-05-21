import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype='uint8')

rec = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

b_and = cv.bitwise_and(rec,circle)
b_xor = cv.bitwise_xor(rec,circle)

cv.imshow("rectangle", b_and)
cv.imshow("CIRCLE", b_xor)

cv.waitKey(0)
