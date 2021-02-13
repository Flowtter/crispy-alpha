import asyncio
import os
from videos.videos import video_object

cwd = os.getcwd()

async def split(start :int, end :int, name : str, path: str):
    proc = await asyncio.create_subprocess_exec(
        "ffmpeg", "-y",
        "-i", f"{cwd}/tmp/videos/main.mp4",
        "-vf", f"trim=start={start}:end={end},setpts=PTS-STARTPTS",
        "-af", f"atrim=start={start}:end={end},asetpts=PTS-STARTPTS",
        f"{path}{name}.mp4",
        "-loglevel", "error",
        "-stats"
    )
    returncode = await proc.wait()

def trim_video_from_tasks(tasks):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()

def create_tasks_from_videos_objects(videos_objects):
    tasks = []
    for video_obj in videos_objects:
        tasks.append(create_task(video_obj))
    return tasks
    

def create_task(video_obj :video_object):
    return asyncio.ensure_future(split(video_obj.start, video_obj.end, video_obj.name, "tmp/videos/output/"))
