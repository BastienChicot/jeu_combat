# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 12:13:44 2022

@author: basti
"""

from classes import *
from settings import *
import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()

myfont = pygame.font.SysFont('corbel', 20, bold=True)
Gus_font = pygame.font.SysFont('corbel', 16, bold=True)
big_font = pygame.font.SysFont('corbel', 40, bold=True)

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Justi fight")

def jeu_fight():
    lenivo = "parc"
    
    gameExit=False
    
    a = 0
    frame_count = 0
    
    p1 = joueur("basti", 1, lenivo)
    perso = p1.fr[0]
    
    lvl = level(lenivo)
    
    clock = pygame.time.Clock()
    
    while not gameExit :
        
        if p1.vie > 0 :
            if frame_count <= 60:
                frame_count += 1
            else:
                frame_count = 0
                p1.animation = False
                p1.type_anim = "none"
            
            if frame_count <= 15:
                a=0
            elif 15 < frame_count <= 30:
                a=1
            elif 30 < frame_count <= 45:
                a=2
            elif 45 < frame_count <= 60 :
                a=3
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                   
                  # Condition becomes true when keyboard is pressed   
                if event.type == pygame.KEYDOWN:
       
                    if event.key == p1.saut :
    
                        p1.jump = True
                        
                    if event.key == p1.descend :
                        p1.fall = True
                        
                    if event.key == p1.gauche :
                        p1.move_x = -2
                        p1.side = False
                        
                    if event.key == p1.droite :
                        p1.move_x = 2
                        p1.side = True
                        
                    if event.key == p1.action :
                        p1.attack = True
                    if event.key == p1.coup :
                        p1.super_attack = True         
                        
                if event.type == pygame.KEYUP:
       
                    if event.key == p1.saut :
                        p1.jump = False
                        
                    if event.key == p1.descend :
                        p1.fall = False
                        
                    if event.key == p1.gauche :
                        p1.move_x = 0
    
                    if event.key == p1.droite :
                        p1.move_x = 0
    
                    if event.key == p1.action :
                        p1.attack = False
                    if event.key == p1.coup :
                        p1.super_attack = False
            
            if p1.side:
                if p1.type_anim == "none":
                    perso=p1.fr[a]
                elif p1.type_anim == "punch":
                    perso = p1.punchr[a]
                elif p1.type_anim == "kick":
                    perso = p1.piedr[a]
                elif p1.type_anim == "super_punch":
                    perso = p1.sper[a]
                elif p1.type_anim =="jump_punch":
                    perso = p1.jumpr[a]
                elif p1.type_anim =="adv_c2c":
                    perso = p1.hitr[a]
                elif p1.type_anim =="adv_sp":
                    perso = p1.hitr[a]
    
            else:
                if p1.type_anim == "none":
                    perso=p1.fl[a]
                elif p1.type_anim == "punch":
                    perso = p1.punchl[a]
                elif p1.type_anim == "kick":
                    perso = p1.piedl[a]
                elif p1.type_anim == "super_punch":
                    perso = p1.spel[a]
                elif p1.type_anim =="jump_punch":
                    perso = p1.jumpl[a]
                elif p1.type_anim =="adv_c2c":
                    perso = p1.hitl[a]
                elif p1.type_anim =="adv_sp":
                    perso = p1.hitl[a]
                    
            if p1.y < p1.limite or p1.jump : #and not rect_gugus.colliderect(fightrect)) 
                
                p1.air_time += 1
     
            if p1.jump : 
                p1.move_y = -(p1.detente/p1.air_time)
                
            if p1.y < p1.limite and p1.air_time > p1.detente:
                p1.move_y = 3
            elif p1.y < p1.limite and p1.fall :
                p1.move_y = 5
            elif p1.y >= p1.limite and not p1.jump:
                p1.move_y = 0
                p1.y = p1.limite
                p1.jump = False
                p1.air_time = 1

            perso_rect = perso.get_rect()
                
            # if rect_gugus.colliderect(fightrect):
            #     if abs(rect_gugus.bottom - fightrect.top) <= 10 and move_y > 0:
            #         move_y = 0
            #         air_time = 1
            #         jump = False
            #     if abs(rect_gugus.top - fightrect.bottom) <= 10 and move_y < 0:
            #         move_y = 0
            #     if abs(rect_gugus.left - fightrect.right) <= 10 and move_x < 0:
            #         move_x = 0             
            #     if abs(rect_gugus.right - fightrect.left) <= 10 and move_x > 0:
            #         move_x = 0
    
    
            # if abs(rect_gugus.right - fightrect.left) <= 80 and move_x > 0 and y2-20 < y < y2+20:
            #     if 50 < x2 < 400:
            #         x2 += move_x/4
            #     elif x2 >= 400 :
            #         x2 -= move_x
            # if abs(rect_gugus.left - fightrect.right) <= 80 and move_x < 0 and y2-20 < y < y2+20:
            #     if 50 < x2 < 400:
            #         x2 += move_x/4
            #     elif x2 <= 50 :
            #         x2 -= move_x
                
            ##COUP SIMPLE AVEC A
            if p1.attack and p1.move_x != 0: # abs(rect_gugus.left - fightrect.right) <= 5 and 
                # fighter_life -=5
                if p1.clean_hit < 5:
                    p1.clean_hit += 1
                # x2 -= 20
                # opp_clean = 0
                p1.animation = True
                p1.type_anim = "punch"
                frame_count = 1
            if p1.attack and p1.move_x != 0: #abs(rect_gugus.right - fightrect.left) <= 5 and 
                # fighter_life -=5
                # x2 += 20
                if p1.clean_hit < 5:
                    p1.clean_hit += 1
                # opp_clean = 0
                p1.animation = True
                p1.type_anim = "punch"
                frame_count = 1
                
            ##COUP COMBO A ET Z
            if p1.attack and p1.move_x != 0 and p1.super_attack: #abs(rect_gugus.left - fightrect.right) <= 5 and 
                # fighter_life -= 10
                if p1.clean_hit < 5:
                    p1.clean_hit += 1
                p1.x += 20
                # opp_clean = 0
                p1.animation = True
                p1.type_anim = "kick"
                frame_count = 1
            if p1.attack and p1.move_x != 0 and p1.super_attack:#abs(rect_gugus.right - fightrect.left) <= 5 and 
                # fighter_life -= 10
                p1.x -= 20
                if p1.clean_hit < 5:
                    p1.clean_hit += 1
                # opp_clean = 0
                p1.animation = True
                p1.type_anim = "kick"
                frame_count = 1
    
            ##SUPER COUP AVEC Z
            if p1.super_attack and p1.move_x != 0 and p1.clean_hit >= 5: #abs(rect_gugus.left - fightrect.right) <= 5 and 
                # fighter_life -=15
                p1.clean_hit = 0
                # x2 -= 120
                # opp_clean = 0
                p1.animation = True
                p1.type_anim = "super_punch"
                frame_count = 1
            if p1.super_attack and p1.move_x != 0 and p1.clean_hit >= 5:#abs(rect_gugus.right - fightrect.left) <= 5 and 
                # fighter_life -=15
                # x2 += 120
                p1.clean_hit = 0
                # opp_clean = 0
                p1.animation = True
                p1.type_anim = "super_punch"
                frame_count = 1
                
            ##COUP SAUTE
            if p1.attack and 10 < p1.air_time < 35:#abs(rect_gugus.left - fightrect.right) <= 15 
                # fighter_life -= 10
                if p1.clean_hit < 5:
                    p1.clean_hit += 1
                # opp_clean = 0
                # x2 -= 50
                p1.animation = True
                p1.type_anim = "jump_punch"
                frame_count = 1
                
            if p1.attack and 10 < p1.air_time < 35:#abs(rect_gugus.right - fightrect.left) <= 15 and 
                # fighter_life -=10
                # x2 += 50
                if p1.clean_hit < 5:
                    p1.clean_hit += 1
                # opp_clean = 0
                p1.animation = True
                p1.type_anim = "jump_punch"
                frame_count = 1
            

            ##COUP ADVERSAIRE
            # if rect_gugus.colliderect(fightrect):
            #     collision = True
            # elif not rect_gugus.colliderect(fightrect):
            #     collision = False
                
            # if collision and move_x == 0 and not attack and not jump:
            #     hit = True
            # else:
            #     hit = False
    
            # ##CORP A CORP           
            # if abs(rect_gugus.left - fightrect.right) <= 1 and hit:
            #     Gus.pv -=5
            #     x += 80
            #     clean_hit = 0
            #     opp_clean += 1
            #     animation = True
            #     type_anim = "adv_c2c"
            #     frame_count = 1            
                
            # if abs(rect_gugus.right - fightrect.left) <= 1 and hit:
            #     Gus.pv -=5
            #     x -= 80
            #     clean_hit = 0
            #     opp_clean += 1
            #     animation = True
            #     type_anim = "adv_c2c"
            #     frame_count = 1            
                
            # ##SUPER COUP ADVERSAIRE
            # if abs(rect_gugus.left - fightrect.right) <= 5 and hit and opp_clean == 3:
            #     Gus.pv -= 10
            #     x += 100
            #     clean_hit = 0
            #     opp_clean = 0
            #     animation = True
            #     type_anim = "adv_sp"
            #     frame_count = 1            
                
            # if abs(rect_gugus.right - fightrect.left) <= 5 and hit and opp_clean == 3:
            #     Gus.pv -=10
            #     x -= 100
            #     clean_hit = 0
            #     opp_clean = 0
            #     animation = True
            #     type_anim = "adv_sp"
            #     frame_count = 1            
                
            ##COMBO ADVERSAIRE
            ##PROJECTILE??           
                    
            # if p1.move_x == 0 and not p1.jump:
            #     if x2 > x and not collision and x2 > 50:
            #         x2 -= 0.5
            #         if type_anim == "none":
            #             fightr = fighter_1_r[a]
            #         elif type_anim == "adv_c2c":
            #             fightr = fighter_pch_r[a]
            #         elif type_anim == "adv_sp":
            #             fightr = fighter_sp_r[a]
            #         elif type_anim == "punch" or type_anim == "kick" or type_anim == "super_punch" or type_anim == "jump_punch":
            #             fightr = fighter_ouille_r[a]
    
            #     elif x2 < x and not collision and x2 < 400:
            #         x2 += 0.5
            #         if type_anim == "none":
            #             fightr = fighter_1_l[a]
            #         elif type_anim == "adv_c2c":
            #             fightr = fighter_pch_l[a]
            #         elif type_anim == "adv_sp":
            #             fightr = fighter_sp_l[a]
            #         elif type_anim == "punch" or type_anim == "kick" or type_anim == "super_punch" or type_anim == "jump_punch":
            #             fightr = fighter_ouille_l[a]
    
            #     else:
            #         x2 = x2
            #         if type_anim == "none" and side:
            #             fightr = fighter_1_r[a]
            #         elif type_anim == "none" and not side:
            #             fightr = fighter_1_l[a]
            #         elif type_anim == "adv_c2c" and side:
            #             fightr = fighter_pch_r[a]
            #         elif type_anim == "adv_c2c" and not side:
            #             fightr = fighter_pch_l[a]
            #         elif type_anim == "adv_sp" and side:
            #             fightr = fighter_sp_r[a]
            #         elif type_anim == "adv_sp" and not side:
            #             fightr = fighter_sp_l[a]
            #         elif (type_anim == "punch" or type_anim == "kick" or type_anim == "super_punch" or type_anim == "jump_punch") and side:
            #             fightr = fighter_ouille_r[a]
            #         elif (type_anim == "punch" or type_anim == "kick" or type_anim == "super_punch" or type_anim == "jump_punch") and not side:
            #             fightr = fighter_ouille_l[a]
                       
            p1.x += p1.move_x
            p1.y += p1.move_y  
    
            if p1.x > 450 :
                p1.x=450
            if p1.x < 0:
                p1.x = 0
            # if x2 > 480:
            #     x2 = 480
            # if x2 < 20:
            #     x2 = 20
            
            screen.fill((0,0,0))
            
            perso_rect.topleft = (p1.x,p1.y)        
            # fightrect.topleft = (x2,y2)        
            
            decors = lvl.anim_level[a]
            screen.blit(decors,(0,0))
            screen.blit(perso,perso_rect)
            # screen.blit(fightr,fightrect)
            
            clean_bar = power_bar[p1.clean_hit]

            screen.blit(clean_bar,(20,70))
            
            pv = Gus_font.render("Santé : " + str(p1.vie), False, (220, 220, 220))
            super_punch = Gus_font.render("Super power : ", False, (220, 220, 220))
            lieu = Gus_font.render("Niveau : "+str(lenivo), False, (220, 220, 220))
            frapper = Gus_font.render("Frapper", False, (220, 220, 220))
            control = Gus_font.render("(A et/ou Z) + flèches", False, (220, 220, 220))
        
            screen.blit(pv , (20,35))
            screen.blit(super_punch,(20,50))
            screen.blit(lieu , (20,95))
            screen.blit(frapper, (400,65))
            screen.blit(control, (360,95))
            
            # textsurface = myfont.render(str(fighter_life), False, (210, 210, 210))
            # screen.blit(textsurface,(460,35))
        
        elif p1.vie <= 0 :
            gameExit = True
            
            
        pygame.display.update()
        
        clock.tick(100)
        
jeu_fight()
pygame.quit()
