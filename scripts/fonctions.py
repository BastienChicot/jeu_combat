# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 12:27:29 2022

@author: basti
"""
import pygame
from settings import *
from classes import *

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
            
def pause(screen,gameExit,Gus,sac,tr):
    keys=pygame.key.get_pressed()
    
    screen.blit(poze, (50 , 150))
    
    if keys[pygame.K_s]:
        other_s.play()
        gus_save = Gus.iter_objects()
        sac_save = sac.iter_objects()
        trigger_save = tr.iter_objects()
        with open('Story/saves/Gus.pkl', 'wb') as f:
            pickle.dump(gus_save, f, pickle.HIGHEST_PROTOCOL)
        with open('Story/saves/Sac.pkl', 'wb') as fi:
            pickle.dump(sac_save, fi, pickle.HIGHEST_PROTOCOL)       
        with open('Story/saves/Trigger.pkl', 'wb') as tr:
            pickle.dump(trigger_save, tr, pickle.HIGHEST_PROTOCOL)
            
        pygame.font.init()
 
        myfont = pygame.font.SysFont('corbel', 25, bold=True)
        
        textsurface = myfont.render("Partie sauvegardée", False, (0, 0, 0))
        screen.blit(textsurface,(135,350))

    if keys[pygame.K_q]: 
        other_s.play()
        pygame.quit()
        
def load(Gus,sac,tr):
    with open('Story/saves/Gus.pkl', 'rb') as f:
        gus_load = pickle.load(f)
    for key,value in gus_load.items():
        setattr(Gus,key,value)
    
    with open('Story/saves/Sac.pkl', 'rb') as fi:
        sac_load = pickle.load(fi)    
    for key,value in sac_load.items():
        setattr(sac,key,value)
        
    with open('Story/saves/Trigger.pkl', 'rb') as trig:
        trigger_load = pickle.load(trig)    
    for key,value in trigger_load.items():
        setattr(tr,key,value)
        
    return(Gus,sac,tr)

def accueil(jeu):
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    pygame.display.set_caption('Justi FIGHT')
    clock = pygame.time.Clock()
    gui_font = pygame.font.Font(None,30)
    
    buttons = []
    
    button1 = Button('Multijoueur',200,50,(100,50),5,buttons,screen)
    button2 = Button('Histoire',200,50,(100,200),5,buttons,screen)
    button3 = Button('Options',200,50,(100,350),5,buttons,screen)    
    
    a = 0
    frame_count = 0
    
    lvl = level("centre_com")
    
    gameExit = False

    while not gameExit and jeu.page == "accueil":
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
                sys.exit()
    
        decors = lvl.anim_level[a]
        screen.blit(decors,(0,0))
        buttons_draw(buttons,screen)
    
        pygame.display.update()
        clock.tick(60)

