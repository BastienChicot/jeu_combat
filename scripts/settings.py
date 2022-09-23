# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 12:14:13 2022

@author: basti
"""
import pygame

display_width = 500
display_height = 500

hauteur = {
    "basti":35,
    "clou":20,
    "coach":30,
    "justi":25
    }

punch = {
    "basti":-10,
    "clou":-8,
    "coach":-15,
    "justi":-5
    }

kicks = {
    "basti":-5,
    "clou":-8,
    "coach":-12,
    "justi":-10
    }

supers = {
    "basti":-15,
    "clou":-12,
    "coach":-15,
    "justi":-20
    }

sauter = {
    "basti":-10,
    "clou":-10,
    "coach":-12,
    "justi":-15
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


power_bar0 = pygame.image.load("..\\_bank\\image\\super_power0.png")
power_bar1 = pygame.image.load("..\\_bank\\image\\super_power1.png")
power_bar2 = pygame.image.load("..\\_bank\\image\\super_power2.png")
power_bar3 = pygame.image.load("..\\_bank\\image\\super_power3.png")
power_bar4 = pygame.image.load("..\\_bank\\image\\super_power4.png")
power_bar5 = pygame.image.load("..\\_bank\\image\\super_power5.png")
power_bar = [power_bar0,power_bar1,power_bar2,power_bar3,power_bar4,power_bar5]