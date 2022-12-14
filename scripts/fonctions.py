# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 12:27:29 2022

@author: basti
"""
import pygame
from settings import *
from classes import *
import pickle
import os
import time

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
        
def zone_dialogue(screen,texte_zone,liste_phrases):
    
    pygame.font.init()
 
    myfont = pygame.font.SysFont('corbel', 19, bold=True)
    
    textsurface = myfont.render(texte_zone, False, (110, 110, 110))
    screen.blit(fond_text,(260,380))
    screen.blit(textsurface,(280,385))

    j = 405
    for phrases in liste_phrases :
        
        textsurface2 = myfont.render(phrases, False, (110, 110, 110))
        screen.blit(textsurface2,(270,j))

        j += 15    
            
def pause(screen,buttons_pause):

    buttons_draw(buttons_pause,screen)

def accueil(jeu):
    pygame.init()

    buttons = []

    solo = Button('Solo',200,100,(250,50),5,buttons,screen)    
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
            if event.type == pygame.JOYDEVICEADDED:
                joystick = pygame.joystick.Joystick(0)
    
                joystick.init()
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
    
                jeu.joystick = True
                jeu.manette = joystick
            
            if event.type == pygame.JOYDEVICEREMOVED:
                joystick.quit()
                del joysticks[event.instance_id]
                
                jeu.joystick = False

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
    
        decors = lvl.anim_level[a]
        screen.blit(decors,(0,0))
        buttons_draw(buttons,screen)
        
        if solo.pressed:
            jeu.mode_solo = True
            jeu.selected = "multi_lvl"
            select_boom.play()
            time.sleep(0.1)   
        if multijoueur.pressed:
            jeu.mode_solo = False
            jeu.selected = "multi_lvl"
            select_boom.play()
            time.sleep(0.1)
        if quitter.pressed:
            pygame.quit()
            time.sleep(0.1)
        if options.pressed :
            select_boom.play()
            jeu.selected = "options"
            time.sleep(0.1)
            
        if hist.pressed : 
            select_boom.play()
            jeu.selected = "accueil_histoire"
            time.sleep(0.1)
            
        pygame.display.update()
        clock.tick(60)

def Choix_level(jeu,story):
    pygame.init()

    buttons = []
    images = []
    
    retour = Button('Retour',200,30,(50,400),5,buttons,screen)
    for key in story.unlock_nivo:
        #globals()['%s' % key] = 
        Image_select(str(key),story.unlock_nivo[key],5,images)

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
            if event.type == pygame.JOYDEVICEADDED:
                joystick = pygame.joystick.Joystick(0)
    
                joystick.init()
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
    
                jeu.joystick = True
                jeu.manette = joystick
                
            if event.type == pygame.JOYDEVICEREMOVED:
                joystick.quit()
                del joysticks[event.instance_id]
                
                jeu.joystick = False
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
    
        decors = lvl.anim_level[a]
        screen.blit(decors,(0,0))
        buttons_draw(buttons,screen)
        buttons_draw(images,screen)
        
        for img in images:
            if img.pressed:
                select_boom.play()
                jeu.selected = "choix_joueur1"
                jeu.nivo = img.text
                time.sleep(0.1)
        
        if retour.pressed:
            select_boom.play()
            jeu.selected = "none"
            time.sleep(0.1)
            
        pygame.display.update()
        clock.tick(60)
        
        
def Choix_joueur1(jeu,story):
    pygame.init()

    buttons = []
    images = []
    
    Titre = Button('Joueur 1 : choisi ton combattant',350,30,(75,25),5,buttons,screen)
    retour = Button('Retour',200,30,(50,400),5,buttons,screen)
    for key in story.unlock_perso:
        #globals()['%s' % key] = 
        Image_select(str(key),story.unlock_perso[key],5,images)        

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
            if event.type == pygame.JOYDEVICEADDED:
                joystick = pygame.joystick.Joystick(0)
    
                joystick.init()
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
    
                jeu.joystick = True
                jeu.manette = joystick
                
            if event.type == pygame.JOYDEVICEREMOVED:
                joystick.quit()
                del joysticks[event.instance_id]
                
                jeu.joystick = False
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
    
        decors = lvl.anim_level[a]
        screen.blit(decors,(0,0))
        buttons_draw(buttons,screen)
        buttons_draw(images,screen)
        
        for img in images:
            if img.pressed:
                a = select_sounds[str(img.text)]
                a.set_volume(jeu.vol_fx)
                a.play()
                jeu.selected = "choix_joueur2"
                jeu.joueur1 = str(img.text)
                time.sleep(0.1)
        
        if retour.pressed:
            jeu.selected = "multi_lvl"
            time.sleep(0.1)
            
        pygame.display.update()
        clock.tick(60)
        
def Choix_joueur2(jeu,story):
    pygame.init()

    buttons = []
    images = []
    
    Titre = Button('Joueur 2 : choisi ton combattant',350,30,(75,25),5,buttons,screen)
    
    retour = Button('Retour',200,30,(50,400),5,buttons,screen)
    for key in story.unlock_perso2:
        #globals()['%s' % key] = 
        Image_select(str(key),story.unlock_perso2[key],5,images)
        

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
            if event.type == pygame.JOYDEVICEADDED:
                joystick = pygame.joystick.Joystick(0)
    
                joystick.init()
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
    
                jeu.joystick = True
                jeu.manette = joystick
                
            if event.type == pygame.JOYDEVICEREMOVED:
                joystick.quit()
                del joysticks[event.instance_id]
                
                jeu.joystick = False
                
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
    
        decors = lvl.anim_level[a]
        screen.blit(decors,(0,0))
        buttons_draw(buttons,screen)
        buttons_draw(images,screen)
        
        for img in images:
            if img.pressed and jeu.mode_solo:
                a = select_sounds[str(img.text)]
                a.set_volume(jeu.vol_fx)
                a.play()
                jeu.selected = "solo"
                jeu.joueur2 = str(img.text)
                time.sleep(0.1)
            elif img.pressed and not jeu.mode_solo:
                a = select_sounds[str(img.text)]
                a.set_volume(jeu.vol_fx)
                a.play()
                jeu.selected = "multi"
                jeu.joueur2 = str(img.text)
                time.sleep(0.1)
        
        if retour.pressed:
            jeu.selected = "choix_joueur1"
            time.sleep(0.1)
            
        pygame.display.update()
        clock.tick(60)
        
def update_vol_menu(jeu):
    liste_slider = []
    pygame.mixer.music.set_volume(jeu.vol_music_menu)
    vol_music_menu = Slider(250, 50, (125,100), 5, liste_slider,jeu.vol_music_menu)

def update_vol_fight(jeu):
    liste_slider = []
    vol_music_jeu = Slider(250, 50, (125,100), 5, liste_slider,jeu.vol_music_fight)

def update_vol_fx(jeu):
    liste_slider = []
    vol_fx_jeu = Slider(250, 50, (125,100), 5, liste_slider,jeu.vol_fx)
        
def Options(jeu):
    pygame.init()

    buttons = []
    liste_slider = []
    textes = []
    saisie_j1 = []
    saisie_j2 = []
    
    Titre = Affiche_texte('Options',350,30,(75,25),5,textes,screen,"Titre")
    
    reinit = Button('Reinitialiser',200,15,(150,65),5,buttons,screen)
    
    joueur1 = Button("Joueur 1",200,20,(30,325),5,buttons,screen)
    joueur2 = Button('Joueur 2',200,20,(270,325),5,buttons,screen)
    
    retour = Button('Retour',200,30,(30,450),5,buttons,screen)
    save = Button("Sauvegarder",200,30,(270,450),5,buttons,screen)
    
    vol_music_menu = Slider(180, 50, (300,100), 5, liste_slider,jeu.vol_music_menu)
    vol_music_jeu = Slider(180, 50, (300,175), 5, liste_slider,jeu.vol_music_fight)
    vol_fx_jeu = Slider(180, 50, (300,250), 5, liste_slider,jeu.vol_fx)

    vol_menu = Affiche_texte('Volume musique menu',275,30,(20,110),5,textes,screen)
    vol_fight = Affiche_texte('Volume musique jeu',275,30,(20,185),5,textes,screen)
    vol_fx = Affiche_texte('Volume des effets',275,30,(20,260),5,textes,screen)

    touche1 = Affiche_texte("Coup 1",100,20,(30,355),5,textes,screen)
    touche2 = Affiche_texte("Coup 2",100,20,(270,355),5,textes,screen)
    touche3 = Affiche_texte("Gauche",100,20,(30,385),5,textes,screen)
    touche4 = Affiche_texte("Droite",100,20,(270,385),5,textes,screen)
    touche5 = Affiche_texte("Retomber",100,20,(30,415),5,textes,screen)
    touche6 = Affiche_texte("Sauter",100,20,(270,415),5,textes,screen)


    saisie_1 = Affiche_texte(str(jeu.touche_j1_1_text),75,20,(155,355),5,saisie_j1,screen,"saisie_1",saisie = True)
    saisie_2 = Affiche_texte(str(jeu.touche_j1_2_text),75,20,(400,355),5,saisie_j1,screen,"saisie_2",saisie = True)
    saisie_l = Affiche_texte(str(jeu.touche_j1_L_text),75,20,(155,385),5,saisie_j1,screen,"saisie_l",saisie = True)
    saisie_r = Affiche_texte(str(jeu.touche_j1_R_text),75,20,(400,385),5,saisie_j1,screen,"saisie_r",saisie = True)
    saisie_d = Affiche_texte(str(jeu.touche_j1_D_text),75,20,(155,415),5,saisie_j1,screen,"saisie_d",saisie = True)
    saisie_u = Affiche_texte(str(jeu.touche_j1_U_text),75,20,(400,415),5,saisie_j1,screen,"saisie_u",saisie = True)


    saisie_1_2 = Affiche_texte(str(jeu.touche_j2_1_text),75,20,(155,355),5,saisie_j2,screen,"saisie_1_2",saisie = True)
    saisie_2_2 = Affiche_texte(str(jeu.touche_j2_2_text),75,20,(400,355),5,saisie_j2,screen,"saisie_2_2",saisie = True)
    saisie_l_2 = Affiche_texte(str(jeu.touche_j2_L_text),75,20,(155,385),5,saisie_j2,screen,"saisie_l_2",saisie = True)
    saisie_r_2 = Affiche_texte(str(jeu.touche_j2_R_text),75,20,(400,385),5,saisie_j2,screen,"saisie_r_2",saisie = True)
    saisie_d_2 = Affiche_texte(str(jeu.touche_j2_D_text),75,20,(155,415),5,saisie_j2,screen,"saisie_d_2",saisie = True)
    saisie_u_2 = Affiche_texte(str(jeu.touche_j2_U_text),75,20,(400,415),5,saisie_j2,screen,"saisie_u_2",saisie = True)
        
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
            
                if event.key == pygame.K_RETURN :
                    select_boom.play()

                    for s in saisie_j1:
                        if s.active:
                            s.click += 1
                            jeu.update_touches(s.name,s)
                            
        if reinit.pressed:
            if os.path.exists("saves/options_jeu.pkl."):
                os.remove("saves/options_jeu.pkl.")
            jeu.reinitialise_options()
            retour = Button('Retour',200,30,(30,450),5,buttons,screen)
            save = Button("Sauvegarder",200,30,(270,450),5,buttons,screen)
            
            vol_music_menu = Slider(180, 50, (300,100), 5, liste_slider,jeu.vol_music_menu)
            vol_music_jeu = Slider(180, 50, (300,175), 5, liste_slider,jeu.vol_music_fight)
            vol_fx_jeu = Slider(180, 50, (300,250), 5, liste_slider,jeu.vol_fx)
        
            vol_menu = Affiche_texte('Volume musique menu',275,30,(20,110),5,textes,screen)
            vol_fight = Affiche_texte('Volume musique jeu',275,30,(20,185),5,textes,screen)
            vol_fx = Affiche_texte('Volume des effets',275,30,(20,260),5,textes,screen)
        
            saisie_1 = Affiche_texte(str(jeu.touche_j1_1_text),80,30,(350,350),5,textes,screen,saisie = True)
            saisie_2 = Affiche_texte(str(jeu.touche_j1_2_text),75,20,(400,355),5,saisie_j1,screen,"saisie_2",saisie = True)
            saisie_l = Affiche_texte(str(jeu.touche_j1_L_text),75,20,(155,385),5,saisie_j1,screen,"saisie_l",saisie = True)
            saisie_r = Affiche_texte(str(jeu.touche_j1_R_text),75,20,(400,385),5,saisie_j1,screen,"saisie_r",saisie = True)
            saisie_d = Affiche_texte(str(jeu.touche_j1_D_text),75,20,(155,415),5,saisie_j1,screen,"saisie_d",saisie = True)
            saisie_u = Affiche_texte(str(jeu.touche_j1_U_text),75,20,(400,415),5,saisie_j1,screen,"saisie_u",saisie = True)
        
        
            saisie_1_2 = Affiche_texte(str(jeu.touche_j2_1_text),75,20,(155,355),5,saisie_j2,screen,"saisie_1_2",saisie = True)
            saisie_2_2 = Affiche_texte(str(jeu.touche_j2_2_text),75,20,(400,355),5,saisie_j2,screen,"saisie_2_2",saisie = True)
            saisie_l_2 = Affiche_texte(str(jeu.touche_j2_L_text),75,20,(155,385),5,saisie_j2,screen,"saisie_l_2",saisie = True)
            saisie_r_2 = Affiche_texte(str(jeu.touche_j2_R_text),75,20,(400,385),5,saisie_j2,screen,"saisie_r_2",saisie = True)
            saisie_d_2 = Affiche_texte(str(jeu.touche_j2_D_text),75,20,(155,415),5,saisie_j2,screen,"saisie_d_2",saisie = True)
            saisie_u_2 = Affiche_texte(str(jeu.touche_j2_U_text),75,20,(400,415),5,saisie_j2,screen,"saisie_u_2",saisie = True)
            time.sleep(0.1)
                            
        decors = lvl.anim_level[a]
        screen.blit(decors,(0,0))
        buttons_draw(buttons,screen)
        buttons_draw(liste_slider,screen)
        buttons_draw(textes,screen)

        if joueur2.pressed:
            joueur1.pressed = False
            buttons_draw(saisie_j2,screen)
        
        elif joueur1.pressed:
            buttons_draw(saisie_j1,screen)
            joueur2.pressed = False       
        
        if vol_music_menu.pressed:
            jeu.vol_music_menu = vol_music_menu.val_curseur
            update_vol_menu(jeu)

        if vol_music_jeu.pressed:
            jeu.vol_music_fight = vol_music_jeu.val_curseur
            update_vol_fight(jeu)
            
        if vol_fx_jeu.pressed:
            jeu.vol_fx = vol_fx_jeu.val_curseur
            update_vol_fx(jeu)
                
        if retour.pressed:
            select_boom.play()
            jeu.selected = "none"
            time.sleep(0.1)
            
        if save.pressed:
            jeu.selected = "none"
            options_save = jeu.iter_objects()
            with open('saves/options_jeu.pkl', 'wb') as f:
                pickle.dump(options_save, f, pickle.HIGHEST_PROTOCOL)
            time.sleep(0.1)
                    
        pygame.display.update()
        clock.tick(60)
        
def Launch_histoire(jeu,story):
    
    pygame.init()

    buttons = []
    loads = []
    textes = []
    images = []
    perso = 0
    
    Titre = Affiche_texte('Mode histoire',350,30,(75,25),5,textes,screen,"Titre")
    
    new = Button('Nouvelle partie',250,50,(25,200),5,buttons,screen)      
    retour = Button('Retour',200,30,(30,450),5,buttons,screen)
    arrow_l = Button('<',30,30,(290,300),5,buttons,screen)
    arrow_r = Button('>',30,30,(470,300),5,buttons,screen)
    load = Button('Continuer une partie',250,50,(25,300),5,loads,screen)      

    a = 0
    frame_count = 0
    
    lvl = level("centre_com")
    
    gameExit = False

    while not gameExit and jeu.selected == "accueil_histoire":
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
            
            if event.type == pygame.JOYDEVICEADDED:
                joystick = pygame.joystick.Joystick(0)
    
                joystick.init()
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
    
                jeu.joystick = True
                jeu.manette = joystick
                
            if event.type == pygame.JOYDEVICEREMOVED:
                joystick.quit()
                del joysticks[event.instance_id]
                
                jeu.joystick = False
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                
        decors = lvl.anim_level[a]
        screen.blit(decors,(0,0))
        buttons_draw(buttons,screen)
        buttons_draw(textes,screen)
        
        screen.blit(mega_story_perso[perso], mega_rect[perso])
        
        if arrow_r.pressed and perso < 1:
            perso += 1
        elif arrow_r.pressed and perso >= 1:
            perso = 1

        if arrow_l.pressed and perso > 0:
            perso -= 1
        elif arrow_r.pressed and perso <= 0:
            perso = 0
                
        if new.pressed:
            select_boom.play()

            if os.path.exists("saves/histoire.pkl."):
                os.remove("saves/histoire.pkl.")
            
            story.stage = 0
            story_save = story.iter_objects()
            if perso == 0:
                story.selected_perso = "justi"
            elif perso == 1:
                story.selected_perso = "basti"
                
            with open('saves/histoire.pkl', 'wb') as f:
                pickle.dump(story_save, f, pickle.HIGHEST_PROTOCOL)
                
            jeu.selected = "histoire"
            time.sleep(0.1)
                                
        if retour.pressed:
            select_boom.play()
            jeu.selected = "none"
            time.sleep(0.1)
            
        if os.path.exists("saves/histoire.pkl."): 
            buttons_draw(loads, screen)
            if load.pressed:
                select_boom.play()
                story = load_story(jeu)
                jeu.selected = "histoire"
                time.sleep(0.1)
                
            
        pygame.display.update()
        clock.tick(60)   
        
        
    
        
    
def load(jeu):
    with open('saves/options_jeu.pkl', 'rb') as f:
        options_jeu_load = pickle.load(f)
    for key,value in options_jeu_load.items():
        setattr(jeu,key,value)
        
    return(jeu)

def load_story(story):
    with open('saves/histoire.pkl', 'rb') as f:
        histoire_load = pickle.load(f)
    for key,value in histoire_load.items():
        setattr(story,key,value)
        
    return(story)            

            
