# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 11:04:19 2021

@author: ic2140
"""
import pygame

pygame.init()
screen = pygame.display.set_mode([1000,800])
screen.fill((0,0,0))
'''
pressed_keys = pygame.key_pressed()
'''
running = True

surf = pygame.Surface((100,100))
surf.fill((255,255,255))
rect = surf.get_rect()
screen.blit(surf,(450,350))
pygame.display.flip()

while running:
        for event in pygame.event.get():
            if event.type ==KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                    running = False
        
        
        
pygame.quit()

