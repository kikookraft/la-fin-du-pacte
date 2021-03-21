import pygame
import os
import sys
import json

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
    init_lvl = []

    def initialisation(self, screen, imgperso=["perso1.png","perso2.png"], posperso=[(650,220),(150,220)], scaleperso=[(300,500),(300,500)], weapon=["None","None"], background="None.jpg", music="None.wav", restart_music=False, name="None"):
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
        level.init_lvl = [screen, imgperso, posperso, scaleperso, weapon, background, music, False, name]
        #écran de fond
        if background not in ["None",None,"None.jpg"]:
            background1 = str('assets/bg/{}'.format(background))
            bgd = pygame.image.load(background1)
            bgd = pygame.transform.scale(bgd, (width,height))
            screen.blit(bgd, bgd.get_rect())
        #personnage
        if imgperso[0] != "None" and imgperso != "None":
            for perso in imgperso:
                persosave = perso
                if perso == "perso" and name != "None":
                    perso = str(name+".png")
                boy = pygame.image.load(str("assets/"+str(perso)))
                scalepersotmp = scaleperso[imgperso.index(persosave)]
                pospersotmp = posperso[imgperso.index(persosave)]
                if scaleperso != "None": boyr = pygame.transform.scale(boy,(int(scalepersotmp[0]),int(scalepersotmp[1])))
                screen.blit(boyr,(int(pospersotmp[0]),int(pospersotmp[1])))
        #musique
        if restart_music and music != "None":
            pygame.mixer.music.stop()
            pygame.mixer.music.load("assets/sounds/%s" %(music))
            pygame.mixer.music.play(loops=-1) 
            pygame.mixer.music.set_volume(0.3)
        pygame.display.flip()
        
    def death(self, screen=screen, raison=None):
        '''Affiche l'écran de mort du joueur\n
        `screen` = écran\n
        `raison` = texte a afficher en dessous du message 'tu es mort'\n
        retourne "exit" si le joueur veut quitter le niveau\n
        retourne "quit" si le joueur veux quitter le jeux\n'''
        pygame.mixer.music.stop()
        pygame.mixer.music.load("assets/sounds/death.wav")
        pygame.mixer.music.play(loops=-1) 
        pygame.mixer.music.set_volume(0.3)
        font = pygame.font.SysFont('Helvetica', 40, bold=True)
        screen.fill((0,0,0))
        background_death = pygame.image.load("assets/death.jpg").convert()
        screen.blit(background_death,(0,0))
        #afficher raison de mort
        button_text = font.render(raison, True, (255, 25, 25))
        text_rect = button_text.get_rect(center=(width/2, height/2+150))
        screen.blit(button_text,text_rect)
        pygame.display.flip()
        tmp = self.wait(650)
        pygame.mixer.music.stop()
        if tmp == "quit" or tmp == "exit":
            return tmp

    def wait(self, wait): #fonction qui sert a attendre sans bloquer la fenetre et qui permet de skipper (avec 's') ou en cliquant su l'écran
        '''Pour attendre un peu dans le jeu (sans bloquer l'écran sur windows)\n
        `initialisation`\n
        `wait` = temps a attendre (nb de secondes × 100 , ex: pour 5 sec mettre 500)\n
        retourne "exit" si le joueur veut quitter le niveau\n
        retourne "quit" si le joueur veux quitter le jeux\n'''
        for i in range(int(wait)):
            pygame.time.wait(10)
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return "quit"
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :
                        return "exit"
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

    def choice(self, screen, nbchoix, choix1=[], choix2=[], choix3=["None"]): #fonction pour generer des choix
        '''Pour créer un écran de choix\n
        `screen` = écran (variable screen)\n
        `nbchoix` = nombre de choix possibles (2 ou 3) \n
        `choix1` = texte du choix 1 (liste, 3 éléments max (3 lignes max))\n
        `choix2` = texte du choix 2 (liste, 3 éléments max (3 lignes max))\n
        `choix3` = texte du choix 3 (si 3 choix)(liste, 3 éléments max (3 lignes max)) \n
        retourne "exit" si le joueur veut quitter le niveau\n
        retourne "quit" si le joueur veux quitter le jeux\n
        retourne 1, 2 ou 3 en fonction du choix du joueur\n'''
        font = pygame.font.SysFont('Helvetica', 22, bold=True)
        choice = True
        TEXT = ""
        TEXT2= ""
        TEXT3= ""
        i = 0
        while choice:
            pygame.display.flip()
            if i < 3:
                for tt in range(3):
                    pygame.draw.rect(screen, (100, 5, 5), (tt*width/3+10, height-110, width/3-20, 100))
                    if tt == 0:
                        TEXT=choix1[0]
                        try: TEXT2= choix1[1]
                        except:pass
                        try: TEXT3= choix1[2]
                        except:pass
                    if tt == 1 and nbchoix == 3:
                        TEXT=choix2[0]
                        try: TEXT2= choix2[1]
                        except:pass
                        try: TEXT3= choix2[2]
                        except:pass
                    if tt == 1 and nbchoix == 2:
                        TEXT=""
                        TEXT2= ""
                        TEXT3= ""
                    if tt == 2 and nbchoix == 3:
                        TEXT=choix3[0]
                        try: TEXT2= choix3[1]
                        except:pass
                        try: TEXT3= choix3[2]
                        except:pass
                    if tt == 2 and nbchoix == 2:
                        TEXT=choix2[0]
                        try: TEXT2= choix2[1]
                        except:pass
                        try: TEXT3= choix2[2]
                        except:pass
                    button_text = font.render(str(TEXT), True, (255, 255, 255))
                    screen.blit(button_text, (tt*width/3+20, height-100))
                    button_text2 = font.render(str(TEXT2), True, (255, 255, 255))
                    screen.blit(button_text2, (tt*width/3+20, height-70))
                    button_text3 = font.render(str(TEXT3), True, (255, 255, 255))
                    screen.blit(button_text3, (tt*width/3+20, height-50))
                    i+=1
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return "exit"
                if event.type == pygame.quit:
                    return "quit"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q or event.type == pygame.KEYDOWN and event.key == pygame.K_a or event.type == pygame.KEYDOWN and event.key == pygame.K_1 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_1 \
                    or event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 0*width/3+10 and pygame.mouse.get_pos()[0] < (0*width/3+10)+width/3-20 and pygame.mouse.get_pos()[1] > height-110 and pygame.mouse.get_pos()[1] < height-10:
                    pygame.draw.rect(screen, (255,255,255), (0*width/3+8, height-113, width/3-16, 106), 6)
                    pygame.display.flip()
                    choice = False
                    return 1
                if nbchoix == 2:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_b or event.type == pygame.KEYDOWN and event.key == pygame.K_2 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_2 \
                        or event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 2*width/3+10 and pygame.mouse.get_pos()[0] < (2*width/3+10)+width/3-20 and pygame.mouse.get_pos()[1] > height-110 and pygame.mouse.get_pos()[1] < height-10:
                        pygame.draw.rect(screen, (255,255,255), (2*width/3+8, height-113, width/3-16, 106), 6)
                        pygame.display.flip()
                        choice = False
                        return 2
                if nbchoix == 3:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_b or event.type == pygame.KEYDOWN and event.key == pygame.K_2 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_2 \
                        or event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 1*width/3+10 and pygame.mouse.get_pos()[0] < (1*width/3+10)+width/3-20 and pygame.mouse.get_pos()[1] > height-110 and pygame.mouse.get_pos()[1] < height-10:
                        pygame.draw.rect(screen, (255,255,255), (1*width/3+8, height-113, width/3-16, 106), 6)
                        pygame.display.flip()
                        choice = False
                        return 2
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_c or event.type == pygame.KEYDOWN and event.key == pygame.K_3 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_3 \
                        or event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 2*width/3+10 and pygame.mouse.get_pos()[0] < (2*width/3+10)+width/3-20 and pygame.mouse.get_pos()[1] > height-110 and pygame.mouse.get_pos()[1] < height-10:
                        pygame.draw.rect(screen, (255,255,255), (2*width/3+8, height-113, width/3-16, 106), 6)
                        pygame.display.flip()
                        choice = False
                        return 3
    
    def dialogue(self, list_dialog=["Prhase numéro une","Phrase numéro 2"], time_between=10, make_init=True):
        '''Pour créer un écran de choix\n
        `list_dialog` = Liste des phrases a afficher (liste de str)\n
        `time_between` = Temp d'attente entre chaque dialogue avant d'afficher le prochain (temp en sec * 100  , 1 sec => 100)\n
        `make_init` = Si True: faire l'initialisation de l'écran pour effacer le texte, mettre a False pour laisser le texte affiché\n
        exemples: si il y a une question et l'action suivante est un choix (pour laisser la question visible)
        Une fois tout les dialogues fait (ceux de la liste), le joueur doit cliquer \n
        pour continuer et passer a la suite (passer aux lignes de code suivantes) \n
        retourne "exit" si le joueur veut quitter le niveau\n
        retourne "quit" si le joueur veux quitter le jeux\n'''
        level.initialisation(self, level.init_lvl[0], level.init_lvl[1], level.init_lvl[2], level.init_lvl[3], level.init_lvl[4], level.init_lvl[5], level.init_lvl[6], level.init_lvl[7], level.init_lvl[8])
        font = pygame.font.SysFont('Helvetica', 40, bold=True)
        scen = 1
        y = 21
        nb = 0
        number = 0
        remaindialog = True
        texte_remain = "Nothing"
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
                list_dialog.insert(list_dialog.index(textesave)+1, texte_remain)
            for l in current_speech: #morceau de code pour afficher les lettres une par une
                text = font.render(str(l), True, (255, 255, 255)) 
                x+=text.get_width()
                screen.blit(text, (x2+30,y))
                x2 = x
                if skip_dial == False:
                    tmp = level.wait(self, 4)
                if tmp == "quit" or tmp == "exit":
                    return tmp
                elif tmp == 0:
                    skip_dial = True
                pygame.display.flip()
            y += 48
            pygame.display.flip()
            tmp = level.wait(self, time_between)
            if tmp == "quit" or tmp == "exit":
                return tmp
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
                        level.initialisation(self, level.init_lvl[0], level.init_lvl[1], level.init_lvl[2], level.init_lvl[3], level.init_lvl[4], level.init_lvl[5], level.init_lvl[6], level.init_lvl[7], level.init_lvl[8])
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return "exit"
                if event.type == pygame.quit:
                    return "quit"

