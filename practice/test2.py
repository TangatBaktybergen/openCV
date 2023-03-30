import cv2
import random
#change one part of image by another

img = cv2.imread('test.jpeg',-1)


tag = img[700:770,650:700]
img[600:670,630:680] = tag
cv2.imwrite('test3.jpeg',img)





cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

