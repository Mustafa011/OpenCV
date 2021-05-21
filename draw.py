import cv2 as cv
import numpy as np

img = cv.imread("bochan.jpg")

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow("Blank", blank)

# #cv.rectangle(img, (0,0), (img.shape[1],img.shape[0]), (0,0,255), thickness=5)
# cv.putText(img, 'MANU', (80,240), cv.FONT_HERSHEY_TRIPLEX, 1.0 , (0,0,255),2)
# cv.imshow("Text", img)

# canny = cv.Canny(img, 125, 175)

# cv.imshow("Image", canny)

# b,g,r = cv.split(img)

# cv.imshow("BLUE", b);
# cv.imshow("green",g);
# cv.imshow("red", r);

cv.waitKey(0)

