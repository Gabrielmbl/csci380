# Change the frame color into grayscale
# Resize the screen windows with following requirements:
#     Increase the window by the double size of the original size (You will need to get the original window size by OpenCV)
#     Decrease the window by the half size of the original size
# Move the display screen to the position, (0,-30)

import cv2
print(cv2.__version__)

cam = cv2.VideoCapture(0)
ret,frame = cam.read()
height = frame.shape[0]
width = frame.shape[1]


while True:
    ret,frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # print(gray.shape) # (480,640)
    frameDouble = cv2.resize(gray, (int(width*2), int(height*2)))
    frameHalf = cv2.resize(gray, (int(width/2), int(height/2)))
    cv2.imshow('grayDouble', frameDouble)
    cv2.imshow('grayHalf', frameHalf)
    cv2.moveWindow('grayDouble', 0,-30)
    cv2.moveWindow('grayHalf', int(width*2), -30)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()