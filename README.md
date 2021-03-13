# La Fin Du Pacte
![Bannière](https://github.com/kikookraft/la-fin-du-pacte/blob/main/.github_res/banniere-small.png "La Fin Du Pacte")


Bienvenu sur le repos de **La Fin Du Pacte** !!

### [Télécharger le jeux](https://github.com/kikookraft/la-fin-du-pacte/archive/main.zip) (l'archive est assez lourde, peut prendre du temps a télécharger)
### [Télécharger la version test](https://github.com/kikookraft/la-fin-du-pacte/archive/test.zip)
> Attention, la version test comporte souvent des bugs qui peuvent entrainer des crash !   
> La version test n'est pas toujour au point pour android !
## **Le projet est toujour en cour de création !!!**
**Il manque encore la majoritée niveaux et un personnage**


---
- ## Pour démarer le jeux sur linux : 
    - [Télécharger](https://github.com/kikookraft/la-fin-du-pacte/archive/main.zip) La Fin Du Pacte
    - Ouvrir un terminal dans le dossier `la-fin-du-pacte-main`
    - Installer les modules necessaires au jeux ( commande : `pip install nom_du_module` ):   
    Modules (certains sont installé par defaut):
        - Pygame
        - Os
        - Sys
        - json
        - Math
    - Faire : `python main.py` (pour démarer)
    - Le jeux se lance (si tout va bien)
- ## Pour démarer le jeux sur windows:
    - Installer [Python](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe)
    - [Télécharger](https://github.com/kikookraft/la-fin-du-pacte/archive/main.zip) La Fin Du Pacte
    - Ouvrir un terminal dans le dossier `la-fin-du-pacte-main`   
    en faisant `SHIFT + Click droit  >>  Ouvrir la fenetre powershell ici`
    - Installer les modules necéssaires comme sur linux (voir ci-dessus)
    - Lancer le jeux (comme sur linux)
- ## Pour démarrer le jeux sur android :
    - [Télécharger](https://github.com/kikookraft/la-fin-du-pacte/archive/main.zip) La Fin Du Pacte
    - Extraire les fichier et se souvenir du dossier ou ils sont
    - Installer l'application [Pydroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3&hl=fr&gl=FR) (ou une autre du même genre)
    - Installer les modules necessaires au jeux (voir l'onglet Pip et ecrire le nom des modules)   
    Modules (certains sont installé par defaut):
        - Pygame
        - Os
        - Sys
        - json
        - Math
    - Ouvrir le fichier `main.py` avec l'application puis lancer le jeux

    > Attention ! Ne retournez pas le téléphone en pleine partie, cela fait crash le jeu !   
    > Penser a retourner votre téléphone avant.

---

## Les touches et actions
### Pour les écrans tactiles:
- Cliquez pour faire une action (selection, passer les dialogues, ...)
- Touche retour pour quitter
### Pour les ordinateurs:
1. ### Sur le menu
    - `ECHAP` pour quitter le jeux
    - `R` pour reinitialiser le jeux (temporairement désactivé)
2. ### Dans le jeux
    - Sur les dialogues :
        - `ESPACE` passer a la suite quand le carré blanc en haut a droite est affiché
        - `S` pour passer les dialogues et les attentes
    - Sur les choix:
        - `A` ou `1` ou `&` (clavier numerique ou pas) pour choisir le choix **A**
        - `B` ou `2` ou `é` (clavier numerique ou pas) pour choisir le choix **B**
        - `B` ou `3` ou `"` (clavier numerique ou pas) pour choisir le choix **C** (si il est disponible)
    - Valable tout le temps du jeux:
        - `ECHAP` pour revenir au menu
---

### Le jeux se structure en plusieurs fichiers :
 
1. **main.py** qui est le fichier principal, c'est lui qu'il faut lancer pour jouer au jeux!  
2. **game.py** est le fichier qui sert a faire fonctionner le menu et la gestion des fichiers **main.py**
3. **nvx/levelmanager.py** est le fichier qui sert de module pour les niveaux, il contient le système de dialogue, choix, affichage, son, sauvegardes, ... C'est le moteur du jeu !

---