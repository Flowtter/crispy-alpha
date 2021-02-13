import cv2
from videos.videos import *
from videos.splitter import *
from videos.concat import *
from audio.audio import *
from images.images import *
from templates.templates import *
from utils.paths import *
from utils.utils import *


#print(get_all_files_from_path("."))

#create_log_file_of_videos("tmp/videos/output/")
concat_videos_from_directory("tmp/videos/output/")


"""
#810, 920, 910, 1001
#100, 1300, 300, 1880
images, _ = extract_images_and_crop_them(VIDEOS_PATH + "output.mp4", 1)
print("searching templates")
template_im = cv2.imread("assets/template.jpg")
frames_template = find_template_in_images(images, template_im, False)
print("post processing")
"""

"""
frames_processed = post_process_frames_with_template([6, 7, 9, 10, 15, 68, 69, 70, 71, 72, 73])
tuples_processed = post_process_frames_in_tuples(frames_processed)
print(tuples_processed)

videos_objects = create_video_object_from_frames_processed(tuples_processed, 2, 3, 75, "test")

post_process_videos_objects(videos_objects)

tasks = create_tasks_from_videos_objects(videos_objects)
trim_video_from_tasks(tasks)
"""