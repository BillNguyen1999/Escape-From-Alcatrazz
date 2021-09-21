from MinigameData import *
from MinigameView import *
from MgValidationController import *
from pygame.sprite import Sprite, Group
import pygame, sys
pygame.init()
clock = pygame.time.Clock()
class MinigameController:
    def __init__(self):
        self.mgd = MinigameData()
        self.mgv = MinigameView()
        
        
        
    def setMinigame(self, minigameNum, key):
        if(minigameNum == 1):
            self.mgd = makeMinigame1()
            self.mgd.key = key
            self.mgvc = MgValidationController(self.mgd)
    
    def listener(self):
        self.MovePlayer()

    def updatePositions(self):
        self.mgd.player.updatePlayer(self.mgd)
        
        for enemy in self.mgd.enemies:
            enemy.updateEnemy()

    def display(self):
        self.mgv.setupScreen()
        self.mgv.drawMinigame(self.mgd)
        self.mgv.updatePygame(self.mgd)

    def restart(self):
        self.mgd.playing = True
        if(self.mgd.minigameNum == 1):
            self.mgd = makeMinigame1()
    
    def exit(self):
        self.mgd.running = False

    def detectCollisions(self):
        for enemy in self.mgd.enemies:
            if(enemy.x == self.mgd.player.x and enemy.y == self.mgd.player.y):
                self.mgd.lives -= 1
        
        if(self.mgd.item.x == self.mgd.player.x and self.mgd.item.y == self.mgd.player.y):
            self.mgd.won = True
            self.mgd.playing = False
        if(self.mgd.lives == 0):
            self.mgd.playing = False
        return "no event"
        
        

    def main(self, time_amount):
        self.mgd.running = True
        i = 0
        from gameScreen import countdown

        clock_time = pygame.time.Clock()
        rect = win.get_rect()
        delta = 0
        fps = 60
        timer_font = pygame.font.Font(None, 38)
        position = rect.centerx, 20
        timer = countdown.DisplayCountDown(time_amount, timer_font, pygame.Color("white"), position, "midtop")
        timer_group = Group(timer.text)
        while self.mgd.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.mgd.running = False
                    sys.exit()
                
            # Did the user click the window close button?
            if(self.mgd.minigameNum == 1):
                clock.tick(8)
                if(not(self.mgd.won) and self.mgd.playing):
                    self.listener()
                    self.updatePositions()
                    self.detectCollisions()
                    self.display()
                elif(self.mgd.won):
                    self.mgvc.setStatus("winning")
                    self.mgvc.main(self)
                elif(not(self.mgd.won) and not(self.mgd.playing)):
                    self.mgvc.setStatus("losing")
                    self.mgvc.main(self)
                #to display timer in minigame
                ticks = pygame.time.get_ticks()
                timer.update(ticks)
            
                    # Draw
                timer_group.draw(win)
            
                    # Render to screen
                pygame.display.flip()
            
                    # Sleep, Idle, and Delta
                delta = clock_time.tick(fps)
                
    

    def MovePlayer(self): #mg1
        
            keys = pygame.key.get_pressed()   

            if keys[pygame.K_LEFT]:
                self.mgd.player.left = True
            else:
                self.mgd.player.left = False
            if keys[pygame.K_RIGHT]:
                self.mgd.player.right = True
            else:
                self.mgd.player.right = False
            if keys[pygame.K_UP]:
                self.mgd.player.up = True
            else:
                self.mgd.player.up = False
            if keys[pygame.K_DOWN]:
                self.mgd.player.down = True
            else:
                self.mgd.player.down = False

    

