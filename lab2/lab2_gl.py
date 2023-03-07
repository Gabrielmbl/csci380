# Use OpenCV to write a code with the requirements shown as below:
# •	Create a camera instance
# •	Use loop to repeatedly grab the frame from the camera instance
# •	Play the camera and display the camera screen
# •	Design the key, “q”, to exit the loop and release the camera instance


import cv2
print(cv2.__version__)
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    cv2.imshow('webcam', frame)
    cv2.moveWindow('webcam', 0,0)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()