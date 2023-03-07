# •	Extract an area (usually a rectangle shape) from the frame, which is regarded as the RoI.
# •	Convert the entire frame as the grayscale.
# •	However, as you have extracted the RoI before the color conversion, the image is shown as the colorful in the area of the RoI



import cv2
import numpy as np 
print(cv2.__version__)

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    roi = frame[50:250, 200:400].copy()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    frame[50:250, 200:400] = roi
    cv2.rectangle(frame, (200,50), (400, 250), (255,0,0), 2)

    
    cv2.imshow('webcam', frame)
    cv2.moveWindow('webcam', 0,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()