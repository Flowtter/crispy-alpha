import librosa
import IPython.display as ipd
import os

cwd = os.getcwd()


def get_beast_per_minute(path):
    x, sr = librosa.load(path)
    tempo, _ = librosa.beat.beat_track(x, sr=sr)
    return tempo
