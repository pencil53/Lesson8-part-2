import cv2
import numpy
import os,sys

people = cv2.imread("people.jpg")

facecascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

greypeople = cv2.cvtColor(people,cv2.COLOR_BGR2GRAY)
faces = facecascade.detectMultiScale(greypeople, scaleFactor= 1.1, minNeighbors= 9)
for (x,y,w,h) in faces:
    cv2.rectangle(people,(x,y), (x+w,y+h), (255,0,0), 3)

cv2.imshow("group of friends", people)
cv2.waitKey(0) 
cv2.destroyAllWindows()