import cv2
from utils.utils import get_numbers_from_string
from templates.templates import find_template


def crop_and_save_image(input_path: str, output_path: str):
    number = get_numbers_from_string(input_path)[-1]
    logo_cropped, feed_cropped = crop_image_from_path(input_path)

    cv2.imwrite(f"{output_path}/logo{number}.jpg", logo_cropped)
    cv2.imwrite(f"{output_path}/killfeed{number}.jpg", feed_cropped)


def crop_image_from_path(input_path: str):
    im = cv2.imread(input_path, cv2.IMREAD_COLOR)
    return crop_image_from_object(im)


def crop_image_from_object(im):
    logo_cropped = crop(im, 810, 920, 910, 1001)
    feed_cropped = crop(im, 100, 1300, 300, 1880)

    return logo_cropped, feed_cropped


def crop(image, x, y, width, height):
    return image[x:width, y:height]


def find_template_in_images(images, template, write=False):
    result = []
    if write:
        f = open(".tmp/kill.log", 'w')

    for i in range(len(images)):
        if find_template(images[i], template):
            if write:
                f.write(str(i) + "\n")
            result.append(i)
    return result
