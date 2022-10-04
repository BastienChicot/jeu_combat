# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 13:59:58 2022

@author: basti
"""
import pygame, sys
from settings import *

pygame.init()
pygame.font.init()

class Jeu():
    def __init__(self,nivo = "none"):
        self.nivo = nivo
        self.selected = "none"
        self.pause = 0
        
        self.vol_music_menu = 0.5
        self.vol_music_fight = 0.5
        self.vol_fx = 0.5
        
        ##JOUEUR 1
        self.touche_j1_1 = pygame.key.key_code("t")
        self.touche_j1_1_text = pygame.key.name(self.touche_j1_1)

        self.touche_j1_2 = pygame.key.key_code("y")
        self.touche_j1_2_text = pygame.key.name(self.touche_j1_2)        

        self.touche_j1_L = pygame.key.key_code("q")
        self.touche_j1_L_text = pygame.key.name(self.touche_j1_L)

        self.touche_j1_R = pygame.key.key_code("d")
        self.touche_j1_R_text = pygame.key.name(self.touche_j1_R)        

        self.touche_j1_D = pygame.key.key_code("s")
        self.touche_j1_D_text = pygame.key.name(self.touche_j1_D)

        self.touche_j1_U = pygame.key.key_code("z")
        self.touche_j1_U_text = pygame.key.name(self.touche_j1_U)  

        ##JOUEUR 2
        self.touche_j2_1 = pygame.key.key_code(",")
        self.touche_j2_1_text = pygame.key.name(self.touche_j2_1)

        self.touche_j2_2 = pygame.key.key_code(";")
        self.touche_j2_2_text = pygame.key.name(self.touche_j2_2)        

        self.touche_j2_L = pygame.key.key_code("left")
        self.touche_j2_L_text = pygame.key.name(self.touche_j2_L)

        self.touche_j2_R = pygame.key.key_code("right")
        self.touche_j2_R_text = pygame.key.name(self.touche_j2_R)        

        self.touche_j2_D = pygame.key.key_code("down")
        self.touche_j2_D_text = pygame.key.name(self.touche_j2_D)

        self.touche_j2_U = pygame.key.key_code("up")
        self.touche_j2_U_text = pygame.key.name(self.touche_j2_U)        

        ###MULTI
        
        self.joueur1 = "none"
        self.joueur2 = "none"
        
        self.unlock_perso = {
            "basti":(75,75),
            "clou":(175,75),
            "coach":(275,75),
            "justi":(375,75)
            }

        self.unlock_perso2 = {
            "basti":(125,75),
            "clou":(225,75),
            "coach":(325,75),
            "justi":(425,75)
            }
        
        self.unlock_nivo = {
            "gare":(75,50),
            "metro":(175,50),
            "parc":(275,50),
            "toit":(375,50),
            "theatre":(75,175),
            "usine":(175,175),
            "montagne":(275,175),
            "lac":(375,175),
            "espace":(75,300)
            }
    
    def update_touches(self,saisie,objet):

        if saisie == "saisie_1":           
            self.touche_j1_1 = pygame.key.key_code(str(objet.text))
            self.touche_j1_1_text = pygame.key.name(self.touche_j1_1)
        elif saisie == "saisie_2":           
            self.touche_j1_2 = pygame.key.key_code(str(objet.text))
            self.touche_j1_2_text = pygame.key.name(self.touche_j1_2) 
        elif saisie == "saisie_l":           
            self.touche_j1_L = pygame.key.key_code(str(objet.text))
            self.touche_j1_L_text = pygame.key.name(self.touche_j1_L)
        elif saisie == "saisie_r":           
            self.touche_j1_R = pygame.key.key_code(str(objet.text))
            self.touche_j1_R_text = pygame.key.name(self.touche_j1_R)
        elif saisie == "saisie_d":           
            self.touche_j1_D = pygame.key.key_code(str(objet.text))
            self.touche_j1_D_text = pygame.key.name(self.touche_j1_D)
        elif saisie == "saisie_u":           
            self.touche_j1_U = pygame.key.key_code(str(objet.text))
            self.touche_j1_U_text = pygame.key.name(self.touche_j1_U)

        elif saisie == "saisie_1_2":           
            self.touche_j2_1 = pygame.key.key_code(str(objet.text))
            self.touche_j2_1_text = pygame.key.name(self.touche_j2_1)
        elif saisie == "saisie_2_2":           
            self.touche_j2_2 = pygame.key.key_code(str(objet.text))
            self.touche_j2_2_text = pygame.key.name(self.touche_j2_2) 
        elif saisie == "saisie_l_2":           
            self.touche_j2_L = pygame.key.key_code(str(objet.text))
            self.touche_j2_L_text = pygame.key.name(self.touche_j2_L)
        elif saisie == "saisie_r_2":           
            self.touche_j2_R = pygame.key.key_code(str(objet.text))
            self.touche_j2_R_text = pygame.key.name(self.touche_j2_R)
        elif saisie == "saisie_d_2":           
            self.touche_j2_D = pygame.key.key_code(str(objet.text))
            self.touche_j2_D_text = pygame.key.name(self.touche_j2_D)
        elif saisie == "saisie_u_2":           
            self.touche_j2_U = pygame.key.key_code(str(objet.text))
            self.touche_j2_U_text = pygame.key.name(self.touche_j2_U)
                
    def reinitialise_options(self):
        self.vol_music_menu = 0.5
        self.vol_music_fight = 0.5
        self.vol_fx = 0.5
        
        self.touche_j1_1 = pygame.key.key_code("t")
        self.touche_j1_1_text = pygame.key.name(self.touche_j1_1)
        
        self.touche_j1_2 = pygame.key.key_code("y")
        self.touche_j1_2_text = pygame.key.name(self.touche_j1_2)        

        self.touche_j1_L = pygame.key.key_code("q")
        self.touche_j1_L_text = pygame.key.name(self.touche_j1_L)

        self.touche_j1_R = pygame.key.key_code("d")
        self.touche_j1_R_text = pygame.key.name(self.touche_j1_R)        

        self.touche_j1_D = pygame.key.key_code("s")
        self.touche_j1_D_text = pygame.key.name(self.touche_j1_D)

        self.touche_j1_U = pygame.key.key_code("z")
        self.touche_j1_U_text = pygame.key.name(self.touche_j1_U)        

        ##JOUEUR 2
        self.touche_j2_1 = pygame.key.key_code(",")
        self.touche_j2_1_text = pygame.key.name(self.touche_j2_1)

        self.touche_j2_2 = pygame.key.key_code(";")
        self.touche_j2_2_text = pygame.key.name(self.touche_j2_2)        

        self.touche_j2_L = pygame.key.key_code("left")
        self.touche_j2_L_text = pygame.key.name(self.touche_j2_L)

        self.touche_j2_R = pygame.key.key_code("right")
        self.touche_j2_R_text = pygame.key.name(self.touche_j2_R)        

        self.touche_j2_D = pygame.key.key_code("down")
        self.touche_j2_D_text = pygame.key.name(self.touche_j2_D)

        self.touche_j2_U = pygame.key.key_code("up")
        self.touche_j2_U_text = pygame.key.name(self.touche_j2_U)     
        
    def iter_objects(self):
        return (self.__dict__) 

class level():
    def __init__ (self,nivo):
        self.path = "..\\_bank\\level\\"+str(nivo)

        self.img1 = pygame.image.load(self.path+"\\"+str(nivo)+"_1.png")
        self.img2 = pygame.image.load(self.path+"\\"+str(nivo)+"_2.png")
        self.img3 = pygame.image.load(self.path+"\\"+str(nivo)+"_3.png")
        self.img4 = pygame.image.load(self.path+"\\"+str(nivo)+"_4.png")
        
        self.start = self.img1
        
        self.anim_level = [self.img1,self.img2,self.img3,self.img4]

class joueur():
    def __init__(self,nom,joueur,nivo,jeu):
        self.path = "..\\_bank\\perso\\"+str(nom)
        
        self.name = nom 
        self.interact = False
        
        self.joueur = joueur
        
        self.hit_fx = hit_fx_sound[self.name]
          
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
        
        ##CONTROLES
        if self.joueur == 1:
            self.saut = jeu.touche_j1_U
            self.descend = jeu.touche_j1_D
            self.gauche = jeu.touche_j1_L
            self.droite = jeu.touche_j1_R
            
            self.action = jeu.touche_j1_1
            self.coup = jeu.touche_j1_2
        elif self.joueur == 2:
            self.saut = jeu.touche_j2_U
            self.descend = jeu.touche_j2_D
            self.gauche = jeu.touche_j2_L
            self.droite = jeu.touche_j2_R
            
            self.action = jeu.touche_j2_1
            self.coup = jeu.touche_j2_2        
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
        
        self.punch_move = abs(punch[nom]*2)
        self.kick_force = abs(kicks[nom]*4)
        self.super_force = abs(supers[nom]*10)
        self.jump_force = abs(sauter[nom]*5) 
        
    def move(self,e):           
          # Condition becomes true when keyboard is pressed   
        if e.type == pygame.KEYDOWN:
       
            if e.key == self.saut :
                self.jump = True
                
            if e.key == self.descend :
                self.fall = True
                
            if e.key == self.gauche :
                self.move_x = -2
                self.side = False
                
            if e.key == self.droite :
                self.move_x = 2
                self.side = True
                
            if e.key == self.action :
                self.attack = True
            if e.key == self.coup :
                self.super_attack = True         
                
        if e.type == pygame.KEYUP:
       
            if e.key == self.saut :
                self.jump = False
                
            if e.key == self.descend :
                self.fall = False
                
            if e.key == self.gauche :
                self.move_x = 0
    
            if e.key == self.droite :
                self.move_x = 0
    
            if e.key == self.action :
                self.attack = False
            if e.key == self.coup :
                self.super_attack = False
                    
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
                
        return(perso)
        
    def collision_joueur(self,perso_rect,perso_rect2,p2):
        if perso_rect.colliderect(perso_rect2):
            if abs(perso_rect.bottom - perso_rect2.top) <= 10 and self.move_y > 0:
                self.move_y = 0
                self.air_time = 1
                self.jump = False
                self.interact = True
            if abs(perso_rect.top - perso_rect2.bottom) <= 10 and self.move_y < 0:
                self.move_y = 0
                self.interact = True
            if abs(perso_rect.left - perso_rect2.right) <= 10 and self.move_x < 0:
                self.move_x = 0             
                self.interact = True
            if abs(perso_rect.right - perso_rect2.left) <= 10 and self.move_x > 0:
                self.move_x = 0
                self.interact = True
                
        else:
            self.interact = False
    
        return(self.move_y,self.move_x) 
    
    def punch_anim(self,frame_count):
        if self.attack and not self.super_attack and self.clean_hit < 5 and self.type_anim == "none":
            self.animation = True
            self.type_anim = "punch"
            frame_count = 1
        elif self.attack and self.super_attack and self.clean_hit < 5 and self.type_anim == "none": 
            self.animation = True
            self.type_anim = "kick"
            frame_count = 1
        elif self.super_attack and self.move_x != 0 and self.clean_hit >= 5 and not self.attack and self.type_anim == "none":
            self.clean_hit = 0
            self.animation = True
            self.type_anim = "super_punch"
            frame_count = 1
        elif self.attack and 10 < self.air_time < 35 and self.type_anim == "none":
            self.animation = True
            self.type_anim = "jump_punch"
            frame_count = 1
            
        return(frame_count)
            
            
    def damage(self,perso_rect,perso_rect2,p2,jeu,frame_count):
        if frame_count <= 4:
            if  abs(perso_rect.left - perso_rect2.right) <= 5 and self.attack and not self.super_attack :#/ and self.move_x != 0:
                p2.hit_fx.set_volume(jeu.vol_fx)
                p2.hit_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=punch[self.name]
                else:
                    p2.vie -=punch[self.name]/2
                p2.x -= 20
                p2.clean_hit = 0 
                p2.type_anim = "hit"              
            if  abs(perso_rect.right - perso_rect2.left) <= 5 and self.attack and not self.super_attack :# and self.move_x != 0:
                p2.hit_fx.set_volume(jeu.vol_fx)
                p2.hit_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=punch[self.name]
                else:
                    p2.vie -=punch[self.name]/2
                p2.x += 20
                p2.clean_hit = 0    
                p2.type_anim = "hit"              
    
            if  abs(perso_rect.left - perso_rect2.right) == 0 and self.attack and not self.super_attack :# and self.move_x == 0:
                p2.hit_fx.set_volume(jeu.vol_fx)
                p2.hit_fx.play()
                p2.vie -=punch[self.name]/4
                p2.x -= 5
                p2.type_anim = "hit"              
            if  abs(perso_rect.right - perso_rect2.left) == 0 and self.attack and not self.super_attack : # and self.move_x == 0:
                p2.hit_fx.set_volume(jeu.vol_fx)
                p2.hit_fx.play()
                p2.vie -=punch[self.name]/4
                p2.x += 5
                p2.type_anim = "hit"              
                
            if  abs(perso_rect.left - perso_rect2.right) <= 10 and self.attack and self.super_attack : #and self.move_x != 0:
                p2.hit_fx.set_volume(jeu.vol_fx)
                p2.hit_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=kicks[self.name]
                else:
                    p2.vie -=kicks[self.name]/2
                p2.x -= 30
                p2.clean_hit = 0 
                p2.type_anim = "hit"              
            if  abs(perso_rect.right - perso_rect2.left) <= 10 and self.attack and self.super_attack : #and self.move_x != 0:
                p2.hit_fx.set_volume(jeu.vol_fx)
                p2.hit_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=kicks[self.name]
                else:
                    p2.vie -=kicks[self.name]/2
                p2.x += 30
                p2.clean_hit = 0    
                p2.type_anim = "hit"              
    
            if  abs(perso_rect.left - perso_rect2.right) == 0 and self.attack and self.super_attack : #and self.move_x == 0:
                p2.hit_fx.set_volume(jeu.vol_fx)
                p2.hit_fx.play()
                p2.vie -=kicks[self.name]/3
                p2.x -= 5
                p2.type_anim = "hit"              
            if  abs(perso_rect.right - perso_rect2.left) == 0 and self.attack and self.super_attack : #and self.move_x == 0:
                p2.hit_fx.set_volume(jeu.vol_fx)
                p2.hit_fx.play()
                p2.vie -=kicks[self.name]/3
                p2.x += 5
                p2.type_anim = "hit"  
                
            if  abs(perso_rect.left - perso_rect2.right) <= 25 and not self.attack and self.super_attack and self.clean_hit >= 5: #and self.move_x != 0
                p2.hit_fx.set_volume(jeu.vol_fx)
                p2.hit_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=supers[self.name]
                else:
                    p2.vie -=supers[self.name]/1.5
    
                p2.x -= 50
                p2.clean_hit = 0 
                p2.type_anim = "hit"              
            if  abs(perso_rect.right - perso_rect2.left) <= 25 and not self.attack and self.super_attack and self.clean_hit >= 5: #and self.move_x != 0 
                p2.hit_fx.set_volume(jeu.vol_fx)
                p2.hit_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=supers[self.name]
                else:
                    p2.vie -=supers[self.name]/1.5
                p2.x += 50
                p2.clean_hit = 0    
                p2.type_anim = "hit"              
    
            if  abs(perso_rect.left - perso_rect2.right) <= 15 and self.attack and 10 < self.air_time < 35:
                p2.hit_fx.set_volume(jeu.vol_fx)
                p2.hit_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=sauter[self.name]
                else:
                    p2.vie -=sauter[self.name]/2
                p2.x -=10
                p2.clean_hit = 0 
                p2.type_anim = "hit"              
            if  abs(perso_rect.right - perso_rect2.left) <= 15 and self.attack and 10 < self.air_time < 35:
                p2.hit_fx.set_volume(jeu.vol_fx)
                p2.hit_fx.play()
                if self.clean_hit < 5:
                    self.clean_hit += 1
                if p2.type_anim == "none":
                    p2.vie -=sauter[self.name]
                else:
                    p2.vie -=sauter[self.name]/2
                p2.x += 10
                p2.clean_hit = 0    
                p2.type_anim = "hit"
            
        return(p2)

class Button:
    def __init__(self,text,width,height,pos,elevation,buttons,screen):
        
		#Core attributes 
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]
        self.screen = screen

		# top rectangle 
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#94B3C1'

		# bottom rectangle 
        self.bottom_rect = pygame.Rect(pos,(width,height))
        self.bottom_color = '#3D615E'
		#text
        self.text = text
        self.text_surf = gui_font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        buttons.append(self)

    def change_text(self, newtext):
        self.text_surf = gui_font.render(newtext, True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self,screen):
		# elevation logic 
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center 

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
        pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()
        self.update()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos)and not self.pressed:
            self.top_color = '#DE0B0B'
        elif not self.top_rect.collidepoint(mouse_pos) and not self.pressed:
            self.dynamic_elecation = self.elevation
            self.top_color = '#94B3C1'
            
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.top_rect.collidepoint(mouse_pos)and not self.pressed:
            self.dynamic_elecation = 0
            self.pressed = True
            self.change_text(f"{self.text}")
            self.top_color = '#DE0B0B'
            
        elif pygame.mouse.get_pressed()[0] and self.top_rect.collidepoint(mouse_pos)and self.pressed:
            self.dynamic_elecation = 0
            self.pressed = False
            self.change_text(f"{self.text}")
            self.top_color = '#94B3C1'
        else:
            self.dynamic_elecation = self.elevation

class Image_select:
    def __init__(self,image,pos,elevation,buttons):

        self.path = "..\\_bank\\image"
        self.image = pygame.image.load(self.path+"\\"+str(image)+"_mini.png")
		#Core attributes 
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]
        
        self.rectangle = self.image.get_rect()
        self.pos = pos
        self.height = int(self.rectangle.height)
        self.width = int(self.rectangle.width)

		# bottom rectangle 
        self.bottom_rect = pygame.Rect(pos,(self.width,self.height))
        self.bottom_color = '#3D615E'
		#text
        self.text = image
        self.text_color = "#FFFFFF"
        self.text_surf = gui_font.render(image,True,self.text_color)
        self.text_rect = self.text_surf.get_rect(topleft = self.rectangle.bottomleft)
        
        buttons.append(self)

    def draw(self,screen):
		# elevation logic 
        self.rectangle.topleft = (self.pos)
        self.text_rect.topleft = self.rectangle.bottomleft

        self.bottom_rect.midtop = self.rectangle.midtop
        self.bottom_rect.height = self.height + self.dynamic_elecation

        pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
        self.text_surf = gui_font.render(self.text,True,self.text_color)
        self.text_rect = self.text_surf.get_rect(topleft = self.rectangle.bottomleft)
        
        screen.blit(self.image, self.rectangle)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()
        self.update()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rectangle.collidepoint(mouse_pos)and not self.pressed:
            self.bottom_color = '#DE0B0B'
            self.text_color = '#000000'
        elif not self.rectangle.collidepoint(mouse_pos) and not self.pressed:
            self.dynamic_elecation = self.elevation
            self.bottom_color = '#94B3C1'
            self.text_color = '#FFFFFF'
            
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.rectangle.collidepoint(mouse_pos)and not self.pressed:
            self.dynamic_elecation = 0
            self.pressed = True
            self.bottom_color = '#DE0B0B'
            self.text_color = '#000000'
            
        elif pygame.mouse.get_pressed()[0] and self.rectangle.collidepoint(mouse_pos)and self.pressed:
            self.dynamic_elecation = 0
            self.pressed = False
            self.bottom_color = '#3D615E'
        else:
            self.dynamic_elecation = self.elevation
            
class Slider:
    def __init__(self,width,height,pos,elevation,liste,volume,block = True):
        self.width = width
        self.height = height
        
		#Core attributes 
        self.pressed = False
        self.elevation = elevation
        self.dynamic_moins = elevation
        self.dynamic_plus = elevation
        self.original_y_pos = pos[1]
        self.block = block
        
        self.pos = pos        
        self.pos_plus = pos
        self.pos_plus = ((width + self.pos[0])-(width/5),self.pos[1])
        self.original_y_plus = self.pos_plus[1]
        
        self.barre_pos = ((pos[0]+(width/5)),(pos[1]+(height/2 - 5)))
        self.curseur_pos_list = [self.pos[0] + ((width*volume)-(width/20)),self.pos[1]]
        self.curseur_pos = tuple(self.curseur_pos_list)
        
		# top rectangle 
        self.top_rect_moins = pygame.Rect(pos,(width/5,height))
        self.top_rect_plus = pygame.Rect(self.pos_plus,(width/5,height))
        self.top_moins_color = '#475F77'
        self.top_plus_color = '#475F77'
        self.top_color = '#475F77'
        
        self.barre_rect = pygame.Rect(self.barre_pos,((width/5)*3,(10)))
        self.curseur_rect = pygame.Rect(self.curseur_pos,((width/10),height))

		# bottom rectangle 
        self.bottom_rect_moins = pygame.Rect(pos,(width/5,height))
        self.bottom_rect_plus = pygame.Rect(self.pos_plus,(width/5,height))
        self.bottom_color = '#354B5E'
		#text
        self.text_moins = "-"
        self.text_plus = "+"
        self.val_curseur = volume
        self.text_moins_surf = gui_font.render(self.text_moins,True,'#FFFFFF')
        self.text_plus_surf = gui_font.render(self.text_plus,True,'#FFFFFF')
        self.text_moins_rect = self.text_moins_surf.get_rect(center = self.top_rect_moins.center)
        self.text_plus_rect = self.text_plus_surf.get_rect(center = self.top_rect_plus.center)
        liste.append(self)

    def draw(self,screen):
		# elevation logic 
        self.top_rect_moins.y = self.original_y_pos - self.dynamic_moins
        self.top_rect_plus.y = self.original_y_plus - self.dynamic_plus
        self.text_moins_rect.center = self.top_rect_moins.center 
        self.text_plus_rect.center = self.top_rect_plus.center 

        self.bottom_rect_moins.midtop = self.top_rect_moins.midtop
        self.bottom_rect_plus.midtop = self.top_rect_plus.midtop
        
        self.bottom_rect_moins.height = self.top_rect_moins.height + self.dynamic_moins
        self.bottom_rect_plus.height = self.top_rect_plus.height + self.dynamic_plus

        pygame.draw.rect(screen,self.bottom_color, self.bottom_rect_moins,border_radius = 12)
        pygame.draw.rect(screen,self.bottom_color, self.bottom_rect_plus,border_radius = 12)

        pygame.draw.rect(screen,self.top_moins_color, self.top_rect_moins,border_radius = 12)
        pygame.draw.rect(screen,self.top_plus_color, self.top_rect_plus,border_radius = 12)

        pygame.draw.rect(screen,self.bottom_color,self.barre_rect)
        
        screen.blit(self.text_moins_surf, self.text_moins_rect)
        screen.blit(self.text_plus_surf, self.text_plus_rect)
        self.check_click()
        self.update(screen)

        pygame.draw.rect(screen,self.top_color,self.curseur_rect,border_radius = 12)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        
        if self.top_rect_moins.collidepoint(mouse_pos) and not self.pressed:
            self.top_moins_color = '#DE0B0B'
        elif not self.top_rect_moins.collidepoint(mouse_pos) and not self.pressed:
            self.dynamic_moins = self.elevation
            self.top_moins_color = '#94B3C1'
        elif self.top_rect_plus.collidepoint(mouse_pos) and not self.pressed:
            self.top_plus_color = '#DE0B0B'
        elif not self.top_rect_plus.collidepoint(mouse_pos) and not self.pressed:
            self.dynamic_plus = self.elevation
            self.top_plus_color = '#94B3C1'
            
    def update(self,screen):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.top_rect_moins.collidepoint(mouse_pos) and not self.top_rect_plus.collidepoint(mouse_pos):
            self.dynamic_moins = 0
            self.pressed = True
            self.top_moins_color = '#D74B4B'
            if self.curseur_pos_list[0] > (self.pos[0] + (self.width/5)):
                self.curseur_pos_list[0] -= 1
                self.curseur_pos = tuple(self.curseur_pos_list)
                self.curseur_rect = pygame.Rect(self.curseur_pos,((self.width/10),self.height))
                self.val_curseur = (self.curseur_pos_list[0] - self.barre_pos[0] +(self.width/20))/((self.width/5)*3)
            else:
                self.curseur_pos_list[0] -= 0
                self.curseur_pos = tuple(self.curseur_pos_list)
                self.curseur_rect = pygame.Rect(self.curseur_pos,((self.width/10),self.height))
                self.val_curseur = 0

            pygame.draw.rect(screen,self.top_color,self.curseur_rect,border_radius = 12)
            
        elif pygame.mouse.get_pressed()[0] and self.top_rect_plus.collidepoint(mouse_pos) and not self.top_rect_moins.collidepoint(mouse_pos):
            self.dynamic_plus = 0
            self.pressed = True
            self.top_plus_color = '#D74B4B'
            if self.curseur_pos_list[0] < (self.pos_plus[0] - (self.width/10)):
                self.curseur_pos_list[0] += 1
                self.curseur_pos = tuple(self.curseur_pos_list)
                self.curseur_rect = pygame.Rect(self.curseur_pos,((self.width/10),self.height))
                self.val_curseur = (self.curseur_pos_list[0] - self.barre_pos[0] +(self.width/20))/((self.width/5)*3)
            else:
                self.curseur_pos_list[0] += 0
                self.curseur_pos = tuple(self.curseur_pos_list)
                self.curseur_rect = pygame.Rect(self.curseur_pos,((self.width/10),self.height))
                self.val_curseur = 1
        else:
            self.dynamic_moins = self.elevation
            self.dynamic_plus = self.elevation
            self.top_plus_color = '#475F77'
            self.top_moins_color = '#475F77' 

class Affiche_texte:
    def __init__(self,text,width,height,pos,elevation,liste,screen,nom = "",saisie = False):
        
        self.name = nom
        self.saisie = saisie
        self.active = False
        self.user_text = text
        self.key = ""
        self.color_active = pygame.Color('lightskyblue3')
        self.click = -1

		#Core attributes 
        self.elevation = elevation
        self.original_y_pos = pos[1]
        self.screen = screen
        self.dynamic_elecation = elevation
        
		# top rectangle 
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#94B3C1'

		# bottom rectangle 
        self.bottom_rect = pygame.Rect(pos,(width,height))
        self.bottom_color = '#3D615E'
		#text
        if self.saisie:
            self.text = self.user_text
        else:
            self.text = text
        self.text_surf = gui_font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        liste.append(self)

    def change_text(self, newtext):
        self.text_surf = gui_font.render(newtext, True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self,screen):
		# elevation logic 
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center 

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 8)
        pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 8)

        if self.saisie :
            self.update_text()        
        screen.blit(self.text_surf, self.text_rect)
    
    def update_text(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.top_rect.collidepoint(mouse_pos) :
            self.click += 1
        else:
            self.dynamic_elecation = self.elevation         

            
        if (self.click%2) != 1:
            self.dynamic_elecation = 0
            self.active = True
            self.top_color = self.color_active
            self.bottom_color = '#DE0B0B'
            self.text_color = '#000000'
            for event in pygame.event.get():
  
                if event.type == pygame.KEYDOWN :
                                            
                    if event.key != pygame.K_RETURN:
                        
                        self.key = event.key
         
                        self.text = str(pygame.key.name(event.key))
                        
                        self.change_text(self.text) 
        else:
            self.active = False
            
        

