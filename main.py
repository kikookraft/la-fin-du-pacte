# -*- coding : utf8 -*-
import pygame
from game import Game
import os
pygame.init()
level = 0
dialog = 0
name = "None"
clock=pygame.time.Clock()
 
#charger le jeux et les scores
game = Game()
scre = game.score().load()
level = scre[0]
dialog = scre[1]
name = scre[2]

credit = 0
FPS = 100

#fenetre
pygame.display.set_caption("La fin du pacte - Menu")
screen = pygame.display.set_mode((1080, 720))
info = pygame.display.Info()
width = info.current_w
height = info.current_h
if width == 1080 and height == 720:
    modified = False
    speed = 1
else:
    modified = True
    speed = 3
width_box = 320
height_box = 75
nbbtn = 3
font = pygame.font.SysFont('Helvetica', 60, bold=True)
font2 = pygame.font.SysFont('Helvetica', 50, bold=True)
TEXT=""
COLOR = (100, 5, 5)
mnumove = -800
mnumove2 = 1300
stmn = 1
pygame.key.set_repeat(5000,1000)
 
#fond d'ecran + images
background = pygame.image.load('assets/menu-bg.jpg').convert()
screen.blit(background, (0,0))
logo = pygame.image.load('assets/logo.png').convert_alpha()
 
#Activer la boucle du jeux (pour que le jeux ne dure pas 1 miliseconde)
ypos= 0
men = True
HT = True
ingame = 0

play = 0
cooldown = 0
fade = 255
alpha_fadein = 255
#initialisation des musiquespygame.mixer.music.load('assets/sounds/City Space - kikookraft.mp3')
pygame.mixer.music.load("assets/sounds/City Space - kikookraft.wav")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops=50, start=0.0)
 
#logo du jeux
dimension_fondx2 = logo.get_width()
dimension_fondy2 = logo.get_height()
xmin2 = (info.current_w - dimension_fondx2) / 2
ymin2 = (info.current_h - dimension_fondy2) / 2
xmax2 = info.current_w - xmin2
ymax2 = info.current_h - ymin2
position_fond2 = (xmin2, ymin2)
ypos2 = ymin2
logovar = 1
 
#image de fond
dimension_fondx = background.get_width()
dimension_fondy = background.get_height()
xmin = (info.current_w - dimension_fondx) / 2
ymin = (info.current_h - dimension_fondy) / 2
xmax = info.current_w - xmin
ymax = info.current_h - ymin
position_fond = (xmin, ymin)


def fadein(alpha_fadein):
    if alpha_fadein >= 1:
        alpha_fadein -= 1*speed
        fnd = pygame.Surface((width, height))
        fnd.set_alpha(alpha_fadein)  
        fnd.fill((0,0,0))
        screen.blit(fnd, (0, 0))
        return alpha_fadein
    else:
        return True

#pour l'ecran ractile
touched = False
#----------------------------------------------------------------------------------------------
#BOUCLE DU JEUX

while men:
 
    #appliquer l'arriere plan
    if ingame == 0:
        screen.blit(background, (xmin, ypos))#bg
        screen.blit(logo, (xmin2, ypos2))#logo
 
    #faire bouger le titre au debut
    if logovar == 1:
        ypos2 = ypos2 - 3*speed
        if ypos2 < 40:
            logovar = 0 
 
    #faire bouger le fond
    if ingame == 0:
        if not ypos > 0 and HT == True :
            ypos = ypos + speed
        if ypos > 0 :
            HT = False
        if not ypos < -1640 and HT==False:
            ypos = ypos - speed
        if ypos < -width-200 :
            HT = True
 
    #quitter la fenetre et detection de touches
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            men = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :
            men = False
            game.score().save(level, dialog, name , 1)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r :
            game.new().new()
            level = 0
            dialog = 0
            name = 'None'
            game.score().save(level, dialog, name , 1)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            touched = True
            zone = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            touched = False
 
    #if ingame == 0:
    #detection bouton
    if pygame.mouse.get_pos()[0] > mnumove + width/2 - width_box/2 and pygame.mouse.get_pos()[0] < mnumove + width/2 + width_box/2 and pygame.mouse.get_pos()[1] > height/2 - 75 + 150 * 0 and pygame.mouse.get_pos()[1] < height/2 - 75 + 150 * 0 + height_box and touched == True:
        if cooldown == 0:
            play = 1
            cooldown = 2
            touched = False

    if pygame.mouse.get_pos()[0] > mnumove + width/2 - width_box/2 and pygame.mouse.get_pos()[0] < mnumove + width/2 + width_box/2 and pygame.mouse.get_pos()[1] > height/2 - 75 + 150 * 1 and pygame.mouse.get_pos()[1] < height/2 - 75 + 150 * 1 + height_box and touched == True and credit == 0:
        game.score().save(level,dialog,name)
        credit = 1
        game.credit().start()
        touched = False


    if pygame.mouse.get_pos()[0] > mnumove + width/2 - width_box/2 and pygame.mouse.get_pos()[0] < mnumove + width/2 + width_box/2 and pygame.mouse.get_pos()[1] > height/2 - 75 + 150 * 2 and pygame.mouse.get_pos()[1] < height/2 - 75 + 150 * 2 + height_box and touched == True:
        game.score().save(level, dialog, name)
        pygame.quit()
        quit()

 
    if not cooldown == 0:
        cooldown -= 1

    if play == 1:
        play = 0
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        pygame.display.set_caption("La fin du pacte - JEUX")
        ingame = 1
        game.clear(screen)
        pygame.mixer.music.stop()
        fin = game.lvl().play(screen, level, dialog, name)
        if fin != None:
            level = fin[0]
            dialog = fin[1]
            name = fin[2]
        else:
            level = 0
            dialog = 0
            name = 0
        game.score().save(level,dialog,name)
        pygame.event.clear()
        game.clear(screen)
        pygame.display.set_caption("La fin du pacte")
        ingame = 0
        pygame.mixer.music.load("assets/sounds/City Space - kikookraft.wav")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(loops=50, start=0.0) 
        touched = False

    if ingame == 0:
        #menu
        #afficher les boutons
        if logovar == 0:
            for box in range(nbbtn):
                widthb = width/2 - width_box/2
                heightb = height/2 - 25 * nbbtn + 150 * box
                #pygame.draw.rect(screen, COLOR, (mnumove + widthb, heightb, width_box, height_box), 0)
               
                buttn = pygame.Surface((width_box,height_box))
                buttn.set_alpha(200)  
                if credit == 1 and box == 1:
                    COLOR=(35,0,0)
                else:
                    COLOR=(100,5,5)
                buttn.fill(COLOR)        
                screen.blit(buttn, (mnumove + widthb, heightb))
               
               
                if box == 0:
                    TEXT="JOUER"
                elif box == 1:
                    TEXT="CREDITS"
                elif box == 2:
                    TEXT="QUITTER"
                if credit == 1 and box == 1:
                    button_text = font.render(TEXT, True, (100, 5, 5))
                else:
                    button_text = font.render(TEXT, True, (255, 255, 255))
                screen.blit(button_text, (mnumove + widthb + 30, heightb+5))
 
                clicGauche, *_ = pygame.mouse.get_pressed()
                posPointeur = pygame.mouse.get_pos()
           
 
            if stmn == 1:
                mnumove = mnumove + 5*speed
                if mnumove >= 0:
                    stmn = 0

    if credit == 1 and fade != True:
        fade = fadein(fade)

    # mise a jour de l'ecran
    clock.tick(FPS)
    pygame.display.flip()


