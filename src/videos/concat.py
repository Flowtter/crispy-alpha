import asyncio
from utils.utils import *
from utils.arguments import *

cwd = os.getcwd()


async def concat(path: str, path_out_and_name: str):
    if args.debug:
        proc = await asyncio.create_subprocess_exec(
            "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i",
            cwd + "/" + path, "-r", "60", "-c", "copy", path_out_and_name,
            "-loglevel", "error", "-stats")
    else:
        proc = await asyncio.create_subprocess_exec("ffmpeg", "-y", "-f",
                                                    "concat", "-safe", "0",
                                                    "-i", cwd + "/" + path,
                                                    "-r", "60", "-c", "copy",
                                                    path_out_and_name,
                                                    "-loglevel", "quiet")

    returncode = await proc.wait()


def create_log_file_of_videos(path):
    videos = get_all_files_and_folder_from_path(path)
    with open(path + "videos.log", "w") as f:
        for video in videos:
            if ".mp4" in video:
                f.write("file " + video + "\n")


def concat_videos_from_directory(path, path_out_and_name):
    tasks = [
        asyncio.ensure_future(concat(path + "videos.log", path_out_and_name))
    ]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
