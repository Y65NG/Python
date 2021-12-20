import cv2 as cv


def catch_img_in_video(win_name, camera_id, path_name, catch_pic_num):
    cv.namedWindow('image')
    cap = cv.VideoCapture(0)
    face_cc = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    num = 0
    while cap.isOpened():
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        is_img, img = cap.read()
        if not is_img:
            print("Can't receive frame")
            break
        if_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        if_faces = face_cc.detectMultiScale(if_grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        for (x, y, w, h) in if_face:
            cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            num += 1
            if num > catch_pic_num:
                break
            else:
                img_name = f'{path_name}/{num}.jpg'
                image = img[y-10 : y+h+10, x-10 : x+w+10]
                cv.imwrite(img_name, image)
        font = cv.FONT_HERSHEY_COMPLEX
        cv.putText(img, f'num: {num}', (x+30, y+30), font, 1, (255, 0, 255), 2)
        cap.release()
        cv.destroyAllWindows()
    
def generatePicture(path,maxNum):
    
    ifFace = face_cc.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
    