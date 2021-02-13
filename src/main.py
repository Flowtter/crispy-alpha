import cv2
import os
import moviepy.editor as mpe

from videos.videos import *
from videos.splitter import *
from videos.concat import *
from audio.audio import *
from images.images import *
from templates.templates import *
from utils.paths import *
from utils.utils import *


print("Getting images")
images, _ = extract_images_and_crop_them(VIDEOS_PATH + "main.mp4", 1)
print("Searching for templates")
template_im = cv2.imread("assets/template.jpg")
frames_template = find_template_in_images(images, template_im, False)
print("Frames templates:", frames_template)
print("Post processing templates")
frames_processed = post_process_frames_with_template(frames_template)
tuples_processed = post_process_frames_in_tuples(frames_processed)
print("Tuple processed:", tuples_processed)
print("Creating videos objects")
videos_objects = create_video_object_from_frames_processed(tuples_processed, 2, 3, 75, "test")
print("post processing videos")
post_process_videos_objects(videos_objects)
print("Creating tasks")
tasks = create_tasks_from_videos_objects(videos_objects)
print("Trimming video")
trim_video_from_tasks(tasks)
print("Creating LOG file")
create_log_file_of_videos("tmp/videos/output/")