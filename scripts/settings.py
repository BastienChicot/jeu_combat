# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 12:14:13 2022

@author: basti
"""
import pygame
pygame.init()
pygame.font.init()

pygame.mixer.pre_init(44100, -16, 1, 4096)
pygame.mixer.init()

gui_font = pygame.font.Font(None,30)

display_width = 500
display_height = 500

select_boom = pygame.mixer.Sound("..\\_bank\\fx\\boom.wav")

##SELECTION PERSO
haan = pygame.mixer.Sound("..\\_bank\\fx\\voices\\haan.wav")
haanhigh = pygame.mixer.Sound("..\\_bank\\fx\\voices\\haanhigh.wav")
ohyeahlow = pygame.mixer.Sound("..\\_bank\\fx\\voices\\ohyeahlow.wav")
ohyeahmid = pygame.mixer.Sound("..\\_bank\\fx\\voices\\ohyeahmid.wav")
selectvil = pygame.mixer.Sound("..\\_bank\\fx\\voices\\selectvillager.wav")
selectvil2 = pygame.mixer.Sound("..\\_bank\\fx\\voices\\selectvillager2.wav")
selectvil3 = pygame.mixer.Sound("..\\_bank\\fx\\voices\\selectvillager3.wav")
selectvil4 = pygame.mixer.Sound("..\\_bank\\fx\\voices\\selectvillager4.wav")
selectvil = pygame.mixer.Sound("..\\_bank\\fx\\voices\\selectvillager.wav")
letsgolow = pygame.mixer.Sound("..\\_bank\\fx\\voices\\letsgolow.wav")
letsgomid = pygame.mixer.Sound("..\\_bank\\fx\\voices\\letsgomid.wav")
letsgohigh = pygame.mixer.Sound("..\\_bank\\fx\\voices\\letsgohigh.wav")

##FX COUP PRIS
ohhigh = pygame.mixer.Sound("..\\_bank\\fx\\voices\\ohhigh.wav")
ohmid = pygame.mixer.Sound("..\\_bank\\fx\\voices\\ohmid.wav")
ohlow = pygame.mixer.Sound("..\\_bank\\fx\\voices\\ohlow.wav")
ohtraphigh = pygame.mixer.Sound("..\\_bank\\fx\\voices\\ohtraphigh.wav")
ohtrapmid = pygame.mixer.Sound("..\\_bank\\fx\\voices\\ohtrapmid.wav")
ohtraplow = pygame.mixer.Sound("..\\_bank\\fx\\voices\\ohtraplow.wav")
touche = pygame.mixer.Sound("..\\_bank\\fx\\voices\\touche.wav")
touche_2 = pygame.mixer.Sound("..\\_bank\\fx\\voices\\touche_2.wav")
touche_3 = pygame.mixer.Sound("..\\_bank\\fx\\voices\\touche_3.wav")
touchehigh = pygame.mixer.Sound("..\\_bank\\fx\\voices\\touchehigh.wav")
touchelow = pygame.mixer.Sound("..\\_bank\\fx\\voices\\touchelow.wav")


##FX COUP DONNE


playlist = []

playlist.append("..\\_bank\\bo\\track0.wav")
playlist.append("..\\_bank\\bo\\track1.wav")
playlist.append("..\\_bank\\bo\\track2.wav")
playlist.append("..\\_bank\\bo\\track3.wav")

hit_fx_sound = {
    "basti" : touche,
    "clou" : ohtraphigh,
    "coach" : touchelow,
    "justi" : touchehigh
    }

select_sounds = {
    "basti" : haan,
    "clou" : ohtraphigh,
    "coach" : ohyeahlow,
    "justi" : haanhigh
    }

hauteur = {
    "basti":35,
    "clou":20,
    "coach":30,
    "justi":25
    }

punch = {
    "basti":8,
    "clou":4,
    "coach":12,
    "justi":4
    }

kicks = {
    "basti":4,
    "clou":8,
    "coach":12,
    "justi":8
    }

supers = {
    "basti":15,
    "clou":15,
    "coach":15,
    "justi":15
    }

sauter = {
    "basti":8,
    "clou":8,
    "coach":12,
    "justi":12
    }

level_sol ={
    "centre_com":470,
    "practice":440,
    "espace":465,
    "gare":460,
    "montagne":440,
    "theatre":440,
    "ferme":465,
    "usine":438,
    "lac":340,
    "toit":383,
    "parc":440,
    "metro":280
    }

level_lim_min = {
    "centre_com":470,
    "practice":440,
    "espace":465,
    "gare":460,
    "montagne":440,
    "theatre":440,
    "ferme":465,
    "usine":438,
    "lac":340,
    "toit":383,
    "parc":440,
    "metro":280
    }

level_lim_max = {
    "centre_com":470,
    "practice":440,
    "espace":465,
    "gare":460,
    "montagne":440,
    "theatre":440,
    "ferme":465,
    "usine":438,
    "lac":340,
    "toit":383,
    "parc":440,
    "metro":280
    }

level_tracks = {
    "centre_com":1,
    "practice":2,
    "espace":3,
    "gare":3,
    "montagne":2,
    "theatre":1,
    "ferme":2,
    "usine":3,
    "lac":3,
    "toit":1,
    "parc":2,
    "metro":1
    }



power_bar0 = pygame.image.load("..\\_bank\\image\\super_power0.png")
power_bar1 = pygame.image.load("..\\_bank\\image\\super_power1.png")
power_bar2 = pygame.image.load("..\\_bank\\image\\super_power2.png")
power_bar3 = pygame.image.load("..\\_bank\\image\\super_power3.png")
power_bar4 = pygame.image.load("..\\_bank\\image\\super_power4.png")
power_bar5 = pygame.image.load("..\\_bank\\image\\super_power5.png")
power_bar = [power_bar0,power_bar1,power_bar2,power_bar3,power_bar4,power_bar5]


ko_1 = pygame.image.load("..\\_bank\\image\\autres\\ko_1.png")
ko_2 = pygame.image.load("..\\_bank\\image\\autres\\ko_2.png")
ko_3 = pygame.image.load("..\\_bank\\image\\autres\\ko_3.png")
ko_4 = pygame.image.load("..\\_bank\\image\\autres\\ko_4.png")
ko = [ko_1,ko_2,ko_3,ko_4]


