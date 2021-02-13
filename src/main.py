import cv2
from videos.videos import *
from images.images import *
from utils.paths import *

#810, 920, 910, 1001
#100, 1300, 300, 1880
images = extract_images_and_crop_them(VIDEOS_PATH + "output.mp4", 1)
print("searching templates")
template_im = cv2.imread("assets/template.jpg")
find_template_in_images(images, template_im, True)