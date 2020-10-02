import numpy as np
import math


def _as_floats(image1, image2):
    float_type = np.result_type(image1.dtype, image2.dtype, np.float32)
    image1 = np.asarray(image1, dtype=float_type)
    image2 = np.asarray(image2, dtype=float_type)
    return image1, image2


def immse(image1: np.ndarray, image2: np.ndarray) -> np.ndarray:
    '''The mean-squared error'''
    image1, image2 = _as_floats(image1, image2) # - uncomment if you want same results for immse and psnr
    return ((image1 - image2) ** 2).mean()


def psnr(image1: np.ndarray, image2: np.ndarray) -> np.ndarray:
    '''The peak signal-to-noise ratio'''
    mse = immse(image1, image2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))


def ssim(image1: np.ndarray, image2: np.ndarray) -> np.ndarray:
    '''The structural similarity index for measuring'''
    image1, image2 = _as_floats(image1, image2)
    image1 = image1.flatten()
    image2 = image2.flatten()
    ux = image1.mean()
    uy = image2.mean()
    qx = np.var(image1)
    qy = np.var(image2)
    qxy = np.cov(image1, image2)

    K1 = 0.01
    K2 = 0.03

    C1 = (K1 * 2) ** 2
    C2 = (K2 * 2) ** 2

    res = ((2 * ux * uy + C1) * (2 * qxy + C2)) / ((ux ** 2 + uy ** 2 + C1)*(qx + qy + C2))
    return res.mean()
