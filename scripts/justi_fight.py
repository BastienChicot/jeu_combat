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
        pygame.mixer.music.load ( playlist[0])
        pygame.mixer.music.play() 
        accueil(jeu)
    elif jeu.selected == "none" :
        pygame.mixer.music.load ( playlist[0])
        pygame.mixer.music.play() 
        accueil(jeu)
    elif jeu.selected == "multi_lvl" :
        Choix_level(jeu)
    elif jeu.selected == "choix_joueur1" :
        Choix_joueur1(jeu)
    elif jeu.selected == "choix_joueur2" :
        Choix_joueur2(jeu)
    elif jeu.selected == "multi" :
        pygame.mixer.music.load ( playlist[level_tracks[jeu.nivo]])
        pygame.mixer.music.play() 
        Multi(jeu)
        menu = False

while not gameExit :
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True  

    launch_jeu(jeu)      
    
    pygame.display.update()
    
pygame.quit()