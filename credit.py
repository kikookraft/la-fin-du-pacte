import pygame
import math
class Credit:
    clock=pygame.time.Clock()

    screen = pygame.display.set_mode((1080,720))
    info = pygame.display.Info()
    width = info.current_w
    height = info.current_h
    credit = True
    bgpos = 0

    background = pygame.image.load('assets/credit-bg.jpg').convert()
    logo = pygame.image.load('assets/logo.png').convert_alpha()
    xmin2 = (info.current_w - logo.get_width()) / 2
    ymin2 = (info.current_h - logo.get_height()) / 4
    xmax2 = width - xmin2
    ymax2 = height - ymin2
    position_fond2 = (xmin2, ymin2)
    xmin = (info.current_w - background.get_width()) / 2
    ymin = (info.current_h - background.get_height()) / 2
    xmax = width - xmin
    ymax = height + ymin
    position_fond = (xmin, ymin)

    ypos2 = ymin2
    logovar = 1
    ypos= 0
    HT = True

    boucle = 0
    state = 0
    
    pygame.font.init()
    font = pygame.font.Font('assets/Apocalypse.ttf', 60)

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
            fnd.set_alpha(2)  
            fnd.fill((0,0,0))
            self.screen.blit(fnd, (0, 0)) 
            pygame.display.flip()
            self.wait(2)
            alpha_screen -= 1
        
    def backgroundimg(self):
        if self.logovar == 1:
            self.ypos2 -= 1
            if self.ypos2 < 40:
                self.logovar = 0 
        if not self.ypos > 0 and self.HT == True :
            self.ypos +=0.5
        if self.ypos > 0 :
            self.HT = False
        if not self.ypos < -self.background.get_height()-self.height and self.HT==False:
            self.ypos -=0.5
        if self.ypos < -5.9*self.height :
            self.HT = True
        self.screen.blit(self.background, (self.xmin, math.ceil(self.ypos)))
        self.screen.blit(self.logo, (self.xmin2, self.ypos2))

    def text(self, pos, side, text):
        button_text = self.font.render(text, True, (255, 255, 255))
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
            self.boucle += 1
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
                self.text(50, 2, "TOMY")
            # if self.state > 13 and self.state <= 20: 
            #     self.text(50, 2, "ET")
            # if self.state > 14 and self.state <= 20:
            #     self.text(50, 3, "ANTOINE") #placer antoine pour avoir fait la version 1.0
            
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
            
            # ajouter tout les testeurs

            # ajouter les gens qui ont trouvé les ressources (tomy(musique et image), samuel(autres images,musiques), antoine(images3d, personnage))
            
            # ajouter le createur original des personnages (Zach: antoine, Angela:Quentin, UtopiaJR: Antoine)

            if self.state > 45:
                self.fadeout()
                return

            self.clock.tick(100)
            pygame.display.flip()


        