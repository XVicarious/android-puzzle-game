'''
Created on May 20, 2013

@author: XVicarious
'''

import pygame

try:
    import android
except ImportError:
    android = None
    
class Player(pygame.sprite.DirtySprite):
    
    change_x = 0
    change_y = 0
    
    origin_x = 0
    origin_y = 0
    
    def __init__(self,x,y,scale = 1):
        pygame.sprite.DirtySprite.__init__(self)
        if android:
            sprite = android.assets.open("player.png")
        else:
            sprite = "../assets/player.png"
        self.image = pygame.image.load(sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*scale,self.image.get_height()*scale))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.origin_x = x
        self.rect.y = y
        self.origin_y = y
        self.mask = pygame.mask.from_surface(self.image)
    def changeSpeed(self,x,y):
        self.change_x += x
        self.change_y += y
    def update(self,wall,enemies):
        old_x = self.rect.x
        old_y = self.rect.y
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if pygame.sprite.collide_mask(self,wall):
                self.rect.x = old_x
                self.rect.y = old_y
        for anEnemy in enemies:
            if pygame.sprite.collide_mask(self,anEnemy):
                self.death()
      
    def death(self):
        self.rect.x = self.origin_x
        self.rect.y = self.origin_y
