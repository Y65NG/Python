import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)
cv2.imwrite('watchgray.png', img)
cv2.waitKey(0)
