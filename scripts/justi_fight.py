# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:06:43 2022

@author: basti
"""

import pygame

from fonctions import *
from classes import *
from settings import *
from multi import Multi


pygame.mixer.init()
pygame.init()
pygame.font.init()
pygame.mixer.pre_init(44100, -16, 1, 4096)

jeu = Jeu("none")

gameExit = False

def launch_jeu(jeu):
    if jeu.selected == "none" :
        accueil(jeu)
    if jeu.selected == "multi_lvl" :
        Choix_level(jeu)
    if jeu.selected == "multi" :
        Multi(jeu)


while not gameExit :
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True 
    
    launch_jeu(jeu)
    
    pygame.display.update()
    
pygame.quit()