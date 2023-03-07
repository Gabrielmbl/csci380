# •	Use numpy to create a zero matrix with size 250*250 and use OpenCV to display it.

import cv2 
import numpy as np
print(cv2.__version__)

# cam = cv2.VideoCapture(0)

while True:
    frame = np.zeros((250, 250, 3), dtype = np.uint8)

    cv2.imshow('black', frame)
    cv2.moveWindow('black', 0, 0)
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()


