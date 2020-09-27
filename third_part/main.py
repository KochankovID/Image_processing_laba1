import numpy as np
import cv2
from dataclasses import dataclass
from tqdm import tqdm


def convert_BGR2YUV(src: np.ndarray) -> np.ndarray:
    '''Convert opencv image in BGR to YUV color space'''
    print(src)
    YUV_coeficients = np.array([
        [0.114, 0.436, -0.100],
        [0.587, -0.289, -0.515],
        [0.299, -0.147, 0.615]])

    result = np.dot(src, YUV_coeficients)
    result[:, :, 1:] += 128
    return result.astype(np.uint8)


def convert_YUV2BGR(src: np.ndarray) -> np.ndarray:
    '''Convert opencv image in YUV to BGR color space'''
    BGR_coeficients = np.array([
        [1.00000000e+00,  1.00000000e+00,  1.00000000e+00],
        [2.03199968e+00, -3.94610164e-01, -3.94570707e-05],
        [-4.81376263e-04, -5.80500316e-01,  1.13982797e+00]])

    tmp_img = np.copy(src).astype(float)
    tmp_img[:, :, 1:] -= 128
    result = np.dot(tmp_img, BGR_coeficients)
    return result.astype(np.uint8)


def BGR_brightness_filter(src: np.ndarray, brightness: float) -> src: np.ndarray:
    '''Set brightness of every pixel in bgr color space''



if __name__ == "__main__":
    image = cv2.imread('./third_part/src/halloyne.png')

    yuv_image_bgr2yuv = convert_BGR2YUV(image)
    yuv_image_opencv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

    cv2.imshow('convert_BGR2YIQ',yuv_image_bgr2yuv)
    cv2.imshow('cvtColor', yuv_image_opencv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    bgr_image_yuv2bgr = convert_YUV2BGR(yuv_image_bgr2yuv)
    bgr_image_opencv = cv2.cvtColor(yuv_image_opencv, cv2.COLOR_YUV2BGR)

    cv2.imshow('bgr_opencv', bgr_image_yuv2bgr)
    cv2.imshow('cvtColor', bgr_image_opencv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
