# Step One: Create a trackbar to control the position of the circle in an image and the trackbar, once created, is shown in fig.1
# Step Two: Create an event to convey both X and Y position from the trackbar. 
# Step Three: Use the X and Y from trackbar as the position of where to draw a circle with the radius, “25”.
# Step Four: Display the X and Y as the circle position in the image


import cv2 
print(cv2.__version__)


cam = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars', 640,0)
cv2.resizeWindow('Trackbars', 500, 80)
cv2.createTrackbar('xVal', 'Trackbars', 25, 640, nothing)
cv2.createTrackbar('yVal', 'Trackbars', 25, 480, nothing)


while True:
    ret, frame = cam.read()
    xVal = cv2.getTrackbarPos('xVal', 'Trackbars')
    yVal = cv2.getTrackbarPos('yVal', 'Trackbars')

    cv2.circle(frame, (xVal,yVal), 25, (0,0,255), -1)


    cv2.imshow('webcam', frame)
    cv2.moveWindow('webcam', 0,0)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()