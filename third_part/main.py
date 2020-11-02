import sys
import os.path as osp
import time

import numpy as np
import cv2

from image_processing.converters import BGR2YUV, YUV2BGR
from image_processing.filters import BGR_brightness_filter, YUV_brightness_filter

sys.path.append("../")
from first_part.error_functions.compare_functions import immse


def get_time(f: callable, *args, **kwargs):
    start_time = time.perf_counter()
    result = f(*args, **kwargs)
    end_time = time.perf_counter()

    result_time = end_time - start_time
    print(f'Function {f.__name__} was working {result_time}')

    return result



def test_BGR2YUV_converter(image_path: str) -> None:
    '''Test converter from BGR to YUV on image stored by image_path'''
    image = cv2.imread(image_path)

    yuv_image_bgr2yuv = get_time(BGR2YUV, image)
    yuv_image_opencv = get_time(cv2.cvtColor, image, cv2.COLOR_BGR2YUV)

    create_two_windows(yuv_image_bgr2yuv, yuv_image_opencv, 'BGR2YUV', 'Opencv')


def test_YUV2BGR_converter(image_path: str):
    '''Test converter from YUV to BGR on image stored by image_path'''
    image = cv2.imread(image_path)

    yuv_image_bgr2yuv = BGR2YUV(image)
    yuv_image_opencv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

    bgr_image_yuv2bgr = get_time(YUV2BGR, yuv_image_bgr2yuv)
    bgr_image_opencv = get_time(cv2.cvtColor, yuv_image_opencv, cv2.COLOR_YUV2BGR)

    create_two_windows(bgr_image_yuv2bgr, bgr_image_opencv, 'YUV2BGR', 'Opencv')


def test_brightness_filters(image_path: str):
    '''Test BGR and YUV brightness filters on image stored by image_path'''
    bgr_image = cv2.imread(image_path)

    yuv_image = BGR2YUV(bgr_image)

    higher_brightness_bgr = get_time(BGR_brightness_filter, bgr_image, 100)
    higher_brightness_yuv = get_time(YUV_brightness_filter, yuv_image, 120)
    yuv_converted_to_bgr = YUV2BGR(higher_brightness_yuv)

    create_two_windows(higher_brightness_bgr, yuv_converted_to_bgr, 'BGR', 'YUV')

    error = immse(higher_brightness_bgr, yuv_converted_to_bgr)
    print('The mean-squared error of two images is ' + str(error))


def create_two_windows(image1: np.ndarray, image2: np.ndarray,
                       title1: str = 'Left window', title2: str = 'Right window') -> None:
    '''Create two opencv windows with images and titels'''
    cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow(title2, cv2.WINDOW_AUTOSIZE)

    cv2.moveWindow(title1, 100, 0)
    cv2.moveWindow(title2, 705, 0)

    image1 = cv2.resize(image1, dsize=(600, 600))
    image2 = cv2.resize(image2, dsize=(600, 600))

    cv2.imshow(title1, image1)
    cv2.imshow(title2, image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    try:
        image_path = sys.argv[1]
        assert osp.isfile(image_path), '{} is not a file!'.format(image_path)
    except IndexError:
        print('path to the image is not valid! The default path was set!')
        image_path = './src/halloyne.png'

    test_BGR2YUV_converter(image_path)
    test_YUV2BGR_converter(image_path)
    test_brightness_filters(image_path)
