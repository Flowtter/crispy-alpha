from videos.videos import *
from images.images import *
from utils.paths import *

for i in range(10):
    crop_and_save_image(IMAGES_PATH + f"frame{i}.jpg", "tmp/")

#extract_images_and_save_from_video(VIDEOS_PATH + "output.mp4", IMAGES_PATH)

#print(extract_images_and_crop_them(VIDEOS_PATH + "output.mp4"))