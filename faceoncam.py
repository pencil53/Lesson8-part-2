import cv2,numpy,os,sys

haarcascade = "haarcascade_frontalface_default.xml"

facecascade = cv2.CascadeClassifier(haarcascade)

webcam = cv2.VideoCapture(0)

while True:
    status,frame = webcam.read()