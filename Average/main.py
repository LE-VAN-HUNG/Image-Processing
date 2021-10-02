import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('noiseImg.png')

averaging = cv2.blur(img,(20,20))
gaussian = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)



cv2.imshow("original image",img)
cv2.imshow("Averaging image",averaging)
cv2.imshow("gaussian image",gaussian)
cv2.imshow("median image",median)
cv2.waitKey(0)
cv2.destroyAllWindows()

