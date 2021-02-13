import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"

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


def find_pseudo(img, pseudo: str):
    res = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
    kill = False
    names = res['text']
    for i in range(0, len(names) - 1, 2):
        if names[i] == "":
            continue
        # print('killer:', names[i], 'killed:', names[i+1])
        if names[i] == pseudo:
            # print('\n\n', pseudo, 'made the kill\n\n')
            kill = True
    return kill