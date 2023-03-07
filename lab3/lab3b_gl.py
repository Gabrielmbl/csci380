# Implement user-defined window size for the play. For example, an user
# could use a keyboard to input different values of widths and heights.
# Accordingly, the screen will display in different sizes regarding the user's input.

import cv2
print(cv2.__version__)

cam = cv2.VideoCapture(0)
width = int(input('Desired width: '))
height = int(input('Desired height: '))

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

while True:
    ret,frame = cam.read()
    cv2.imshow('frame', frame)
    cv2.moveWindow('frame', 0,0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()