# Based on Lab 7, we have implemented the moving box could capture the 
# colorful piece of a video. In Lab 8, we need to add the event of mouse-click 
# to the code. After adding the event of mouse-click, when you use mouse to hit 
# inside of the bounding box, it will pop up “Good job!”. If you hot outside of 
# the bounding box, you won’t get the “Good job!”. 


import cv2
import numpy as np 
import math
print(cv2.__version__)

cam = cv2.VideoCapture(0)

width = 640
height = 480
posX = 0
boxW = 120
posY = 0
boxH = 70

dx = 5
dy = 5

evt = -1
font = cv2.FONT_HERSHEY_PLAIN

def click(event,x,y,flags,params):
    global point
    global xpoint
    global ypoint
    global evt
    if event == cv2.EVENT_LBUTTONDOWN:
        point=(x,y)
        xpoint = x
        ypoint = y
        evt = event

cv2.namedWindow('webcam')
cv2.setMouseCallback('webcam', click)




while True:
    ret, frame = cam.read()
    roi = frame[posY:posY + boxH, posX: posX + boxW].copy()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    frame[posY:posY + boxH, posX: posX + boxW] = roi
    cv2.rectangle(frame, (posX,posY), (posX+boxW, posY+boxH), (0,0,255), 2)

    posX += dx
    posY += dy


    if evt == 1:
        cv2.circle(frame, (xpoint,ypoint), 5, (0,0,255), -1)
            
        if xpoint in range(posX, posX + boxW) and ypoint in range(posY, posY + boxH):
            cv2.putText(frame, 'Good Job', (10,25), font, 1, (0,255,0), 2)
            cv2.rectangle(frame, (posX,posY), (posX+boxW, posY+boxH), (0,255,0), 2)
    
        
    if posX+boxW == width:
        dx *= -1
    
    if posY+boxH == height:
        dy *= -1
    
    if posY == 0:
        dy *= -1
    
    if posX == 0:
        dx *= -1


    cv2.imshow('webcam', frame)
    cv2.moveWindow('webcam', 0,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()

