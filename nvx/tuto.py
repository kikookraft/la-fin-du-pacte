import pygame
import nvx.levelmanager as lvm

class Tuto:
    name = None
    dialog = 0

    def game(self, screen):
        lvm.level().initialisation(screen, background="choix-perso.jpg", music="02.  Musique libre de droits  La Grande Table - Delnica-1.wav", restart_music=True)
        result = lvm.story().dialogue(["Inconnue - Ho tiens, salut !","Comment tu t'appelle ?"], make_init=False)
        if result == "exit": return 0, self.dialog, self.name, False
        elif result == "quit": return 0, self.dialog, self.name, True

        result = lvm.story().choice(screen, 3, ["Zach","Un homme tout a fait normal"], ["Angela","Une femme avec un certain","objectif..."], ["Vérouillé !", "Termine le jeu avec un", "personnage pour débloquer."])
        if result == "exit": return 0, self.dialog, self.name, False
        elif result == "quit": return 0, self.dialog, self.name, True

        elif result == 1: self.name = "Zach"
        elif result == 2: self.name = "Angela"
        elif result == 3:
            result = lvm.story().dialogue(["Tu dois terminer l'histoire au moin une fois pour debloquer ce personnage !", "Revien une fois que cela est fait !!"])
            if result == "exit": return 0, self.dialog, self.name, False
            elif result == "quit": return 0, self.dialog, self.name, True
            return 0, 0, "None", False
        
        lvm.level().initialisation(screen, ["perso"], [(650,220)], [(300,500)], ["None"], "Bidonville.jpg", "None", False, self.name)
        
        lvm.story().dialogue(["Inconnue - Ok, dépeche-toi de te préparer {}".format(self.name),"les policiers vont arriver !"],0)
        if result == "exit": return 0, self.dialog, self.name, False
        elif result == "quit": return 0, self.dialog, self.name, True

        pygame.mixer.stop()
        return 1, 0, self.name, False

