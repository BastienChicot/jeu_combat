# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 12:13:44 2022

@author: basti
"""

def nivo_fight(sac,action,Gus,tr):
    gameExit=False
      
    a = 0
    gugus = gus_fight_right[0]
    rect_gugus = gugus.get_rect()
    frame_count = 0
    side = True
    animation = False
    type_anim ="none"

    fightr = fighter_1_r[0]
    
    fightrect = fightr.get_rect()
    
    lvl = lvl_fight[0]
    
    x = 150
    y = 230
    
    x2 = 300
    y2 = 214
    
    move_y = 0
    move_x = 0
    air_time = 1
    
    jump = False
    fall = False
    
    attack = False
    super_attack = False
    hit = False
    collision = False
    
    opp_clean = 0
    clean_hit = 0
    
    gus_life = 100
    fighter_life = 100
    
    clock = pygame.time.Clock()
    
    while not gameExit and Gus.level == 1000:
        
        sac.Planing = 0
        
        if Gus.pv > 0 and fighter_life > 0:
            if frame_count <= 60:
                frame_count += 1
            else:
                frame_count = 0
                animation = False
                type_anim = "none"
            
            if frame_count <= 15 and not animation:
                a=0
            elif 15 < frame_count <= 30 and not animation:
                a=1
            elif 30 < frame_count <= 45 and not animation:
                a=2
            elif 45 < frame_count <= 60 and not animation:
                a=3
    
            elif frame_count <= 15 and animation:
                a = 0
            elif 15 < frame_count <= 30 and animation:
                a = 1
            elif 30 < frame_count <= 45 and animation :
                a = 2
            elif 45 < frame_count <= 60 and animation:
                a = 3
                           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                   
                  # Condition becomes true when keyboard is pressed   
                if event.type == pygame.KEYDOWN:
       
                    if event.key == pygame.K_UP :
    
                        jump = True
                        
                    if event.key == pygame.K_DOWN :
                        fall = True
                        
                    if event.key == pygame.K_LEFT :
                        move_x = -2
                        side = False
                        
                    if event.key == pygame.K_RIGHT :
                        move_x = 2
                        side = True
                        
                    if event.key == pygame.K_a :
                        attack = True
                    if event.key == pygame.K_z :
                        super_attack = True         
                        
                if event.type == pygame.KEYUP:
       
                    if event.key == pygame.K_UP :
                        jump = False
                        
                    if event.key == pygame.K_DOWN :
                        fall = False
                        
                    if event.key == pygame.K_LEFT :
                        move_x = 0
    
                    if event.key == pygame.K_RIGHT :
                        move_x = 0
    
                    if event.key == pygame.K_a :
                        attack = False
                    if event.key == pygame.K_z :
                        super_attack = False
            
            if side:
                if type_anim == "none":
                    gugus=gus_fight_right[a]
                elif type_anim == "punch":
                    gugus = gus_pch_r[a]
                elif type_anim == "kick":
                    gugus = gus_kick_r[a]
                elif type_anim == "super_punch":
                    gugus = gus_sp_r[a]
                elif type_anim =="jump_punch":
                    gugus = gus_jp_r[a]
                elif type_anim =="adv_c2c":
                    gugus = gus_ouille_r[a]
                elif type_anim =="adv_sp":
                    gugus = gus_ouille_r[a]
    
            else:
                if type_anim == "none":
                    gugus=gus_fight_left[a]
                elif type_anim == "punch":
                    gugus = gus_pch_l[a]
                elif type_anim == "kick":
                    gugus = gus_kick_l[a]
                elif type_anim == "super_punch":
                    gugus = gus_sp_l[a]
                elif type_anim =="jump_punch":
                    gugus = gus_jp_l[a]
                elif type_anim =="adv_c2c":
                    gugus = gus_ouille_l[a]
                elif type_anim =="adv_sp":
                    gugus = gus_ouille_l[a]
                    
            if (y < 230 and not rect_gugus.colliderect(fightrect)) or jump :
                air_time += 1
     
            if jump : 
                move_y = -(30/air_time)
                
            if y < 230 and air_time > 30:
                move_y = 3
            elif y < 230 and fall :
                move_y = 5
            elif y >= 230 and not jump:
                move_y = 0
                y = 230
                jump = False
                air_time = 1
                
            if rect_gugus.colliderect(fightrect):
                if abs(rect_gugus.bottom - fightrect.top) <= 10 and move_y > 0:
                    move_y = 0
                    air_time = 1
                    jump = False
                if abs(rect_gugus.top - fightrect.bottom) <= 10 and move_y < 0:
                    move_y = 0
                if abs(rect_gugus.left - fightrect.right) <= 10 and move_x < 0:
                    move_x = 0             
                if abs(rect_gugus.right - fightrect.left) <= 10 and move_x > 0:
                    move_x = 0
    
    
            if abs(rect_gugus.right - fightrect.left) <= 80 and move_x > 0 and y2-20 < y < y2+20:
                if 50 < x2 < 400:
                    x2 += move_x/4
                elif x2 >= 400 :
                    x2 -= move_x
            if abs(rect_gugus.left - fightrect.right) <= 80 and move_x < 0 and y2-20 < y < y2+20:
                if 50 < x2 < 400:
                    x2 += move_x/4
                elif x2 <= 50 :
                    x2 -= move_x
                
            ##COUP SIMPLE AVEC A
            if abs(rect_gugus.left - fightrect.right) <= 5 and attack and move_x != 0:
                fighter_life -=5
                if clean_hit < 5:
                    clean_hit += 1
                x2 -= 20
                opp_clean = 0
                animation = True
                type_anim = "punch"
                frame_count = 1
            if abs(rect_gugus.right - fightrect.left) <= 5 and attack and move_x != 0:
                fighter_life -=5
                x2 += 20
                if clean_hit < 5:
                    clean_hit += 1
                opp_clean = 0
                animation = True
                type_anim = "punch"
                frame_count = 1
                
            ##COUP COMBO A ET Z
            if abs(rect_gugus.left - fightrect.right) <= 5 and attack and move_x != 0 and super_attack:
                fighter_life -= 10
                if clean_hit < 5:
                    clean_hit += 1
                x += 20
                opp_clean = 0
                animation = True
                type_anim = "kick"
                frame_count = 1
            if abs(rect_gugus.right - fightrect.left) <= 5 and attack and move_x != 0 and super_attack:
                fighter_life -= 10
                x -= 20
                if clean_hit < 5:
                    clean_hit += 1
                opp_clean = 0
                animation = True
                type_anim = "kick"
                frame_count = 1
    
            ##SUPER COUP AVEC Z
            if abs(rect_gugus.left - fightrect.right) <= 5 and super_attack and move_x != 0 and clean_hit >= 5:
                fighter_life -=15
                clean_hit = 0
                x2 -= 120
                opp_clean = 0
                animation = True
                type_anim = "super_punch"
                frame_count = 1
            if abs(rect_gugus.right - fightrect.left) <= 5 and super_attack and move_x != 0 and clean_hit >= 5:
                fighter_life -=15
                x2 += 120
                clean_hit = 0
                opp_clean = 0
                animation = True
                type_anim = "super_punch"
                frame_count = 1
                
            ##COUP SAUTE
            if abs(rect_gugus.left - fightrect.right) <= 15 and attack and 10 < air_time < 35:
                fighter_life -= 10
                if clean_hit < 5:
                    clean_hit += 1
                opp_clean = 0
                x2 -= 50
                animation = True
                type_anim = "jump_punch"
                frame_count = 1
                
            if abs(rect_gugus.right - fightrect.left) <= 15 and attack and 10 < air_time < 35:
                fighter_life -=10
                x2 += 50
                if clean_hit < 5:
                    clean_hit += 1
                opp_clean = 0
                animation = True
                type_anim = "jump_punch"
                frame_count = 1
                
            ##COUP ADVERSAIRE
            if rect_gugus.colliderect(fightrect):
                collision = True
            elif not rect_gugus.colliderect(fightrect):
                collision = False
                
            if collision and move_x == 0 and not attack and not jump:
                hit = True
            else:
                hit = False
    
            ##CORP A CORP           
            if abs(rect_gugus.left - fightrect.right) <= 1 and hit:
                Gus.pv -=5
                x += 80
                clean_hit = 0
                opp_clean += 1
                animation = True
                type_anim = "adv_c2c"
                frame_count = 1            
                
            if abs(rect_gugus.right - fightrect.left) <= 1 and hit:
                Gus.pv -=5
                x -= 80
                clean_hit = 0
                opp_clean += 1
                animation = True
                type_anim = "adv_c2c"
                frame_count = 1            
                
            ##SUPER COUP ADVERSAIRE
            if abs(rect_gugus.left - fightrect.right) <= 5 and hit and opp_clean == 3:
                Gus.pv -= 10
                x += 100
                clean_hit = 0
                opp_clean = 0
                animation = True
                type_anim = "adv_sp"
                frame_count = 1            
                
            if abs(rect_gugus.right - fightrect.left) <= 5 and hit and opp_clean == 3:
                Gus.pv -=10
                x -= 100
                clean_hit = 0
                opp_clean = 0
                animation = True
                type_anim = "adv_sp"
                frame_count = 1            
                
            ##COMBO ADVERSAIRE
            ##PROJECTILE??           
                    
            if move_x == 0 and not jump:
                if x2 > x and not collision and x2 > 50:
                    x2 -= 0.5
                    if type_anim == "none":
                        fightr = fighter_1_r[a]
                    elif type_anim == "adv_c2c":
                        fightr = fighter_pch_r[a]
                    elif type_anim == "adv_sp":
                        fightr = fighter_sp_r[a]
                    elif type_anim == "punch" or type_anim == "kick" or type_anim == "super_punch" or type_anim == "jump_punch":
                        fightr = fighter_ouille_r[a]
    
                elif x2 < x and not collision and x2 < 400:
                    x2 += 0.5
                    if type_anim == "none":
                        fightr = fighter_1_l[a]
                    elif type_anim == "adv_c2c":
                        fightr = fighter_pch_l[a]
                    elif type_anim == "adv_sp":
                        fightr = fighter_sp_l[a]
                    elif type_anim == "punch" or type_anim == "kick" or type_anim == "super_punch" or type_anim == "jump_punch":
                        fightr = fighter_ouille_l[a]
    
                else:
                    x2 = x2
                    if type_anim == "none" and side:
                        fightr = fighter_1_r[a]
                    elif type_anim == "none" and not side:
                        fightr = fighter_1_l[a]
                    elif type_anim == "adv_c2c" and side:
                        fightr = fighter_pch_r[a]
                    elif type_anim == "adv_c2c" and not side:
                        fightr = fighter_pch_l[a]
                    elif type_anim == "adv_sp" and side:
                        fightr = fighter_sp_r[a]
                    elif type_anim == "adv_sp" and not side:
                        fightr = fighter_sp_l[a]
                    elif (type_anim == "punch" or type_anim == "kick" or type_anim == "super_punch" or type_anim == "jump_punch") and side:
                        fightr = fighter_ouille_r[a]
                    elif (type_anim == "punch" or type_anim == "kick" or type_anim == "super_punch" or type_anim == "jump_punch") and not side:
                        fightr = fighter_ouille_l[a]
                       
            x += move_x
            y += move_y  
    
            if x > 450 :
                x=450
            if x < 0:
                x = 0
            if x2 > 480:
                x2 = 480
            if x2 < 20:
                x2 = 20
            
            screen.fill((0,0,0))
            
            rect_gugus.topleft = (x,y)        
            fightrect.topleft = (x2,y2)        
            
            lvl = lvl_fight[a]
            screen.blit(lvl,(0,0))
            screen.blit(gugus,rect_gugus)
            screen.blit(fightr,fightrect)
            
            clean_bar = power_bar[clean_hit]

            screen.blit(clean_bar,(20,70))
            
            pv = Gus_font.render("Santé : " + str(Gus.pv), False, (220, 220, 220))
            super_punch = Gus_font.render("Super power : ", False, (220, 220, 220))
            lvl = Gus_font.render("Niveau : FIGHT!", False, (220, 220, 220))
            frapper = Gus_font.render("Frapper", False, (220, 220, 220))
            control = Gus_font.render("(A et/ou Z) + flèches", False, (220, 220, 220))
        
            screen.blit(pv , (20,35))
            screen.blit(super_punch,(20,50))
            screen.blit(lvl , (20,95))
            screen.blit(frapper, (400,65))
            screen.blit(control, (360,95))
            
            textsurface = myfont.render(str(fighter_life), False, (210, 210, 210))
            screen.blit(textsurface,(460,35))
        
        elif Gus.pv <= 0 and fighter_life > 0:
            tr.clopesEst = 0 
            tr.clopes_nn = 0 
            tr.clope_metro = 0
            tr.clope_trome = 0
            tr.capote_nn = 0
            tr.capote_buro = 0
            tr.capote_entree = 0 
            tr.capoteNord = 0
            tr.capote_3 = 0
            tr.seringue_NE = 0
            tr.seringue_NO = 0
            tr.seringueN = 0
            tr.seringueO = 0
            tr.bouteille_NO = 0
            tr.bouteille_alc = 0
            tr.biere = 0
            tr.torchon_salon = 0
            tr.torchonsdb1 = 0
            tr.torchoncoul = 0
            tr.torchonch = 0
            tr.torchon_entre = 0
            tr.torchon_mom = 0
            
            sac.soupe_froide = 0
            sac.soupe_chaude = 0
            sac.Cle_maison = 0
            sac.Briquet = 0
            sac.Bonbons_bizarres = 0 
            sac.Ballon = 0
            
            sac.Telephone = 0
            sac.Clef = 0
            sac.Horaires_bus = 0
            sac.Portefeuille = 0
            sac.Photos = 0
            sac.Filtre_postillon = 0
            sac.Teuteu = 0
            sac.Huile_rateau = 0
            sac.Rythme = 0
            sac.Argent_mac = 0
            sac.Planing = 0
            sac.Papier = 0
            sac.Ticket = 0
            sac.Charisme = 0
            sac.Sandwich =0
            sac.Gateau = 0
            sac.Pince = 0
            sac.Carton = 0
            sac.Barre_Cereales = 0
               
            Gus.money = 0
            Gus.level = 5
            Gus.spawn = 1
            Gus.pv = 100
            
        elif Gus.pv > 0 and fighter_life <= 0:
            Gus.level = 5
            Gus.spawn = 1
            
        pygame.display.update()
        
        clock.tick(100)    