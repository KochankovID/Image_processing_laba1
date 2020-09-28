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
    mode = int(input('mode:'))
    image = cv2.imread('src/google.jpg')

    if mode == 0:
        start = time.time()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        end = time.time()
        print(end - start)

        cv2.imshow('Original image', image)
        cv2.imshow('Gray image', gray)


    if mode == 1:
        start = time.time()
        copy1 = average(image)
        end = time.time()
        print(end - start)

        cv2.imshow('Original image', image)
        cv2.imshow('average image', copy1)

    cv2.waitKey(15000)
    cv2.destroyAllWindows()




