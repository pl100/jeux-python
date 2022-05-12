import pygame as py
from joueur import Joueur
from monstre import Monstre

class Jeu:
    def __init__(perso):
        perso.est_joue = False # Définir si notre jeu a commencé ou non
        perso.joueurs = py.sprite.Group()
        perso.joueur = Joueur(perso) # Génération du joueur
        perso.joueurs.add(perso.joueur)
        perso.monstres = py.sprite.Group() # Groupe de monstre
        perso.entree = {}
        perso.spawn_monstre()
        perso.spawn_monstre()

    def maj(perso, fenetre):
        fenetre.blit(perso.joueur.image, perso.joueur.rect)

        perso.joueur.maj_barre_vie(fenetre)  # Actualisation barre de vie du joueur

        for tir in perso.joueur.tirs:
            tir.deplacement()

        for monstre in perso.monstres:
            monstre.deplacement_monstre()
            monstre.maj_barre_vie(fenetre)

        perso.joueur.tirs.draw(fenetre)

        perso.monstres.draw(fenetre)

        if perso.entree.get(py.K_d) and perso.joueur.rect.x < 820:
            perso.joueur.deplacement_droite()

        elif perso.entree.get(py.K_q) and perso.joueur.rect.x > -50:
            perso.joueur.deplacement_gauche()

        elif perso.entree.get(py.K_z) and perso.joueur.rect.y > 0:
            perso.joueur.deplacement_haut()

        elif perso.entree.get(py.K_s) and perso.joueur.rect.y < 550:
            perso.joueur.deplacement_bas()

    def verif_collision(perso, sprite, groupe):
        return py.sprite.spritecollide(sprite, groupe, False, py.sprite.collide_mask)

    def spawn_monstre(perso):
        monstre = Monstre(perso)
        perso.monstres.add(monstre)