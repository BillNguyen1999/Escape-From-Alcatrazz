import pygame
import os
from pygame.sprite import Sprite, Group
pygame.init()
from MinigameController import *
from gameScreen import gameData
from gameScreen import gameView
from TicTacToe import *
from Riddle import *
from puzzle import *
from snake import *
from gameScreen import gameValidationData


win = gameView.win
clock = pygame.time.Clock()
updateTime = 0
winning_key = gameValidationData.getWinningKey()

class character(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.velocity=8
        self.isJump=False
        self.jumpCount=10
        self.left=False
        self.right=False
        self.walkCount=0

    def draw(self,win):
        global walkCount
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if self.left:  
            win.blit(gameData.moveLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1                          
        elif self.right:
            win.blit(gameData.moveRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(gameData.standing, (self.x, self.y))
            self.walkCount = 0

# Create a player object
player = character(10,400,40,60)
mgc = MinigameController()
mgc.setMinigame(1, winning_key[0])
# user hits space to select a challenge
def selectChallenge():
    global updateTime
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_SPACE]):
        if(64<player.x<106):
            print("Challenge 1") 
            
            mgc.main(updateTime)
        elif(136<player.x<184):
            print("Challenge 2")
            tictactoe(winning_key[1], updateTime)
        elif(220<player.x<268):
            print("Challenge 3")
            riddle(winning_key[2], updateTime)
        elif(292<player.x<340):
            print("Challenge 4")
            puzzle(winning_key[3], updateTime)
        elif(364<player.x<418):
            print("Challenge 5")
            snake(winning_key[4], updateTime)

# when player wants to escape the room
def escapeRoom():
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_SPACE] and 450<player.x):
        print(player.x)
        from gameScreen import gameValidationController


# controlls the movement of the player
def movePlayer():
    keys = pygame.key.get_pressed()   

    if keys[pygame.K_LEFT] and player.x > player.velocity: 
        player.x -= player.velocity
        player.left = True
        player.right = False

    elif keys[pygame.K_RIGHT] and player.x < 600 - player.velocity - player.width:  
        player.x += player.velocity
        player.left = False
        player.right = True
        
    else: 
        player.left = False
        player.right = False
        player.walkCount = 0
        
    if not(player.isJump):
        if keys[pygame.K_SPACE]:
            player.isJump = True
            player.left = False
            player.right = False
            player.walkCount = 0
    else:
        if player.jumpCount >= -10:
            player.y -= (player.jumpCount * abs(player.jumpCount)) * 0.5
            player.jumpCount -= 1
        else: 
            player.jumpCount = 10
            player.isJump = False



def main(difficulty, time_amount):
    global updateTime
    print("This is difficulty:",difficulty)
    from gameScreen import countdown

    clock_time = pygame.time.Clock()
    rect = win.get_rect()
    delta = 0
    fps = 60
    timer_font = pygame.font.Font(None, 38)
    position = rect.centerx, 20
    timer = countdown.DisplayCountDown(time_amount, timer_font, pygame.Color("white"), position, "midtop")
    timer_group = Group(timer.text)
    # Run until the user asks to quit
    running = True
    while running:

        # 27 frames per second
        clock.tick(27)

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                back = gameView.back_button.rect.collidepoint(mouse_x, mouse_y)
                info = gameView.info_button.rect.collidepoint(mouse_x, mouse_y)
                if back:
                    running = False
                if info:
                    gameView.showInfo()

                

        escapeRoom()
        movePlayer()
        gameView.redrawGameWindow(player,win) 
        selectChallenge()

        ticks = pygame.time.get_ticks()
        timer.update(ticks)
 
        # Draw
        timer_group.draw(win)
 
        # Render to screen
        pygame.display.flip()
 
        # Sleep, Idle, and Delta
        delta = clock_time.tick(fps)
        updateTime = timer.current_time()

 


