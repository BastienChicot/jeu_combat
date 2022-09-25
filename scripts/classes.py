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
        self.temps = 30
        self.selected = "none"

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
        
        self.name = nom 
        self.interact = False
        
        self.joueur = joueur
          
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
            self.saut = pygame.K_z
            self.descend = pygame.K_s
            self.gauche = pygame.K_q
            self.droite = pygame.K_d
        
            self.action = pygame.K_t
            self.coup = pygame.K_y
        elif self.joueur == 2:
            self.saut = pygame.K_UP
            self.descend = pygame.K_DOWN
            self.gauche = pygame.K_LEFT
            self.droite = pygame.K_RIGHT
        
            self.action = pygame.K_KP1
            self.coup = pygame.K_KP2
        
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
        if self.attack and not self.super_attack and self.clean_hit < 5:
            self.animation = True
            self.type_anim = "punch"
            frame_count = 1
        elif self.attack and self.super_attack and self.clean_hit < 5: 
            self.animation = True
            self.type_anim = "kick"
            frame_count = 1
        elif self.super_attack and self.move_x != 0 and self.clean_hit >= 5 and not self.attack:
            self.clean_hit = 0
            self.animation = True
            self.type_anim = "super_punch"
            frame_count = 1
        elif self.attack and 10 < self.air_time < 35 :
            self.animation = True
            self.type_anim = "jump_punch"
            frame_count = 1
            
        return(frame_count)
            
            
    def damage(self,perso_rect,perso_rect2,p2):
        if  abs(perso_rect.left - perso_rect2.right) <= 5 and self.attack and not self.super_attack and self.move_x != 0:
            if self.clean_hit < 5:
                self.clean_hit += 1
            p2.vie -=punch[self.name]
            p2.x -= 20
            p2.clean_hit = 0 
            p2.type_anim = "hit"              
        if  abs(perso_rect.right - perso_rect2.left) <= 5 and self.attack and not self.super_attack and self.move_x != 0:
            if self.clean_hit < 5:
                self.clean_hit += 1
            p2.vie -=punch[self.name]
            p2.x += 20
            p2.clean_hit = 0    
            p2.type_anim = "hit"              

        if  abs(perso_rect.left - perso_rect2.right) <= 5 and self.attack and not self.super_attack and self.move_x == 0:
            p2.vie -=punch[self.name]/2
            p2.x -= 5
            p2.type_anim = "hit"              
        if  abs(perso_rect.right - perso_rect2.left) <= 5 and self.attack and not self.super_attack and self.move_x == 0:
            p2.vie -=punch[self.name]/2
            p2.x += 5
            p2.type_anim = "hit"              
            
        if  abs(perso_rect.left - perso_rect2.right) <= 10 and self.attack and self.super_attack and self.move_x != 0:
            if self.clean_hit < 5:
                self.clean_hit += 1
            p2.vie -=kicks[self.name]
            p2.x -= 30
            p2.clean_hit = 0 
            p2.type_anim = "hit"              
        if  abs(perso_rect.right - perso_rect2.left) <= 10 and self.attack and self.super_attack and self.move_x != 0:
            if self.clean_hit < 5:
                self.clean_hit += 1
            p2.vie -=kicks[self.name]
            p2.x += 30
            p2.clean_hit = 0    
            p2.type_anim = "hit"              

        if  abs(perso_rect.left - perso_rect2.right) <= 5 and self.attack and self.super_attack and self.move_x == 0:
            p2.vie -=kicks[self.name]/2
            p2.x -= 5
            p2.type_anim = "hit"              
        if  abs(perso_rect.right - perso_rect2.left) <= 5 and self.attack and self.super_attack and self.move_x == 0:
            p2.vie -=kicks[self.name]/2
            p2.x += 5
            p2.type_anim = "hit"  
            
        if  abs(perso_rect.left - perso_rect2.right) <= 25 and not self.attack and self.super_attack and self.move_x != 0 and self.clean_hit >= 5:
            if self.clean_hit < 5:
                self.clean_hit += 1
            p2.vie -=supers[self.name]
            p2.x -= 50
            p2.clean_hit = 0 
            p2.type_anim = "hit"              
        if  abs(perso_rect.right - perso_rect2.left) <= 25 and not self.attack and self.super_attack and self.move_x != 0 and self.clean_hit >= 5:
            if self.clean_hit < 5:
                self.clean_hit += 1
            p2.vie -=supers[self.name]
            p2.x += 50
            p2.clean_hit = 0    
            p2.type_anim = "hit"              

        if  abs(perso_rect.left - perso_rect2.right) <= 15 and self.attack and 10 < self.air_time < 35:
            if self.clean_hit < 5:
                self.clean_hit += 1
            p2.vie -=sauter[self.name]
            p2.x -=10
            p2.clean_hit = 0 
            p2.type_anim = "hit"              
        if  abs(perso_rect.right - perso_rect2.left) <= 15 and self.attack and 10 < self.air_time < 35:
            if self.clean_hit < 5:
                self.clean_hit += 1
            p2.vie -=sauter[self.name]
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
    def __init__(self,image,pos,elevation,buttons,type_image):
        
        if type_image == "perso":
            self.path = "..\\_bank\\perso\\"+str(image)
            self.image = pygame.image.load(self.path+"\\"+str(image)+"_1.png")

        
        elif type_image == "niveau" :
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
            self.bottom_color = '#3D615E'
            self.text_color = '#000000'
        elif not self.rectangle.collidepoint(mouse_pos) and not self.pressed:
            self.dynamic_elecation = self.elevation
            self.bottom_color = '#16ACEA'
            self.text_color = '#FFFFFF'
            
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.rectangle.collidepoint(mouse_pos)and not self.pressed:
            self.dynamic_elecation = 0
            self.pressed = True
            self.bottom_color = '#3D615E'
            self.text_color = '#000000'
            
        elif pygame.mouse.get_pressed()[0] and self.rectangle.collidepoint(mouse_pos)and self.pressed:
            self.dynamic_elecation = 0
            self.pressed = False
            self.bottom_color = '#3D615E'
        else:
            self.dynamic_elecation = self.elevation
