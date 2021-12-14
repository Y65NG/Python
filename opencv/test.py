# import cv2 as cv
# import numpy as np

# cap = cv.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Can't receive frame")
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     cv.imshow('frame', gray)
#     if cv.waitKey(1) == ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()

# # img = cv.imread('watch.jpg', cv.IMREAD_GRAYSCALE)
# # cv.imshow('image', img)
# # cv.imwrite('watchgray.png', img)
# # cv.waitKey(0) & 0xFF
# # cv.destroyAllWindows()
import cv2 as cv
face_cc = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

cv.namedWindow('image')
cap = cv.VideoCapture(0)

while cap.isOpened():
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    is_img, img = cap.read()
    if not is_img:
        print("Can't receive frame")
        break
    ifFace = face_cc.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in ifFace:
        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        num += 1
        if num > catch_pic_num:
            break
        else:
            img_name = f'{path_name}/{num}.jpg'
            image = imgFrame[y-10 : y+h+10, x-10 : x+w+10]
            cv.imwrite(img_name, image)
    cv.imshow('image', img)
cap.release()
cv.destroyAllWindows()

def generate_samples():
    
