import cv2
import random

img = cv2.imread('test.jpeg',-1)

#print(img)--- shows rgb in arrays 
#print(type(img))--- numpy.ndarray
#print(img.shape)--- (rows height , columns width , channels rgb pixels for 1 color
#print(img[][])

# change pixels to random

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255),random.randint(0,255) ,random.randint(0,255)]
        
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


