import numpy as np


def BGR2YUV(src: np.ndarray) -> np.ndarray:
    '''Convert opencv image in BGR to YUV color space'''
    YUV_coeficients = np.array([
        [0.114, 0.436, -0.100],
        [0.587, -0.289, -0.515],
        [0.299, -0.147, 0.615]])

    result = np.dot(src, YUV_coeficients)
    result[:, :, 1:] += 128
    return result.astype(np.uint8)


def YUV2BGR(src: np.ndarray) -> np.ndarray:
    '''Convert opencv image in YUV to BGR color space'''
    BGR_coeficients = np.array([
        [1.00000000e+00,  1.00000000e+00,  1.00000000e+00],
        [2.03199968e+00, -3.94610164e-01, -3.94570707e-05],
        [-4.81376263e-04, -5.80500316e-01,  1.13982797e+00]])

    tmp_img = np.copy(src).astype(float)
    tmp_img[:, :, 1:] -= 128
    result = np.dot(tmp_img, BGR_coeficients)
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)
