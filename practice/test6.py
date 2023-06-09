import cv2
import numpy as np 
#corner detection 

img = cv2.imread('chess.png')

#cap = cv2.VideoCapture(0)
img = cv2.resize(img, (0,0), fx=0.75 , fy=0.75)
#convert to grei scale image beeefore passing
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Shi Tomasi algorithm
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    # ravels takes an array and flatens it double array into single bracket array
    x,y = corner.ravel()
    cv2.circle(img , (x,y) , 5 , (255,0,0) , -1 )
    
for i in range(len(corners)):
    for j in range(i+1,len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color =tuple(map( lambda x: int(x) , np.random.randint(0,255, size=3)))
        cv2.line(img, corner1,corner2, color, 1 )




cv2.imshow('Frame', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()

