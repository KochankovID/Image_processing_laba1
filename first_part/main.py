import cv2
import os
import sys
import time
from skimage.metrics import mean_squared_error, peak_signal_noise_ratio, structural_similarity

from error_functions.compare_functions import immse, psnr, ssim


def Compare2ImagesFromLibIMMSE(first_image: str, second_image: str) -> None:
    image1 = cv2.imread(first_image)
    image2 = cv2.imread(second_image)

    start = time.time()
    error = mean_squared_error(image1, image2)
    end = time.time()
    print('The mean-squared error from skimage.metrics.mean_squared_error is ' +
          str(error) + ' time ' + str(end - start))
    return error


def Compare2ImagesIMMSE(first_image: str, second_image: str) -> None:
    image1 = cv2.imread(first_image)
    image2 = cv2.imread(second_image)

    start = time.time()
    error = immse(image1, image2)
    end = time.time()
    print('The mean-squared error from algorithm is ' +
          str(error) + ' time ' + str(end - start))
    return error


def Compare2ImagesFromLibPSNR(first_image: str, second_image: str) -> None:
    image1 = cv2.imread(first_image)
    image2 = cv2.imread(second_image)

    start = time.time()
    error = peak_signal_noise_ratio(image1, image2)
    end = time.time()
    print('The peak signal-to-noise ratio from skimage.metrics.peak_signal_noise_ratio is ' +
          str(error) + ' time ' + str(end - start))
    return error


def Compare2ImagesPSNR(first_image: str, second_image: str) -> None:
    image1 = cv2.imread(first_image)
    image2 = cv2.imread(second_image)

    start = time.time()
    error = psnr(image1, image2)
    end = time.time()
    print('The peak signal-to-noise ratio from algorithm is ' +
          str(error) + ' time ' + str(end - start))
    return error


def Compare2ImagesFromLibSSIM(first_image: str, second_image: str) -> None:
    image1 = cv2.imread(first_image)
    image2 = cv2.imread(second_image)
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_RGB2GRAY)

    start = time.time()
    error = structural_similarity(gray_image1, gray_image2)
    end = time.time()
    print('The structural similarity index for measuring from skimage.metrics.structural_similarity is ' +
          str(error) + ' time ' + str(end - start))
    return error


def Compare2ImagesSSIM(first_image: str, second_image: str) -> None:
    image1 = cv2.imread(first_image)
    image2 = cv2.imread(second_image)
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_RGB2GRAY)

    start = time.time()
    error = ssim(gray_image1, gray_image2)
    end = time.time()
    print('The structural similarity index for measuring from algorithm is ' +
          str(error) + ' time ' + str(end - start))
    return error


def create_two_windows(first_image: str, second_image: str,
                       title1: str = 'Left window', title2: str = 'Right window') -> None:
    '''Create two opencv windows with images and titels'''
    image1 = cv2.imread(first_image)
    image2 = cv2.imread(second_image)

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
    if len(sys.argv) != 3 and len(sys.argv) != 1:
        print('Uncorrect args, should be: first_image second_image')
        exit()

    dir_path = os.path.dirname(__file__)
    first_image_path = os.path.join(dir_path, 'src', 'clean_image.jpg')
    second_image_path = os.path.join(dir_path, 'src', 'noise_poisson_image.jpg')

    if len(sys.argv) == 1:
        print('Will be used images from example')
    if len(sys.argv) == 3:
        first_image_path = sys.argv[1]
        second_image_path = sys.argv[2]

    create_two_windows(first_image_path, second_image_path)
    Compare2ImagesFromLibIMMSE(first_image_path, second_image_path)
    Compare2ImagesIMMSE(first_image_path, second_image_path)
    Compare2ImagesFromLibPSNR(first_image_path, second_image_path)
    Compare2ImagesPSNR(first_image_path, second_image_path)
    Compare2ImagesFromLibSSIM(first_image_path, second_image_path)
    Compare2ImagesSSIM(first_image_path, second_image_path)
