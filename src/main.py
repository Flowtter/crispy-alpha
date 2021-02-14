import cv2
import os
import moviepy.editor as mpe
import asyncio
import sys

from videos.videos import *
from videos.splitter import *
from videos.concat import *
from audio.audio import *
from images.images import *
from templates.templates import *
from utils.paths import *
from utils.utils import *


musics = get_all_files_and_folder_from_path_keep_extension(RESOURCES_MUSICS_PATH, ".wav")
videos = get_all_files_and_folder_from_path_keep_extension(RESOURCES_VIDEOS_PATH, ".mp4")

print(musics, videos)

for video in videos:
    create_directories()

    print(video)
    print("Getting images")
    images, _ = extract_images_and_crop_them(RESOURCES_VIDEOS_PATH + video, 1)
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
    tasks = create_tasks_from_videos_objects(videos_objects, VIDEOS_PATH, RESOURCES_VIDEOS_PATH + "main") # refactor
    print("Trimming video")
    trim_video_from_tasks(tasks)
    print("Creating LOG file")
    create_log_file_of_videos(VIDEOS_PATH)
    print("Concat videos")
    concat_videos_from_directory(VIDEOS_PATH, OUTPUT + "/concat_video_" + video) # refactor

    clear_directories(".tmp")



print("Creating FINAL LOG file")
create_log_file_of_videos(OUTPUT)
print("Concat FINAL videos")
concat_videos_from_directory(OUTPUT, "export.mp4") #refactor
if len(musics) > 0:
    print("Loading video")
    my_clip = mpe.VideoFileClip("export.mp4")
    print("Loading audio")
    audio_background = mpe.AudioFileClip(RESOURCES_MUSICS_PATH + musics[0])
    print("Edition audio")
    final_audio = mpe.CompositeAudioClip([my_clip.audio, audio_background])
    final_audio = final_audio.subclip(0, my_clip.duration)
    my_clip.audio = final_audio
    print("Writing video")
    my_clip.write_videofile("export_with_music.mp4")
    print("Removing old video")
    os.remove("export.mp4")

print("Removing output folder")
clear_directories(OUTPUT)


print("Closing loop")
loop = asyncio.get_event_loop()
loop.close()

#clear_directories()
