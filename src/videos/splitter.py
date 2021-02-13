import asyncio
import os

cwd = os.getcwd()

async def do_subprocess(start :int, end :int, name : str):
    proc = await asyncio.create_subprocess_exec(
        "ffmpeg", "-y",
        "-i", f"{cwd}/tmp/videos/output.mp4",
        "-vf", f"trim=start={start}:end={end},setpts=PTS-STARTPTS",
        "-af", f"atrim=start={start}:end={end},asetpts=PTS-STARTPTS",
        f"{name}.mp4",
        "-loglevel", "quiet"
    )
    returncode = await proc.wait()

loop = asyncio.get_event_loop()

tasks = [
    asyncio.ensure_future(do_subprocess(2, 4, "t1")),
    asyncio.ensure_future(do_subprocess(4, 6, "t2")),
]

loop.run_until_complete(asyncio.gather(*tasks))
loop.close()
print("done")