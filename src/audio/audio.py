import librosa
import IPython.display as ipd
import asyncio
import os

cwd = os.getcwd()
 
def get_beast_per_minute(path):
    x, sr = librosa.load(path) 
    tempo, _ = librosa.beat.beat_track(x, sr=sr)
    return tempo

# ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4

# ffmpeg -i video.mp4 -i audio.wav -c copy output.mkv

#ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 output.mp4

# ffmpeg -i v.mp4 -i a.wav -c:v copy -map 0:v:0 -map 1:a:0 new.mp4

async def audio(path_audio: str, path_video: str):
    proc = await asyncio.create_subprocess_exec(
        "ffmpeg",
        "-i", path_video,
        "-i", path_audio,
        "-map", "0:v",
        "-map", "1:a",
        "-c:v", "copy",
        "-c:a", "copy",
        "audio.mp4",
        "-y"
    )
    returncode = await proc.wait()

def add_audio_on_video(path_audio, path_video):
    tasks = [asyncio.ensure_future(audio(path_audio, path_video))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
    