import pygame
from moviepy.editor import *

class Credit:
        
    def video(self, video):
        clip = VideoFileClip(video).resize((1080,720))
        clip.preview(fps=30)
