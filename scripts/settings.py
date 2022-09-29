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
pygame.mixer.music.set_volume(0.1)

gui_font = pygame.font.Font(None,30)

display_width = 500
display_height = 500


playlist = []

playlist.append("..\\_bank\\bo\\track0.wav")
playlist.append("..\\_bank\\bo\\track1.wav")
playlist.append("..\\_bank\\bo\\track2.wav")
playlist.append("..\\_bank\\bo\\track3.wav")

hauteur = {
    "basti":35,
    "clou":20,
    "coach":30,
    "justi":25
    }

punch = {
    "basti":6,
    "clou":4,
    "coach":10,
    "justi":4
    }

kicks = {
    "basti":4,
    "clou":6,
    "coach":10,
    "justi":8
    }

supers = {
    "basti":14,
    "clou":14,
    "coach":14,
    "justi":14
    }

sauter = {
    "basti":8,
    "clou":8,
    "coach":10,
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

