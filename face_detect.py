import cv2 as cv


img = cv.imread('SPJ_2240.jpg')


resize = cv.resize(img,(500,550),interpolation=cv.INTER_AREA)


gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)

cv.imshow("Gray", gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=4)

print(f'No of faces found {len(face_rect)}')

for (x,y,w,h) in face_rect:
    cv.rectangle(resize,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Image',resize)
cv.waitKey(0)