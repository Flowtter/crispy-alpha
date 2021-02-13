import cv2
from errors.errors import *
from images.images import *

class video_object:
    def __init__(self, start, end, name):
        self.start = start
        self.end = end
        self.name = name

def extract_images_and_save_from_video(input_path: str, output_path: str, rate: int):
    vidcap = cv2.VideoCapture(input_path)
    count = 0
    success = True

    fps = int(vidcap.get(cv2.CAP_PROP_FPS))

    if fps == 0:
        raise WrongPath(f"{input_path} is not a valid path")

    while success:
        success = vidcap.grab()
        if count % (fps/rate) == 0:
            success, image = vidcap.read()
            cv2.imwrite(output_path + f"frame{int(count/fps)}.jpg", image)
        count += 1

    vidcap.release()
    return count/fps


def extract_images_and_crop_them(input_path: str, rate: int):
    resultLogo = []
    resultFeed = []

    vidcap = cv2.VideoCapture(input_path)
    count = 0
    success = True

    fps = int(vidcap.get(cv2.CAP_PROP_FPS))

    if fps == 0:
        raise WrongPath(f"{input_path} is not a valid path")

    while success:
        success = vidcap.grab()
        if count % (fps/rate) == 0:
            success, image = vidcap.read()
            tmp = crop_image_from_object(image)
            resultLogo.append(tmp[0])
            resultFeed.append(tmp[1])
        count += 1

    vidcap.release()
    return resultLogo, resultFeed
    


def create_video_object_from_frames_processed(tuples_processed, offset_start, offset_end, video_size_in_frame, name):
    videos_objects = []
    for i, clip in enumerate(tuples_processed):
        starting = clip[0] - offset_start
        ending = clip[0] + clip[1] + offset_end
        if starting < 0: 
            starting = 0
        if ending > video_size_in_frame:
            ending = video_size_in_frame - 2
        
        videos_objects.append(video_object(starting, ending, name + str(i)))
    return videos_objects


def post_process_videos_objects(videos_objects):
    for i in range(len(videos_objects)-1):
        remove_overlap_videos_objects(videos_objects[i], videos_objects[i+1])
    # todo: concat ovelap clips


def remove_overlap_videos_objects(video_obj1 : video_object, video_obj2 : video_object):    
    if video_obj1.end > video_obj2.start:
        overlap_time = video_obj1.end - video_obj2.start
        video_obj1.end -= (overlap_time//2 + 1)
        video_obj2.start += (overlap_time//2 - 1 + overlap_time%2)