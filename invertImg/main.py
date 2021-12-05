import cv2

img = cv2.imread('/home/vanhung/Documents/vanhung/ImageProcess/Image-Processing/invertImage/amee.jpg',0)
imgInvert = 255 - img

cv2.imshow('imput image',img)
cv2.imshow('output image',imgInvert)
cv2.waitKey(10000)
cv2.destroyAllWindows()