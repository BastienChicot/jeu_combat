# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:06:43 2022

@author: basti
"""

import pygame

from fonctions import *
from classes import *
from settings import *
from mode_histoire import * 
from multi import Multi

import os
import random

m = random.choice(random_liste)


pygame.mixer.init()
pygame.init()
pygame.font.init()
pygame.mixer.pre_init(44100, -16, 1, 4096)

story = Story()

if os.path.exists("saves/histoire.pkl."):
    story = load_story(story)
else:
    story = Story()

jeu = Jeu("none")

if os.path.exists("saves/options_jeu.pkl."):
    jeu = load(jeu)
else:
    jeu = jeu

gameExit = False
pygame.mixer.music.load ( start_playlist[m])
pygame.mixer.music.play(-1) 
pygame.mixer.music.set_volume(jeu.vol_music_menu)
select_boom.set_volume(jeu.vol_fx)
        
def launch_jeu(jeu):
    if jeu.selected == "none" :      
        accueil(jeu)
    elif jeu.selected == "none" :
        accueil(jeu)
    elif jeu.selected == "multi_lvl" :
        Choix_level(jeu,story)
    elif jeu.selected == "choix_joueur1" :
        Choix_joueur1(jeu,story)
    elif jeu.selected == "choix_joueur2" :
        Choix_joueur2(jeu,story)
    elif jeu.selected == "options" :
        Options(jeu)
    elif jeu.selected == "multi" :
        pygame.mixer.music.set_volume(jeu.vol_music_fight)
        pygame.mixer.music.load ( playlist[level_tracks[jeu.nivo]])
        pygame.mixer.music.play(-1) 
        Multi(jeu)
        menu = False
    elif jeu.selected == "accueil_histoire":
        Launch_histoire(jeu,story)
    elif jeu.selected == "histoire":
        pygame.mixer.music.set_volume(jeu.vol_music_fight)
        pygame.mixer.music.load ( playlist[level_tracks[stage_liste[story.stage]]])
        pygame.mixer.music.play(-1) 
        Histoire(jeu,story)    
    
while not gameExit :

    select_boom.set_volume(jeu.vol_fx)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True  

    launch_jeu(jeu)      
    
    pygame.display.update()
    
pygame.quit()