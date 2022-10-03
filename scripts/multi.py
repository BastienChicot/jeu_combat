# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 12:13:44 2022

@author: basti
"""

from classes import *
from settings import *
from fonctions import *
import pygame, sys

pygame.init()
# pygame.font.init()
# pygame.mixer.init()

# myfont = pygame.font.SysFont('corbel', 20, bold=True)
# Gus_font = pygame.font.SysFont('corbel', 16, bold=True)
# big_font = pygame.font.SysFont('corbel', 40, bold=True)

# screen = pygame.display.set_mode((display_width,display_height))
# pygame.display.set_caption("Justi fight")

def Multi(jeu):
    pygame.init()
    lenivo = jeu.nivo
    
    buttons=[]
    liste_slider = []
    textes = []
    
    retour = Button('Retour au menu',200,30,(275,450),5,buttons,screen)
    restart = Button('Recommencer',200,30,(25,450),5,buttons,screen)
    
    buttons_pause = []
    retour2 = Button('Retour au menu',200,30,(150,400),5,buttons_pause,screen)
    quitter = Button('Quitter le jeu',200,30,(150,450),5,buttons_pause,screen)
    
    vol_music_jeu = Slider(180, 50, (300,225), 5, liste_slider,jeu.vol_music_fight)
    vol_fx_jeu = Slider(180, 50, (300,300), 5, liste_slider,jeu.vol_fx)


    vol_fight = Affiche_texte('Volume musique jeu',275,30,(20,225),5,textes,screen)
    vol_fx = Affiche_texte('Volume des effets',275,30,(20,300),5,textes,screen)

    gameExit=False
    
    a = 0
    b = 0
    frame_count_1 = 0
    frame_count_2 = 0
    seconds = 0
    
    compteur = big_font.render("5", False, (255, 20, 20))
    compteur_fond = big_font.render("5", False, (0, 0, 0))
    
    p1 = joueur(str(jeu.joueur1), 1, lenivo,jeu)
    p2 = joueur(str(jeu.joueur2),2,lenivo,jeu)
    perso1 = p1.fr[0]
    perso2 = p2.fl[0]
    
    perso1_rect = perso1.get_rect()
    perso2_rect = perso2.get_rect()
    
    lvl = level(lenivo)
    
    liste_p = [p1,p2]
    
    start_ticks=pygame.time.get_ticks()
    
    clock = pygame.time.Clock()
    
    while not gameExit and jeu.selected == "multi" :
        
        pygame.mixer.music.set_volume(jeu.vol_music_fight)
        
        pause_text = big_font.render("PAUSE", False, (255, 20, 20))
        pause_fond = big_font.render("PAUSE", False, (0, 0, 0))
        
        if (jeu.pause%2) != 1:
            seconds=(pygame.time.get_ticks()-start_ticks)/1000
            countdown = int(185 - seconds)
        
        if seconds < 185 and p1.vie > 0 and p2.vie > 0:
            
            if seconds <= 5 and (jeu.pause%2) != 1:
                start = int(5 - seconds)
                compteur = big_font.render(str(start), False, (255, 20, 20))
                compteur_fond = big_font.render(str(start), False, (0, 0, 0))
            elif 5 < seconds <185 and (jeu.pause%2) != 1:
                countdown = int(185 - seconds)
                compteur = big_font.render(str(countdown), False, (255, 20, 20))
                compteur_fond = big_font.render(str(countdown), False, (0, 0, 0))
                
            if frame_count_1 <= 100:
                frame_count_1 += 1
            else:
                frame_count_1 = 0
                p1.animation = False
                p1.type_anim = "none"

            if frame_count_2 <= 100:
                frame_count_2 += 1
            else:
                frame_count_2 = 0
                p2.animation = False
                p2.type_anim = "none"
                
            if frame_count_1 <= 25:
                a=0
            elif 25 < frame_count_1 <= 50:
                a=1
            elif 50 < frame_count_1 <= 75:
                a=2
            elif 75 < frame_count_1 <= 100 :
                a=3

            if frame_count_2 <= 25:
                b=0
            elif 25 < frame_count_2 <= 50:
                b=1
            elif 50 < frame_count_2 <= 75:
                b=2
            elif 75 < frame_count_2 <= 100 :
                b=3
            
            evenement = pygame.event
            
            for event in evenement.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    sys.exit(0)
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        jeu.pause += 1 
            
                if seconds > 5 :
                    if (jeu.pause%2) != 1:
                        p1.move_x,p1.move_y = p1.move(event)
                        p2.move_x,p2.move_y = p2.move(event)
            
            perso1 = p1.maj_anim(a)
            perso2 = p2.maj_anim(b)
                    
            for p in liste_p:
                if (p.y < p.limite and not p.interact) or p.jump :#and not rect_gugus.colliderect(fightrect)) 
                    
                    p.air_time += 1
         
                if p.jump : 
                    p.move_y = -(p.detente/p.air_time)
                    
                if p.y < p.limite and p.air_time > p.detente:
                    p.move_y = 3
                elif p.y < p.limite and p.fall :
                    p.move_y = 5
                elif p.y >= p.limite and not p.jump:
                    p.move_y = 0
                    p.y = p.limite
                    p.jump = False
                    p.air_time = 1
                
            p1.move_y,p1.move_x =p1.collision_joueur(perso1_rect,perso2_rect,p2)
            p2.move_y,p2.move_x =p2.collision_joueur(perso2_rect,perso1_rect,p1)
            
            p2 = p1.damage(perso1_rect,perso2_rect,p2)
            p1 = p2.damage(perso2_rect,perso1_rect,p1)
                
            frame_count_1 = p1.punch_anim(frame_count_1)
            frame_count_2 = p2.punch_anim(frame_count_2)
                       
            p1.x += p1.move_x
            p1.y += p1.move_y  

            p2.x += p2.move_x
            p2.y += p2.move_y  
    
            if p1.x > 450 :
                p1.x=450
            if p1.x < 0:
                p1.x = 0

            if p2.x > 450 :
                p2.x=450
            if p2.x < 0:
                p2.x = 0
            
            screen.fill((0,0,0))
            
            perso1_rect.topleft = (p1.x,p1.y)       
            perso2_rect.topleft = (p2.x,p2.y)       
            
            decors = lvl.anim_level[a]
            screen.blit(decors,(0,0))

            screen.blit(perso1,perso1_rect)
            screen.blit(perso2,perso2_rect)
            
            clean_bar_1 = power_bar[p1.clean_hit]
            clean_bar_2 = power_bar[p2.clean_hit]

            screen.blit(clean_bar_1,(20,60))
            screen.blit(clean_bar_2,(390,60))
            
            pv = Gus_font.render("Santé : " + str(int(p1.vie)), False, (220, 220, 220))
            super_punch = Gus_font.render("Super power : ", False, (220, 220, 220))
            lieu = Gus_font.render("Niveau : "+str(lenivo), False, (220, 220, 220))
            
            pv2 = Gus_font.render("Santé : " + str(int(p2.vie)), False, (220, 220, 220))
            super_punch2 = Gus_font.render("Super power : ", False, (220, 220, 220))
            
            screen.blit(pv , (20,25))
            screen.blit(super_punch,(20,40))
            screen.blit(pv2 , (390,25))
            screen.blit(super_punch2,(390,40))
            screen.blit(lieu , (210,5))
            screen.blit(compteur_fond,(207,23))
            screen.blit(compteur,(210,20))
            

            if (jeu.pause%2) == 1:
                buttons_draw(buttons_pause,screen)                
                buttons_draw(liste_slider,screen) 
                buttons_draw(textes,screen) 
                screen.blit(pause_fond,(157,153))
                screen.blit(pause_text,(160,150))

                if vol_music_jeu.pressed:
                    jeu.vol_music_fight = vol_music_jeu.val_curseur
                    update_vol_fight(jeu)
                    
                if vol_fx_jeu.pressed:
                    jeu.vol_fx = vol_fx_jeu.val_curseur
                    update_vol_fx(jeu)
                
        elif seconds >= 180 and p1.vie > 0 and p2.vie > 0:
            if frame_count_1 <= 100:
                frame_count_1 += 1
            else:
                frame_count_1 = 0
                p1.animation = False
                p1.type_anim = "none"

            if frame_count_2 <= 100:
                frame_count_2 += 1
            else:
                frame_count_2 = 0
                p2.animation = False
                p2.type_anim = "none"
                
            if frame_count_1 <= 25:
                a=0
            elif 25 < frame_count_1 <= 50:
                a=1
            elif 50 < frame_count_1 <= 75:
                a=2
            elif 75 < frame_count_1 <= 100 :
                a=3

            if frame_count_2 <= 25:
                b=0
            elif 25 < frame_count_2 <= 50:
                b=1
            elif 50 < frame_count_2 <= 75:
                b=2
            elif 75 < frame_count_2 <= 100 :
                b=3
            
            evenement = pygame.event
            
            for event in evenement.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    sys.exit(0)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        jeu.pause += 1 
                        
            perso1 = p1.maj_anim(a)
            perso2 = p2.maj_anim(b)
                    
            for p in liste_p:
                if (p.y < p.limite and not p.interact) or p.jump :#and not rect_gugus.colliderect(fightrect)) 
                    
                    p.air_time += 1
         
                if p.jump : 
                    p.move_y = -(p.detente/p.air_time)
                    
                if p.y < p.limite and p.air_time > p.detente:
                    p.move_y = 3
                elif p.y < p.limite and p.fall :
                    p.move_y = 5
                elif p.y >= p.limite and not p.jump:
                    p.move_y = 0
                    p.y = p.limite
                    p.jump = False
                    p.air_time = 1
                
            p1.move_y,p1.move_x =p1.collision_joueur(perso1_rect,perso2_rect,p2)
            p2.move_y,p2.move_x =p2.collision_joueur(perso2_rect,perso1_rect,p1)
            
            p2 = p1.damage(perso1_rect,perso2_rect,p2)
            p1 = p2.damage(perso2_rect,perso1_rect,p1)
                
            frame_count_1 = p1.punch_anim(frame_count_1)
            frame_count_2 = p2.punch_anim(frame_count_2)
                                   
            screen.fill((0,0,0))
            
            perso1_rect.topleft = (p1.x,p1.y)       
            perso2_rect.topleft = (p2.x,p2.y)       
            
            decors = lvl.anim_level[a]
            screen.blit(decors,(0,0))

            screen.blit(perso1,perso1_rect)
            screen.blit(perso2,perso2_rect)
            
            clean_bar_1 = power_bar[p1.clean_hit]
            clean_bar_2 = power_bar[p2.clean_hit]

            screen.blit(clean_bar_1,(20,60))
            screen.blit(clean_bar_2,(390,60))
            
            pv = Gus_font.render("Santé : " + str(int(p1.vie)), False, (220, 220, 220))
            super_punch = Gus_font.render("Super power : ", False, (220, 220, 220))
            lieu = Gus_font.render("Niveau : "+str(lenivo), False, (220, 220, 220))
            
            pv2 = Gus_font.render("Santé : " + str(int(p2.vie)), False, (220, 220, 220))
            super_punch2 = Gus_font.render("Super power : ", False, (220, 220, 220))
            
            screen.blit(pv , (20,25))
            screen.blit(super_punch,(20,40))
            screen.blit(pv2 , (390,25))
            screen.blit(super_punch2,(390,40))
            screen.blit(lieu , (210,25))
            buttons_draw(buttons,screen)
            
            if p1.vie >= p2.vie:                
                text_victoire = ("JOUEUR 1 GAGNE")
                text_surf = gui_font.render(text_victoire,True,'#DE0B0B')
                
            else:                
                text_victoire = ("JOUEUR 2 GAGNE")
                text_surf = gui_font.render(text_victoire,True,'#DE0B0B')
                
            screen.blit(text_surf,(150,400))
        
            if (jeu.pause%2) == 1:
                buttons_draw(buttons_pause,screen)
                screen.blit(pause_fond,(157,203))
                screen.blit(pause_text,(160,200))


        elif p1.vie <= 0 and p2.vie > 0:
            p1.start_pos = p1.kor[2].get_rect()
            p1.height = int(p1.start_pos.height)
        
            p1.limite = level_sol[lenivo]-p1.height
                        
            frame_count_1 += 1
            p1.type_anim = "ko"
        
            if frame_count_2 <= 100:
                frame_count_2 += 1
            else:
                frame_count_2 = 0
                p2.animation = False
                p2.type_anim = "none" 
                
            if (p2.y < p2.limite and not p2.interact) or p2.jump :#and not rect_gugus.colliderect(fightrect)) 
                
                p2.air_time += 1
         
            if p2.jump : 
                p2.move_y = -(p2.detente/p2.air_time)
                
            if p2.y < p2.limite and p2.air_time > p2.detente:
                p2.move_y = 3
            elif p2.y < p2.limite and p2.fall :
                p2.move_y = 5
            elif p2.y >= p2.limite and not p2.jump:
                p2.move_y = 0
                p2.y = p.limite
                p2.jump = False
                p2.air_time = 1
                
            p2.y += p2.move_y 
                
            if frame_count_1 <= 25:
                a=0
            elif 25 < frame_count_1 <= 50:
                a=1
            elif 50 < frame_count_1 <= 75:
                a=2
            elif 75 < frame_count_1 :
                a=3
        
            if frame_count_2 <= 25:
                b=0
            elif 25 < frame_count_2 <= 50:
                b=1
            elif 50 < frame_count_2 <= 75:
                b=2
            elif 75 < frame_count_2 <= 100 :
                b=3
            
            evenement = pygame.event
            
            for event in evenement.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    sys.exit(0)
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        jeu.pause += 1 
            
            perso_1 = p1.maj_anim(a)
            perso_2 = p2.maj_anim(b)
            
            screen.fill((0,0,0))
            
            perso1_rect.topleft = (p1.x,p1.limite)       
            perso2_rect.topleft = (p2.x,p2.y)       
            
            decors = lvl.anim_level[a]
            screen.blit(decors,(0,0))
        
            screen.blit(perso_1,perso1_rect)
            screen.blit(perso_2,perso2_rect)
            
            clean_bar_1 = power_bar[0]
            clean_bar_2 = power_bar[0]
        
            screen.blit(clean_bar_1,(20,60))
            screen.blit(clean_bar_2,(390,60))
            
            pv = Gus_font.render("Santé : " + str(int(p1.vie)), False, (220, 220, 220))
            super_punch = Gus_font.render("Super power : ", False, (220, 220, 220))
            lieu = Gus_font.render("Niveau : "+str(lenivo), False, (220, 220, 220))
            
            pv2 = Gus_font.render("Santé : " + str(int(p2.vie)), False, (220, 220, 220))
            super_punch2 = Gus_font.render("Super power : ", False, (220, 220, 220))
            
            screen.blit(pv , (20,25))
            screen.blit(super_punch,(20,40))
            screen.blit(pv2 , (390,25))
            screen.blit(super_punch2,(390,40))
            screen.blit(lieu , (210,25))  
            buttons_draw(buttons,screen)
            
            text_victoire = ("JOUEUR 2 GAGNE")
            text_surf = gui_font.render(text_victoire,True,'#DE0B0B')
            screen.blit(text_surf,(150,400))
            
            anim = ko[b]
            screen.blit(anim,(150,200))
                    
        elif p2.vie <= 0 and p1.vie > 0:
            p2.start_pos = p2.kor[2].get_rect()
            p2.height = int(p2.start_pos.height)
        
            p2.limite = level_sol[lenivo]-p2.height
                        
            frame_count_2 += 1
            p2.type_anim = "ko"
        
            if frame_count_1 <= 100:
                frame_count_1 += 1
            else:
                frame_count_1 = 0
                p1.animation = False
                p1.type_anim = "none" 
                
            if (p1.y < p1.limite and not p1.interact) or p1.jump :#and not rect_gugus.colliderect(fightrect)) 
                
                p1.air_time += 1
         
            if p1.jump : 
                p1.move_y = -(p1.detente/p1.air_time)
                
            if p1.y < p1.limite and p1.air_time > p1.detente:
                p1.move_y = 3
            elif p1.y < p1.limite and p1.fall :
                p1.move_y = 5
            elif p1.y >= p1.limite and not p1.jump:
                p1.move_y = 0
                p1.y = p.limite
                p1.jump = False
                p1.air_time = 1
                
            p1.y += p1.move_y 
                
            if frame_count_2 <= 25:
                b=0
            elif 25 < frame_count_2 <= 50:
                b=1
            elif 50 < frame_count_2 <= 75:
                b=2
            elif 75 < frame_count_2 :
                b=3
        
            if frame_count_1 <= 25:
                a=0
            elif 25 < frame_count_1 <= 50:
                a=1
            elif 50 < frame_count_1 <= 75:
                a=2
            elif 75 < frame_count_1 <= 100 :
                a=3
            
            evenement = pygame.event
            
            for event in evenement.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    sys.exit(0)
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        jeu.pause += 1 
            
            perso_1 = p1.maj_anim(a)
            perso_2 = p2.maj_anim(b)
            
            screen.fill((0,0,0))
            
            perso1_rect.topleft = (p1.x,p1.limite)       
            perso2_rect.topleft = (p2.x,p2.y)       
            
            decors = lvl.anim_level[a]
            screen.blit(decors,(0,0))
        
            screen.blit(perso_1,perso1_rect)
            screen.blit(perso_2,perso2_rect)
            
            clean_bar_1 = power_bar[0]
            clean_bar_2 = power_bar[0]
        
            screen.blit(clean_bar_1,(20,60))
            screen.blit(clean_bar_2,(390,60))
            
            pv = Gus_font.render("Santé : " + str(int(p1.vie)), False, (220, 220, 220))
            super_punch = Gus_font.render("Super power : ", False, (220, 220, 220))
            lieu = Gus_font.render("Niveau : "+str(lenivo), False, (220, 220, 220))
            
            pv2 = Gus_font.render("Santé : " + str(int(p2.vie)), False, (220, 220, 220))
            super_punch2 = Gus_font.render("Super power : ", False, (220, 220, 220))
            
            screen.blit(pv , (20,25))
            screen.blit(super_punch,(20,40))
            screen.blit(pv2 , (390,25))
            screen.blit(super_punch2,(390,40))
            screen.blit(lieu , (210,25))  
            buttons_draw(buttons,screen)
            
            text_victoire = ("JOUEUR 1 GAGNE")
            text_surf = gui_font.render(text_victoire,True,'#DE0B0B')
            screen.blit(text_surf,(150,400))
            
            anim = ko[a]
            screen.blit(anim,(150,200))            
            
        if restart.pressed:
            jeu.selected = "multi"
            p1.vie = 100
            p2.vie = 100
            jeu.pause = 0
            Multi(jeu)
        
        if retour.pressed:
            jeu.selected = "none"
            pygame.mixer.music.set_volume(jeu.vol_music_menu)
            pygame.mixer.music.load ( playlist[0])
            pygame.mixer.music.play(-1) 
            jeu.pause = 0
            
        if retour2.pressed :
            retour.pressed = True

        if quitter.pressed :
            pygame.quit()
            
        pygame.display.update()
        
        clock.tick(100)
        



