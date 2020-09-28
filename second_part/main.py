import numpy as np
import cv2
import time

import sys
import os.path as osp


def average(img):
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    single = (b + g + r) / 3
    copy = img.copy()

    copy[:, :, 0] = single
    copy[:, :, 1] = single
    copy[:, :, 2] = single

    return copy


def time_cv(image1):
    start = time.time()
    gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    end = time.time()
    print('opencv time: ', end - start)
    cv2.imshow('Gray image', gray)


def time_average(image1):
    start = time.time()
    copy1 = average(image1)
    end = time.time()
    print('other realisation: ', end - start)
    cv2.imshow('average image', copy1)


if __name__ == "__main__":
    try:
        image_path = sys.argv[1]
        assert osp.isfile(image_path), '{} is not a file!'.format(image_path)
    except IndexError:
        raise AssertionError('image path must be specified!')

    # image = cv2.imread('src/google.jpg')
    image = cv2.imread(image_path)
    cv2.imshow('Original image', image)

    time_cv(image)
    time_average(image)

    cv2.waitKey(30000)
    cv2.destroyAllWindows()
