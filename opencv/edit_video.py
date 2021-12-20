import numpy as np
import cv2 as cv

def generatePicture(path,maxNum):  # path是保存图片的文件夹的名字
    cap=cv.VideoCapture(0)
    # isImg,img=cap.read()
    # cv.imwrite("video.jpg",img)
    # cap.release()
    face_cc = cv.CascadeClassifier("haarcascade_frontalface_default.xml") # 分类器,从图片中按照特征值进行分类.""里面的就是人脸的特征值
    num=0
    
    while cap.isOpened():
        keyVal=cv.waitKey(10)
        if keyVal ==113:
          break
        isImg,img=cap.read()  # isImg是boolean, img是矩阵,表示图片
        if isImg==False:
            print('read image is failed')
            break
        # ifFaces=face_cc.detectMultiScale(img,scaleFactor=1.2,minNeighbors=3,minSize=(32,32))  # 表示人脸位置的数组(x,y,w,h),w是宽,h是高
        ifFaces = face_cc.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
        
        if len(ifFaces) >0:
            for (x,y,w,h) in ifFaces:   # x,y表示的是所选区域的左下角,x为向右的宽,h为向上的高
                cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)    # 在找到的人脸上画一个矩形框出来
                num=num+1
                if num>maxNum:
                    break
                else:
                    img_name='%s/%d.jpg' % (path,num)   # %s 表示当前位置被一个String所填补,%d 表示被一个digit填补.填补的内容就在(path,num)里
                    image=img[y-10:y+h+10,x-10:x+w+10]   # 以矩形之外一点点为边界,保存一张图片
                    cv.imwrite(img_name,image)
        cv.imshow(f'image', img)

    cap.release()


generatePicture('other_photo',100)
# 按Q可以关闭摄像头
