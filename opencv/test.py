import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame")
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

# img = cv.imread('watch.jpg', cv.IMREAD_GRAYSCALE)
# cv.imshow('image', img)
# cv.imwrite('watchgray.png', img)
# cv.waitKey(0) & 0xFF
# cv.destroyAllWindows()
