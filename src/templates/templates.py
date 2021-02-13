import cv2
import numpy as np

def find_template(image, template):
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, _, _ = cv2.minMaxLoc(res)
    return max_val > 0.80
    # return np.where(res > 0.80)

def draw_template(image, template):
    height, width, chan = template.shape
    for point in zip(*find_template(image, template)[::-1]):
        cv2.rectangle(image, (point[0] - 2, point[1] - 2),
                          (point[0] + width + 2, point[1] + height + 2),
                          (200,200,200), 2)

def post_process_frames_with_template(frames):
    result = []
    sub_result = []
    last = 0

    for i in range(len(frames)):
        if last + 1 == frames[i] or last == 0:
            sub_result.append(frames[i])
        else:
            result.append(sub_result)
            sub_result = [frames[i]]
        last = frames[i]
    result.append(sub_result)
    return result

def post_process_frames_in_tuples(frames_processed):
    result = []
    for clip in frames_processed:
        result.append((clip[0], len(clip)))
    return result
