# La Fin Du Pacte
Une histoire interactive créée en python...


Bienvenu sur le repos de **La Fin Du Pacte** !!

### [Télécharger le jeux](https://github.com/kikookraft/la-fin-du-pacte/archive/main.zip) (l'archive fait 391Mo, peut prendre du temps a télécharger)
## **Le projet est toujour en cour de création !!!**


---
- ## Pour démarer le jeux sur linux : 
    - [Télécharger](https://github.com/kikookraft/la-fin-du-pacte/archive/main.zip) La Fin Du Pacte
    - Ouvrir un terminal dans le dossier `la-fin-du-pacte-main`
    - Installer les modules necessaires au jeux ( commande : `pip install nom_du_module` ):   
    Modules :
        - Pygame
    - Faire : `python main.py` (pour démarer)
    - Le jeux se lance (si tout va bien)
- ## Pour démarer le jeux sur windows:
    - Installer [Python](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe)
    - [Télécharger](https://github.com/kikookraft/la-fin-du-pacte/archive/main.zip) La Fin Du Pacte
    - Ouvrir un terminal dans le dossier `la-fin-du-pacte-main`   
    en faisant `SHIFT + Click droit  >>  Ouvrir la fenetre powershell ici`)
    - Installer les modules necéssaires comme sur linux (voir ci-dessus)
    - Lancer le jeux (comme sur linux)
- ## Pour démarrer le jeux sur android :
    - [Télécharger](https://github.com/kikookraft/la-fin-du-pacte/archive/main.zip) La Fin Du Pacte
    - Extraire les fichier et se souvenir du dossier ou ils sont
    - Installer l'application [Pydroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3&hl=fr&gl=FR) (ou une autre du même genre)
    - Installer les modules necessaires au jeux (voir l'onglet Pip et ecrire le nom des modules)   
    Modules :
        - Pygame
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
    - `R` pour reinitialiser le jeux
2. ### Dans le jeux
    - Sur les dialogues :
        - `ESPACE` passer a la suite quand le carré blanc en haut a droite est affiché
        - `S` pour passer les dialogues et les attentes
    - Sur les choix:
        - `A` ou `1` ou `&` (clavier numerique ou pas) pour choisir le choix **A**
        - `B` ou `2` ou `é` (clavier numerique ou pas) pour choisir le choix **B**
        - `B` ou `3` ou `"` (clavier numerique ou pas) pour choisir le choix **C** (si il est disponible)
    - Durant les vidéos :
        - `ECHAP` pour arreter la vidéo et passer a la suite
    - Valable tout le temps du jeux:
        - `ECHAP` pour revenir au menu
---

### Le jeux se structure en plusieurs fichiers :
 
1. **main.py** qui est le fichier principal, c'est lui qu'il faut lancer pour jouer au jeux!  
2. **game.py** est le fichier qui sert a importer tout les autres dans **main.py**
3. **level.py** est le fichier qui gère les niveaux, c'est lui qui detecte le niveau actuel et qui lance la suite de l'histoire (ou relance le niveau si tu était mort ;)
4. **score.py** est le fichier qui sauvegarde et charge les scores à chaque arrêt/démarrage du jeux
5. **credit.py** est le fichier qui sert a afficher les credits (sera bientot suprimé pour être ajouté dans **main.py**)
6. **new.py** est le fichier qui sert a réinitialiser les scores et recommencer au début du jeux

---

## Créer son propre niveau

Il est possible de créer son propre niveau sans coder en python !  
Ce que fait le jeux, c'est qu'il lit un fichier texte ligne par ligne et execute des actions en fonction de ce qui est écrit !   
Regarde dans les fichiers par toi-meme, tu verras.   
   
      


### Commandes

- `end--`

    Met fin au niveau et ramene au menu


- `end++`

    Met fin au niveau, ramene au menu et fait passer au niveau suivant


- `init- (Zach.png,kevin.png; 650,225/0,250; 300,500/300,500; None; bg.jpg; lava.wav; True)`

    initialisation du menu avec 7 arguments (chaque arguments est séparé par un point virgule et un espace `; `):   
    -   1 er argument : Chemin des images des personnages (Zach.png,kevin.png;). sépare les personnages par des virgules   
    Il est possible d'afficher le personnage choisit au debut par le joueur, pour cela il suffit d'écrire `perso`.   
    -   2eme : position des personnages. chaque personnage possède un groupe des 2 nombre séparé par des virgules et les groupes sont séparés par des slash `/`   
    -   3eme : taille des images des personnages, fonctionne comme pour la position   
    -   4eme : Arme du personnage (ne fonctionne pas pour l'instant) pour afficher une arme, faire afficher l'arme comme pour un personnage.   
    -   5eme : image de fond d'ecran   
    -   6eme : musique du niveau   
    -   7eme : definit si la musique doit etre rechargée, si c'est a True, la musique s'arrete et celle spécifiée sera jouée, sinon si c'est sur False aucun changement n'est fait et l'ancienne musique continue   


- `title ("Titre")`

    Changer le Titre de la fenetre



- `temps (500)`

    Temps a attendre en centieme de secondes. `temps (100)` attendra 1 seconde.   
   
      
     

- ```
    dialg (2, 6000)
    "Ceci est le premier texte"
    "Ceci le deuxieueème"
    ```

    Sert a afficher les dialogues.
    -   1er paramètre = Nombres de lignes a afficher (les lignes de texte affiché sont ecrites en dessous de l'appel de la fonction)   
    -   2eme = temp d'attente avant l'affichage du texte suivant en centième de secondes (comme au dessus)   

    L'initialisation du texte est syncronisée avec l'initialisation précédente (la musique/les personnages et le fond restera le même)   



- `choix (nbchoix=3, "Choix1", "Choix2", "Choix3", goto1="marque1", goto2="marque2", goto3="marque3")`

    -   1er argument = nombre de choix   
    -   Les 2 ou 3 arguments suivants (en fonction du nombre de choix) : texte des choix   
    -   2 (ou 3) arguments suivant: mot clé de la suite de l'histoire .   
    -   C'est a dire que si tu ecrit `masse`, le jeux va chercher ce mot dans tout le fichier texte et quand il le trouve il continue l'histoire (utilisé pour les choix pour amener a des moments differents de l'histoire du personnage).    



- `markr (2)`

    marqueur indiquant la position a laquelle le joueur reviendra si il quitte le jeux (sauf si un autre marqueur est spécifié après)

- `towait (qqch)`

    Recherche dans le fichier texte la ligne qui commence par `qqch` pour continuer le jeux a partir de cet endroit   


- `video (assets/test.mp4)`

    video a afficher

    > Actuellement les vidéos sont désactivée car cela ne fonctionne pas sur les téléphones

- `img-- (kevin.png; 0,0; 500,500)`

    Image a afficher suivit de la position et de la taille



- `sound (sounds/lava.wav)`

    jouer des sons, utilisé pour les bruitages



- `mort- (CHEEEEEEEH)`

    Faire crever le joueur en affichant `CHEEEEEEEH` .   
   

voici un exemple :
```
init- (Zach.png; 650,225; 300,500; None; bg.jpg; lava.wav; True)
title (La Fin Du Pacte - Le Tutoriel)
dialg (3; 300)
Bienvenue dans ce test de niveaux !
Tu vas beaucoup aimer (je pense) &é(-è_çà)=É
Que veut tu faire en premier ?
markr (1)
choix (3; A - Attendre 5 sec; B - Parler; C - La réponse C; waitthe5sec; speeak; wasted)

waitthe5sec
init- (Zach.png,kevin.png; 650,225/0,250; 300,500/300,500; None; bg.jpg; lava.wav; True)
temps (500)
dialg (3; 300)
Tu veux un trophé pour etre arrivé ici ?
A moin que tu n'en veuille pas ...
Bon je vais quand meme t'en donner un ...
img-- (assets/trophes.png; 490,310; 100,100)
sound (assets/sounds/AMBIANCE DE GROTTE - Bruitage Gratuit.mp3)
temps (1000)
end++

speeak
markr (2)
dialg (2; 200)
Donc tu veux parler ?
Alors si c'est ce que tu veux, c'est partis!
markr (3)
dialg (3; 300)
Quand j'était petit, ma grand mère m'aimait...
Elle me faisait souvent des gâteaux...
Enfin voila tu merite de crever...
mort- (mdr ☺)
end--

wasted
markr (75)
video (assets/movies/credit.mp4)
mort- (Tu l'as mérité !)
end--
```
Cet exemple comprend la majoritée possibilités, amuse-toi avec !   
   
Pour tester ce niveau, remplace un fichier texte deja existant (ton niveau actuel par exemple) **mais n'oublie pas de le sauvegarder avant de le changer !** 
   
Ensuite lance le jeux et atteint le niveau concerné.   
   
