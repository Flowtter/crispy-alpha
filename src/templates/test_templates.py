import pytest
import templates
import cv2


def test_find_template():
    for i in range(10):
        img = cv2.imread(f"../../tmp/images/logo{i}.jpg")
        templ = cv2.imread("tmp/template4.jpg")
        # cv2.imwrite(f"../../tmp/results/res{i}.png", img)
        if i in [6,7,9]:
            assert templates.find_template(img, templ) == True
        else:
            assert templates.find_template(img, templ) == False