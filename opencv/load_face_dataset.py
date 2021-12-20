import cv2 as cv
import os

IMAGE_SIZE = 64

def resize_image(image, height=IMAGE_SIZE, width=IMAGE_SIZE):
    top, left, bottom, right = 0, 0, 0, 0
    
    # get dimensions of image
    h, w, _ = image.shape # 256, 256, 3
    l_edge = max(h, w) # get the longest edge of the image

    if h < l_edge:
        dh = l_edge - h
        top = dh // 2
        bottom = dh - top
        
    elif w < l_edge:
        dw = l_edge - w
        left = dw // 2
        right = dw - left
    else:
        pass 
    
    BLACK = [0, 0, 0]

    constant = cv.copyMakeBorder(image, top, bottom, left, right, cv.BORDER_CONSTANT, value=BLACK)

    return cv.resize(constant, (height, width))


# read training dataset
images = []
labels = []



def read_path(path):
    for dir_item in os.listdir(path):
        full_path = os.path.abspath(os.path.join(path, dir_item))

        if os.path.isdir(full_path): # if folder, keep recurring
            read_path(full_path)
        else: # file
            if dir_item.endswith('.jpg'):
                image = cv.imread(full_path)
                image = resize_image(image)

                images.append(image)
                labels.append(path)
    
    return images, labels