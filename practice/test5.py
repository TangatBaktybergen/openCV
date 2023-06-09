import numpy as np
import cv2

#Colors and color detection

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    
    result = cv2.bitwise_and(frame,frame, mask=mask)
   
   # 1 1 = 1 #0 1 = 0    #1 0 = 0    # 0 0 = 0

    cv2.imshow('frame',result)
    cv2.imshow('frame2',mask)
        

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()


#BGR_color = np.array([[[255,0,0]]])
#x=cv2.cvtColor([[[255,0,0]]],COLOR_BGRHSV)
#x[0][0]


