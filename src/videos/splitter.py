import asyncio
import os
from videos.videos import video_object

from utils.arguments import *


async def split(start: int, end: int, name: str, path_to_save: str,
                path_video: str):
    if not os.path.exists(path_video):
        print(f"{path_video} does not exist")
        exit()

    if args.debug:
        proc = await asyncio.create_subprocess_exec(
            "ffmpeg", "-y", "-i", path_video, "-vf",
            f"trim=start={start}:end={end},setpts=PTS-STARTPTS", "-af",
            f"atrim=start={start}:end={end},asetpts=PTS-STARTPTS",
            f"{path_to_save}{name}.mp4", "-loglevel", "error", "-stats")
    else:
        proc = await asyncio.create_subprocess_exec(
            "ffmpeg", "-y", "-i", path_video, "-vf",
            f"trim=start={start}:end={end},setpts=PTS-STARTPTS", "-af",
            f"atrim=start={start}:end={end},asetpts=PTS-STARTPTS",
            f"{path_to_save}{name}.mp4", "-loglevel", "quiet")

    returncode = await proc.wait()


def trim_video_from_tasks(tasks):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))


def create_tasks_from_videos_objects(videos_objects, path_to_save: str,
                                     path_video: str):
    tasks = []
    for video_obj in videos_objects:
        tasks.append(create_task(video_obj, path_to_save, path_video))
    return tasks


def create_task(video_obj: video_object, path_to_save, path_video):
    return asyncio.ensure_future(
        split(video_obj.start, video_obj.end, video_obj.name, path_to_save,
              path_video))
