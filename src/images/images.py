import cv2
from utils.utils import get_numbers_from_string


def crop_image(input_path :str, output_path :str):
    im = cv2.imread(input_path, cv2.IMREAD_COLOR)
    number = get_numbers_from_string(input_path)[-1]

    logo_cropped = crop(im, 790, 900, 925, 1020)
    feed_cropped = crop(im, 100, 1300, 300, 1880)

    cv2.imwrite(f"{output_path}/logo{number}.jpg", logo_cropped)
    cv2.imwrite(f"{output_path}/killfeed{number}.jpg", feed_cropped)


def crop(image, x, y, width, height):
    return image[x:width, y:height]
