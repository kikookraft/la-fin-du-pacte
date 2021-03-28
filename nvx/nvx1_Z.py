import pygame
import nvx.levelmanager as lvm

class Level1_Z:
    dialog = 0
    level = 1
    next_level = 2

    def game(self, screen, dialog, name):
        self.dialog = dialog
        if self.dialog < 1: #Introduction
            lvm.level().initialisation(screen, ["None"], [(650,220)], [(300,500)], "None", "None.jpg", "place de la tour.mp3", True, name)
            result = lvm.story().dialogue(["Votre épopée débute dans un futur lointains où l’humanité tel que vous la connaissiez n’existe plus."])
            if result == "exit": return self.level, self.dialog, name, False
            elif result == "quit": return self.level, self.dialog, name, True

            lvm.level().initialisation(screen, ["None"], [(650,220)], [(300,500)], "None", "background.jpg", "None", False, name)
            intro = [["Les derniers membres de ton espèce errent quelque part dans l’Univers, accroché à un rocher flottant dans le vide."],["Cette ‘île’ était transpercé par une tour si grande que l’île en paraissait petite","Mais ce joyaux architectural cachait des habitations enflammées par les guerres civiles."],["Plus on se dirigeait vers la périphérie, plus les gens étaient pauvres et formait un triste bidonville."],["La gravité permettait à l’autre face de l’île d’être habitable, mais cette zone était interdite d’accès et était utilisée à des fins plus obscures..."]]
            for dial in intro:
                result = lvm.story().dialogue(dial)
                if result == "exit": return self.level, self.dialog, name, False
                elif result == "quit": return self.level, self.dialog, name, True
            self.dialog = 1


        if self.dialog < 2:
            lvm.level().initialisation(screen, ["None"], [(650,220)], [(300,500)], "None", "noir.jpg", "None", False, name)
            lvm.media().sound("assets/sounds/souris.wav")
            result = lvm.level().wait(150)
            if result == "exit": return self.level, self.dialog, name, False
            elif result == "quit": return self.level, self.dialog, name, True

            result = lvm.story().dialogue(["Vous vous réveillez dans une pièce sombre, elle est sale et humide, vous entendez des rats mais ça ne vous gène en rien, vous avez l’habitude."])
            if result == "exit": return self.level, self.dialog, name, False
            elif result == "quit": return self.level, self.dialog, name, True

            lvm.media().sound("assets/sounds/porte.wav", 1)
            lvm.level().initialisation(screen, ["policier.png"], [(650,220)], [(300,500)], "None", "Bidonville.jpg", "None", False, name)
            lvm.level().wait(100)
            if result == "exit": return self.level, self.dialog, name, False
            elif result == "quit": return self.level, self.dialog, name, True
            
            dialog_list = [["Policier: Vous êtes en retard pour le rassemblement !!"],["Narrateur : En effet, aujourd’hui était un jour spécial, c’était le jour des nominations pour les death run, une épreuve de survies à travers les méandres du dessous de l’île."]]
            for dial in dialog_list:
                result = lvm.story().dialogue(dial)
                if result == "exit": return self.level, self.dialog, name, False
                elif result == "quit": return self.level, self.dialog, name, True
            self.dialog = 2

        if self.dialog < 3:
            lvm.level().initialisation(screen, ["policier.png","Zach.png"], [(650,220),(150,220)], [(300,500),(300,500)], "None", "Bidonville.jpg", "None", False, name)    
            result = lvm.story().dialogue(["Zach : J'arrive","Policier : Dépêchez vous !"],make_init=False)
            if result == "exit": return self.level, self.dialog, name, False
            elif result == "quit": return self.level, self.dialog, name, True

            result = lvm.story().choice(screen, 2, ["Suivre le policier"],["Lui resister"])
            if result == "exit": return self.level, self.dialog, name, False
            elif result == "quit": return self.level, self.dialog, name, True
            elif result == 1: pass #si le joueur choisit le choix 1 il peut continuer
            elif result == 2: 
                lvm.level().wait(50)
                if result == "exit": return self.level, self.dialog, name, False
                elif result == "quit": return self.level, self.dialog, name, True
                lvm.media().sound("assets/sounds/gunshot.wav", 1)
                lvm.level().death(raison="Le policier vous a fusillé !")
                return self.level, self.dialog, name, False

            lvm.level().wait(150)
            if result == "exit": return self.level, self.dialog, name, False
            elif result == "quit": return self.level, self.dialog, name, True
            self.dialog = 3
        
        if self.dialog < 4:
            lvm.level().initialisation(screen, ["UtopiaJR.png"], [(650,220)], [(300,500)], "None", "background.jpg", "place de la tour.mp3", True, name)
            lvm.media().sound("assets/sounds/foule.wav", loop=True)
            result = lvm.story().dialogue(["Le policier vous emmène au centre de l’île, au pied de la tour où la population est rassemblé pour écouter le discours d’Utopia Jr, le Directeur de la société du même nom qui dirige l’île."])
            if result == "exit": return self.level, self.dialog, name, False
            elif result == "quit": return self.level, self.dialog, name, True

            dialog_list = [["Utopia Jr: Bienvenue aux 10e death run !!!","Eh oui mes camarades cela fait 100 ans déjà que le pacte a été signé.","Une sombre époque pour nous tous."],["Rappelez vous des souffrances qu’ont enduré notre peuple à cause de résistant anarchique.","Souvenez vous des terribles conséquences qu’ont engendré cette hérésie appelé révolution."],["Mon père a malheureusement dut sévir à l’époque mais pour vous remettre dans le droit chemin.","Vous êtes la base de la société et vous devez donc vivre sous le sommet.","Sans cet équilibre notre civilisation meurt."],["Cela peut paraître injuste mais vous êtes né ainsi, c’est votre seul but."],["Heureusement par extrême générosité, nous permettons tous les 10 ans à 10 d’entre vous de rentrer dans notre élite,","parmi les grands de notre société."],["Mais parce que rien est gratuit vous devrez prouvez votre valeur dans les death run !","J’ai a coté de moi, dans mon bureau 10 urnes avec les noms de millions d’âmes, les vôtres,","et seule 10 d’entre elles pourront prétendre a rejoindre l’élite."],["Narateur: Le Directeur annonce un a un les noms de ce que le peuples appelait les condamné car tous savais qu’il était presque impossible de survivre..."],["Notre personnage regarde les condamné avec pitié mais n’avait pas peur d’être tiré au sort car les chance était trop mince..."],["Le Directeur : Zach, fils de ... personne"]]
            for dial in dialog_list:
                result = lvm.story().dialogue(dial)
                if result == "exit": return self.level, self.dialog, name, False
                elif result == "quit": return self.level, self.dialog, name, True

        return self.next_level, 0, name, False

