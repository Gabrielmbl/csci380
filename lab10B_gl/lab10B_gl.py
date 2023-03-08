# Create a .PY file, “Lab10B.py”, to object tracking by contour 


import cv2
print(cv2.__version__)
import numpy as np

cam = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars', 0,460)
cv2.resizeWindow('Trackbars', 300, 350)

cv2.createTrackbar('hueLower', 'Trackbars', 0, 179, nothing)
cv2.createTrackbar('hueUpper', 'Trackbars', 50, 179, nothing)
cv2.createTrackbar('satLow', 'Trackbars', 70, 255, nothing)
cv2.createTrackbar('satHigh', 'Trackbars', 255, 255, nothing)
cv2.createTrackbar('valLow', 'Trackbars', 100, 255, nothing)
cv2.createTrackbar('valHigh', 'Trackbars', 255, 255, nothing)

while True:
    ret,frame = cam.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hueLow = cv2.getTrackbarPos('hueLower', 'Trackbars')
    hueUp = cv2.getTrackbarPos('hueUpper', 'Trackbars')

    Ls = cv2.getTrackbarPos('satLow', 'Trackbars')
    Us = cv2.getTrackbarPos('satHigh', 'Trackbars')

    Lv = cv2.getTrackbarPos('valLow', 'Trackbars')
    Uv = cv2.getTrackbarPos('valHigh', 'Trackbars')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (hueLow, Ls, Lv), (hueUp, Us, Uv))

    ret, im = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY_INV)
    contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        (x,y,w,h)=cv2.boundingRect(cnt)
        if area >=150:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    frames_horizontal = cv2.hconcat((frame, mask))
    
    cv2.imshow('webcam', frames_horizontal)
    cv2.moveWindow('webcam', 0,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows