import cv2
import os
import moviepy.editor as mpe
from moviepy.editor import VideoFileClip, concatenate_videoclips
import asyncio
import sys

import progressbar

from videos.videos import *
from videos.splitter import *
from videos.concat import *
from audio.audio import *
from images.images import *
from templates.templates import *
from utils.paths import *
from utils.utils import *
from utils.arguments import *

musics = get_all_files_and_folder_from_path_keep_extension(
    RESOURCES_MUSICS_PATH, ".wav")
videos = get_all_files_and_folder_from_path_keep_extension(
    RESOURCES_VIDEOS_PATH, ".mp4")

print(
    "Thanks for using crispy !\nTo create a video, simply put mp4 files in resources/videos and a wav file in resources/audio\nCreating a video could take several minutes"
)

if len(videos) == 0:
    print(
        "Add videos in .mp4 in resources/videos and a music in resources/audio"
    )
    exit()

logging.info(concat_args(musics, videos))

bar = progressbar.ProgressBar(max_value=len(videos))

for i, video in enumerate(videos):
    bar.update(i)
    create_directories()

    logging.info(concat_args("Editing", video))
    logging.debug("Getting images")

    images, _ = extract_images_and_crop_them(RESOURCES_VIDEOS_PATH + video, 1)
    logging.debug("Searching for templates")

    frames_template = []

    templates = os.listdir("assets")
    for template_path in templates:
        template = cv2.imread(os.path.join("assets", template_path))
        frames_template += find_template_in_images(images, template, False)

    if frames_template == []:
        print(
            f"No kill found in {video}, double check the video or increase the quality"
        )
        continue

    logging.info(concat_args("Frames templates:", frames_template))
    logging.debug("Post processing templates")

    frames_processed = post_process_frames_with_template(frames_template)
    tuples_processed = post_process_frames_in_tuples(frames_processed)
    logging.debug(concat_args("Tuple processed:", tuples_processed))
    logging.debug("Creating videos objects")

    videos_objects = create_video_object_from_frames_processed(
        tuples_processed, 2, 1, len(images), "test")
    logging.debug("post processing videos")

    post_process_videos_objects(videos_objects)
    logging.debug("Creating tasks")
    tasks = create_tasks_from_videos_objects(videos_objects, VIDEOS_PATH,
                                             RESOURCES_VIDEOS_PATH + video)

    logging.debug("Trimming video")
    trim_video_from_tasks(tasks)

    logging.debug("Creating LOG file")
    create_log_file_of_videos(VIDEOS_PATH)
    logging.debug("Concat videos")
    concat_videos_from_directory(VIDEOS_PATH,
                                 OUTPUT + "/concat_video_" + video)  # refactor

    clear_directories(".tmp")

bar.finish()

bar = progressbar.ProgressBar(max_value=4)

logging.info("Concat FINAL videos")
cliparray = []
clips = os.listdir(OUTPUT)
clips.sort()

for filename in clips:
    cliparray.append(VideoFileClip(OUTPUT + filename))

bar.update(1)

#fade_duration = 1
#cliparray = [clip.crossfadein(fade_duration) for clip in cliparray]

final_clip = concatenate_videoclips(cliparray)  #, padding=-fade_duration)

bar.update(2)

if len(musics) > 0:
    audio_background = mpe.AudioFileClip(RESOURCES_MUSICS_PATH + musics[0])
    logging.debug("Edition audio")
    final_audio = mpe.CompositeAudioClip([final_clip.audio, audio_background])
    final_audio = final_audio.subclip(0, final_clip.duration)
    final_clip.audio = final_audio
    bar.update(3)
    logging.debug("Writing video")
    sys.stdout = open("stats.log", 'w')
    final_clip.write_videofile("export_with_music.mp4",
                               verbose=False,
                               logger=None)
    sys.stdout.close()
else:
    sys.stdout = open("stats.log", 'w')
    final_clip.write_videofile("export.mp4", verbose=False, logger=None)
    sys.stdout.close()

bar.finish()

if not args.keep:
    logging.debug("Removing output folder")
    clear_directories(OUTPUT)

logging.debug("Closing loop")
loop = asyncio.get_event_loop()
loop.close()

logging.info("Done")
