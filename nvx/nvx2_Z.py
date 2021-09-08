import pygame
import nvx.levelmanager as lvm
import json

class Level2_Z:
    dialog = 0
    level = 2
    next_level = 3

    def game(self, screen, dialog, name):
        try: weapon = lvm.media().save_file().read("nvx2_Z/weapon.json")
        except FileNotFoundError: weapon = None
        weapon = weapon['weapon']
        self.dialog = dialog
        if self.dialog < 1: #Introduction
            lvm.level().initialisation(screen, ["None"], [(650,220)], [(300,500)], ["None"], "noir.jpg", "desert.mp3", True, name, 1)
            intro = [["Narateur: 1 semaine plus tard, après s’être entraîné a survivre, les condamnés sont prêts."],["Présentateur 1 : Bienvenue cher téléspectateur aux 10e death run aujourd’hui 10 combattant vont en découdre pour rejoindre l’élite !!","Présentateur 2 : Tout a fais mais n’oublions pas que c’est une épreuve très périlleuse et que les épreuve font en sorte qu’il n’y ai qu’un seul vainqueur."],["Présentateur 1 : Oui il n’y a pas de deuxième place mais cela rend les jeux plus drôle à regarder !!","Présentateur 2 : Tient on m’annonce que les participant vont arriver."],["OH les voila !"]]
            for dial in intro:
                result = lvm.story().dialogue(dial, make_init=True)
                if result == "exit": return self.level, self.dialog, name, False
                elif result == "quit": return self.level, self.dialog, name, True
            self.dialog = 1

        if self.dialog < 2:
            lvm.level().initialisation(screen, ["perso"], [(650,220)], [(300,500)], ["None"], "night-desert-original.jpg", "desert.mp3", False, name, 1)

            intro = [["Présentateur 1 : Haaaa cette année c’est dans un désert que va se produire la première épreuve.","Présentateur 2 : Et un petit rappel des règle s’impose pour les nouveaux qui ne connaissent pas cette épreuve."],["Présentateur 2 : Pour la première épreuve, l’épreuve de survie, les participants vont devoir survivre durant une nuit. Tout ceux qui auront survécu pourront accéder à la prochaine épreuve."],["Présentateur 1 : Mais nous n’allons pas les laisser sans défense ?"],["Présentateur 2 : Non, avant de commencer ils vont choisir entre entre une hache, des poings américains et une grande masse."]]
            for dial in intro:
                result = lvm.story().dialogue(dial)
                if result == "exit": return self.level, self.dialog, name, False
                elif result == "quit": return self.level, self.dialog, name, True
            self.dialog = 2

        if self.dialog < 3 or weapon == None:
            lvm.level().initialisation(screen, ["perso"], [(650,220)], [(300,500)], ["None"], "night-desert-original.jpg", "desert.mp3", False, name, 1)
            result = lvm.story().choice(screen, 3, ["Prendre la Hache"],["Prendre Les Poings","Américains"],["Prendre la masse"," "])
            if result == "exit": return self.level, self.dialog, name, False
            elif result == "quit": return self.level, self.dialog, name, True
            elif result == 1: 
                weapon = "hache"
                result = lvm.story().dialogue(["Une hache, excellent choix. Cette arme, ni trop lourde ni trop légère, vous permettra de survivre !","Du moins, si vous en faite bonne usage..."])
                if result == "exit": return self.level, self.dialog, name, False
                elif result == "quit": return self.level, self.dialog, name, True
            elif result == 2: 
                weapon = "poing_am"
                result = lvm.story().dialogue(["Très légère, cette arme vous permettra peut être pas de tuer en masse mais facilitera la fuite"])
                if result == "exit": return self.level, self.dialog, name, False
                elif result == "quit": return self.level, self.dialog, name, True
            elif result == 3: 
                weapon = "masse"
                result = lvm.story().dialogue(["Elle est lourde et tout le monde ne peut pas la porter","Cependant, les hordes d’ennemies ne pourront rien si vous arrivez à la manier !"])
                if result == "exit": return self.level, self.dialog, name, False
                elif result == "quit": return self.level, self.dialog, name, True
            lvm.media().save_file().create("nvx2_Z/weapon.json", {'weapon':weapon})
            self.dialog = 3
        
        if self.dialog < 4:
            lvm.level().initialisation(screen, ["perso"], [(650,220)], [(300,500)], ["None"], "night-desert-original.jpg", "desert.mp3", False, name, 1)
            intro = [["Les death run vont bientôt commencer","Présentateur 1 : L’arbitre va annoncer le compte très bientôt…"],["Arbitre : 10   9   8   7   6   5   4   3   2   1   0","Que les death run commencent !!!"],["Présentateur 2 : On vient de m’apprendre que des zombies étaient arrivé dans le centre de l’arène,","cette année les organisateurs n’y sont pas allé de main de morte !!"]]
            for dial in intro:
                result = lvm.story().dialogue(dial)
                if result == "exit": return self.level, self.dialog, name, False
                elif result == "quit": return self.level, self.dialog, name, True
            self.dialog = 4

        #choix importants
        if weapon == "hache": 
            if self.dialog < 5:
                lvm.level().initialisation(screen, ["perso"], [(650,220)], [(300,500)], ["hache.png"], "night-desert-zombie.jpg", "desert.mp3", True, name, 1)
                result = lvm.story().choice(screen, 2, ["Fuir les zombies"], ["Combattre"])
                if result == "exit": return self.level, self.dialog, name, False
                elif result == "quit": return self.level, self.dialog, name, True
                lvm.media().save_file().create("nvx2_Z/fuite.json", {'choice':result})
                self.dialog = 5
            else: 
                result = lvm.media().save_file().read("nvx2_Z/fuite.json")
                result = result['choice']

            if result == 1: #fuir les zombies
                if self.dialog < 6:    
                    lvm.level().initialisation(screen, ["perso"], [(650,220)], [(300,500)], ["hache.png"], "night-desert-zombie.jpg", "desert.mp3", False, name, 1)
                    result = lvm.story().dialogue(["Présentateur 1: Ah Zach décide de prendre les jambes à son cou !!","Heureusement qu’il a pris la hache car la masse l’aurais ralenti !","Tiens pas loin se trouve un combattant en difficulté !"])
                    if result == "exit": return self.level, self.dialog, name, False
                    elif result == "quit": return self.level, self.dialog, name, True

                    result = lvm.story().choice(screen, 2, ["Aider le combattant"], ["Abandoner le combatant"])
                    if result == "exit": return self.level, self.dialog, name, False
                    elif result == "quit": return self.level, self.dialog, name, True
                    lvm.media().save_file().create("nvx2_Z/aide.json", {'choice':result})
                    self.dialog = 6
                else: 
                    result = lvm.media().save_file().read("nvx2_Z/aide.json")
                    result = result['choice']

                if result == 1: #aider max
                    if self.dialog < 7:    
                        lvm.level().initialisation(screen, ["perso","Max.png"], [(650,220),(300,220)], [(300,500),(300,500)], ["hache.png"], "night-desert.jpg", "desert.mp3", False, name, 1)
                        intro = (["Présentateur 2 : Attendez je vois Zach courir à son secour, c’est incroyable il est entrain de le sauver !", "Je crois qu’une alliance viens de se former !!"],["Max : Merci mon nom est Max ","Zach : Moi c’est Zach ","Max : Dépêchons-nous ils reviennent !"])
                        for dial in intro:
                            result = lvm.story().dialogue(dial, make_init=True)
                            if result == "exit": return self.level, self.dialog, name, False
                            elif result == "quit": return self.level, self.dialog, name, True

                        lvm.level().initialisation(screen, ["perso","Max.png"], [(650,220),(300,220)], [(300,500),(300,500)], ["hache.png"], "night-desert-zombie.jpg", "desert.mp3", False, name, 1)
                        intro = (["Présentateur 1 : C’est beau l’amitié, ils vont pouvoir fuir main dans la main. "],["Présentateur 2 : Je crois que la première mort approche,", "regardez!", "deux jeunes enfants se sont fait encerclés…"],["Zach et Max ne sont pas loin,","ils vont sûrement vouloir jouer les héros !"])
                        for dial in intro:
                            result = lvm.story().dialogue(dial, make_init=True)
                            if result == "exit": return self.level, self.dialog, name, False
                            elif result == "quit": return self.level, self.dialog, name, True

                        result = lvm.story().choice(screen, 2, ["Aider les enfants"], ["Abandoner les gosses"])
                        if result == "exit": return self.level, self.dialog, name, False
                        elif result == "quit": return self.level, self.dialog, name, True
                        lvm.media().save_file().create("nvx2_Z/aide_2.json", {'choice':result})
                        self.dialog = 7
                    else: 
                        result = lvm.media().save_file().read("nvx2_Z/aide_2.json")
                        result = result['choice']

                    if result == 1: #aider les enfants
                        if self.dialog < 8:    
                            lvm.level().initialisation(screen, ["perso","Max.png"], [(650,220),(300,220)], [(300,500),(300,500)], ["hache.png"], "night-desert.jpg", "desert.mp3", False, name, 1)
                            intro = (["Zach : On y va !","Max : Non ils n’en valent pas la peine !"],["Présentateur 1 : Je crois que leur amitié ne vas pas durer."])
                            for dial in intro:
                                result = lvm.story().dialogue(dial, make_init=True)
                                if result == "exit": return self.level, self.dialog, name, False
                                elif result == "quit": return self.level, self.dialog, name, True
                            
                            lvm.story().dialogue(["Regardez, Zach et Max se dispu…"],no_wait=True)
                            lvm.level().wait(50)
                            lvm.media().sound("assets/sounds/decapitation.wav")
                            lvm.level().initialisation(screen, ["None"], [(650,220)], [(300,500)], ["None"], "night-desert-kill.jpg", "desert.mp3", False, name, 1)
                            result = lvm.story().dialogue(["Narrateur : Le présentateur reste figé par la haine de votre allié.","Il a pris votre hache et vous a décapité. Vous étiez devenu un poids."], make_init=True)
                            if result == "exit": return self.level, self.dialog, name, False
                            elif result == "quit": return self.level, self.dialog, name, True
                                
                            lvm.level().death(screen, "Vous ralentissez Max !")
                            self.dialog = 8
                        else: 
                            result = lvm.media().save_file().read("nvx2_Z/aide_2.json")
                            result = result['choice']
                    elif result == 2: #laisser les enfants mourir
                        pass

                elif result == 2: #laisser max
                    pass

            elif result == 2: #combattre les zombies
                if self.dialog < 6: 
                    lvm.level().initialisation(screen, ["perso"], [(650,220)], [(300,500)], ["hache.png"], "night-desert-zombie.jpg", "desert.mp3", True, name, 1)
                    intro=[["Présentateur 2 : Zach fonce sur les zombies !! Ils les tue à la chaine !!"],["Présentateur 1 : Je n’ai jamais vu quelqu’un manier aussi bien la hache !","Quels panache !","Regardez il envoie sa hache sur un ennemi..."],["En pleine tête !!","Attendez il n'a plus d’arme du coup ?"]]
                    for dial in intro:
                        result = lvm.story().dialogue(dial)
                        if result == "exit": return self.level, self.dialog, name, False
                        elif result == "quit": return self.level, self.dialog, name, True
                    lvm.level().initialisation(screen)
                    result = lvm.story().dialogue(["Narrateur : Dans le feu de l’action vous avez abandonné votre arme.","Vous finissez dévoré par une horde de zombies..."])
                    if result == "exit": return self.level, self.dialog, name, False
                    elif result == "quit": return self.level, self.dialog, name, True
                    lvm.level().death(screen, "Vous avez fait le festin des zombies")
                    self.dialog = 6

        elif weapon == "poing_am":
            lvm.level().initialisation(screen, ["perso"], [(650,220)], [(300,500)], ["poing_am.png"], "night-desert-zombie.jpg", "desert.mp3", True, name, 1)
            lvm.level().wait(500)


        elif weapon == "masse":
            lvm.level().initialisation(screen, ["perso"], [(650,220)], [(300,500)], ["masse.png"], "night-desert-zombie.jpg", "desert.mp3", True, name, 1)
            lvm.level().wait(500)


        else: 
            print("Erreur lors du chargement de l'arme, veuillez la rechoisir !")
            return self.level, 2, name, False

        return self.next_level, 0, name, False

