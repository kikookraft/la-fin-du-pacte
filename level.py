import pygame
import os
from score import Score
import sys
class Lvl:   
    screen = pygame.display.set_mode((1080,720))
    info = pygame.display.Info()
    width = info.current_w
    height = info.current_h


    def play(self, screen, level, dialog, name):
        level = int(level)
        dialog = int(dialog)
        name = str(name)

        #recherche des fichiers du niveau
        if name == "Zach":
            if level == 0:
                file = "nvx/tuto.py"
            elif level == 1:
                file = "nvx/nvx1.py"
            elif level == 2:
                file = "nvx/nvx2.py"
            elif level == 3:
                file = "nvx/nvx3.py"
            elif level == 4:
                file = "nvx/nvx4.py"
        elif name == "Angela":
            if level == 0:
                file = "nvx/tuto.py"
            elif level == 1:
                file = "nvx/nvx1A.py"
            elif level == 2:
                file = "nvx/nvx2A.py"
            elif level == 3:
                file = "nvx/nvx3A.py"
            elif level == 4:
                file = "nvx/nvx4A.py"
        elif name == "UtopiaJr":
            if level == 0:
                file = "nvx/tuto.py"
            elif level == 1:
                file = "nvx/nvxU.py"
            elif level == 2:
                file = "nvx/nvxUU.py"
            elif level == 3:
                file = "nvx/nvxUUU.py"
            elif level == 4:
                file = "nvx/nvxX.py"
        else:
            file = "nvx/tuto.py"
