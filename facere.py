#importing open cv
import cv2
from random import randrange as r
#dataset load
trainedData=cv2.CascadeClassifier("face.xml")

#choose a image
#img=cv2.imread('group.jpg')

#starting web camera
webcam=cv2.VideoCapture(0)

while True:
    success,img=webcam.read()



    #cv2.imshow('single person',img)
    #cv2.waitKey()

    #conversion of blach and white
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #detect faces
    faceCoordinates=trainedData.detectMultiScale(grayimg)
    for x,y,w,h in faceCoordinates:
        cv2.rectangle(img,(x,y),(x+w,y+h),(r(0,255),r(0,255),r(0,255)),2)

    cv2.imshow('window ',img)
    key=cv2.waitKey(1)
    if(key==81 or key==113):
     break
webcam.release()
 #print(faceCoordinates)
#cv2.imshow('single person1',grayimg)
#cv2.waitKey()

