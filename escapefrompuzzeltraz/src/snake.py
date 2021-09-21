import pygame
import sys
import random
from pygame.locals import *
from button_2 import Button
import time
from pygame.sprite import Sprite, Group


#constant
window_width = 600
window_height = 500
white = (255, 255, 255)
blue = (0, 0, 128)
green = (0, 255, 0)
black = (0, 0, 0)
pink = (255, 182, 193)
expected_score = 2
win_game = False

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake")

#create button
back_button=Button(window,"BACK")
reset_button=Button(window,"RETURN")

def isdead(snakePosition):
    return snakePosition[0] > 580 or snakePosition[0] < 0\
         or snakePosition[1] > 480 or snakePosition[1] < 0

def gameover(window, font, reset_button):
    window.fill(white)
    lost_mesg = font.render('You lost the game! ', True, white, black)
    lost_Rect = lost_mesg.get_rect()
    lost_Rect.center = (window_width/2, window_height/2)
    window.blit(lost_mesg, lost_Rect)
    reset_button.draw_button()
    pygame.display.update()

def move(direction, snakePosition):
    if direction == 'right':
        snakePosition[0] += 20
    if direction == 'left':
        snakePosition[0] -= 20
    if direction == 'up':
        snakePosition[1] -= 20
    if direction == 'down':
        snakePosition[1] += 20
    return snakePosition

def set_food(foodPostion, foodTotal):
    x = random.randrange(1, 30)
    y = random.randrange(3, 21)
    foodPostion = [int(x * 20), int(y * 20)]
    foodTotal = 1
    return foodPostion, foodTotal

def eatfood(snakePosition, foodPostion):
    return snakePosition[0] == foodPostion[0] and snakePosition[1] == foodPostion[1]

def is_win_game(score):
    if score >= expected_score:
        return True
    return False

def setup_game(snakePosition, snakeSegments, foodPostion, foodTotal, direction, changeDirection, score):
    snakePosition = [100, 100] 
    snakeSegments = [[100, 100], [80, 100]]
    foodPostion = [200, 200]
    foodTotal = 1
    direction = 'right'
    changeDirection = direction
    score = 0
    return snakePosition, snakeSegments, foodPostion, foodTotal, direction, changeDirection, score


def snake(code, time_amount):
    from gameScreen import countdown
    global win_game
    ## timer
    clock_time = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 32)
    rect = window.get_rect()
    position = rect.centerx, 20
    timer = countdown.DisplayCountDown(time_amount, font, white, position, "midtop")
    timer_group = Group(timer.text)

    snakePosition = [100, 100] 
    snakeSegments = [[100, 100], [80, 100]]
    foodPostion = [200, 200]
    foodTotal = 1
    direction = 'right'
    changeDirection = direction
    score = 0
    
    start_game = True
    loss_game = False
    #gameloop 
    while start_game:
        ticks = pygame.time.get_ticks()
        timer.update(ticks)
        timer_group.draw(window)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                back = back_button.rect.collidepoint(mouse_x, mouse_y)
                reset = reset_button.rect.collidepoint(mouse_x, mouse_y)
                if back and not loss_game:
                    start_game = False
                if reset and loss_game:
                    loss_game = False
                    snakePosition, snakeSegments, foodPostion, foodTotal, direction, changeDirection, score\
                     = setup_game(snakePosition, snakeSegments, foodPostion, foodTotal, direction, changeDirection, score)
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    changeDirection = 'right'
                if event.key == K_LEFT:
                    changeDirection = 'left'
                if event.key == K_UP:
                    changeDirection = 'up'
                if event.key == K_DOWN:
                    changeDirection = 'down'

        #display the winning code
        if (is_win_game(score) or win_game):
            win_game = True
            window.fill(white)
            #winning message
            text = font.render('The winning code is '+ code, True, green, blue)
            textRect = text.get_rect()
            textRect.center = (window_width // 2, window_height // 2)
            window.blit(text, textRect)
            back_button.draw_button()
            pygame.display.update()
            continue

        #snake is dead
        if (isdead(snakePosition)):
            loss_game = True
            gameover(window, font, reset_button)
            continue

        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection

        snakePosition =  move(direction, snakePosition)
        snakeSegments.insert(0, list(snakePosition))
        if eatfood(snakePosition, foodPostion):
            foodTotal = 0
            score += 1
        else:
            snakeSegments.pop()  

        #regenerate food
        if foodTotal == 0:
            foodPostion, foodTotal =  set_food(foodPostion, foodTotal)

        window.fill(black)
        for position in snakeSegments:  
            pygame.draw.rect(window, pink, Rect(position[0], position[1], 20, 20))
            pygame.draw.rect(window, blue, Rect(foodPostion[0], foodPostion[1], 20, 20))

        #display score
        score_msg = font.render('Score: '+ str(score), True, white, black)
        score_rect = score_msg.get_rect()
        score_rect.center = (window_width-100, window_height-50)
        window.blit(score_msg, score_rect)
        back_button.draw_button()
        pygame.display.update()

        clock.tick(10)
