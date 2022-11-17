# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 21:42:37 2022

@author: basti
"""
import pygame, sys
from settings import *
import random

class Pnj():
    def __init__(self,nom,joueur,nivo,jeu):
        self.path = "..\\_bank\\perso\\"+str(nom)
        
        self.name = nom 
        self.interact = False
        
        self.dist = adv_dist[nom]
        self.range = range_adv[nom]
        self.prob_jump = adv_proba_jump[nom]
        self.speed = adv_speed[nom]
        
        self.joueur = joueur
        
        self.hit_fx = hit_fx_sound[self.name]
        self.punch_fx = touche_point_sound[self.name]
        self.coup_fx = touche_autre_sound[self.name]
          
        ##BASE
        self.pos1 = pygame.image.load(self.path+"\\"+str(nom)+"_1.png")
        self.pos2 = pygame.image.load(self.path+"\\"+str(nom)+"_2.png")

        self.pos1_l = pygame.transform.flip(self.pos1, True, False)
        self.pos2_l = pygame.transform.flip(self.pos2, True, False)
        
        self.fr = [self.pos1,self.pos2,self.pos1,self.pos2]
        self.fl = [self.pos1_l,self.pos2_l,self.pos1_l,self.pos2_l]
        
        self.start_pos = self.fr[0].get_rect()
        self.height = int(self.start_pos.height)

        self.limite = level_sol[nivo]-self.height
        self.detente = hauteur[nom]
        
        ##HIT
        self.hit1 = pygame.image.load(self.path+"\\"+str(nom)+"_hit_1.png")
        self.hit2 = pygame.image.load(self.path+"\\"+str(nom)+"_hit_2.png")

        self.hit1_l = pygame.transform.flip(self.hit1, True, False)
        self.hit2_l = pygame.transform.flip(self.hit2, True, False)
        
        self.hitr = [self.hit1,self.hit1,self.hit2,self.hit2]
        self.hitl = [self.hit1_l,self.hit1_l,self.hit2_l,self.hit2_l]
        
        ##JUMP
        self.jump1 = pygame.image.load(self.path+"\\"+str(nom)+"_jump_1.png")
        self.jump2 = pygame.image.load(self.path+"\\"+str(nom)+"_jump_2.png")
        self.jump3 = pygame.image.load(self.path+"\\"+str(nom)+"_jump_3.png")
        self.jump4 = pygame.image.load(self.path+"\\"+str(nom)+"_jump_4.png")

        self.jump1_l = pygame.transform.flip(self.jump1, True, False)
        self.jump2_l = pygame.transform.flip(self.jump2, True, False)
        self.jump3_l = pygame.transform.flip(self.jump3, True, False)
        self.jump4_l = pygame.transform.flip(self.jump4, True, False)
        
        self.jumpr = [self.jump1,self.jump2,self.jump3,self.jump4]
        self.jumpl = [self.jump1_l,self.jump2_l,self.jump3_l,self.jump4_l]
        
        ##KO
        self.ko1 = pygame.image.load(self.path+"\\"+str(nom)+"_ko_1.png")
        self.ko2 = pygame.image.load(self.path+"\\"+str(nom)+"_ko_2.png")

        self.ko1_l = pygame.transform.flip(self.ko1, True, False)
        self.ko2_l = pygame.transform.flip(self.ko2, True, False)
        
        self.kor = [self.ko1,self.ko1,self.ko2,self.ko2]
        self.kol = [self.ko1_l,self.ko1_l,self.ko2_l,self.ko2_l]
        
        ##PIED
        self.pied1 = pygame.image.load(self.path+"\\"+str(nom)+"_pied_1.png")
        self.pied2 = pygame.image.load(self.path+"\\"+str(nom)+"_pied_2.png")
        self.pied3 = pygame.image.load(self.path+"\\"+str(nom)+"_pied_3.png")
        self.pied4 = pygame.image.load(self.path+"\\"+str(nom)+"_pied_4.png")

        self.pied1_l = pygame.transform.flip(self.pied1, True, False)
        self.pied2_l = pygame.transform.flip(self.pied2, True, False)
        self.pied3_l = pygame.transform.flip(self.pied3, True, False)
        self.pied4_l = pygame.transform.flip(self.pied4, True, False)
        
        self.piedr = [self.pied1,self.pied2,self.pied3,self.pied4]
        self.piedl = [self.pied1_l,self.pied2_l,self.pied3_l,self.pied4_l]
        
        ##PUNCH
        self.punch1 = pygame.image.load(self.path+"\\"+str(nom)+"_punch_1.png")
        self.punch2 = pygame.image.load(self.path+"\\"+str(nom)+"_punch_2.png")
        self.punch3 = pygame.image.load(self.path+"\\"+str(nom)+"_punch_3.png")
        self.punch4 = pygame.image.load(self.path+"\\"+str(nom)+"_punch_4.png")

        self.punch1_l = pygame.transform.flip(self.punch1, True, False)
        self.punch2_l = pygame.transform.flip(self.punch2, True, False)
        self.punch3_l = pygame.transform.flip(self.punch3, True, False)
        self.punch4_l = pygame.transform.flip(self.punch4, True, False)
        
        self.punchr = [self.punch1,self.punch2,self.punch3,self.punch4]
        self.punchl = [self.punch1_l,self.punch2_l,self.punch3_l,self.punch4_l]        

        ##SPE
        self.spe1 = pygame.image.load(self.path+"\\"+str(nom)+"_spe_1.png")
        self.spe2 = pygame.image.load(self.path+"\\"+str(nom)+"_spe_2.png")
        self.spe3 = pygame.image.load(self.path+"\\"+str(nom)+"_spe_3.png")
        self.spe4 = pygame.image.load(self.path+"\\"+str(nom)+"_spe_4.png")

        self.spe1_l = pygame.transform.flip(self.spe1, True, False)
        self.spe2_l = pygame.transform.flip(self.spe2, True, False)
        self.spe3_l = pygame.transform.flip(self.spe3, True, False)
        self.spe4_l = pygame.transform.flip(self.spe4, True, False)
        
        self.sper = [self.spe1,self.spe2,self.spe3,self.spe4]
        self.spel = [self.spe1_l,self.spe2_l,self.spe3_l,self.spe4_l]
        
        ##LOW
        self.low1 = pygame.image.load(self.path+"\\"+str(nom)+"_low1.png")
        self.low2 = pygame.image.load(self.path+"\\"+str(nom)+"_low2.png")
        self.low3 = pygame.image.load(self.path+"\\"+str(nom)+"_low3.png")
        self.low4 = pygame.image.load(self.path+"\\"+str(nom)+"_low4.png")

        self.low1_l = pygame.transform.flip(self.low1, True, False)
        self.low2_l = pygame.transform.flip(self.low2, True, False)
        self.low3_l = pygame.transform.flip(self.low3, True, False)
        self.low4_l = pygame.transform.flip(self.low4, True, False)
        
        self.lowr = [self.low1,self.low2,self.low3,self.low4]
        self.lowl = [self.low1_l,self.low2_l,self.low3_l,self.low4_l]        

        ##DOWN
        self.down1 = pygame.image.load(self.path+"\\"+str(nom)+"_down1.png")
        self.down2 = pygame.image.load(self.path+"\\"+str(nom)+"_down2.png")
        self.down3 = pygame.image.load(self.path+"\\"+str(nom)+"_down3.png")
        self.down4 = pygame.image.load(self.path+"\\"+str(nom)+"_down4.png")

        self.down1_l = pygame.transform.flip(self.down1, True, False)
        self.down2_l = pygame.transform.flip(self.down2, True, False)
        self.down3_l = pygame.transform.flip(self.down3, True, False)
        self.down4_l = pygame.transform.flip(self.down4, True, False)
        
        self.downr = [self.down1,self.down2,self.down3,self.down4]
        self.downl = [self.down1_l,self.down2_l,self.down3_l,self.down4_l] 
        
        ##PUNCH 2
        self.punch2_1 = pygame.image.load(self.path+"\\"+str(nom)+"_punch2_1.png")
        self.punch2_2 = pygame.image.load(self.path+"\\"+str(nom)+"_punch2_2.png")
        self.punch2_3 = pygame.image.load(self.path+"\\"+str(nom)+"_punch2_3.png")
        self.punch2_4 = pygame.image.load(self.path+"\\"+str(nom)+"_punch2_4.png")

        self.punch2_1_l = pygame.transform.flip(self.punch2_1, True, False)
        self.punch2_2_l = pygame.transform.flip(self.punch2_2, True, False)
        self.punch2_3_l = pygame.transform.flip(self.punch2_3, True, False)
        self.punch2_4_l = pygame.transform.flip(self.punch2_4, True, False)
        
        self.punch2_r = [self.punch2_1,self.punch2_2,self.punch2_3,self.punch2_4]
        self.punch2_l = [self.punch2_1_l,self.punch2_2_l,self.punch2_3_l,self.punch2_4_l] 
         
      
        ##ATTRIBUTS
        self.vie = 100
        self.move_y = 0
        self.move_x = 0
        self.air_time = 1
        self.clean_hit = 0 

        self.jump = False
        self.fall = False
        
        self.attack = False
        self.super_attack = False
        self.hit = False
        self.collision = False
        
        if self.joueur == 1:
            self.side = True
            self.x = 150
            self.y = level_sol[nivo]-self.height
            
        elif self.joueur == 2:
            self.side = False
            self.x = 300
            self.y = level_sol[nivo]-self.height

        self.animation = False
        self.type_anim ="none"
        
        self.punch_force = punch[nom]
        self.kick_force = kicks[nom]
        self.super_force = supers[nom]
        self.jump_force = sauter[nom]
        self.low_force = low[nom]
        
        self.punch_move = abs(punch[nom]*2)
        self.kick_move = abs(kicks[nom]*4)
        self.super_move = abs(supers[nom]*10)
        self.jump_move = abs(sauter[nom]*5) 
        self.low_move = abs(low[nom]*3)
        
        self.liste_anim = ["punch","punch2","kick","jump_punch"]
        
    def move(self,p1,frame_count,perso_rect,perso_rect2):
        
        if p1.side and perso_rect.left - perso_rect2.right > 0 and not (p1.jump or p1.interact):
            self.side = False
            if not self.interact :
                self.move_x = -self.speed
            elif self.interact and frame_count < 10 :
                self.move_x = -self.speed
            elif self.interact and frame_count >= 10 :
                self.move_x = self.speed
            
        elif not p1.side and perso_rect.left - perso_rect2.right < 0 and not (p1.jump or p1.interact):
            self.side = True
            if not self.interact:
                self.move_x = self.speed
            elif self.interact and frame_count < 10:
                self.move_x = self.speed
            elif self.interact and frame_count >= 10:
                self.move_x = -self.speed
        
        if p1.type_anim == "low" and abs(perso_rect.left - perso_rect2.right) <= self.dist*3:
            a = random.randint(1,self.prob_jump)
            if (a%2) != 1 :            
                self.jump = True
                self.move_x = 10
            elif a == 5:
                self.move_x = 10
        if p1.type_anim == "low" and abs(perso_rect.right - perso_rect2.left) <= self.dist*3:
            a = random.randint(1,self.prob_jump)
            if (a%2) != 1 :            
                self.jump = True
                self.move_x = -10
            elif a == 5:
                self.move_x = -10
                
        if p1.move_x != 0 and self.vie < 100 and not (p1.jump or p1.interact):
            if p1.move_x > 0:
                self.move_x = self.speed
            elif p1.move_x < 0:
                self.move_x = -self.speed
                                    
        return(self.move_x,self.move_y)
            
    def maj_anim(self,a):

        if self.side:
            if self.type_anim == "none":
                perso=self.fr[a]
            elif self.type_anim == "punch":
                perso = self.punchr[a]
            elif self.type_anim == "kick":
                perso = self.piedr[a]
            elif self.type_anim == "super_punch":
                perso = self.sper[a]
            elif self.type_anim =="jump_punch":
                perso = self.jumpr[a]
            elif self.type_anim =="hit":
                perso = self.hitr[a]
            elif self.type_anim =="ko":
                perso = self.kor[a]
            elif self.type_anim =="low":
                perso = self.lowr[a]
            elif self.type_anim =="down":
                perso = self.downr[a]
            elif self.type_anim =="punch2":
                perso = self.punch2_r[a]
        else:
            if self.type_anim == "none":
                perso=self.fl[a]
            elif self.type_anim == "punch":
                perso = self.punchl[a]
            elif self.type_anim == "kick":
                perso = self.piedl[a]
            elif self.type_anim == "super_punch":
                perso = self.spel[a]
            elif self.type_anim =="jump_punch":
                perso = self.jumpl[a]
            elif self.type_anim =="hit":
                perso = self.hitl[a]
            elif self.type_anim =="ko":
                perso = self.kol[a]
            elif self.type_anim =="low":
                perso = self.lowl[a]
            elif self.type_anim =="down":
                perso = self.downl[a]
            elif self.type_anim =="punch2":
                perso = self.punch2_l[a]
        
        return(perso)
        
    def collision_joueur(self,perso_rect,perso_rect2,p2):
        if perso_rect.colliderect(perso_rect2):
            if abs(perso_rect.bottom - perso_rect2.top) <= self.dist*2 :
                self.move_y = 0
                self.air_time = 1
                self.jump = False
                self.interact = True
            if abs(perso_rect.top - perso_rect2.bottom) <= self.dist*2 :
                self.move_y = 0
                self.interact = True
            if abs(perso_rect.left - perso_rect2.right) <= self.dist*2 :
                self.move_x = 0             
                self.interact = True
            if abs(perso_rect.right - perso_rect2.left) <= self.dist*2 :
                self.move_x = 0
                self.interact = True
                
        else:
            self.interact = False
    
        return(self.move_y,self.move_x) 
    
    def punch_anim(self,frame_count,p2):
        if self.interact and frame_count <= 1 and p2.type_anim == "none":
            a = random.randint(1,self.range)
            
            if a == 1 and self.clean_hit < 5 and self.type_anim == "none":
                self.animation = True
                self.type_anim = "punch"
                frame_count = 1
            elif a == 2 and self.clean_hit < 5 and self.type_anim == "none":
                self.animation = True
                self.type_anim = "punch2"
                frame_count = 1
            elif a == 3 and self.clean_hit < 5 and self.type_anim == "none": 
                self.animation = True
                self.type_anim = "kick"
                frame_count = 1
            elif a == 4 and self.type_anim == "none": 
                self.animation = True
                self.type_anim = "low"
                frame_count = 1
            elif (a%2) != 1 and a < 8 and self.move_x != 0 and self.clean_hit >= 5 and self.type_anim == "none":
                self.clean_hit = 0
                self.animation = True
                self.type_anim = "super_punch"
                frame_count = 1
            elif a == 4 and 10 < self.air_time < 35 and not self.fall and self.type_anim == "none":
                self.animation = True
                self.type_anim = "jump_punch"
                frame_count = 1
            elif a == 2 and self.air_time > 1 and self.fall and self.type_anim == "none":
                self.animation = True
                self.type_anim = "down"
                frame_count = 1
            else:
                self.type_anim = "none"
                
        return(frame_count)
            
            
    def damage(self,perso_rect,perso_rect2,p2,jeu,frame_count):
            
        if frame_count <= 1:
            a = random.randint(1,self.range)
            ##PUNCH
            if  0 < abs(perso_rect.left - perso_rect2.right) <= self.dist and p2.type_anim == "none" and a == 1:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.punch_fx.set_volume(jeu.vol_fx/2)
                self.punch_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=punch[self.name]
                else:
                    p2.vie -=punch[self.name]/2
                p2.x -= int(self.punch_move)
                p2.clean_hit = 0 
                p2.type_anim = "hit"              
            elif 0 < abs(perso_rect.right - perso_rect2.left) <= self.dist and p2.type_anim == "none" and a == 1:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.punch_fx.set_volume(jeu.vol_fx/2)
                self.punch_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=punch[self.name]
                else:
                    p2.vie -=punch[self.name]/2
                p2.x += int(self.punch_move)
                p2.clean_hit = 0    
                p2.type_anim = "hit"              
    
            elif  abs(perso_rect.left - perso_rect2.right) == 0 and p2.type_anim == "none" and a == 1:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.punch_fx.set_volume(jeu.vol_fx/2)
                self.punch_fx.play()
                p2.vie -=punch[self.name]/4
                p2.x -= int(self.punch_move/4)
                p2.type_anim = "hit"              
            elif  abs(perso_rect.right - perso_rect2.left) == 0 and p2.type_anim == "none" and a == 1:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.punch_fx.set_volume(jeu.vol_fx/2)
                self.punch_fx.play()
                p2.vie -= int(punch[self.name]/4)
                p2.x += self.punch_move/4
                p2.type_anim = "hit"            

            ##PUNCH2                
            if 0 < abs(perso_rect.left - perso_rect2.right) <= self.dist and p2.type_anim == "none" and a == 2:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.punch_fx.set_volume(jeu.vol_fx/2)
                self.punch_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=punch[self.name]
                else:
                    p2.vie -=punch[self.name]/2
                p2.x -= int(self.punch_move)
                p2.clean_hit = 0 
                p2.type_anim = "hit"              
            elif 0 < abs(perso_rect.right - perso_rect2.left) <= self.dist and p2.type_anim == "none" and a == 2:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.punch_fx.set_volume(jeu.vol_fx/2)
                self.punch_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=punch[self.name]
                else:
                    p2.vie -=punch[self.name]/2
                p2.x += int(self.punch_move)
                p2.clean_hit = 0    
                p2.type_anim = "hit"              
    
            elif  abs(perso_rect.left - perso_rect2.right) == 0 and p2.type_anim == "none" and a == 2:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.punch_fx.set_volume(jeu.vol_fx/2)
                self.punch_fx.play()
                p2.vie -=punch[self.name]/4
                p2.x -= int(self.punch_move/4)
                p2.type_anim = "hit"              
            elif  abs(perso_rect.right - perso_rect2.left) == 0 and p2.type_anim == "none" and a == 2:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.punch_fx.set_volume(jeu.vol_fx/2)
                self.punch_fx.play()
                p2.vie -= int(punch[self.name]/4)
                p2.x += self.punch_move/4
                p2.type_anim = "hit"                   
                
            ##KICK    
            if 0 < abs(perso_rect.left - perso_rect2.right) <= self.dist and p2.type_anim == "none" and a == 3:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.punch_fx.set_volume(jeu.vol_fx/2)
                self.punch_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=kicks[self.name]
                else:
                    p2.vie -=kicks[self.name]/2
                p2.x -= int(self.kick_move)
                p2.clean_hit = 0 
                p2.type_anim = "hit"              
            elif 0 < abs(perso_rect.right - perso_rect2.left) <= self.dist and p2.type_anim == "none" and a == 3:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.punch_fx.set_volume(jeu.vol_fx/2)
                self.punch_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=kicks[self.name]
                else:
                    p2.vie -=kicks[self.name]/2
                p2.x += int(self.kick_move)
                p2.clean_hit = 0    
                p2.type_anim = "hit"              
    
            elif  abs(perso_rect.left - perso_rect2.right) == 0 and p2.type_anim == "none" and a == 3:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.punch_fx.set_volume(jeu.vol_fx/2)
                self.punch_fx.play()
                p2.vie -=kicks[self.name]/3
                p2.x -= int(self.kick_move/4)
                p2.type_anim = "hit"              
            elif  abs(perso_rect.right - perso_rect2.left) == 0 and p2.type_anim == "none" and a == 3:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.punch_fx.set_volume(jeu.vol_fx/2)
                self.punch_fx.play()
                p2.vie -=kicks[self.name]/3
                p2.x += int(self.kick_move/4)
                p2.type_anim = "hit"  

            ##LOW
            if 0 < abs(perso_rect.left - perso_rect2.right) <= self.dist and p2.type_anim == "none" and a == 4:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.punch_fx.set_volume(jeu.vol_fx/2)
                self.punch_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=kicks[self.name]
                else:
                    p2.vie -=kicks[self.name]/2
                p2.x -= int(self.low_move)
                p2.clean_hit = 0 
                p2.type_anim = "hit"              
            elif 0 < abs(perso_rect.right - perso_rect2.left) <= self.dist and p2.type_anim == "none" and a == 4:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.punch_fx.set_volume(jeu.vol_fx/2)
                self.punch_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=kicks[self.name]
                else:
                    p2.vie -=kicks[self.name]/2
                p2.x += int(self.low_move)
                p2.clean_hit = 0    
                p2.type_anim = "hit"              
    
            elif  abs(perso_rect.left - perso_rect2.right) == 0 and p2.type_anim == "none" and a == 4:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.punch_fx.set_volume(jeu.vol_fx/2)
                self.punch_fx.play()
                p2.vie -=kicks[self.name]/3
                p2.x -= int(self.low_move/4)
                p2.type_anim = "hit"              
            elif  abs(perso_rect.right - perso_rect2.left) == 0 and p2.type_anim == "none" and a == 4:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.punch_fx.set_volume(jeu.vol_fx/2)
                self.punch_fx.play()
                p2.vie -=kicks[self.name]/3
                p2.x += int(self.low_move/4)
                p2.type_anim = "hit"  
                
            ##SPE    
            if  abs(perso_rect.left - perso_rect2.right) <= self.dist*4 and p2.type_anim == "none" and (a%2) != 1 and a < 8 and self.clean_hit >= 5:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.coup_fx.set_volume(jeu.vol_fx/2)
                self.coup_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=supers[self.name]
                else:
                    p2.vie -=supers[self.name]/1.5
    
                p2.x -= int(self.super_move)
                p2.clean_hit = 0 
                p2.type_anim = "hit"              
            elif  abs(perso_rect.right - perso_rect2.left) <= self.dist*4 and p2.type_anim == "none" and (a%2) != 1 and a < 8 and self.clean_hit >= 5:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.coup_fx.set_volume(jeu.vol_fx/2)
                self.coup_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=supers[self.name]
                else:
                    p2.vie -=supers[self.name]/1.5
                p2.x += int(self.super_move)
                p2.clean_hit = 0    
                p2.type_anim = "hit"              

            ##JUMP    
            if  abs(perso_rect.left - perso_rect2.right) <= self.dist*3 and a == 4 and 10 < self.air_time < 35:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.coup_fx.set_volume(jeu.vol_fx/2)
                self.coup_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=sauter[self.name]
                else:
                    p2.vie -=sauter[self.name]/2
                p2.x -=int(self.jump_move)
                p2.clean_hit = 0 
                p2.type_anim = "hit"              
            elif  abs(perso_rect.right - perso_rect2.left) <= self.dist*3 and a == 4 and 10 < self.air_time < 35:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.coup_fx.set_volume(jeu.vol_fx/2)
                self.coup_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=sauter[self.name]
                else:
                    p2.vie -=sauter[self.name]/2
                p2.x += int(self.jump_move)
                p2.clean_hit = 0    
                p2.type_anim = "hit"

            ##DOWN    
            if  abs(perso_rect.bottom - perso_rect2.top) <= self.dist*2 and a == 2 and 0 < self.air_time < 25:
                p2.hit_fx.set_volume(jeu.vol_fx/2)
                p2.hit_fx.play()
                self.coup_fx.set_volume(jeu.vol_fx/2)
                self.coup_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=sauter[self.name]*2
                else:
                    p2.vie -=sauter[self.name]
                p2.x -=int(self.jump_move)
                p2.clean_hit = 0 
                p2.type_anim = "hit"                         
            
        return(p2)        