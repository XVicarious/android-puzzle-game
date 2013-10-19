'''
Created on May 23, 2013

@author: XVicarious
'''
import base64, pygame
from Player import Player
from EndPortal import EndPortal
from Enemy import Enemy

try:
    import android
except ImportError:
    android = None
    
class LoadLevel(object):
    
    levelList = None
    
    def __init__(self, levelNumber):
        self.levelList = []
        if android:
            level64 = android.assets.open(levelNumber)
        else:
            level = "../assets/" + levelNumber
            level64 = open(level,'r')
        levelString = base64.standard_b64decode(level64.read())
        for line in levelString:
            for char in line:
                if char != '\r' and char != '\n':
                    self.levelList.append(char)
        
class TileMapper(object):

    enemyList = None
    extraList = None
    player = None
    endPortal = None
    
    def __init__(self,levelList,scale = 1):
        self.enemyList = pygame.sprite.Group()
        self.extraList = pygame.sprite.Group()
        self.enemyList.empty()
        self.extraList.empty()
        for i in range(0,13):
            for j in range(0,20):
                # 2 -- player
                # 3 -- Vertical Enemy
                # 4 -- Horizontal Enemy
                # 5 -- Fast Vertical Enemy
                # 6 -- Fast Horizontal Enemy
                if levelList.levelList[(i*20)+j] == '2':
                    self.player = Player(j*32,i*32,scale)
                    self.extraList.add(self.player)
                elif levelList.levelList[(i*20)+j] == '3':
                    self.enemyList.add(Enemy(j*32,i*32,2,scale))
                elif levelList.levelList[(i*20)+j] == '4':
                    self.enemyList.add(Enemy(j*32,i*32,0,scale))
                elif levelList.levelList[(i*20)+j] == '5':
                    self.enemyList.add(Enemy(j*32,i*32,3,scale))
                elif levelList.levelList[(i*20)+j] == '6':
                    self.enemyList.add(Enemy(j*32,i*32,1,scale))
                elif levelList.levelList[(i*20)+j] == '9':
                    self.endPortal = EndPortal(j*32,i*32)
                    self.extraList.add(self.endPortal)

class Level(pygame.sprite.Sprite):
    
    def __init__(self,image,levelData = None):
        pygame.sprite.Sprite.__init__(self)
        if android:
            sprite = android.assets.open(image)
        else:
            sprite = "../assets/" + image
        self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
