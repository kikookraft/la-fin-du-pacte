#importation des differents fichiers
import pygame
import math
import os
import json

class Game:
    def __init__(self):
        print("\n\n----------------------------------------------\n                LA FIN DU PACTE\n----------------------------------------------\n\n")
        
    def clear(self, screen):
        screen.fill((0,0,0))

    class lvl:   
        screen = pygame.display.set_mode((1080,720))
        info = pygame.display.Info()
        width = info.current_w
        height = info.current_h

        # Importation des niveaux (oui je le fait en plain millieu XD)
        from nvx.tuto import Tuto
        from nvx.exemple import dawa
        from nvx.nvx1_Z import Level1_Z

        def play(self, screen, level, dialog, name):
            level = int(level)
            dialog = int(dialog)
            name = str(name)

            #recherche des fichiers du niveau
            if level == -1: #niveau de test
                file = "nvx/exemple.py"
                nvx = self.dawa().game(screen, name)
                pygame.mixer.music.stop()
                if nvx[3] == True:
                    return nvx[0], nvx[1], nvx[2], True
                else:
                    return nvx[0], nvx[1], nvx[2], False

            elif name == "Zach":
                if level == 1:
                    nvx = self.Level1_Z().game(screen, dialog, name)
                    pygame.mixer.music.stop()
                    if nvx[3] == True:
                        return nvx[0], nvx[1], nvx[2], True
                    else:
                        return nvx[0], nvx[1], nvx[2], False
                elif level == 2:
                    file = "nvx/nvx2.py"
                elif level == 3:
                    file = "nvx/nvx3.py"
                elif level == 4:
                    file = "nvx/nvx4.py"
            elif name == "Angela":
                if level == 1:
                    file = "nvx/nvx1A.py"
                elif level == 2:
                    file = "nvx/nvx2A.py"
                elif level == 3:
                    file = "nvx/nvx3A.py"
                elif level == 4:
                    file = "nvx/nvx4A.py"
            elif name == "UtopiaJr":
                if level == 1:
                    file = "nvx/nvxU.py"
                elif level == 2:
                    file = "nvx/nvxUU.py"
                elif level == 3:
                    file = "nvx/nvxUUU.py"
                elif level == 4:
                    file = "nvx/nvxX.py"

            else:
                nvx = self.Tuto().game(screen)
                pygame.mixer.music.stop()
                if nvx[3] == True:
                    return nvx[0], nvx[1], nvx[2], True
                else:
                    return nvx[0], nvx[1], nvx[2], False
                



    class new:
        def new(self):
            print("Cette fonctionnalitée est temporairement désactivée !")
            # print("\nSupression de 'nvx/nvx2/player.txt'")
            # try:
            #     os.remove('nvx/nvx2/player.txt')
            # except:
            #     print("Erreur, il n'y a rien a suprimmer dans le niveau 2!\n")
            # print("\nSupression de 'data/player.txt'")



    class score:
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

        def save(self, level, dialog, name):
            f = open("data/player.txt", 'w')
            f.write(str(level)+"\r")
            f.write(str(dialog)+"\r") 
            f.write(str(name)+"\r")



    class credit:
        clock=pygame.time.Clock()

        screen = pygame.display.set_mode((1080,720))
        info = pygame.display.Info()
        width = info.current_w
        height = info.current_h
        if width == 1080 and height == 720:
            modified = False
            speed = 1
        else:
            modified = True
            speed = 3
        credit = True
        bgpos = 0

        background = pygame.image.load('assets/credit-bg.jpg').convert()
        xmin = (info.current_w - background.get_width()) / 2
        ymin = (info.current_h - background.get_height()) / 2
        xmax = width - xmin
        ymax = height + ymin
        position_fond = (xmin, ymin)

        ypos= 0
        HT = True

        boucle = 0
        state = 0
        
        pygame.font.init()
        font = pygame.font.Font('assets/font/Apocalypse.ttf', 60)
        font2 = pygame.font.Font('assets/font/Apocalypse.ttf', 80)
        alpha_fadeout = 0
        fadein_finished = False
        alpha_fadein = 255

        def wait(self, wait):
            for i in range(int(wait)):
                pygame.time.wait(10)
                try:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            return 1
                        elif event.type == pygame.KEYDOWN and event.key != pygame.K_ESCAPE or event.type == pygame.MOUSEBUTTONDOWN:
                            return 0
                except:
                    pass

        def init(self):
            pygame.mixer.music.stop()
            pygame.display.set_caption("Les credits")
            pygame.mixer.music.load("assets/sounds/kikookraft - Space Fight.wav")
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(loops=50, start=0.0) 

        def fadeout(self):
            alpha_screen = 255
            while alpha_screen > 0:
                fnd = pygame.Surface((self.width, self.height))
                fnd.set_alpha(self.speed)  
                fnd.fill((0,0,0))
                self.screen.blit(fnd, (0, 0)) 
                pygame.display.flip()
                self.wait(1)
                alpha_screen -= self.speed
                
        def fadein(self):
            if self.alpha_fadein >= 1:
                self.alpha_fadein -= self.speed
                fnd = pygame.Surface((self.width, self.height))
                fnd.set_alpha(self.alpha_fadein)  
                fnd.fill((0,0,0))
                self.screen.blit(fnd, (0, 0)) 
            else:
                return True
            
        def backgroundimg(self):
            if not self.ypos > 0 and self.HT == True :
                self.ypos +=0.5*self.speed
            if self.ypos > 0 :
                self.HT = False
            if not self.ypos < -self.background.get_height()-self.height and self.HT==False:
                self.ypos -=0.5*self.speed
            if self.ypos < -5.9*self.height :
                self.HT = True
            self.screen.blit(self.background, (self.xmin, math.ceil(self.ypos)))
            
        def text(self, pos, side, text, font=1):
            if font == 1:
                button_text = self.font.render(text, True, (255, 255, 255))
            else:
                button_text = self.font2.render(text, True, (255, 255, 255))
            self.screen.blit(button_text, (side*self.width/4-button_text.get_width()/2, self.height/2+pos))

        def start(self):
            self.init()
            self.fadeout()
            self.wait(50)
            while self.credit:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                self.backgroundimg()
                self.text(-340, 2, "LA FIN DU", 2)
                self.text(-260, 2, "PACTE", 2)
                if self.fadein_finished != True:
                    self.fadein_finished = self.fadein()
                if self.fadein_finished == True:
                    self.boucle += self.speed
                if self.boucle > 46:
                    self.boucle = 0
                    self.state+=1
                
                if self.state >= 1 and self.state <= 10:
                    self.text(-100, 2, "LA FIN DU PACTE")
                if self.state >= 2 and self.state <= 10:
                    self.text(-30, 2, "UNE IDEE ORIGINALE DE:")
                if self.state >= 3 and self.state <= 10:
                    self.text(50, 1, "ANTOINE")
                if self.state >= 4 and self.state <= 10:
                    self.text(50, 2, "ET")
                if self.state >= 5 and self.state <= 10:
                    self.text(50, 3, "QUENTIN")

                if self.state > 11 and self.state <= 20:
                    self.text(-30, 2, "CODE FAIT PAR")
                if self.state > 12 and self.state <= 20:
                    self.text(50, 1, "TOMY")
                if self.state > 13 and self.state <= 20: 
                    self.text(50, 2, "ET")
                if self.state > 14 and self.state <= 20:
                    self.text(50, 3, "ANTOINE")
                
                if self.state > 21 and self.state <= 30:
                    self.text(-30, 2, "SCENARIO FAIT PAR")
                if self.state > 22 and self.state <= 30:
                    self.text(50, 1, "QUENTIN")
                if self.state > 23 and self.state <= 30:
                    self.text(50, 2, "ET")
                if self.state > 24 and self.state <= 30:
                    self.text(50, 3, "ANTOINE")
                
                if self.state > 31 and self.state <= 40:
                    self.text(-100, 2, "STRUCTURE DU JEUX")
                    self.text(-30, 2, "ET ORGANISATION")
                if self.state > 32 and self.state <= 40:
                    self.text(50, 1, "SAMUEL")
                if self.state > 33 and self.state <= 40:
                    self.text(50, 2, "ET")
                if self.state > 34 and self.state <= 40:
                    self.text(50, 3, "TOMY")

                if self.state > 41 and self.state <= 50:
                    self.text(-30, 2, "MUSIQUES ET IMAGES")
                if self.state > 42 and self.state <= 50:
                    self.text(50, 2, "TOMY")
                
                if self.state > 51 and self.state <= 60:
                    self.text(-30, 2, "SCENES ET RENDU 3D")
                if self.state > 52 and self.state <= 60:
                    self.text(50, 2, "ANTOINE")

                if self.state > 61 and self.state <= 70:
                    self.text(-100, 2, "SCENARIO DES PERSONNAGES")
                    self.text(-30, 2, "ZACH ET UTOPIA JR")
                if self.state > 62 and self.state <= 70:
                    self.text(50, 2, "ANTOINE")
                
                if self.state > 71 and self.state <= 80:
                    self.text(-100, 2, "SCENARIO DU PERSONNAGE")
                    self.text(-30, 2, "ANGELA")
                if self.state > 72 and self.state <= 80:
                    self.text(50, 2, "QUENTIN")
                
                if self.state > 81 and self.state <= 90:
                    self.text(-100, 2, "CODE DE LA V 2")
                if self.state > 82 and self.state <= 90:
                    self.text(62, 2, "TOMY")
                
                # attendre scenario antoine suite

                if self.state > 91:
                    self.fadeout()
                    return

                self.clock.tick(100)
                pygame.display.flip()