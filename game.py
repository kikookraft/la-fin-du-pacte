#importation des differents fichiers
import pygame
from score import Score
from credit import Credit
from level import Lvl
from new import New

class Game:
    def __init__(self):
        #grace a ceci , on peut faire : game.score. ...
        #cela fait gagner de la place dans main
        self.score = Score()
        self.credit = Credit()
        self.lvl = Lvl()
        self.new = New()
        
    def clear(self, screen):
        screen.fill((0,0,0))

        