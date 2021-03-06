import pygame
import os
#from moviepy.editor import *
from score import Score
import sys
class Lvl:   
    screen = pygame.display.set_mode((1080,720))
    info = pygame.display.Info()
    width = info.current_w
    height = info.current_h
    
    def initialisation(self, screen, imgperso=("perso1.png"), posperso=((0,0)), scaleperso=((500,500)), weapon=("None"), background="None.jpg", music="None.wav", statemusic=False, name="None"):
        '''Permet d'initialiser l'écran!\n
        `screen` = ecran,\n 
        `imgperso` = images de chaque personnages,\n 
        `posperso` = position de chaque personnages,\n 
        `scaleperso` = taille des personnages,\n 
        `weapon` = non fonctionnel pour l'instant,\n 
        `background` = image de fond,\n 
        `music` = musique a mettre,\n 
        `statemusic` = activer ou pas la musique'''
        background1 = str("assets/bg/"+background)
        bgd = pygame.image.load(background1)
        bgd = pygame.transform.scale(bgd, (self.width,self.height))
        screen.blit(bgd, bgd.get_rect())
        #personnage
        if imgperso != "None":
            if imgperso == "perso":
                imgperso =  str(name+".png")
            #mise en forme des variable (les mettre dans les bon format)
            imgperso = imgperso.split(',')
            posperso = posperso.split('/')
            scaleperso = scaleperso.split('/')
            for perso in imgperso:
                #print(perso,scaleperso[imgperso.index(perso)].split(","),posperso[imgperso.index(perso)].split(","))
                boy = pygame.image.load(str("assets/"+str(perso)))
                scalepersotmp = scaleperso[imgperso.index(perso)].split(",")
                pospersotmp = posperso[imgperso.index(perso)].split(",")
                boyr = pygame.transform.scale(boy,(int(scalepersotmp[0]),int(scalepersotmp[1])))
                screen.blit(boyr,(int(pospersotmp[0]),int(pospersotmp[1])))

        #musique
        if statemusic and music != "None":
            pygame.mixer.music.stop()
            pygame.mixer.music.load("assets/sounds/%s" %(music))
            pygame.mixer.music.play(loops=-1) 
            pygame.mixer.music.set_volume(0.3)
    
    def mort(self, screen, raison):
        pygame.mixer.music.stop()
        font = pygame.font.SysFont('Helvetica', 40, bold=True)
        screen.fill((0,0,0))
        background = pygame.image.load("assets/death.jpg").convert()
        screen.blit(background,(0,0))
        #afficher raison de mort
        button_text = font.render(raison, True, (255, 25, 25))
        text_rect = button_text.get_rect(center=(self.width/2, self.height/2+150))
        screen.blit(button_text,text_rect)
        pygame.display.flip()
        tmp = self.wait(500)
        if tmp == 1:
            return 1

    def wait(self, wait): #fonction qui sert a attendre sans bloquer la fenetre et qui permet de skipper (avec 's')
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
                        
    def choice(self, screen, line): #fonction pour generer des choix
        data_choice = line[7:-1]
        show_choice = tuple(data_choice.split('; '))
        nbchoix = int(show_choice[0])
        choix1 = show_choice[1]
        choix2 = show_choice[2]
        try:
            choix3 = show_choice[3]
        except:
            pass
        font = pygame.font.SysFont('Helvetica', 22, bold=True)
        choice = True
        i = 0
        while choice:
            pygame.display.flip()
            if i < 3:
                for tt in range(3):
                    pygame.draw.rect(screen, (100, 5, 5), (tt*self.width/3+10, self.height-110, self.width/3-20, 100))
                    if tt == 0:
                        TEXT=choix1
                    if tt == 1 and nbchoix == 3:
                        TEXT=choix2
                    if tt == 1 and nbchoix == 2:
                        TEXT=""
                    if tt == 2 and nbchoix == 3:
                        TEXT=choix3
                    if tt == 2 and nbchoix == 2:
                        TEXT=choix2
                    button_text = font.render(TEXT, True, (255, 255, 255))
                    screen.blit(button_text, (tt*self.width/3+20, self.height-100))
                    i+=1

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.quit:
                    return 0
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q or event.type == pygame.KEYDOWN and event.key == pygame.K_a or event.type == pygame.KEYDOWN and event.key == pygame.K_1 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_1 \
                    or event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 0*self.width/3+10 and pygame.mouse.get_pos()[0] < (0*self.width/3+10)+self.width/3-20 and pygame.mouse.get_pos()[1] > self.height-110 and pygame.mouse.get_pos()[1] < self.height-10:
                    pygame.draw.rect(screen, (255,255,255), (0*self.width/3+8, self.height-113, self.width/3-16, 106), 6)
                    choice = False
                    return 1
                if nbchoix == 2:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_b or event.type == pygame.KEYDOWN and event.key == pygame.K_2 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_2 \
                        or event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 2*self.width/3+10 and pygame.mouse.get_pos()[0] < (2*self.width/3+10)+self.width/3-20 and pygame.mouse.get_pos()[1] > self.height-110 and pygame.mouse.get_pos()[1] < self.height-10:
                        pygame.draw.rect(screen, (255,255,255), (2*self.width/3+8, self.height-113, self.width/3-16, 106), 6)
                        choice = False
                        return 2
                if nbchoix == 3:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_b or event.type == pygame.KEYDOWN and event.key == pygame.K_2 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_2 \
                        or event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 1*self.width/3+10 and pygame.mouse.get_pos()[0] < (1*self.width/3+10)+self.width/3-20 and pygame.mouse.get_pos()[1] > self.height-110 and pygame.mouse.get_pos()[1] < self.height-10:
                        pygame.draw.rect(screen, (255,255,255), (1*self.width/3+8, self.height-113, self.width/3-16, 106), 6)
                        choice = False
                        return 2
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_c or event.type == pygame.KEYDOWN and event.key == pygame.K_3 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_3 \
                        or event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 2*self.width/3+10 and pygame.mouse.get_pos()[0] < (2*self.width/3+10)+self.width/3-20 and pygame.mouse.get_pos()[1] > self.height-110 and pygame.mouse.get_pos()[1] < self.height-10:
                        pygame.draw.rect(screen, (255,255,255), (2*self.width/3+8, self.height-113, self.width/3-16, 106), 6)
                        choice = False
                        return 3


    def play(self, screen, level, dialog, name):
        level = int(level)
        dialog = int(dialog)
        name = str(name)
        nvx = []
        skip = 0
        towait = "None"
        init = 0
        initdial = 0
        #recherche des fichiers du niveau
        if name == "Zach":
            if level == 0:
                file = "nvx/tuto.txt"
            elif level == 1:
                file = "nvx/nvx1.txt"
            elif level == 2:
                file = "nvx/nvx2.txt"
            elif level == 3:
                file = "nvx/nvx3.txt"
            elif level == 4:
                file = "nvx/nvx4.txt"
        elif name == "Angela":
            if level == 0:
                file = "nvx/tuto.txt"
            elif level == 1:
                file = "nvx/nvx1A.txt"
            elif level == 2:
                file = "nvx/nvx2A.txt"
            elif level == 3:
                file = "nvx/nvx3A.txt"
            elif level == 4:
                file = "nvx/nvx4A.txt"
        elif name == "UtopiaJr":
            if level == 0:
                file = "nvx/tuto.txt"
            elif level == 1:
                file = "nvx/nvxU.txt"
            elif level == 2:
                file = "nvx/nvxUU.txt"
            elif level == 3:
                file = "nvx/nvxUUU.txt"
            elif level == 4:
                file = "nvx/nvxX.txt"
        else:
            file = "nvx/tuto.txt"
            
        #ouverture du fichier
        try:
            f = open(str(file), 'r', encoding='utf-8')
        except FileNotFoundError:
            raise FileNotFoundError(file,"Le fichier n'a pas été trouvé ",file,"File Not Found")
        line = f.readline().rstrip('\n')
        sound = None
        while line:
            if int(dialog) != 0 and init != 0 and initdial == 0:
                towait = "markr ("+str(dialog)+")"
                initdial = 1

            if not str(towait) == "None":
                while line!=str(towait):
                    line = f.readline().rstrip('\n')
                else:
                    towait = "None"

            else:
                #fin du niveau
                if line[0:5] == "end--":
                    try:
                        sound.stop()
                    except:
                        pass
                    return level, dialog, name
                
                #niveau suivant
                elif line[0:5] == "end++":
                    try:
                        sound.stop()
                    except:
                        pass
                    return level+1, 0, name
                
                #recuperer choix du perso dans le tuto
                elif file == "nvx/tuto.txt" and line[0:6] == "output":
                    name = line[8:-1]

                #dialogue suivant
                elif line[0:5] == "markr":
                    dialog = line[7:-1]
                    initdial = 1
                
                #saut dans le fichier
                elif line[0:6] == "towait":
                    towait = str(line[8:-1])

                #appel de l'initialisation
                elif line[0:5] == "init-":
                    varinit = tuple(str(line[7:-1]).split('; '))
                    # 0, 1 et 2 sont des tuples
                    self.initialisation(screen, varinit[0], varinit[1], varinit[2], varinit[3], varinit[4], varinit[5], varinit[6], name)
                    init+=1

                #afficher des images
                elif line[0:5] == "img--":
                    data_img = tuple(str(line[7:-1]).split('; '))
                    img = pygame.image.load(data_img[0])
                    pos = data_img[1].split(',')
                    scale = data_img[2].split(',')
                    imgprint = pygame.transform.scale(img,(int(scale[0]),int(scale[1])))
                    screen.blit(imgprint,(int(pos[0]),int(pos[1])))

                #jouer un son
                elif line[0:5] == "sound":
                    sound = pygame.mixer.Sound(line[7:-1])
                    sound.set_volume(0.5)
                    sound.play()

                #mettre un titre
                elif line[0:5] == "title":
                    title = line[7:-1]
                    pygame.display.set_caption(title)

                #attendre un certain moment (wait est en 10eme de secondes)
                elif line[0:5] == "temps":
                    timetowait = line[7:-1]
                    tmp = self.wait(timetowait)
                    if tmp == 1:
                        return level, dialog, name
                
                #mort
                elif line[0:5] == "mort-":
                    raison = line[7:-1]
                    tmp = self.mort(screen, raison)
                    return level, 0, name
                
                #vidéo
                # elif line[0:5] == "video":
                #    try:
                #        sound.stop()
                #    except:
                #        pass
                #    video = str(line[7:-1])
                #    clip = VideoFileClip(video).resize((1080,720))
                #    clip.preview(fps=30)

                elif line[0:5] == "dialg":
                    self.initialisation(screen, varinit[0], varinit[1], varinit[2], varinit[3], varinit[4], varinit[5], False, name)
                    font = pygame.font.SysFont('Helvetica', 40, bold=True)
                    scen = 1
                    y = 21
                    nb = 0
                    number = 0
                    remaindialog = True
                    texte_remain = "None"
                    data_text = line[7:-1]
                    dialog_data = list(data_text.split('; '))
                    while remaindialog:
                        if texte_remain != "None":
                            texte = texte_remain
                            texte_remain = "None"
                        elif number+1 <= int(dialog_data[0]):
                            texte = f.readline().rstrip('\n')
                            number+=1
                        else:
                            remaindialog = False
                            break
                        fnd = pygame.Surface((self.width-40, 48))
                        fnd.set_alpha(200)  
                        fnd.fill((100, 5, 5))
                        screen.blit(fnd, (20, y)) 
                        r = ""
                        x = 0
                        x2 = 0
                        skip_dial = False
                        textesave = texte
                        text_width = 0
                        # systeme pour passer a la ligne le texte quand il est trop long
                        if font.render(str(texte), True, (255,255,255)).get_width() > self.width-60:
                            while font.render(str(texte), True, (255,255,255)).get_width() > self.width-60:
                                texte = texte[:-1]
                            while texte[len(texte)-1] != " ": #voir ou est l'espace précédent pour eviter de couper des mots
                                texte = texte[:-1]
                            texte_remain = textesave[len(texte):]
                        for l in texte: #morceau de code pour afficher les lettres une par une
                            text = font.render(str(l), True, (255, 255, 255)) 
                            x+=text.get_width()
                            screen.blit(text, (x2+30,y))
                            x2 = x
                            if skip_dial == False:
                                tmp = self.wait(4)
                            if tmp == 1:
                                return level, dialog, name
                            elif tmp == 0:
                                skip_dial = True
                            pygame.display.flip()
                        # for l in texte:
                        #     r = r + l
                        #     text = font.render(str(r), True, (255, 255, 255))
                        #     #text_width = text.get_width()
                        #     screen.blit(text, (30,y))
                        #     tmp = self.wait(4)
                        #     if tmp == 1:
                        #         return level, dialog, name
                        #     elif tmp == 0:
                        #         text = font.render(str(texte), True, (255, 255, 255))
                        #         screen.blit(text, (30,y))
                        #         pygame.display.flip()
                        #         break
                        #     pygame.display.flip()
                        y += 48
                        pygame.display.flip()
                        tmp = self.wait(dialog_data[1])
                        if tmp == 1:
                            return level, dialog, name
                    fnd = pygame.Surface((20, 20))
                    fnd.set_alpha(255)  
                    fnd.fill((255,255,255))
                    screen.blit(fnd, (self.width-20, 0))
                    pygame.display.flip()
                    while nb == 0:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN: #and event.key == pygame.K_s
                                nb = 1
                                if dialog_data[-1] == "True":
                                    self.initialisation(screen, varinit[0], varinit[1], varinit[2], varinit[3], varinit[4], varinit[5], False, name)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                                return level, dialog, name

                #generation des choix
                elif line[0:5] == "choix":
                    rslt = self.choice(screen, line)
                    if rslt == 0:
                        return level, dialog, name
                    ln = line[7:-1]
                    tpl = tuple(ln.split('; '))
                    towait = str(tpl[int(tpl[0])+rslt])

            pygame.display.flip()
            tmp = self.wait(10)
            if tmp == 1:
                return level, dialog, name
            if towait == "None":
                line = f.readline().rstrip('\n')
