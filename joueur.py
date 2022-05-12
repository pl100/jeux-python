import pygame as py
from tir import Tir

class Joueur(py.sprite.Sprite):
    def __init__(perso, jeu):
        super().__init__() #appel d'une superclasse
        perso.jeu = jeu
        perso.vie = 100
        perso.max_vie = 100
        perso.attaque = 1
        perso.vitesse = 5
        perso.tirs = py.sprite.Group() #regroupement de tous les tirs
        perso.image = py.image.load("images/medecin.png")
        perso.rect = perso.image.get_rect()
        perso.rect.x = 400
        perso.rect.y = 400

    def degats(perso, compteur):
        if perso.vie - compteur > compteur:
            perso.vie -= compteur


    def maj_barre_vie(perso, surface):
        couleur_barre = (91, 211, 30) # Couleur barre de vie
        couleur_fond = (120, 123, 118)  # Couleur arrière plan barre de vie

        position_barre = [perso.rect.x + 100, perso.rect.y - 10, perso.vie, 7]
        position_fond = [perso.rect.x + 100, perso.rect.y - 10, perso.max_vie, 7]

        py.draw.rect(surface, couleur_fond, position_fond)  # Dessin de l'arrière plan de la barre de vie
        py.draw.rect(surface, couleur_barre, position_barre) # Dessin de la barre de vie

    def lancement_tir(perso):
        tir = Tir(perso)
        perso.tirs.add(tir)

    def deplacement_droite(perso):
        if not perso.jeu.verif_collision(perso, perso.jeu.monstres): #Si le joueur n'est pas en collision
            perso.rect.x += perso.vitesse

    def deplacement_gauche(perso):
        perso.rect.x -= perso.vitesse

    def deplacement_haut(perso):
        perso.rect.y -= perso.vitesse

    def deplacement_bas(perso):
        perso.rect.y += perso.vitesse