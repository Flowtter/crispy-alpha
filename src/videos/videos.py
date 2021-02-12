import cv2
import time
from errors.errors import *

def extract_images_and_save_from_video(input_path: str, output_path: str):
    start_time = time.time()

    vidcap = cv2.VideoCapture(input_path)
    count = 0
    success = True

    fps = int(vidcap.get(cv2.CAP_PROP_FPS))

    if fps == 0:
        raise WrongPath(f"{input_path} is not a valid path")

    while success:
        success = vidcap.grab()
        if count % fps == 0:
            success, image = vidcap.read()
            cv2.imwrite(output_path + f"frame{int(count/fps)}.jpg", image)
        count += 1

    vidcap.release()
    return count/fps, time.time() - start_time
