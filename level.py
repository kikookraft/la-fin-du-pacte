#importation des niveaux sous la forme : dossier.nom_du_niveau
import pygame
import os
from moviepy.editor import *
from score import Score
import sys
class Lvl:
 
    screen = pygame.display.set_mode((1080, 720))

    # def __init__(self):
    #     #comme pour le fichier game mais pour les niveaux
    #     #self.test = Test()
    #     print("Chargé !")


    def initialisation(self, screen, imgperso=("perso1.png"), posperso=((0,0)), scaleperso=((500,500)), weapon=("None"), background="None.jpg", music="None.wav", statemusic=False):
        '''Permet d'initialiser l'écran!\n
        `screen` = ecran,\n 
        `imgperso` = images de chaque personnages,\n 
        `posperso` = position de chaque personnages,\n 
        `scaleperso` = taille des personnages,\n 
        `weapon` = non fonctionnel pour l'instant,\n 
        `background` = image de fond,\n 
        `music` = musique a mettre,\n 
        `statemusic` = activer ou pas la musique'''
        #mise en forme des variable (les mettre dans les bon format)
        imgperso = imgperso.split(',')
        posperso = posperso.split('/')
        scaleperso = scaleperso.split('/')
        #image de fond
        background1 = str("assets/bg/"+background)
        bgd = pygame.image.load(background1)
        bgd = pygame.transform.scale(bgd,(1080,720))
        screen.blit(bgd, bgd.get_rect())
        #personnage
        for perso in imgperso:
            #print(perso,scaleperso[imgperso.index(perso)].split(","),posperso[imgperso.index(perso)].split(","))
            boy = pygame.image.load(str("assets/"+str(perso)))
            scalepersotmp = scaleperso[imgperso.index(perso)].split(",")
            pospersotmp = posperso[imgperso.index(perso)].split(",")
            boyr = pygame.transform.scale(boy,(int(scalepersotmp[0]),int(scalepersotmp[1])))
            screen.blit(boyr,(int(pospersotmp[0]),int(pospersotmp[1])))

        #musique
        if statemusic:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("assets/sounds/%s" %(music))
            pygame.mixer.music.play(loops=-1) 
            pygame.mixer.music.set_volume(0.5)
    
    def mort(self, screen, raison):
        pygame.mixer.music.stop()
        font = pygame.font.SysFont('Helvetica', 40, bold=True)
        screen.fill((0,0,0))
        background = pygame.image.load("assets/death.jpg").convert()
        screen.blit(background,(0,0))
        button_text = font.render(raison, True, (255, 25, 25))
        text_rect = button_text.get_rect(center=(540, 360+150))
        screen.blit(button_text,text_rect)
        pygame.display.flip()
        tmp = self.wait(500)
        if tmp == 1:
            return 1

    def wait(self, wait):
        for i in range(int(wait)):
            pygame.time.wait(10)
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return 1
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :
                        return 1
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_s :
                        return 0
            except:
                pass
    
    def choice(self, screen, line):
        data_choice = line[7:-1]
        show_choice = tuple(data_choice.split(', '))
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
                    pygame.draw.rect(screen, (100, 5, 5), (tt*1080/3+10, 610, 340, 100))
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
                    screen.blit(button_text, (tt*1080/3+20, 620))
                    i+=1

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :
                    return 0
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q or event.type == pygame.KEYDOWN and event.key == pygame.K_a or event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    pygame.draw.rect(screen, (255,255,255), (8, 608, 344, 104), 6)
                    pygame.draw.rect(screen, (0,0,0), (7, 607, 345, 105), 2)
                    choice = False
                    return 1
                if nbchoix == 2:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_b or event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                        pygame.draw.rect(screen, (255,255,255), (728, 608, 344, 104), 6)
                        pygame.draw.rect(screen, (0,0,0), (727, 607, 345, 105), 2)
                        choice = False
                        return 2
                if nbchoix == 3:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_b or event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                        pygame.draw.rect(screen, (255,255,255), (368, 608, 344, 104), 6)
                        pygame.draw.rect(screen, (0,0,0), (367, 607, 345, 105), 2)
                        choice = False
                        return 2
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_c or event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                        pygame.draw.rect(screen, (255,255,255), (728, 608, 344, 104), 6)
                        pygame.draw.rect(screen, (0,0,0), (727, 607, 345, 105), 2)
                        choice = False
                        return 3


    def play(self, screen, level, dialog, name):

        nvx = []
        skip = 0
        towait = "None"
        init = 0
        initdial = 0
        #recherche des fichiers du niveau
        if name == "Zach":
            if level == 1:
                file = "nvx/nvx1.txt"
            elif level == 2:
                file = "nvx/nvx2.txt"
            elif level == 3:
                file = "nvx/nvx3.txt"
            elif level == 4:
                file = "nvx/nvx4.txt"
        elif name == "Angela":
            if level == 1:
                file = "nvx/nvx1A.txt"
            elif level == 2:
                file = "nvx/nvx2A.txt"
            elif level == 3:
                file = "nvx/nvx3A.txt"
            elif level == 4:
                file = "nvx/nvx4A.txt"
        elif name == "UtopiaJr":
            if level == 1:
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
        f = open(str(file), 'r', encoding='utf-8')
        line = f.readline().rstrip('\n')
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
                    return level+1, dialog, name
                
                #dialogue suivant
                elif line[0:5] == "markr":
                    dialog = line[7:-1]
                    initdial = 1

                #appel de l'initialisation
                elif line[0:5] == "init-":
                    varinit = tuple(str(line[7:-1]).split('; '))
                    # 0, 1 et 2 sont des tuples
                    self.initialisation(screen, varinit[0], varinit[1], varinit[2], varinit[3], varinit[4], varinit[5], varinit[6])
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
                elif line[0:5] == "video":
                    video = str(line[7:-1])
                    clip = VideoFileClip(video)
                    clip.preview(fps=30)
                    
                #generation des dialogues
                elif line[0:5] == "dialg":
                    self.initialisation(screen, varinit[0], varinit[1], varinit[2], varinit[3], varinit[4], varinit[5], False)
                    font = pygame.font.SysFont('Helvetica', 40, bold=True)
                    scen = 1
                    y = 21
                    nb = 0
                    data_text = line[7:-1]
                    showed_text = tuple(data_text.split(', '))
                    for number in range(int(showed_text[0])):
                        fnd = pygame.Surface((1040, 48))
                        fnd.set_alpha(200)  
                        fnd.fill((100, 5, 5))
                        screen.blit(fnd, (20, y))
                        texte = f.readline().rstrip('\n')
                        r = ""
                        text_width = 0
                        for l in texte:
                            r = r + l
                            text = font.render(str(r), True, (255, 255, 255))
                            text_width = text.get_width()
                            screen.blit(text, (30,y))
                            tmp = self.wait(5)
                            if tmp == 1:
                                return level, dialog, name
                            elif tmp == 0:
                                text = font.render(str(texte), True, (255, 255, 255))
                                screen.blit(text, (30,y))
                                pygame.display.flip()
                                break
                            pygame.display.flip()
                        y += 48
                        pygame.display.flip()
                        tmp = self.wait(showed_text[1])
                        if tmp == 1:
                            return level, dialog, name
                    fnd = pygame.Surface((20, 20))
                    fnd.set_alpha(255)  
                    fnd.fill((255,255,255))
                    screen.blit(fnd, (1060, 0))
                    pygame.display.flip()
                    while nb == 0:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or event.type == pygame.KEYDOWN : #and event.key == pygame.K_s
                                nb = 1
                                if showed_text[-1] == "True":
                                    self.initialisation(screen, varinit[0], varinit[1], varinit[2], varinit[3], varinit[4], varinit[5], False)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :
                                return level, dialog, name

                #generation des choix
                elif line[0:5] == "choix":
                    rslt = self.choice(screen, line)
                    if rslt == 0:
                        return level, dialog, name
                    ln = line[7:-1]
                    tpl = tuple(ln.split(', '))
                    towait = str(tpl[int(tpl[0])+rslt])

            pygame.display.flip()
            tmp = self.wait(10)
            if tmp == 1:
                return level, dialog, name
            if towait == "None":
                line = f.readline().rstrip('\n')

                   
            




        # self.test.initialisation(screen, 1, name)
        # nvx = self.test.play(screen, level, dialog, name)

        # if level == 0 or name == 'None':
        #     try:
        #         with open("data/start.txt"):
        #             try:
        #                 with open("data/end.txt"):
        #                     nvx = self.tuto.choiceunlocked()
        #             except IOError:
        #                 nvx = self.tuto.choicelocked()
        #     except IOError:
        #         self.tuto.initialisation(screen ,1)
        #         nvx = self.tuto.tuto(screen)

        # elif level == 1:
        #     if name == "Zach":
        #         self.nvx1.initialisation(screen, 1, name)
        #         nvx = self.nvx1.play(screen, level, dialog, name)
        #     elif name == "Angela":
        #         self.nvx1A.initialisation(screen, 1, name)
        #         nvx = self.nvx1A.play(screen, level, dialog, name)
        #     elif name == "UtopiaJr":
        #         self.nvxU.initialisation('nvx/nvxU/init.txt', 1, name, 1)
        #         nvx = self.nvxU.play(screen, level, dialog, name)

        # elif level == 2:
        #     if name == "Zach":
        #         self.nvx2.initialisation3(screen, 1, name)
        #         nvx = self.nvx2.play(screen, level, dialog, name)
        #     elif name == "Angela":
        #         try:
        #             with open("nvx/nvx1A/player.txt"):
        #                 self.nvx2A2.initialisation('nvx/nvx2A2/init.txt', 1, name, 1)
        #                 nvx = self.nvx2A2.play(screen, level, dialog, name)
        #         except IOError:
        #             self.nvx2A1.initialisation('nvx/nvx2A1/init.txt', 1, name, 1)
        #             nvx = self.nvx2A1.play(screen, level, dialog, name)
        #     elif name == "UtopiaJr":
        #         self.nvxUU.initialisation('nvx/nvxUU/init.txt', 1, name, 1)
        #         nvx = self.nvxUU.play(screen, level, dialog, name)

        # elif level == 3: #le nvx3 a une structure différente
        #     if name == "Zach":
        #         self.nvx3.initialisation("nvx/nvx3/init.txt", 1, name)
        #         nvx = self.nvx3.play(screen, level, dialog, name)
        #     elif name == "Angela":
        #         self.nvx3A.initialisation("nvx/nvx3A/init.txt", 1, name)
        #         nvx = self.nvx3A.play(screen, level, dialog, name)
        #     elif name == "UtopiaJr":
        #         self.nvxUUU.initialisation('nvx/nvxUUU/init.txt', 1, name, 1)
        #         nvx = self.nvxUUU.play(screen, level, dialog, name)

        # elif level == 4:
        #     if name == "Zach":
        #         self.nvx4.initialisation("nvx/nvx4/init.txt", 1, name)
        #         nvx == self.nvx4.play(screen, level, dialog, name)
        #     elif name == "Angela":
        #         self.nvx4A.initialisation("nvx/nvx4A/init.txt", 1, name)
        #         nvx == self.nvx4A.play(screen, level, dialog, name)

        # elif level == 41:
        #     self.nvx41.initialisation("nvx/nvx41/init.txt", 1, name)
        #     nvx = self.nvx41.play(screen, level, dialog, name)

        # elif level == 5:
        #     self.nvx4A.initialisation("nvx/nvx4A/init.txt", 1, name)
        #     nvx = self.nvx4A.play(screen, level, dialog, name)

        # elif level == 666:
        #     self.nvxX.initialisation("nvx/nvxX/init.txt", 1, name)
        #     nvx = self.nvxX.play(screen, level, dialog, name)

        # elif level == 441:
        #     self.nvx4AR.initialisation("nvx/nvx4AR/init.txt", 1, name)
        #     nvx = self.nvx4AR.play(screen, level, dialog, name)



        # if nvx[0] == 100:
        #     print("Tu as débloqué le troisieme personnage !")
        #     with open("data/end.txt", 'a') as ed:
        #         ed.write("\nTu as terminé une histoire !")
        #     pygame.time.wait(1500)
        #     return 0, 0, "None", 1, 0
        # if nvx[0] == 99999:
        #     print("Tu as terminé le jeux !")
        #     clip = VideoFileClip("assets/movies/credit.mp4")
        #     clip.preview(fps=30)
        #     return 0, 0, "None", 1, 0
        # return nvx[0], nvx[1], nvx[2], nvx[3], nvx[4]

