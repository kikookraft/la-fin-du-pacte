import pygame
import os
import sys

screen = pygame.display.set_mode((1080,720))
info = pygame.display.Info()
width = info.current_w
height = info.current_h

class level():
    '''Classe qui gère le fonctionnement principal du niveau\n
    Cette classe comprend les fonctions:\n
    `initialisation`\n
    `death`\n
    `wait`\n
    `title`\n'''
    self.init_lvl = []
    def initialisation(self, screen, imgperso=["perso1.png","perso2.png"], posperso=[(300,0),(200,130)], scaleperso=[(500,500),(200,100)], weapon=["None","None"], background="None.jpg", music="None.wav", restart_music=False, name="None"):
        '''Permet d'initialiser l'écran!\n
        `screen` = écran (variable screen),\n 
        `imgperso` = images de chaque personnages, écrire `perso` pour utiliser le personnage du joueur (liste),\n 
        `posperso` = position de chaque personnages (liste),\n 
        `scaleperso` = taille des personnages (liste),\n 
        `weapon` = non fonctionnel pour l'instant (liste),\n 
        `background` = image de fond (str),\n 
        `music` = musique a mettre (str),\n 
        `restart_music` = redémarer ou pas la musique (true/false)\n
        `name` = variable contenant le nom du personnage'''
        #enregister variable pour les dialogues
        self.init_lvl = [screen, imgperso, posperso, scaleperso, weapon, background, music, False, name]
        #écran de fond
        background1 = str("assets/bg/"+background)
        bgd = pygame.image.load(background1)
        bgd = pygame.transform.scale(bgd, (width,height))
        screen.blit(bgd, bgd.get_rect())
        #personnage
        if imgperso[0] != "None":
            for perso in imgperso:
                if perso == "perso" and name != "None":
                    perso = str(name+".png")
                boy = pygame.image.load(str("assets/"+str(perso)))
                scalepersotmp = scaleperso[imgperso.index(perso)]
                pospersotmp = posperso[imgperso.index(perso)]
                boyr = pygame.transform.scale(boy,(int(scalepersotmp[0]),int(scalepersotmp[1])))
                screen.blit(boyr,(int(pospersotmp[0]),int(pospersotmp[1])))
        #musique
        if restart_music and music != "None":
            pygame.mixer.music.stop()
            pygame.mixer.music.load("assets/sounds/%s" %(music))
            pygame.mixer.music.play(loops=-1) 
            pygame.mixer.music.set_volume(0.3)
        
    def death(self, screen=screen, raison=None):
        '''Affiche l'écran de mort du joueur\n
        `screen` = écran\n
        `raison` = texte a afficher en dessous du message 'tu es mort'\n
        retourne 1 si le joueur veut quitter\n'''
        pygame.mixer.music.stop()
        pygame.mixer.music.load("assets/sounds/death.mp3")
        pygame.mixer.music.play(loops=-1) 
        pygame.mixer.music.set_volume(0.3)
        font = pygame.font.SysFont('Helvetica', 40, bold=True)
        screen.fill((0,0,0))
        background = pygame.image.load("assets/death.jpg").convert()
        screen.blit(background,(0,0))
        #afficher raison de mort
        button_text = font.render(raison, True, (255, 25, 25))
        text_rect = button_text.get_rect(center=(width/2, height/2+150))
        screen.blit(button_text,text_rect)
        pygame.display.flip()
        tmp = self.wait(500)
        pygame.mixer.music.stop()
        if tmp == 1:
            return 1

    def wait(self, wait): #fonction qui sert a attendre sans bloquer la fenetre et qui permet de skipper (avec 's') ou en cliquant su l'écran
        '''Pour attendre un peu dans le jeu (sans bloquer l'écran sur windows)\n
        `initialisation`\n
        `wait` = temps a attendre (nb de secondes × 100 , ex: pour 5 sec mettre 500)\n
        retourne 1 si le joueur veut quitter\n'''
        for i in range(int(wait)):
            pygame.time.wait(10)
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return 1
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :
                        return 1
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_s :
                        return 0
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        return 0
            except:
                pass
    
    def title(self, title):
        '''Changer le titre de la fenetre\n
        '''
        pygame.display.set_caption(title)

