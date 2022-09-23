# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 13:59:58 2022

@author: basti
"""
import pygame
from settings import *

class jeu():
    def __init__(self,nivo,mode):
        self.nivo = nivo
        self.mode = "arcade"
        self.temps = 30

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
    def __init__(self,nom,joueur,nivo):
        self.path = "..\\_bank\\perso\\"+str(nom)
          
        ##BASE
        self.pos1 = pygame.image.load(self.path+"\\"+str(nom)+"_1.png")
        self.pos2 = pygame.image.load(self.path+"\\"+str(nom)+"_2.png")

        self.pos1_l = pygame.transform.flip(self.pos1, True, False)
        self.pos2_l = pygame.transform.flip(self.pos2, True, False)
        
        self.fr = [self.pos1,self.pos2,self.pos1,self.pos2]
        self.fl = [self.pos1_l,self.pos2_l,self.pos1_l,self.pos2_l]
        
        self.start_pos = self.fr[0].get_rect()
        self.height = int(self.start_pos.height)

        self.limite = level_sol["practice"]-self.height
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
        self.saut = pygame.K_UP
        self.descend = pygame.K_DOWN
        self.gauche = pygame.K_LEFT
        self.droite = pygame.K_RIGHT
    
        self.action = pygame.K_a
        self.coup = pygame.K_z
        
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
        
        if joueur == 1:
            self.side = True
            self.x = 150
            self.y = level_sol["practice"]-self.height
            
        elif joueur == 2:
            self.side = False
            self.x = 300
            self.y = level_sol["practice"]-self.height

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
        

