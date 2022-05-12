import pygame as py
from jeu import Jeu

def menu():
    for event in py.event.get():
        if event.type == py.MOUSEBUTTONUP:  # UP
            if bouton_rect.collidepoint(event.pos):
                jeu.est_joue = True
