# •	Based on the image already created, change the image and make it half white and half black.

import cv2 
import numpy as np
print(cv2.__version__)

# cam = cv2.VideoCapture(0)

while True:
    frame = np.zeros((250, 250, 3), dtype = np.uint8)
    frame[0:250,0:125,0]=255
    frame[0:250,0:125,1]=255
    frame[0:250,0:125,2]=255

    cv2.imshow('binary', frame)
    cv2.moveWindow('binary', 0, 0)
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()


