# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 12:13:44 2022

@author: basti
"""

from classes import *
from settings import *
from fonctions import *
import pygame

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
    retour = Button('Retour au menu',200,30,(275,450),5,buttons,screen)
    restart = Button('Recommencer',200,30,(25,450),5,buttons,screen)
    
    gameExit=False
    
    a = 0
    b = 0
    frame_count_1 = 0
    frame_count_2 = 0
    
    p1 = joueur(str(jeu.joueur1), 1, lenivo)
    p2 = joueur(str(jeu.joueur2),2,lenivo)
    perso1 = p1.fr[0]
    perso2 = p2.fl[0]
    
    perso1_rect = perso1.get_rect()
    perso2_rect = perso2.get_rect()
    
    lvl = level(lenivo)
    
    liste_p = [p1,p2]
    
    clock = pygame.time.Clock()
    
    while not gameExit and jeu.selected == "multi" :
        
        if p1.vie > 0 and p2.vie > 0:
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
            screen.blit(lieu , (225,25))
        
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
                
            for event in evenement.get():
                if event.type == pygame.QUIT:
                    gameExit = True                
                
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
            screen.blit(lieu , (225,25))  
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
                
            for event in evenement.get():
                if event.type == pygame.QUIT:
                    gameExit = True                
                
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
            screen.blit(lieu , (225,25))  
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
            Multi(jeu)
        
        if retour.pressed:
            jeu.selected = "none"
        
        pygame.display.update()
        
        clock.tick(100)
        


