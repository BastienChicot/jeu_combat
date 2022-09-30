# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 12:27:29 2022

@author: basti
"""
import pygame
from settings import *
from classes import *
import pickle

pygame.init()
pygame.font.init()
pygame.mixer.init()

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Justi FIGHT')
clock = pygame.time.Clock()

gui_font = pygame.font.Font(None,30)
myfont = pygame.font.SysFont('corbel', 20, bold=True)
Gus_font = pygame.font.SysFont('corbel', 16, bold=True)
big_font = pygame.font.SysFont('corbel', 60, bold=True)

clock = pygame.time.Clock()

def buttons_draw(buttons,screen):
    for b in buttons:
        b.draw(screen)
        
def zone_dialogue(screen,texte_zone,action,liste_phrases,var_iter,max_iter):
    
    pygame.font.init()
 
    myfont = pygame.font.SysFont('corbel', 19, bold=True)
    
    textsurface = myfont.render(texte_zone, False, (110, 110, 110))
    screen.blit(fond_text,(260,380))
    screen.blit(textsurface,(280,385))
    i=var_iter
    j = 405
    for phrases in liste_phrases :
        
        if i < max_iter and action.click == True:
            textsurface2 = myfont.render(phrases, False, (110, 110, 110))
            screen.blit(textsurface2,(270,j))

            j += 15
    
        if var_iter >= max_iter and action.click == True:
            i -= max_iter
            
def pause(screen,buttons_pause):

    buttons_draw(buttons_pause,screen)

def accueil(jeu):
    pygame.init()

    buttons = []
    
    multijoueur = Button('Multijoueur',200,100,(250,175),5,buttons,screen)
    hist = Button('Histoire',200,100,(250,300),5,buttons,screen)
    options = Button('Options',200,50,(250,425),5,buttons,screen) 
    quitter = Button('Quitter le jeu',150,75,(25,25),5,buttons,screen)
    
    a = 0
    frame_count = 0
    
    lvl = level("centre_com")
    
    gameExit = False

    while not gameExit and jeu.selected == "none":
        if frame_count <= 100:
            frame_count += 1
        else:
            frame_count = 0
            
        if frame_count <= 25:
            a=0
        elif 25 < frame_count <= 50:
            a=1
        elif 50 < frame_count <= 75:
            a=2
        elif 75 < frame_count <= 100 :
            a=3

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
    
        decors = lvl.anim_level[a]
        screen.blit(decors,(0,0))
        buttons_draw(buttons,screen)
        
        if multijoueur.pressed:
            jeu.selected = "multi_lvl"
        if quitter.pressed:
            pygame.quit()
        if options.pressed :
            jeu.selected = "options"
            
        pygame.display.update()
        clock.tick(60)

def Choix_level(jeu):
    pygame.init()

    buttons = []
    images = []
    
    retour = Button('Retour',200,30,(50,400),5,buttons,screen)
    for key in jeu.unlock_nivo:
        #globals()['%s' % key] = 
        Image_select(str(key),jeu.unlock_nivo[key],5,images)

    a = 0
    frame_count = 0
    
    lvl = level("centre_com")
    
    gameExit = False

    while not gameExit and jeu.selected == "multi_lvl":
        if frame_count <= 100:
            frame_count += 1
        else:
            frame_count = 0
            
        if frame_count <= 25:
            a=0
        elif 25 < frame_count <= 50:
            a=1
        elif 50 < frame_count <= 75:
            a=2
        elif 75 < frame_count <= 100 :
            a=3

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
    
        decors = lvl.anim_level[a]
        screen.blit(decors,(0,0))
        buttons_draw(buttons,screen)
        buttons_draw(images,screen)
        
        for img in images:
            if img.pressed:
                jeu.selected = "choix_joueur1"
                jeu.nivo = img.text
        
        if retour.pressed:
            jeu.selected = "none"
            
        pygame.display.update()
        clock.tick(60)
        
        
def Choix_joueur1(jeu):
    pygame.init()

    buttons = []
    images = []
    
    Titre = Button('Joueur 1 : choisi ton combattant',350,30,(75,25),5,buttons,screen)
    retour = Button('Retour',200,30,(50,400),5,buttons,screen)
    for key in jeu.unlock_perso:
        #globals()['%s' % key] = 
        Image_select(str(key),jeu.unlock_perso[key],5,images)        

    a = 0
    frame_count = 0
    
    lvl = level("centre_com")
    
    gameExit = False

    while not gameExit and jeu.selected == "choix_joueur1":
        if frame_count <= 100:
            frame_count += 1
        else:
            frame_count = 0
            
        if frame_count <= 25:
            a=0
        elif 25 < frame_count <= 50:
            a=1
        elif 50 < frame_count <= 75:
            a=2
        elif 75 < frame_count <= 100 :
            a=3

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
    
        decors = lvl.anim_level[a]
        screen.blit(decors,(0,0))
        buttons_draw(buttons,screen)
        buttons_draw(images,screen)
        
        for img in images:
            if img.pressed:
                jeu.selected = "choix_joueur2"
                jeu.joueur1 = str(img.text)
        
        if retour.pressed:
            jeu.selected = "multi_lvl"
            
        pygame.display.update()
        clock.tick(60)
        
def Choix_joueur2(jeu):
    pygame.init()

    buttons = []
    images = []
    
    Titre = Button('Joueur 2 : choisi ton combattant',350,30,(75,25),5,buttons,screen)
    
    retour = Button('Retour',200,30,(50,400),5,buttons,screen)
    for key in jeu.unlock_perso2:
        #globals()['%s' % key] = 
        Image_select(str(key),jeu.unlock_perso2[key],5,images)
        

    a = 0
    frame_count = 0
    
    lvl = level("centre_com")
    
    gameExit = False

    while not gameExit and jeu.selected == "choix_joueur2":
        if frame_count <= 100:
            frame_count += 1
        else:
            frame_count = 0
            
        if frame_count <= 25:
            a=0
        elif 25 < frame_count <= 50:
            a=1
        elif 50 < frame_count <= 75:
            a=2
        elif 75 < frame_count <= 100 :
            a=3

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
    
        decors = lvl.anim_level[a]
        screen.blit(decors,(0,0))
        buttons_draw(buttons,screen)
        buttons_draw(images,screen)
        
        for img in images:
            if img.pressed:
                jeu.selected = "multi"
                jeu.joueur2 = str(img.text)
        
        if retour.pressed:
            jeu.selected = "choix_joueur1"
            
        pygame.display.update()
        clock.tick(60)
        
def update_vol_menu(jeu):
    liste_slider = []
    pygame.mixer.music.set_volume(jeu.vol_music_menu)
    vol_music_menu = Slider(250, 50, (125,100), 5, liste_slider,jeu.vol_music_menu)

def update_vol_fight(jeu):
    liste_slider = []
    vol_music_jeu = Slider(250, 50, (125,100), 5, liste_slider,jeu.vol_music_fight)

        
def Options(jeu):
    pygame.init()

    buttons = []
    liste_slider = []
    textes = []

    Titre = Affiche_texte('Options',350,30,(75,25),5,textes,screen)
    
    retour = Button('Retour',200,30,(30,450),5,buttons,screen)
    save = Button("Sauvegarder",200,30,(270,450),5,buttons,screen)
    
    vol_music_menu = Slider(180, 50, (300,100), 5, liste_slider,jeu.vol_music_menu)
    vol_music_jeu = Slider(180, 50, (300,175), 5, liste_slider,jeu.vol_music_fight)

    vol_menu = Affiche_texte('Volume musique menu',275,30,(20,110),5,textes,screen)
    vol_fight = Affiche_texte('Volume musique jeu',275,30,(20,185),5,textes,screen)

    saisie_1 = Affiche_texte('',30,30,(20,250),5,textes,screen,saisie = True)
    
    a = 0
    frame_count = 0
    
    lvl = level("centre_com")
    
    gameExit = False

    while not gameExit and jeu.selected == "options":
        if frame_count <= 100:
            frame_count += 1
        else:
            frame_count = 0
            
        if frame_count <= 25:
            a=0
        elif 25 < frame_count <= 50:
            a=1
        elif 50 < frame_count <= 75:
            a=2
        elif 75 < frame_count <= 100 :
            a=3

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
 
            if event.type == pygame.KEYDOWN :
            
                if event.key == pygame.K_RETURN and saisie_1.active :
                    saisie_1.click += 1 

# pygame.key.key_code("return") == pygame.K_RETURN
        decors = lvl.anim_level[a]
        screen.blit(decors,(0,0))
        buttons_draw(buttons,screen)
        buttons_draw(liste_slider,screen)
        buttons_draw(textes,screen)
        
        if vol_music_menu.pressed:
            jeu.vol_music_menu = vol_music_menu.val_curseur
            update_vol_menu(jeu)

        if vol_music_jeu.pressed:
            jeu.vol_music_fight = vol_music_jeu.val_curseur
            update_vol_fight(jeu)
                
        if retour.pressed:
            jeu.selected = "none"
            
        if save.pressed:
            jeu.selected = "none"
            options_save = jeu.iter_objects()
            with open('saves/options_jeu.pkl', 'wb') as f:
                pickle.dump(options_save, f, pickle.HIGHEST_PROTOCOL)
        
        print(pygame.key.key_code(str(saisie_1.text)),saisie_1.text)
        pygame.display.update()
        clock.tick(60)
        
    
def load(jeu):
    with open('saves/options_jeu.pkl', 'rb') as f:
        options_jeu_load = pickle.load(f)
    for key,value in options_jeu_load.items():
        setattr(jeu,key,value)
        
    return(jeu)

            

            
