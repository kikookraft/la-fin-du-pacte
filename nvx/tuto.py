import pygame
import nvx.levelmanager as lvm

class Tuto:
    def tuto(self, screen):
        lvm.level().initialisation(screen, "None", "None", "None", "None", "choix-perso.jpg", "02.  Musique libre de droits  La Grande Table - Delnica-1.wav", True)
        lvm.story().dialogue(["Bienvenue à toi inconnu !","Comment t'appelle-tu ?"], make_init=False)
        lvm.story().choice(screen, 2, ["Zach","Un homme tout a fait normal"], ["Angela", "Une femme avec un certain objectif..."])

        pygame.time.wait(10000)

        pygame.mixer.stop()
        background = pygame.image.load('nvx/tuto/choix-perso.jpg').convert()
        screen.blit(background, (0,0))
        pygame.display.flip()
        font = pygame.font.SysFont('Helvetica', 22, bold=True)

        
        
        pygame.time.wait(3500)
        with open("data/start.txt", "w") as fichier:
	        fichier.write("Tu vien de demarrer ta premiere partie !\nNe suprimme pas ce fichier, il est important!")
        return 1, 0, Name, 0

