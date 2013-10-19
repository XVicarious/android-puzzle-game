'''
Created on Jun 3, 2013

@author: xvicarious
'''

import pygame

try:
    import android
except ImportError:
    android = None
    
class GameScreen(object):
    
    mynative = None
    drawnScreen = None
    levelSurf = None
    newHeight = None
    scroll_y_limit = None

    def __init__(self, levelSurface):
        self.mynative = pygame.display.list_modes()
        self.newHeight = (416*self.mynative[0][0])/640
        self.levelSurf = levelSurface
        self.drawnScreen = levelSurface.copy()
        
    def drawScreen(self,screen,tMap,scroll_x,scroll_y):
        self.drawnScreen.blit(self.levelSurf,(0,0))
        tMap.enemyList.draw(self.drawnScreen)
        tMap.extraList.draw(self.drawnScreen)
        levelScaled = pygame.transform.scale(self.drawnScreen,(self.mynative[0][0],(416*self.mynative[0][0])/640))
        self.scroll_y_limit = self.newHeight - (self.mynative[0][1] + scroll_y)
        subSurfLevel = levelScaled.subsurface((scroll_x, scroll_y, self.mynative[0][0], self.mynative[0][1]))
        screen.blit(subSurfLevel,(0,0))
        
class MenuScreen(object):
    
    # Full menu, like the first menu!
    def __init__(self):
        # do nothing as of now!
        self.mynative = pygame.display.list_modes()
        self.newHeight = (416*self.mynative[0][0])/640

class MenuButton(pygame.sprite.Sprite):
    
    def __init__(self,x,y,text):
        pygame.sprite.Sprite.__init__(self)
        if android:
            sprite = android.assets.open("button.png")
        else:
            sprite = "../assets/button.png"
        self.image = pygame.image.load(sprite).convert_alpha()
        self.text = text
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

