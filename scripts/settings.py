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
playlist.append("..\\_bank\\bo\\track4.wav")
playlist.append("..\\_bank\\bo\\track5.wav")
playlist.append("..\\_bank\\bo\\track6.wav")

hit_fx_sound = {
    "basti" : touche,
    "clou" : ohtraphigh,
    "coach" : touchelow,
    "justi" : touchehigh,
    "gus" : ohtrapmid,
    "sam" : ohlow,
    "dad" : ohmid,
    "villageman" : haanhigh
    }

touche_point_sound = {
    "basti" : kick_1,
    "clou" : slap_1,
    "coach" : slap_2,
    "justi" : slap_3,
    "gus" : kick_6,
    "sam" : slap_4,
    "dad" : slap_5,
    "villageman" : slap_1
    }

touche_autre_sound = {
    "basti" : kick_2,
    "clou" : kick_3,
    "coach" : kick_4,
    "justi" : kick_5,
    "gus" : kick_7,
    "sam" : kick_8,
    "dad" : kick_9,
    "villageman" : kick_10
    }

select_sounds = {
    "basti" : haan,
    "clou" : ohtraphigh,
    "coach" : ohyeahlow,
    "justi" : haanhigh,
    "gus" : letsgomid,
    "sam" : letsgolow,
    "dad" : ohtrapmid,
    "villageman" : haan
    }

hauteur = {
    "basti":40,
    "clou":35,
    "coach":40,
    "justi":40,
    "gus" : 35,
    "sam" : 40,
    "dad" : 35,
    "villageman" : 40
    }

punch = {
    "basti":12,
    "clou":6,
    "coach":16,
    "justi":6,
    "gus" : 8,
    "sam" : 16,
    "dad" : 14,
    "villageman" : 10
    }

kicks = {
    "basti":8,
    "clou":14,
    "coach":16,
    "justi":14,
    "gus" : 10,
    "sam" : 12,
    "dad" : 14,
    "villageman" : 10
    }

supers = {
    "basti":20,
    "clou":20,
    "coach":20,
    "justi":20,
    "gus" : 20,
    "sam" : 20,
    "dad" : 22,
    "villageman" : 20
    }

sauter = {
    "basti":12,
    "clou":12,
    "coach":16,
    "justi":16,
    "gus" : 12,
    "sam" : 14,
    "dad": 10,
    "villageman" : 12
    }

low = {
    "basti":6,
    "clou":9,
    "coach":12,
    "justi":9,
    "gus" : 6,
    "sam" : 16,
    "dad" : 14,
    "villageman" : 9
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
    "practice" : 1,
    "parc" : 2,
    "ferme" : 3,
    "metro" : 4,
    "usine" : 5,
    "montagne" : 6,
    "theatre" : 2,
    "gare" : 3,
    "toit" : 4,
    "lac" : 5,
    "espace" : 1
    }

stage_liste = [
    "practice",
    "parc",
    "ferme",
    "metro",
    "usine",
    "montagne"
    # "toit",
    # "theatre",
    # "gare",
    # "lac",
    # "espace"
    ]

adv_liste = [
    "coach",
    "gus",
    "clou",
    "sam",
    "dad",
    "villageman"
    ]

range_adv = {
    "coach":64,
    "gus" : 64,
    "clou":32,
    "sam": 28,
    "dad" : 24,
    "villageman" : 20
    }

adv_dist = {
            "coach" : 5,
            "gus" : 6,
            "clou" : 7,
            "sam" : 9,
            "dad" : 7,
            "villageman" : 10
            }

adv_proba_jump = {
    "coach" : 9,
    "gus" : 9,
    "clou" : 8,
    "sam" : 9,
    "dad" : 8,
    "villageman" : 6
    }

adv_speed = {
    "coach" : 1,
    "gus" : 1,
    "clou" : 2,
    "sam" : 1,
    "dad" : 1,
    "villageman" : 1
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
