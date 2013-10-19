'''
Created on May 20, 2013

@author: XVicarious
'''

import pygame, math
try:
    import android
except ImportError:
    android = None
    
# Import our objects
from Player import Player
from Enemy import Enemy
from EndPortal import EndPortal
from Control import Controller
from LoadLevel import Level, TileMapper, LoadLevel
from Screen import GameScreen, MenuButton

clock = pygame.time.Clock()

def main():
    pygame.init()
    print "start game!"
    
    if android:
        android.init()
        android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)
    
    mynative = pygame.display.list_modes()
    s_res = (mynative[0][0],mynative[0][1])
    screen = pygame.display.set_mode(s_res,pygame.FULLSCREEN)
    # Level Surface
    currentLevel = 0
    gameState = "splashScreen"
    print gameState
    scroll_x = 0
    scroll_y = 0
    if android:
        s = android.assets.open("bg.png")
    else: 
        s = "../assets/bg.png"
    stars = pygame.image.load(s).convert()
    
    #Get dem menu itemz
    if android:
        fontName = "PixAntiqua.ttf"
    else:
        fontName = "../assets/PixAntiqua.ttf"
    myFont = pygame.font.Font(fontName,36)
    color = (128,128,128)
    playButton = MenuButton(mynative[0][0]/2-288,mynative[0][1]/2,"Play")
    levelsButton = MenuButton(mynative[0][0]/2-144,mynative[0][1]/2+100,"Levels")
    quitButton = MenuButton(mynative[0][0]/2,mynative[0][1]/2+200,"Quit")
    playText = myFont.render(playButton.text,False,color)
    playRect = playText.get_rect()
    playRect.center = playButton.rect.center
    levelsText = myFont.render(levelsButton.text,False,color)
    levelsRect = levelsText.get_rect()
    levelsRect.center = levelsButton.rect.center
    quitText = myFont.render(quitButton.text,False,color)
    quitRect = quitText.get_rect()
    quitRect.center = quitButton.rect.center
    menuButtons = pygame.sprite.Group()
    menuButtons.add(playButton)
    menuButtons.add(levelsButton)
    menuButtons.add(quitButton)
    
    if android:
        # Setup Onscreen Controller
        minus96 = mynative[0][1]-96
        minus192 = mynative[0][1]-192
        minus288 = mynative[0][1]-288
        controllerList = pygame.sprite.Group()
        middle = Controller(96,minus192,"none")
        controllerList.add(middle)
        upArrow = Controller(96,minus288,"up")
        controllerList.add(upArrow)
        downArrow = Controller(96,minus96,"down")
        controllerList.add(downArrow)
        leftArrow = Controller(0,minus192,"left")
        controllerList.add(leftArrow)
        rightArrow = Controller(192,minus192,"right")
        controllerList.add(rightArrow)
        upleftArrow = Controller(0,minus288,"upleft")
        controllerList.add(upleftArrow)
        uprightArrow = Controller(192,minus288,"upright")
        controllerList.add(uprightArrow)
        downleftArrow = Controller(0,minus96,"downleft")
        controllerList.add(downleftArrow)
        downrightArrow = Controller(192,minus96,"downright")
        controllerList.add(downrightArrow)
            
    done = True
    
    if android:
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP])
    else:
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
        
    tickClock = 0
    
    dirties = None

    while done == True:
        
        if tickClock == 30:
            print math.floor(clock.get_fps()), gameState
            tickClock = 0
            
        tickClock += 1
        
        # Track event happening
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print "Quitting..."
                    done = False
            if gameState == "level":
                if android:
                    # Movement
                    if event.type == pygame.MOUSEMOTION:
                        mouse_pos = pygame.mouse.get_pos()
                        mousex,mousey = mouse_pos
                        if upArrow.rect.collidepoint(mouse_pos):
                            player.change_x = 0
                            player.change_y = -3
                        elif downArrow.rect.collidepoint(mouse_pos):
                            player.change_x = 0
                            player.change_y = 3
                        elif leftArrow.rect.collidepoint(mouse_pos):
                            player.change_x = -3
                            player.change_y = 0
                        elif rightArrow.rect.collidepoint(mouse_pos):
                            player.change_x = 3
                            player.change_y = 0
                        elif upleftArrow.rect.collidepoint(mouse_pos):
                            player.change_x = -3
                            player.change_y = -3
                        elif uprightArrow.rect.collidepoint(mouse_pos):
                            player.change_x = 3
                            player.change_y = -3
                        elif downleftArrow.rect.collidepoint(mouse_pos):
                            player.change_x = -3
                            player.change_y = 3
                        elif downrightArrow.rect.collidepoint(mouse_pos):
                            player.change_x = 3
                            player.change_y = 3
                        elif middle.rect.collidepoint(mouse_pos):
                            middle.rect.centerx,middle.rect.centery = mouse_pos
                            leftArrow.rect.centerx = mousex-96
                            leftArrow.rect.centery = mousey
                            rightArrow.rect.centerx = mousex+96
                            rightArrow.rect.centery = mousey
                            upArrow.rect.centerx = mousex
                            upArrow.rect.centery = mousey-96
                            downArrow.rect.centerx = mousex
                            downArrow.rect.centery = mousey+96
                            upleftArrow.rect.centerx = mousex-96
                            upleftArrow.rect.centery = mousey-96
                            uprightArrow.rect.centerx = mousex+96
                            uprightArrow.rect.centery = mousey-96
                            downleftArrow.rect.centerx = mousex-96
                            downleftArrow.rect.centery = mousey+96
                            downrightArrow.rect.centerx = mousex+96
                            downrightArrow.rect.centery = mousey+96
                        else:
                            player.change_x = 0
                            player.change_y = 0
                    elif event.type == pygame.MOUSEBUTTONUP:
                        player.change_x = 0
                        player.change_y = 0
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            player.changeSpeed(-3,0)
                        if event.key == pygame.K_RIGHT:
                            player.changeSpeed(3,0)
                        if event.key == pygame.K_UP:
                            player.changeSpeed(0,-3)
                        if event.key == pygame.K_DOWN:
                            player.changeSpeed(0,3)
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                            player.changeSpeed(3,0)
                        if event.key == pygame.K_RIGHT:
                            player.changeSpeed(-3,0)
                        if event.key == pygame.K_UP:
                            player.changeSpeed(0,3)
                        if event.key == pygame.K_DOWN:
                            player.changeSpeed(0,-3)
            elif gameState == "splashScreen":
                if event.type == pygame.MOUSEBUTTONUP:
                    gameState = "menuScreen"
            elif gameState == "menuScreen":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if playButton.rect.collidepoint(pygame.mouse.get_pos()):
                        gameState = "levelLoad"
                    elif quitButton.rect.collidepoint(pygame.mouse.get_pos()):
                        done = False
        
        if gameState == "splashScreen":
            if android:
                xv = android.assets.open("splash.png")
            else:
                xv = "../assets/splash.png"
            xvicarious = pygame.image.load(xv).convert()
            xvicarious = pygame.transform.scale(xvicarious,(mynative[0][0],mynative[0][1]))
            screen.blit(xvicarious,(0,0))
            pygame.display.flip()
        elif gameState == "levelLoad":
            currentLevel += 1
            paddedLevel = currentLevel.__str__().zfill(2)
            if (paddedLevel+".png") in android.assets.list():
                screen.fill((255,255,255))
                newLevel = LoadLevel(paddedLevel+".level")
                tMap = TileMapper(newLevel)
                myLevel = Level(paddedLevel+".png")
                player = tMap.player
                endPortal = tMap.endPortal
                level = pygame.Surface((640,416))
                level.blit(stars,(0,0))
                level.blit(myLevel.image,(0,0))
                gameLevel = GameScreen(level)
                dirties = []
                for e in tMap.enemyList:
                    dirties.append(e.rect)     
                gameLevel.drawScreen(screen,tMap,scroll_x,scroll_y)
                pygame.display.flip()
                gameState = "level"
            else:
                done = False
        elif gameState == "level":
            # Perform Updates
            if player.change_x or player.change_y:
                player.update(myLevel,tMap.enemyList)
                dirties.append(player.rect)
            for enemy in tMap.enemyList:
                enemy.update(myLevel)
            if endPortal.update(player):
                gameState = "levelLoad"
                
            # Draw
            gameLevel.drawScreen(screen,tMap,scroll_x,scroll_y)
            if android:
                controllerList.draw(screen)
            
            # Game Camera
            # Buggy, always starts on top, but works.
            if (player.rect.y >= 208):
                if (gameLevel.scroll_y_limit >= 3) and player.change_y > 0:
                    scroll_y += 3
            elif (player.rect.y <= 208):
                if (scroll_y > 0) and player.change_y < 0:
                    scroll_y -= 3
    
            pygame.display.update(dirties)
        elif gameState == "menuScreen":
            screen.fill((0,0,0))
            newLevel = LoadLevel("01.level")
            tMap = TileMapper(newLevel)
            myLevel = Level("01.png")
            endPortal = tMap.endPortal
            level = pygame.Surface((640,416))
            level.blit(stars,(0,0))
            level.blit(myLevel.image,(0,0))
            gameLevel = GameScreen(level)
            dirties = []
            for e in tMap.enemyList:
                dirties.append(e.rect)     
            gameLevel.drawScreen(screen,tMap,scroll_x,scroll_y)
            menuButtons.draw(screen)
            screen.blit(playText,playRect)
            screen.blit(levelsText,levelsRect)
            screen.blit(quitText,quitRect)
            pygame.display.flip()
        elif gameState == "levelSelect":
            foo = "bar"
            
        # Check if Android version is not focused, if so pause the game            
        if android:
            if android.check_pause():
                android.wait_for_resume()
                    
        clock.tick(30)

# This isn't run on Android.
if __name__ == "__main__":
    main()