class media():
    '''Cette classe sert a afficher/ecouter des source de médias\n
    comme des images, des effets sonores, ...
    Cette classe comprend les fonctions:\n
    `image`\n
    `sound`\n
    `save_file` (classe pour fichier de sauvegarde)'''

    def image(self, file, pos=(0,0), scale=(50,50)):
        '''Afficher une image\n
        `file` = fichier de l'image a afficher\n
        `pos` = position de l'image\n
        `scale` = taille de l'image (pour redimensionner)\n'''
        img = pygame.image.load(file)
        imgprint = pygame.transform.scale(img,scale)
        screen.blit(imgprint,pos)
    
    def sound(self, file, vol=0.5, loop=False):
        '''Jouer un son\n
        `file` = fichier du son\n
        `vol` = volume du son\n'''
        sound = pygame.mixer.Sound(file)
        sound.set_volume(vol)
        if loop: sound.play(-1)
        else: sound.play()
    
    class save_file:
        '''Contient les fonction pour sauvegarder et lire les fichiers des niveaux
        '''

        def create(self, file_name, data):
            with open("level_data"+str(file_name), 'w') as outfile:
                json.dump(data, outfile, indent=4)
        
        def read(self, file_name):
            try:
                with open("level_data"+str(file_name), "r") as f:
                    data = json.load(f)
                return data
            except FileNotFoundError: raise FileNotFoundError("Le fichier '{}' n'a pas été trouvé!".format(file_name))
        
        # Pour créer un fichier de sauvegarde json:
        # score.File().create("test.json", {'name':"Zach",'choice':[1,5,1,5,3,8,1],'machettes':True})
        # 
        # Pour le lire et recuperer les infos du fichier
        # data = score.File().read("test.json")