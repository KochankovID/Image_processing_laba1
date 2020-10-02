import logging
import numpy as np


logger = logging.getLogger()


def BGR_brightness_filter(src: np.ndarray, brightness_change: int) -> np.ndarray:
    '''Add brightness_change to every pixel in bgr color space'''
    if brightness_change > 255:
        logger.warning(f'Your brightness {brightness_change} '
                        'is higer than 255 wich is maximum value!')
    if brightness_change < -255:
        logger.warning(f'Your brightness {brightness_change} '
                        'is lower than -255 wich is minimum value!')

    result = np.copy(src).astype(int)
    result += brightness_change
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)


def YUV_brightness_filter(src: np.ndarray, brightness_change: int) -> np.ndarray:
    '''Add brightness_change to every pixel in yuv color space'''
    if brightness_change > 255:
        logger.warning(f'Your brightness {brightness_change} '
                        'is higer than 255 wich is maximum value!')
    if brightness_change < -255:
        logger.warning(f'Your brightness {brightness_change} '
                        'is lower than -255 wich is minimum value!')

    result = np.copy(src).astype(int)
    result[:, :, 0] += brightness_change
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)