import cv2
import numpy as np

image = cv2.imread('/home/vanhung/Documents/vanhung/ImageProcess/Image-Processing/invertImage/amee.jpg', 0);
width = image.shape[1]
height = image.shape[0]
result = np.zeros((image.shape[0], image.shape[1]), int)

def meanFilter():
  for row in range(height):
     for col in range(width):
         currentElement=0; left=0; right=0; top=0; bottom=0; topLeft=0;
         topRight=0; bottomLeft=0; bottomRight=0;
         counter = 1
         currentElement = image[row][col]

         if not col-1 < 0:
             left = image[row][col-1]
             counter +=1
         if not col+1 > width-1:
             right = image[row][col+1]
             counter +=1
         if not row-1 < 0:
             top = image[row-1][col]
             counter +=1
         if not row+1 > height-1:
             bottom = image[row+1][col]
             counter +=1

         if not row-1 < 0 and not col-1 < 0:
             topLeft = image[row-1][col-1]
             counter +=1
         if not row-1 < 0 and not col+1 > width-1:
             topRight = image[row-1][col+1]
             counter +=1
         if not row+1 > height-1 and not col-1 < 0:
             bottomLeft = image[row+1][col-1]
             counter +=1
         if not row+1 > height-1 and not col+1 > width-1:
             bottomRight = image[row+1][col+1]
             counter +=1

         total = int(currentElement)+int(left)+int(right)+int(top)+int(bottom)+int(topLeft)+int(topRight)+int(bottomLeft)+int(bottomRight)
         avg = total/counter
         result[row][col] = avg

meanFilter();
cv2.imshow('Averaging Filter', result);
cv2.waitKey(0)
cv2.destroyAllWindows()