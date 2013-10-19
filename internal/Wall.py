'''
Created on May 21, 2013

@author: XVicarious
'''

import pygame

try:
    import android
except ImportError:
    android = None

class Wall(pygame.sprite.Sprite):

    def __init__(self,x,y,scale,t = 0):
        pygame.sprite.Sprite.__init__(self)
        if t == 0:
            if android:
                sprite = android.assets.open("wall.png")
            else:
                sprite = "../assets/wall.png"
        elif t == 1:
            if android:
                sprite = android.assets.open("ubridge.png")
            else:
                sprite = "../assets/ubridge.png"
        elif t == 2:
            if android:
                sprite = android.assets.open("ubridge2.png")
            else:
                sprite = "../assets/ubridge2.png"
        self.image = pygame.image.load(sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*scale,self.image.get_height()*scale))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)