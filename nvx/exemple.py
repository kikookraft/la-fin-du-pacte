import pygame
import nvx.levelmanager as lvm

class dawa:
    dialog = 0
    next_level = -1

    def game(self, screen, name):
        #changer le titre de la fenetre
        lvm.level().title("HAAAAAAAA ISSSOU")
        #initialisation
        lvm.level().initialisation(screen, ["perso"], [(650,220)], [(300,500)], "None", "Bidonville.jpg", "02.  Musique libre de droits  La Grande Table - Delnica-1.wav", True, name)
        #dialogue
        result = lvm.story().dialogue(["Bienvenu(e) dans le niveau d'exemple !", "Que veut-tu faire ?"], make_init=False)
        if result == "exit": return self.next_level, self.dialog, name, False
        elif result == "quit": return self.next_level, self.dialog, name, True

        #choix
        result = lvm.story().choice(screen, 3, ["Changer de fond"], ["Faire un exemple de dialogue"], ["Faire le zbeub", "(tkt ca va bien se passer)"])
        if result == "exit": return self.next_level, self.dialog, name, False
        elif result == "quit": return self.next_level, self.dialog, name, True

        #initialisation
        elif result == 1: lvm.level().initialisation(screen, ["perso"], [(650,220)], [(300,500)], "None", "bg.jpg", "lava.wav", True, name)
        elif result == 2: 
            #dialogue
            result = lvm.story().dialogue(["Bon... ok!","Par contre je ne sait pas quoi dire..."])
            if result == "exit": return self.next_level, self.dialog, name, False
            elif result == "quit": return self.next_level, self.dialog, name, True
            #bref... que des dialogues...
            result = lvm.story().dialogue(["Ha si, je vais te raconter une annecdote:","Le personnage Utopia JR à été créé à partir d'une image de Donald Trump !!"])
            if result == "exit": return self.next_level, self.dialog, name, False #     Si le texte est trop long, il est coupé automatiquement et la suite passe a la ligne
            elif result == "quit": return self.next_level, self.dialog, name, True
            result = lvm.story().dialogue(["De base le jeux était uniquement destiné à Linux !","Maintenant il est aussi disponible sur windows et android"])
            if result == "exit": return self.next_level, self.dialog, name, False
            elif result == "quit": return self.next_level, self.dialog, name, True
            result = lvm.story().dialogue(["Bref, je pense que tu as vu comme les dialogues","fonctionnent bien"])
            if result == "exit": return self.next_level, self.dialog, name, False
            elif result == "quit": return self.next_level, self.dialog, name, True
        elif result == 3: 
            nbelement = 0
            while nbelement < 7:
                pygame.display.flip()
                nbelement+=1
                result = lvm.level().wait(200)
                if result == "exit": return self.next_level, self.dialog, name, False
                elif result == "quit": return self.next_level, self.dialog, name, True
                if nbelement == 1: lvm.media().image("assets/knife.png", (200,200), (100,100))
                if nbelement == 2: lvm.media().sound("assets/sounds/explosion.wav", 1)
                if nbelement == 3: lvm.media().sound("assets/sounds/feu.wav")
                if nbelement == 4: lvm.media().image("assets/masse.png", (100,300), (50,50))
                if nbelement == 5: lvm.media().image("assets/kevin.png", (150,220), (300,500))
                if nbelement == 6: lvm.media().sound("assets/sounds/gunshot.wav", 1)
            lvm.media().sound("assets/sounds/gunshot.wav", 1)
            lvm.media().sound("assets/sounds/gunshot.wav", 1)
            lvm.level().death(screen, "Finalement ca s'est mal passé...")
            lvm.media().sound("assets/sounds/gunshot.wav", 1)
            result = lvm.level().wait(100)
            if result == "exit": return self.next_level, self.dialog, name, False
            elif result == "quit": return self.next_level, self.dialog, name, True
            pygame.mixer.stop()
            return -1, self.dialog, name, False
        
        #dialogue
        result = lvm.story().dialogue(["C'est donc la fin de ce niveau,","Tu as de la chance d'avoir survécu ;)"])
        if result == "exit": return self.next_level, self.dialog, name, False
        elif result == "quit": return self.next_level, self.dialog, name, True


        pygame.mixer.stop()
        return self.next_level, self.dialog, name, False

