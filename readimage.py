import numpy
import cv2

image = cv2.imread('./images/1.jpg',-1)

#cv2.namedWindow('myimage', cv2.WINDOW_NORMAL)
cv2.imshow('myimage',image)
cv2.waitKey(0)
cv2.destroyAllWindows()