# •	Create a .PY file, “fpsMeasurement_your initial.py”, to measure the fps for the video play. 
# •	Capture an image from the camera.
# •	Grab the fps and display the fps by “cv2.putText( )”.



import cv2 
import time
print(cv2.__version__)

cam = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX
timeStamp = time.time()
fpsFilter = 0

while True:
    ret, frame = cam.read()

    dt = time.time()-timeStamp
    timeStamp = time.time()
    fps = 1/dt
    fpsFilter = 0.95*fpsFilter + 0.05*fps
    cv2.putText(frame, str(round(fpsFilter,1)) + 'fps', (0,30), font, 1, (0,0,255), 2)

    cv2.imshow('webcam', frame)
    cv2.moveWindow('webcam', 0,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()