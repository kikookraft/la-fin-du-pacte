import pygame
import nvx.levelmanager as lvm

class Tuto:
    name = None
    dialog = 0

    def game(self, screen):
        lvm.level().initialisation(screen, ["perso"], [(650,220)], [(300,500)], "None", "Bidonville.jpg", "02.  Musique libre de droits  La Grande Table - Delnica-1.wav", True, self.name)
        result = lvm.story().dialogue(["Vous voyez un policier qui arrive vers vous.","Le policier a l'air très préssé..."])
        if result == "exit": return 0, self.dialog, self.name, False
        elif result == "quit": return 0, self.dialog, self.name, True

        result = lvm.story().choice(screen, 3, ["Zach","Un homme tout a fait normal"], ["Angela","Une femme avec un certain","objectif..."], ["Vérouillé !", "Termine le jeu avec un", "personnage pour débloquer."])
        if result == "exit": return 0, self.dialog, self.name, False
        elif result == "quit": return 0, self.dialog, self.name, True

        
        lvm.level().initialisation(screen, ["perso"], [(650,220)], [(300,500)], "None", "Bidonville.jpg", "None", False, self.name)
        
        lvm.story().dialogue(["Inconnue - Ok, dépeche-toi de te préparer {}".format(self.name),"les policiers vont arriver !"],0)
        if result == "exit": return 0, self.dialog, self.name, False
        elif result == "quit": return 0, self.dialog, self.name, True

        pygame.mixer.stop()
        # background = pygame.image.load('nvx/tuto/choix-perso.jpg').convert()
        # screen.blit(background, (0,0))
        # pygame.display.flip()
        # font = pygame.font.SysFont('Helvetica', 22, bold=True)

        
        with open("data/start.txt", "w") as fichier:
	        fichier.write("Tu vien de demarrer ta premiere partie !\nNe suprimme pas ce fichier, il est important!")
        return 1, self.dialog, self.name, False

