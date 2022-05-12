import pygame as py
import random

class Monstre(py.sprite.Sprite):
    def __init__(perso, jeu):
        super().__init__()
        perso.jeu = jeu
        perso.vie = 100
        perso.max_vie = 100
        perso.attaque = 0.3
        perso.image = py.image.load("images/corona_vert.png")
        perso.image = py.transform.scale(perso.image, (100,100)) # Réduction taille image
        perso.rect = perso.image.get_rect()
        perso.rect.x = 950 + random.randint(50, 300)
        perso.rect.y = random.randint(20, 550)
        perso.vitesse = 1

    def degats(perso, compteur):
        perso.vie -= compteur

        if perso.vie <= 0: # Vérifier si son nombre de point de vie est inférieur ou égal à 0
            perso.rect.x = 1000 + random.randint(50, 300) # Réapparition comme un nouveau monstre
            perso.rect.y = random.randint(50, 550)
            perso.vitesse = 1
            perso.vie = perso.max_vie

    def maj_barre_vie(perso, surface):
        couleur_barre = (91, 211, 30) # Couleur barre de vie
        couleur_fond = (120, 123, 118)  # Couleur arrière plan barre de vie

        position_barre = [perso.rect.x + 2, perso.rect.y - 10, perso.vie, 5]
        position_fond = [perso.rect.x + 2, perso.rect.y - 10, perso.max_vie, 5]

        py.draw.rect(surface, couleur_fond, position_fond)  # Dessin de l'arrière plan de la barre de vie
        py.draw.rect(surface, couleur_barre, position_barre) # Dessin de la barre de vie

    def deplacement_monstre(perso):
        # Déplacement réalisé seulement s'il n'y a pas de collision avec un groupe de joueur
        if not perso.jeu.verif_collision(perso, perso.jeu.joueurs): # Si le joueur n'est pas en collision
            perso.rect.x -= perso.vitesse

        # Si le monstre est en collision avec le joueur
        else:
            perso.jeu.joueur.degats(perso.attaque)