class story():
    '''Classe qui gère le déroulement de l'histoire (dialogues, choixs)\n
    Cette classe comprend les fonctions:\n
    `choice`\n
    `dialogue`\n'''

    def choice(self, screen, nbchoix, choix1, choix2, choix3="None"): #fonction pour generer des choix
        '''Pour créer un écran de choix\n
        `screen` = écran (variable screen)\n
        `nbchoix` = nombre de choix possibles (2 ou 3) \n
        `choix1` = texte du choix 1 \n
        `choix2` = texte du choix 2 \n
        `choix3` = texte du choix 3 (si 3 choix) \n
        retourne 0 si le joueur veut quitter
        retourne 1, 2 ou 3 en fonction du choix du joueur'''
        font = pygame.font.SysFont('Helvetica', 22, bold=True)
        choice = True
        i = 0
        while choice:
            pygame.display.flip()
            if i < 3:
                for tt in range(3):
                    pygame.draw.rect(screen, (100, 5, 5), (tt*width/3+10, height-110, width/3-20, 100))
                    if tt == 0:
                        TEXT=choix1
                        TEXT2= None
                    if tt == 1 and nbchoix == 3:
                        TEXT=choix2
                    if tt == 1 and nbchoix == 2:
                        TEXT=""
                    if tt == 2 and nbchoix == 3:
                        TEXT=choix3
                    if tt == 2 and nbchoix == 2:
                        TEXT=choix2
                    button_text = font.render(TEXT, True, (255, 255, 255))
                    screen.blit(button_text, (tt*width/3+20, height-100))
                    i+=1
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.quit:
                    return 0
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q or event.type == pygame.KEYDOWN and event.key == pygame.K_a or event.type == pygame.KEYDOWN and event.key == pygame.K_1 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_1 \
                    or event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 0*width/3+10 and pygame.mouse.get_pos()[0] < (0*width/3+10)+width/3-20 and pygame.mouse.get_pos()[1] > height-110 and pygame.mouse.get_pos()[1] < height-10:
                    pygame.draw.rect(screen, (255,255,255), (0*width/3+8, height-113, width/3-16, 106), 6)
                    choice = False
                    return 1
                if nbchoix == 2:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_b or event.type == pygame.KEYDOWN and event.key == pygame.K_2 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_2 \
                        or event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 2*width/3+10 and pygame.mouse.get_pos()[0] < (2*width/3+10)+width/3-20 and pygame.mouse.get_pos()[1] > height-110 and pygame.mouse.get_pos()[1] < height-10:
                        pygame.draw.rect(screen, (255,255,255), (2*width/3+8, height-113, width/3-16, 106), 6)
                        choice = False
                        return 2
                if nbchoix == 3:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_b or event.type == pygame.KEYDOWN and event.key == pygame.K_2 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_2 \
                        or event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 1*width/3+10 and pygame.mouse.get_pos()[0] < (1*width/3+10)+width/3-20 and pygame.mouse.get_pos()[1] > height-110 and pygame.mouse.get_pos()[1] < height-10:
                        pygame.draw.rect(screen, (255,255,255), (1*width/3+8, height-113, width/3-16, 106), 6)
                        choice = False
                        return 2
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_c or event.type == pygame.KEYDOWN and event.key == pygame.K_3 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_3 \
                        or event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 2*width/3+10 and pygame.mouse.get_pos()[0] < (2*width/3+10)+width/3-20 and pygame.mouse.get_pos()[1] > height-110 and pygame.mouse.get_pos()[1] < height-10:
                        pygame.draw.rect(screen, (255,255,255), (2*width/3+8, height-113, width/3-16, 106), 6)
                        choice = False
                        return 3
    
    def dialogue(self, list_dialog=["Prhase numéro une","Phrase numéro 2"], time_between=100, make_init=True):
        '''Pour créer un écran de choix\n
        `list_dialog` = Liste des phrases a afficher (liste de str)\n
        `time_between` = Temp d'attente entre chaque dialogue avant d'afficher le prochain (temp en sec * 100  , 1 sec => 100)\n
        `make_init` = Si True: faire l'initialisation de l'écran pour effacer le texte, mettre a False pour laisser le texte affiché\n
        exemples: si il y a une question et l'action suivante est un choix (pour laisser la question visible)
        Une fois tout les dialogues fait (ceux de la liste), le joueur doit cliquer \n
        pour continuer et passer a la suite (passer aux lignes de code suivantes) \n
        retourne 1 si le joueur veut quitter\n'''
        self.initialisation(self.init_lvl[0], self.init_lvl[1], self.init_lvl[2], self.init_lvl[3], self.init_lvl[4], self.init_lvl[5], self.init_lvl[6], self.init_lvl[7], self.init_lvl[8])
        font = pygame.font.SysFont('Helvetica', 40, bold=True)
        scen = 1
        y = 21
        nb = 0
        number = 0
        remaindialog = True
        texte_remain = "None"
        for current_speech in list_dialog:
            fnd = pygame.Surface((width-40, 48))
            fnd.set_alpha(200)  
            fnd.fill((100, 5, 5))
            screen.blit(fnd, (20, y)) 
            r = ""
            x = 0
            x2 = 0
            skip_dial = False
            textesave = current_speech
            text_width = 0
            # systeme pour passer a la ligne le texte quand il est trop long
            if font.render(str(current_speech), True, (255,255,255)).get_width() > width-60:
                while font.render(str(current_speech), True, (255,255,255)).get_width() > width-60:
                    current_speech = current_speech[:-1]
                while current_speech[len(current_speech)-1] != " ": #voir ou est l'espace précédent pour eviter de couper des mots
                    current_speech = current_speech[:-1]
                texte_remain = textesave[len(current_speech):]
            for l in current_speech: #morceau de code pour afficher les lettres une par une
                text = font.render(str(l), True, (255, 255, 255)) 
                x+=text.get_width()
                screen.blit(text, (x2+30,y))
                x2 = x
                if skip_dial == False:
                    tmp = self.wait(4)
                if tmp == 1:
                    return 1
                elif tmp == 0:
                    skip_dial = True
                pygame.display.flip()
            y += 48
            pygame.display.flip()
            tmp = self.wait(time_between)
            if tmp == 1:
                return 1
        fnd = pygame.Surface((20, 20))
        fnd.set_alpha(255)  
        fnd.fill((255,255,255))
        screen.blit(fnd, (width-20, 0))
        pygame.display.flip()
        while nb == 0:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN: #and event.key == pygame.K_s
                    nb = 1
                    if make_init:
                        self.initialisation(self.init_lvl[0], self.init_lvl[1], self.init_lvl[2], self.init_lvl[3], self.init_lvl[4], self.init_lvl[5], self.init_lvl[6], self.init_lvl[7], self.init_lvl[8])
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                    return 1

class media():
    '''Cette classe sert a afficher/ecouter des source de médias\n
    comme des images, des effets sonores, ...
    Cette classe comprend les fonctions:\n
    `image`\n
    `sound`\n'''

    def image(self, file, pos, scale):
        '''Afficher une image\n
        `file` = fichier de l'image a afficher\n
        `pos` = position de l'image\n
        `scale` = taille de l'image (pour redimensionner)\n'''
        imgprint = pygame.transform.scale(file,(int(scale[0]),int(scale[1])))
        screen.blit(imgprint,(int(pos[0]),int(pos[1])))
    
    def sound(self, file, vol=0.5):
        '''Jouer un son\n
        `file` = fichier du son\n
        `vol` = volume du son\n'''
        sound = pygame.mixer.Sound(file)
        sound.set_volume(vol)
        sound.play()