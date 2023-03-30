import cv2
#read the image
img = cv2.imread('test.jpeg',1)
#resizing the image
img = cv2.resize(img, (0,0),fx=0.5,fy=0.5)
#rotating the image
img = cv2.rotate(img,cv2.ROTATE_180)
#saving rotated img as new image
cv2.imwrite('newtest.jpeg',img)
#open rotated image 
cv2.imshow('Image',img)
#wait infinetly long until any key pressed
cv2.waitKey(0)
#if button pressed close 
cv2.destroyAllWindows()

