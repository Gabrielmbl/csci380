# •	Based on Task One, make the RoI dynamically navigate (basically horizontal and vertical) in the overall frame.
# •	During the RoI moves, any fraction of the frame shown in the RoI should be colorful. 


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

while True:
    ret, frame = cam.read()
    roi = frame[posY:posY + boxH, posX: posX + boxW].copy()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    frame[posY:posY + boxH, posX: posX + boxW] = roi
    cv2.rectangle(frame, (posX,posY), (posX+boxW, posY+boxH), (255,0,0), 2)

    posX += dx
    posY += dy
    
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

