import numpy as np 
import cv2
#code to access camera

# 0 or filename ''
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #returns frame imageand ret telling if it worked
    
    width = int(cap.get(3))
    height = int(cap.get(4))
    #created a black screen
    image = np.zeros(frame.shape, np.uint8)
    
    smaller_frame=cv2.resize(frame,(0,0), fx=0.5,fy=0.5)
    #psting cams in 4 parts
    image[:height//2,:width//2]=cv2.rotate(smaller_frame,cv2.ROTATE_180)
    image[height//2:,:width//2]=smaller_frame
    image[:height//2,width//2:]=cv2.rotate(smaller_frame,cv2.ROTATE_180)
    image[height//2:,width//2:]=smaller_frame
    

    cv2.imshow('frame',image)
    #if value of key in ascii to q  then stop
    if cv2.waitKey(1) == ord('q'):
        break 

cap.release()
cv2.destroyAllWindows()
