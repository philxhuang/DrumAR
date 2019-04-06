import cv2
import numpy as np

## Main Video Code

#range of color
colorLower = np.array([22, 60, 200], np.uint8)
colorUpper = np.array([60, 255, 255], np.uint8)

cap = cv2.VideoCapture(0)

while(True):
    #ret=True if frame is available, frame will actually capture the frame
    ret, frame = cap.read()

    frame = cv2.resize(frame, (0,0), fx = 2, fy = 2)
    frame = cv2.flip(frame, +1)
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    colorMask = cv2.inRange(frameHSV, colorLower, colorUpper)
    res = cv2.bitwise_and(frame, frame, mask = colorMask)
    
    #creating a frame
    cv2.imshow("Hello", res)
    cv2.imshow("Drum AR", frame)
        
    #if condition is met, break out of loop at keyPress "q"
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

