
import cv2

image = cv2.imread('amee.jpg',1)
flip=cv2.flip(image,0)

cv2.imshow("invert image",flip)


cv2.waitKey(0)
cv2.destroyAllWindows()
