import pytest
import cv2
import templates

def test_find_template():
    for i in range(10):
        img = cv2.imread(f"tmp/images/logo{i}.jpg")
        templ = cv2.imread("assets/template4.jpg")
        # cv2.imwrite(f"../../tmp/results/res{i}.png", img)
        if i in [6,7,9]:
            assert templates.find_template(img, templ) == True
        else:
            assert templates.find_template(img, templ) == False

def test_find_pseudo():
    for i in range(10):
        print(i)
        img = cv2.imread(f"tmp/images/killfeed{i}.jpg", cv2.IMREAD_GRAYSCALE)
        if i in [6,7,9]:
            templates.find_pseudo(img, "TheFlowlessOtter")
            assert True
        else:
            assert templates.find_pseudo(img, "TheFlowlessOtter") == False