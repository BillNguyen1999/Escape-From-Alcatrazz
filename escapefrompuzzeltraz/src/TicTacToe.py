import pygame
import random
from button import Button
import time
from pygame.locals import *
from pygame.sprite import Sprite, Group

pygame.init()
clock = pygame.time.Clock()
screen_width = 600
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
back_button = Button(screen,"BACK")
replay_button = Button(screen,"Play Again")
pygame.display.set_caption('TicTacToe')
font = pygame.font.SysFont(None, 40)

markers = []
for x in range(3):
    row = [0] * 3
    markers.append(row)

rand_pos = [[0,0], [0,1], [0,2],
            [1,0], [1,1], [1,2],
            [2,0], [2,1], [2,2]]

clicked = False
pos = []
winner = 0
game_over = False
#define colors
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)

    pygame.draw.line(screen, grid, (150, 150), (450, 150), 6)
    pygame.draw.line(screen, grid, (150, 250), (450, 250), 6)
    
    pygame.draw.line(screen, grid, (250, 50), (250, 350), 6)
    pygame.draw.line(screen, grid, (350, 50), (350, 350), 6)

def draw_markers():
    y_pos = 0
    for y in markers:
        x_pos = 0
        for x in y:
            if x == 1:
                pygame.draw.line(screen, green, ((x_pos * 100) + 150 + 15, y_pos * 100 + 50 + 15), (x_pos * 100 + 150 + 85, y_pos * 100 + 50 + 85), 6)
                pygame.draw.line(screen, green, ((x_pos * 100) + 150 + 15, y_pos * 100 + 50 + 85), (x_pos * 100 + 150 + 85, y_pos * 100 + 50 + 15), 6)
            if x == -1:
                pygame.draw.circle(screen, red, (x_pos * 100 + 150 + 50, y_pos * 100 + 50 + 50), 38, 6)
            x_pos += 1
        y_pos += 1

def check_winner():
    global winner
    global game_over
    x_pos = 0
    for y in markers:
        #check columns
        if sum(y) == 3:
            winner = 1
            game_over = True
        if sum(y) == -3:
            winner = -1
            game_over = True
        #check rows
        if markers[0][x_pos] + markers[1][x_pos] + markers[2][x_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][x_pos] + markers[1][x_pos] + markers[2][x_pos] == -3:
            winner = -1
            game_over = True
        x_pos += 1

    #check cross
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3 :
        winner = 1
        game_over = True
    elif markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = -1
        game_over = True

def tictactoe(code, time_amount):
    from gameScreen import countdown
    global winner
    global game_over
    global clicked
    global markers
    global rand_pos
    global y
    global x
    y = None
    x = None
    player = 1

    ## timer
    clock_time = pygame.time.Clock()
    timer_font = pygame.font.Font(None, 38)
    rect = screen.get_rect()
    position = rect.centerx, 20
    timer = countdown.DisplayCountDown(time_amount, timer_font, pygame.Color("Black"), position, "midtop")
    timer_group = Group(timer.text)
    
    run = True
    while run:
        draw_grid()
        draw_markers()
        back_button.draw_button()
        replay_button.draw_button()

        ticks = pygame.time.get_ticks()
        timer.update(ticks)
        timer_group.draw(screen)

        #add event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                
                cell_x = pos[0]
                cell_y = pos[1]

                back = back_button.rect.collidepoint(cell_x, cell_y)
                if back:
                    run = False

                again = replay_button.rect.collidepoint(cell_x, cell_y)

                if game_over == False:
                    if (150 <= cell_x and cell_x < 250) and (50 <= cell_y and cell_y < 150):
                        x = 0; y = 0
                    elif (250 <= cell_x and cell_x < 350) and (50 <= cell_y and cell_y < 150):
                        x = 0; y = 1
                    elif (350 <= cell_x and cell_x < 450) and (50 <= cell_y and cell_y < 150):
                        x = 0; y = 2
                    elif (150 <= cell_x and cell_x < 250) and (150 <= cell_y and cell_y < 250):
                        x = 1; y = 0
                    elif (250 <= cell_x and cell_x < 350) and (150 <= cell_y and cell_y < 250):
                        x = 1; y = 1
                    elif (350 <= cell_x and cell_x < 450) and (150 <= cell_y and cell_y < 250):
                        x = 1; y = 2
                    elif (150 <= cell_x and cell_x < 250) and (250 <= cell_y and cell_y < 350):
                        x = 2; y = 0
                    elif (250 <= cell_x and cell_x < 350) and (250 <= cell_y and cell_y < 350):
                        x = 2; y = 1
                    elif (350 <= cell_x and cell_x < 450) and (250 <= cell_y and cell_y < 350):
                        x = 2; y = 2


                    if y != None and x != None:
                        if markers[x][y] == 0:
                            markers[x][y] = player
                            player *= -1

                    check_winner()
                    if (len(rand_pos) == 1 and winner == 0 and player == -1):
                        game_over = True
                        winner = -1
                    ### Computer
                    if (player == -1 and winner == 0): 
                        rand_index = random.randint(0,len(rand_pos) - 1)
                        rand_x = rand_pos[rand_index][0]
                        rand_y = rand_pos[rand_index][1]
                        while(markers[rand_x][rand_y] != 0):
                            if (len(rand_pos) == 1):
                                game_over = True
                                winner = -1
                            else:
                                rand_pos.remove([rand_x,rand_y])
                                rand_index = random.randint(0,len(rand_pos) - 1)
                                rand_x = rand_pos[rand_index][0]
                                rand_y = rand_pos[rand_index][1]
                        if (len(rand_pos) == 1):
                            game_over = True
                            winner = -1
                        else:
                            rand_pos.remove([rand_x,rand_y])
                            rand_index = random.randint(0,len(rand_pos) - 1)
                            markers[rand_x][rand_y] = -1
                            player *= -1
                    
                    check_winner()
                    

                if again:
                    player = 1
                    winner = 0
                    markers = []
                    game_over = False
                    for x in range(3):
                        row = [0] * 3
                        markers.append(row)

                    rand_pos = [[0,0], [0,1], [0,2],
                                [1,0], [1,1], [1,2],
                                [2,0], [2,1], [2,2]]
                
        if game_over == True and winner == 1:
            win_text = "You WON! Your Code is: " + code
            win_img = font.render(win_text, True, blue)
            screen.blit(win_img, (150, 400))
        elif (game_over == True and winner == -1) or time_amount <= 0:
            win_text = "You LOST! Try again quick" 
            win_img = font.render(win_text, True, red)
            screen.blit(win_img, (150, 400))
            
        pygame.display.update()

