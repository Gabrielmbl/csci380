# •	Create a .PY file, “Lab10.py”, to implement the user-controlling monochrome (Red) in an image. 


import cv2 
print(cv2.__version__)


cam = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars', 640,0)
cv2.resizeWindow('Trackbars', 500, 80)
cv2.createTrackbar('RedBar', 'Trackbars', 25, 255, nothing)

font = cv2.FONT_HERSHEY_PLAIN

xVal = int(640/2)
yVal = int(480/2)

while True:
    ret, frame = cam.read()
    RedBar = cv2.getTrackbarPos('RedBar', 'Trackbars')
    cv2.circle(frame, (xVal,yVal), 25, (0,0,RedBar), -1)

    cv2.putText(frame, f'RedBar: {RedBar}', (10,25), font, 1, (0,0,255), 2)

    cv2.imshow('webcam', frame)
    cv2.moveWindow('webcam', 0,0)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()