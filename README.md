# La Fin Du Pacte
Une histoire interactive créée en python...


Bienvenu sur le repos de **La Fin Du Pacte** !!

---

Le jeux se structure en plusieurs fichiers.
 
1. **main.py** qui est le fichier principal, c'est lui qu'il faut lancer pour jouer au jeux!  
    - ## Pour demmarer le jeux sur linux : 
        - Ouvrir le terminal dans le dossier `la fin du pacte`
        - Installer les modules necessaires au jeux ( commande : `pip install nom_du_module` ):
            - Pygame
            - Moviepy
        - Faire : `python main.py`
        - Le jeux se lance (normalement)
    - ## Pour demarer le jeux sur windows:
        - Installer [Python](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe)
        - Ouvrir un terminal dans le dossier la fin du pacte (en faisant `SHIFT + Click droit  >>  Ouvrir un terminal powershell`)
        - Installer les modules comme sur linux (voir ci-dessus)
        - Lancer le jeux (comme pour linux)
2. **game.py** est le fichier qui sert a importer tout les autres dans **main.py**
3. **level.py** est le fichier qui gère les niveaux, c'est lui qui detecte le niveau actuel et qui lance la suite de l'histoire (ou relance le niveau si tu était mort ;)
4. **score.py** est le fichier qui sauvegarde et charge les scores à chaque arrêt/démarrage du jeux
5. **credit.py** est le fichier qui sert a afficher les credits (sera bientot suprimé pour être ajouté dans **main.py**)
6. **new.py** est le fichier qui sert a réinitialiser les scores et recommencer au début du jeux

---

## Les touches

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

## Créer son propre niveau

Il est possible de créer son propre niveau sans coder en python !  
Ce que fait le jeux, c'est qu'il lit un fichier texte ligne par ligne et execute des actions en fonction de ce qui est écrit !   
Regarde dans les fichiers par toi-meme, tu verras.   
   
      
Pour commencer voici un exemple :
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
Mais elle et décédé du COVID-19...
mort- (Toi aussi mdr ☺)
end--

wasted
markr (75)
video (assets/movies/credit.mp4)
mort- (Tu l'as mérité !)
end--
```
Cet exemple comprend toutes les possibilités, donc amuse-toi a modifier ca si tu en as l'envie !   
   
Pour tester ce niveau, remplace un fichier texte deja existant (ton niveau actuel par exemple) **mais n'oublie pas de le sauvegarder avant de le changer !** 
   
Ensuite lance le jeux et atteint le niveau concerné.

> La documentation du fonctionnement des commandes est en cour...
> 
> 
