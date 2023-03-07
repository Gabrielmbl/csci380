# •	Load a video file into python code.
# •	Calculate the fps and display it on the screen.



import cv2 
import time
print(cv2.__version__)

cam = cv2.VideoCapture("video.mp4")

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