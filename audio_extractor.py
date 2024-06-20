import moviepy.editor as mp
import os

path = input("enter path of the file:")

Videoclip = mp.VideoFileClip(path)
Audioclip = Videoclip.audio
Audioclip.write_audiofile("audio.mp3")