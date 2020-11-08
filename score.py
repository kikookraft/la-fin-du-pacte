import pygame
import os

class Score:
    def __init__(self):
        print("\n\n----------------------------------------------\n                LA FIN DU PACTE\n----------------------------------------------\n\n")
           
    def load(self):
        if os.path.exists('data/player.txt'):
            with open("data/player.txt", 'r') as f:
                level = f.readline().rstrip('\r\n')
                dialog = f.readline().rstrip('\r\n')
                name = f.readline().rstrip('\r\n')
                return level, dialog, name
        else:
            self.add()
            level = 0
            dialog = 0
            name = "None"
            return level, dialog, name
            
    def add(self):
        level = 0
        dialog = 0
        name = "None"
        with open("data/player.txt", 'w') as f:
            f.write(str(level)+"\r")
            f.write(str(dialog)+"\r")
            f.write(str(name)+"\r")

    def save(self, level, dialog, name, close=0):
        f = open("data/player.txt", 'w')
        f.write(str(level)+"\r")
        f.write(str(dialog)+"\r") 
        f.write(str(name)+"\r")
        if close == 1:
            pygame.quit()
            quit()
        
