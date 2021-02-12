import cv2
import numpy as np
import pytesseract

def find_template(image, template):
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, _, _ = cv2.minMaxLoc(res)
    print(max_val)
    return max_val > 0.80
    # return np.where(res > 0.80)

def draw_template(image, template):
    height, width, chan = template.shape
    for point in zip(*find_template(image, template)[::-1]):
        cv2.rectangle(image, (point[0] - 2, point[1] - 2),
                          (point[0] + width + 2, point[1] + height + 2),
                          (200,200,200), 2)


def find_pseudo()