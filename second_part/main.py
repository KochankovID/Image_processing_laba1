import numpy as np
import cv2
import time

def average (img):
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]
    single = (b + g + r) / 3
    copy = img.copy()
    copy[:, :, 0] = single = (b + g + r) / 3
    copy[:, :, 1] = single = (b + g + r) / 3
    copy[:, :, 2] = single = (b + g + r) / 3
    return copy



if __name__ == "__main__":
    print('hello world')

    image = cv2.imread('src/google.jpg')
    start = time.time()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    end = time.time()
    print(end - start)

    cv2.imshow('Original image', image)
    cv2.imshow('Gray image', gray)



    image2 = cv2.imread('src/image2.jpg')
    start = time.time()
    copy1 = average(image2)
    end = time.time()
    print(end - start)

    cv2.imshow('Original image', image2)
    cv2.imshow('average image', copy1)



    cv2.waitKey(30000)
    cv2.destroyAllWindows()




