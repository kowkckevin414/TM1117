# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 15:11:10 2021

@author: ic2140
"""

import pygame
import random
import math
from inputbox import InputBox
from pygame.locals import(
        RLEACCEL,
        K_UP,
        K_a,
        K_DOWN,
        K_LEFT,
        K_RIGHT,
        K_ESCAPE,
        KEYDOWN,
        MOUSEBUTTONDOWN,
        QUIT)


pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
pygame.mixer.init()
pygame.init()

SCREEN_HEIGHT=800
SCREEN_WIDTH=800
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
clock = pygame.time.Clock()
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY,250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)
pygame.mixer.music.load("game.mp3")
hitmp3 = pygame.mixer.Sound("hit.mp3")
hitmp2 = pygame.mixer.Sound("AYAYA.mp3")
pygame.mixer.music.play(loops=-1)
scorelist = {}

text = myfont.render('Play' , True , (100,100,100))
bulletsize = 30
level = [True,True,True]


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("jet.png").convert()  
        self.surf.set_colorkey((0,0,0),RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (bulletsize, bulletsize)) 
        self.rect = self.surf.get_rect(topleft=(0, 300))
        self.hp = 3
        self.hit = False
        self.timer = 0
        self.name = ""
        self.score = 0
    
    def reset(self):
        self.rect = self.surf.get_rect(topleft=(0, 300))
        self.hp = 3
        self.hit = False
        self.timer = 0
        self.name = ""
        self.score = 0
    
    def score_i(self):
        self.score +=1
    
    def setname(self,name):
        self.name=name
    
    def update(self, pressed_keys):           
        if self.hp > 0: 
            if pressed_keys[K_UP]:
                self.rect.move_ip(0,-5)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,5)    
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)    
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)
                
            if self.rect.left<= 0:
                self.rect.left=0
                self.surf = pygame.image.load("jet-red.png").convert()
                self.surf.set_colorkey((0,0,0),RLEACCEL)
                self.surf = pygame.transform.scale(self.surf, (50, 50)) 
            if self.rect.right>= SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
                self.surf = pygame.image.load("jet-red.png").convert()
                self.surf.set_colorkey((0,0,0),RLEACCEL)
                self.surf = pygame.transform.scale(self.surf, (50, 50)) 
            if self.rect.top<= 0:
                self.rect.top = 0
                self.surf = pygame.image.load("jet-red.png").convert()
                self.surf.set_colorkey((0,0,0),RLEACCEL)
                self.surf = pygame.transform.scale(self.surf, (50, 50)) 
            if self.rect.bottom>= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT
                self.surf = pygame.image.load("jet-red.png").convert()
                self.surf.set_colorkey((0,0,0),RLEACCEL)
                self.surf = pygame.transform.scale(self.surf, (50, 50)) 
                
        if self.hit:
            if (self.timer/500%2 == 0):
                self.surf = pygame.image.load("jet-red.png").convert()
                self.surf.set_colorkey((0,0,0),RLEACCEL)
                self.surf = pygame.transform.scale(self.surf, (50, 50)) 
            elif (self.timer/500%2 == 1):
                self.surf = pygame.image.load("jet.png").convert()
                self.surf.set_colorkey((0,0,0),RLEACCEL)
                self.surf = pygame.transform.scale(self.surf, (50, 50)) 
        else:
            self.surf = pygame.image.load("jet.png").convert()
            self.surf.set_colorkey((0,0,0),RLEACCEL)
            self.surf = pygame.transform.scale(self.surf, (50, 50)) 
 
class Bullet(pygame.sprite.Sprite):
    def __init__(self,w,y):
        super(Bullet,self).__init__()
        self.surf = pygame.image.load("bullet.png").convert()
        self.surf.set_colorkey((0,0,0),RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (bulletsize, bulletsize)) 
        self.rect = self.surf.get_rect(center=(
                w,y)
            )
        self.speed = 8
        
    def update(self):
        self.rect.move_ip(self.speed,0)
        if self.rect.right > SCREEN_WIDTH:
                self.kill()
    
    def sucide(self):
        self.kill()
 
class Enemy(pygame.sprite.Sprite):
    def __init__(self,xx):
        super(Enemy,self).__init__()
        self.surf = pygame.image.load("enemy.png").convert()
        self.surf.set_colorkey((0,0,0),RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (50, 50)) 
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH +20 , SCREEN_WIDTH +100),
                random.randint(50,SCREEN_HEIGHT),
            )
        )
        self.speed = xx
         
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
                self.kill()
    
    def sucide(self):
        hitmp2.play()
        self.kill()
                
                
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0,0,0),RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (50, 20)) 
        self.rect = self.surf.get_rect(
            center=(random.randint(SCREEN_WIDTH+20 , SCREEN_WIDTH+50),
                    random.randint(0,100),
                    )
            )
        self.speed = 5
        
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right <0:
                self.kill()

        
x = Player()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(x)
running = True
start = False;
input_box = InputBox(275,300,256,50,"")
while running:
    clock.tick(60)
    if start:
        for event in pygame.event.get():
            if event.type ==KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key==K_a:
                    bullet=Bullet(x.rect.x+50, x.rect.y+25)
                    bullets.add(bullet)
                    all_sprites.add(bullet)
                    
            elif event.type == QUIT:
                running = False  
            elif event.type == ADDENEMY:
                new_enemy = Enemy(5+math.log(1+x.score))
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            elif event.type == ADDCLOUD:
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)
                
        if x.timer < 5000 and x.hit:
            x.timer = x.timer + 60
        else:
            x.hit = False
            
        screen.fill((135,206,250))   
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        pressed_keys = pygame.key.get_pressed()
        
        if pygame.sprite.groupcollide(bullets,enemies,False,False):
            hitmp2.play()
            x.score_i()
            if scorelist[x.name] < x.score:
                scorelist[x.name] = x.score
            bulletsize = 30 + x.score//10
            pygame.sprite.groupcollide(bullets,enemies,True,True)
           
            
            
        if pygame.sprite.spritecollideany(x,enemies):
            pygame.sprite.spritecollideany(x,enemies).sucide()
            if (not x.hit):
                hitmp3.play()
                x.hp = x.hp - 1
                x.hit = True
                x.timer = 0
            if x.hp == 0:
                start = False
                x.reset()
                pygame.time.set_timer(ADDENEMY,250)
                level= [True,True,True]
        if x.score == 5 and level[0]:
            pygame.time.set_timer(ADDENEMY,200)
            level[0]=False
        if x.score == 10 and level[1]:
            level[1]=False
            pygame.time.set_timer(ADDENEMY,150)
        if x.score == 15 and level[2]:
            level[2]=False
            pygame.time.set_timer(ADDENEMY,100)        
        textsurface = myfont.render("{:<8}:{}     BULLET LEVEL: {}".format("HP",x.hp,x.score//10), False, (0, 0, 0))
        textsurface1 = myfont.render("{:<8}:{} ({})".format("SCORE",x.score,x.name), False, (0, 0, 0))
        screen.blit(textsurface,(100,0))
        screen.blit(textsurface1,(100,50))
        x.update(pressed_keys)
        enemies.update()
        clouds.update()
        bullets.update()
        pygame.display.flip()   
      
    else:
        count = 1
        screen.fill((135,206,250)) 
        if (scorelist.values()):
            for k in scorelist:
                a = myfont.render('{}.{:^16}:{}'.format(count,k,scorelist[k]) , True , (100,100,100))
                screen.blit(a , (275,435+25*count))
                count += 1
                if (count == 11):
                    break;
        else:
            a = myfont.render('No record' , True , (100,100,100))
            screen.blit(a , (325,435+20*count))
        pygame.draw.rect(screen,(170,170,170),[800/2-50,800/2,100,40])
        screen.blit(text , (800/2-25,800/2-5))
        input_box.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 800/2 <= mouse[0] <= 800/2+140 and 800/2 <= mouse[1] <= 800/2+40:
                    if not input_box.text == "":
                        start=True
                        x.setname(input_box.text)
                        if x.name in scorelist.keys():
                            pass
                        else:
                           scorelist[x.name]=0
            if event.type == pygame.KEYDOWN:
                input_box.update(event)
            elif event.type == QUIT:
                running = False  
        pygame.display.flip()  
        
pygame.quit()