import pygame
import sys
import random
from pygame.locals import *
from button_2 import Button
import time
from pygame.sprite import Sprite, Group

#Constants
window_width = 600
window_height = 500
white = (255, 255, 255)
blue = (0, 0, 128)
green = (0, 255, 0)
black = (0, 0, 0)
cell_each_size = 3
total_cell = cell_each_size*cell_each_size
shuffle = 30
text_size = 32
win_game = False

pygame.init()
#set up window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Puzzle")
#load image
puzzle_image = pygame.image.load('minion.jpg')
puzzle_image = pygame.transform.scale(puzzle_image, (window_width, window_height))

cell_width = int(window_width / cell_each_size)
cell_height = int(window_height / cell_each_size)

#create button
back_button=Button(window,"BACK")

#Generate a board with a cut-off picture
def randomBoard():
    board = []
    for i in range(total_cell):
        board.append(i)
    last = total_cell - 1
    board[last] = -1

    for i in range(shuffle):
        direct = random.randint(1, 4)
        if (direct == 1):
           last = up(board,last)
        elif (direct == 2):
           last = down(board,last)
        elif (direct == 3):
           last = left(board,last)
        elif (direct == 4):
           last = right(board,last)
    return board, last

def up(board, last):
    if last >= total_cell-cell_each_size:
        return last
    new = last+cell_each_size
    board[new], board[last] = board[last], board[new]
    return new

def down(board, last):
    if last < cell_each_size:
        return last
    new = last-cell_each_size
    board[new], board[last] = board[last], board[new]
    return new

def left(board, last):
    if last % cell_each_size == cell_each_size-1:
        return last
    board[last+1], board[last] = board[last], board[last+1]
    return last+1

def right(board, last):
    if last % cell_each_size == 0:
        return last
    board[last-1], board[last] = board[last], board[last-1]
    return last-1

#winning condition
def is_win_game(board, last):
    for i in range(total_cell-1):
        if board[i] != i:
            return False
    return True

def puzzle(code, time_amount):
    from gameScreen import countdown
    global win_game
    ## timer
    clock_time = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 32)
    rect = window.get_rect()
    position = rect.centerx, 20
    timer = countdown.DisplayCountDown(time_amount, font, pygame.Color("Black"), position, "midtop")
    timer_group = Group(timer.text)

    gameBoard, last = randomBoard()
    start_game = True
    #game loop
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
                if back and start_game:
                    start_game = False
            if win_game:
                continue
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                col = int(x / cell_width)
                row = int(y / cell_height)
                index = col + row*cell_each_size
                if (index == last-1 or index == last+1 or index == last-cell_each_size or index == last+cell_each_size):
                    gameBoard[last], gameBoard[index] = gameBoard[index], gameBoard[last]
                    last = index
   
        #display the winning code
        if (is_win_game(gameBoard, last) or win_game):
            win_game = True 
            #winning message
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render('The winning code is '+ code, True, green, blue)
            textRect = text.get_rect()
            textRect.center = (window_width // 2, window_height // 2)
            window.fill(white)
            window.blit(text, textRect)
            back_button.draw_button()
            pygame.display.update()
            continue

        #display the image during the game
        window.fill(white)

        for i in range(total_cell):
            rowDst = int(i / cell_each_size)
            colDst = int(i % cell_each_size)
            rectDst = pygame.Rect(colDst*cell_width, rowDst *
                                cell_height, cell_width, cell_height)

            if gameBoard[i] == -1:
                continue

            rowArea = int(gameBoard[i] / cell_each_size)
            colArea = int(gameBoard[i] % cell_each_size)
            rectArea = pygame.Rect(
                colArea*cell_width, rowArea*cell_height, cell_width, cell_height)
            window.blit(puzzle_image, rectDst, rectArea)

        for i in range(cell_each_size+1):
            pygame.draw.line(window, last, (i*cell_width, 0),
                            (i*cell_width, window_height))
        for i in range(cell_each_size+1):
            pygame.draw.line(window, last, (0, i*cell_height),
                            (window_width, i*cell_height))

        back_button.draw_button()
        pygame.display.update()
        




