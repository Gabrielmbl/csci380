# Change the frame color into grayscale
# Change the frame color into RGB
# Move the frames to the positions, (640,0) and (0,480)
# Play the camera and display the camera screens
# Design the, "q". to exit the loop and release the camera instance 


import cv2
print(cv2.__version__)
cam = cv2.VideoCapture(0)

while True:
    ret,frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    cv2.imshow('rgb', rgb)
    cv2.moveWindow('frame',0,0)
    cv2.moveWindow('gray', 640,0)
    cv2.moveWindow('rgb', 0,480)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()