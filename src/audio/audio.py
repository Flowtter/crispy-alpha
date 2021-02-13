import librosa
import IPython.display as ipd
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
    