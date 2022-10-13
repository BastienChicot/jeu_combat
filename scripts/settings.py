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
kick_1 = pygame.mixer.Sound("..\\_bank\\fx\\kicks\\07_Kick_11_SP.wav")
kick_2 = pygame.mixer.Sound("..\\_bank\\fx\\kicks\\07_Kick_14_SP.wav")
kick_3 = pygame.mixer.Sound("..\\_bank\\fx\\kicks\\Boom-Bap Kick 70.wav")
kick_4 = pygame.mixer.Sound("..\\_bank\\fx\\kicks\\Boom-Bap Kick 73.wav")
kick_5 = pygame.mixer.Sound("..\\_bank\\fx\\kicks\\Boom-Bap Kick 82.wav")
kick_6 = pygame.mixer.Sound("..\\_bank\\fx\\kicks\\break_kick_8.wav")
kick_7 = pygame.mixer.Sound("..\\_bank\\fx\\kicks\\Break_kick_14.wav")
kick_8 = pygame.mixer.Sound("..\\_bank\\fx\\kicks\\brka_kick.wav")
kick_9 = pygame.mixer.Sound("..\\_bank\\fx\\kicks\\dfs_kick.wav")
kick_10 = pygame.mixer.Sound("..\\_bank\\fx\\kicks\\Kick (155).wav")
kick_11 = pygame.mixer.Sound("..\\_bank\\fx\\kicks\\KICK IIIII.wav")
kick_12 = pygame.mixer.Sound("..\\_bank\\fx\\kicks\\Medicated Kick 4.wav")

slap_1 = pygame.mixer.Sound("..\\_bank\\fx\\slaps\\07_Clap_13_SP.wav")
slap_2 = pygame.mixer.Sound("..\\_bank\\fx\\slaps\\clap_tamb.wav")
slap_3 = pygame.mixer.Sound("..\\_bank\\fx\\slaps\\FX (7).wav")
slap_4 = pygame.mixer.Sound("..\\_bank\\fx\\slaps\\pcp_clap05.wav")
slap_5 = pygame.mixer.Sound("..\\_bank\\fx\\slaps\\pcp_rim02.wav")


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

touche_point_sound = {
    "basti" : kick_1,
    "clou" : slap_1,
    "coach" : slap_2,
    "justi" : slap_3
    }

touche_autre_sound = {
    "basti" : kick_2,
    "clou" : kick_3,
    "coach" : kick_4,
    "justi" : kick_5
    }

select_sounds = {
    "basti" : haan,
    "clou" : ohtraphigh,
    "coach" : ohyeahlow,
    "justi" : haanhigh
    }

hauteur = {
    "basti":40,
    "clou":35,
    "coach":40,
    "justi":40
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

low = {
    "basti":3,
    "clou":6,
    "coach":10,
    "justi":6
    }


level_sol ={
    "centre_com":470,
    "practice":400,
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

justinouille = pygame.image.load("..\\_bank\\image\\justi_mega.png")
justi_mega = pygame.transform.flip(justinouille, True, False)
bastinouille = pygame.image.load("..\\_bank\\image\\basti_mega.png")
basti_mega = pygame.transform.flip(bastinouille, True, False)
mega_story_perso = [justi_mega,basti_mega]

justi_mega_rect = justi_mega.get_rect()
justi_mega_rect.topleft = (325,196),
basti_mega_rect = basti_mega.get_rect()
basti_mega_rect.topleft = (325,193)
mega_rect = [justi_mega_rect,basti_mega_rect]
