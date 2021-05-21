import cv2
import numpy as np

# img = cv2.imread("bochan.jpg", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("IMG", img)
# cv2.imwrite('grey.jpg', img)
# cv2.waitKey(0)

# cap = cv2.VideoCapture(0)
# cap.set(3, 640)   //width
# cap.set(4, 480)   //height
# cap.set(10, 100)  //brightness

# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# img = cv2.imread("bochan.jpg")
# g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# y_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
# h_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow('gray',g_img)
# cv2.imshow('yuv',y_img[:,:,1])
# cv2.imshow('hsv',h_img)
# cv2.waitKey(0)

# img = cv2.imread("bochan.jpg")
# rows , col = img.shape[:2]

# t_matrix = np.float32([[1,0,50],[0,1,40]])
# img_translation = cv2.warpAffine(img, t_matrix, (rows+70, col+110))
# # t_matrix = np.float32([[1,0,-30],[0,1,-50]])
# # img_translation = cv2.warpAffine(img, t_matrix, (rows+70+30, col+110+50))
# cv2.imshow("Translation", img_translation)
# cv2.waitKey(0)


# img = cv2.imread("bochan.jpg")
# rows , col = img.shape[:2]

# t_matrix = np.float32([ [1,0,int(0.5*rows)],[0,1,(0.5*col)]])
# r_matrix = cv2.getRotationMatrix2D((rows,col), 30,1)

# img_translation = cv2.warpAffine(img, t_matrix, (2*col,2*rows) )
# img_rotation = cv2.warpAffine(img_translation, r_matrix, (2*col,2*rows) )

# cv2.imshow("Roate", img_rotation)
# cv2.waitKey(0)

img = cv2.imread("bochan.jpg")
s_img = cv2.resize(img, (200,200), interpolation = cv2.INTER_AREA)
cv2.imshow("image",s_img)
cv2.waitKey(0)