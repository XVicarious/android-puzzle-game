'''
Created on May 21, 2013

@author: XVicarious
'''

import pygame

try:
    import android
except ImportError:
    android = None

class EndPortal(pygame.sprite.Sprite):

    def __init__(self,x,y):
        self._image = []
        if android:
            sprite = android.assets.open("endportal.png")
        else:
            sprite = "../assets/endportal.png"
        master_image = pygame.image.load(sprite).convert_alpha()
        master_width, master_height = master_image.get_size()
        self.image = master_image
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.origin_x = x
        self.rect.y = y
        self.origin_y = y
        self.mask = pygame.mask.from_surface(self.image)
    def update(self, player):
        return pygame.sprite.collide_mask(self, player)
    
            