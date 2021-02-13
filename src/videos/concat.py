import asyncio
from utils.utils import *

cwd = os.getcwd()

# ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.mp4
async def concat(path: str):
    print(cwd + path)
    proc = await asyncio.create_subprocess_exec(
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i",  cwd + "/" + path,
        "-c", "copy",
        "concat.mp4",
        "-loglevel", "quiet",
        "-stats"
    )
    returncode = await proc.wait()


def create_log_file_of_videos(path):
    videos = get_all_files_from_path(path)
    with open(path + "videos.log", "w") as f:
        for video in videos:
            if ".mp4" in video:
                f.write(path + video+"\n")

def concat_videos_from_directory(path):
    tasks = [asyncio.ensure_future(concat(path + "videos.log"))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
    