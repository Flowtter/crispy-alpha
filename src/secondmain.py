import cv2
import os
import moviepy.editor as mpe

from videos.videos import *
from videos.splitter import *
from videos.concat import *
from audio.audio import *
from images.images import *
from templates.templates import *
from utils.paths import *
from utils.utils import *

print("Concat videos")
concat_videos_from_directory("tmp/videos/output/", "concat_video.mp4")
print("Loading video")
my_clip = mpe.VideoFileClip("concat_video.mp4")
print("Loading audio")
audio_background = mpe.AudioFileClip("tmp/audio/120BPM.wav")
print("Edition audio")
final_audio = mpe.CompositeAudioClip([my_clip.audio, audio_background])
final_audio = final_audio.subclip(0, my_clip.duration)
my_clip.audio = final_audio
print("Writing video")
my_clip.write_videofile("final.mp4")
print("Removing old video")
os.remove("concat_video.mp4")
