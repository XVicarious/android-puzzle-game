'''
Created on May 22, 2013

@author: XVicarious
'''

import pygame
try:
    import android
except ImportError:
    android = None
    

class Controller(pygame.sprite.Sprite):

    def __init__(self,x,y,direction):
        pygame.sprite.Sprite.__init__(self)
        if direction == "up":
            if android:
                sprite = android.assets.open("up.png")
            else:
                sprite = "../assets/up.png"
        elif direction == "down":
            if android:
                sprite = android.assets.open("down.png")
            else:
                sprite = "../assets/down.png"
        elif direction == "left":
            if android:
                sprite = android.assets.open("left.png")
            else:
                sprite = "../assets/left.png"
        elif direction == "right":
            if android:
                sprite = android.assets.open("right.png")
            else:
                sprite = "../assets/right.png"
        elif direction == "upleft":
            if android:
                sprite = android.assets.open("upleft.png")
            else:
                sprite = "../assets/upleft.png"
        elif direction == "upright":
            if android:
                sprite = android.assets.open("upright.png")
            else:
                sprite = "../assets/upright.png"
        elif direction == "downleft":
            if android:
                sprite = android.assets.open("downleft.png")
            else:
                sprite = "../assets/downleft.png"
        elif direction == "downright":
            if android:
                sprite = android.assets.open("downright.png")
            else:
                sprite = "../assets/downright.png"
        elif direction == "none":
            if android:
                sprite = android.assets.open("centered.png")
            else:
                sprite = "../assets/centered.png"
        self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
