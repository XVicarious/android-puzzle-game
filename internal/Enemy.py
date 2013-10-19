import pygame
try:
    import android
except ImportError:
    android = None
    
class Enemy(pygame.sprite.DirtySprite):
    
    change_x = 0
    change_y = 0
    enemy_type = 0
    
    def __init__(self,x,y,etype,scale):
        pygame.sprite.DirtySprite.__init__(self)
        if etype == 0:
            if android:
                sprite = android.assets.open("enemy_horz.png")
            else:
                sprite = "../assets/enemy_horz.png"
        elif etype == 1:
            if android:
                sprite = android.assets.open("fastenemy_horz.png")
            else:
                sprite = "../assets/fastenemy_horz.png"
        elif etype == 2:
            if android:
                sprite = android.assets.open("enemy_vert.png")
            else:
                sprite = "../assets/enemy_vert.png"
        elif etype == 3:
            if android:
                sprite = android.assets.open("fastenemy_vert.png")
            else:
                sprite = "../assets/fastenemy_vert.png"
        self.image = pygame.image.load(sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*scale,self.image.get_height()*scale))
        self.rect = self.image.get_rect()
        self.rect.x = x + 3
        self.rect.y = y + 3
        self.mask = pygame.mask.from_surface(self.image)
        self.enemy_type = etype
        if self.enemy_type == 0:
            self.change_x = -6
        elif self.enemy_type == 1:
            self.change_x = -12
        elif self.enemy_type == 2:
            self.change_y = -6
        elif self.enemy_type == 3:
            self.change_y = -12
    def update(self,wall):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if pygame.sprite.collide_mask(self, wall):
            self.change_x *= -1
            self.change_y *= -1
            self.rect.x += self.change_x
            self.rect.y += self.change_y
        self.dirty = 1