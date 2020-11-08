import os
class New:
    def new(self):
        print("\nSupression de 'nvx/nvx2/player.txt'")
        try:
            os.remove('nvx/nvx2/player.txt')
        except:
            print("Erreur, il n'y a rien a suprimmer dans le niveau 2!\n")
        print("\nSupression de 'data/player.txt'")
        try:
            os.remove('data/player.txt')
        except:
            print("Erreur, il n'y a rien a suprimmer dans le fichier global!\n")
        print("\nSupression de 'nvx/nvx3/player.txt'")
        try:
            os.remove('nvx/nvx3/player.txt')
        except:
            print("Erreur, il n'y a rien a suprimmer dans le niveau 3!\n")