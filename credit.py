import pygame
from moviepy.editor import *

class Credit:
        
    def video(self, video):
        clip = VideoFileClip(video)
        #clip = clip.volumex(0.3)  #lorsque l'on reduit le volume, le son crash pendant la lecture
        clip.preview(fps=30)
