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
pygame.display.set_caption('Riddle')
font = pygame.font.SysFont(None, 40)
winner = 0
choice = None
game_over = False

clicked = False

#define colors
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
b1 = (0, 204, 204)
b2 = (0, 204, 204)
b3 = (0, 204, 204)
b4 = (0, 204, 204)
babyblue = (0, 204, 204)

q_and_a = [
    {"question": "If I drink, I die. If i eat, I am fine. What am I?", 
        "answer": "d", 
            "a": "Time", 
            "b": "Black Holes", 
            "c": "Sky", 
            "d": "Fire"},
    {"question": "What has a foot on each side and one in the middle?", 
        "answer": "b", 
            "a": "A baseball", 
            "b": "A yardstick", 
            "c": "A staff", 
            "d": "A wand"}, 
    {"question": "The more you take, the more you leave behind. What am I?", 
        "answer": "d", 
            "a": "Time", 
            "b": "Water", 
            "c": "Life", 
            "d": "Footsteps"} 
    ]


def draw_grid(qa):
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    font = pygame.font.SysFont(None, 30)
    text = font.render(qa['question'], True, grid)
    text_rect = text.get_rect(center=(screen_width/2, screen_height/4))
    screen.blit(text, text_rect)

    font = pygame.font.SysFont(None, 20)
    screen_rect = screen.get_rect()

    rect_1 = pygame.Rect(85, 250, 100, 50)
    msg_image1 = font.render(qa['a'], True, grid, b1)
    msg_rect1 = msg_image1.get_rect()
    msg_rect1.center = rect_1.center
    screen.fill(b1, rect_1)
    screen.blit(msg_image1, msg_rect1)

    rect_2 = pygame.Rect(200, 250, 100, 50)
    msg_image2 = font.render(qa['b'], True, grid, b2)
    msg_rect2 = msg_image2.get_rect()
    msg_rect2.center = rect_2.center
    screen.fill(b2, rect_2)
    screen.blit(msg_image2, msg_rect2)

    rect_3 = pygame.Rect(315, 250, 100, 50)
    msg_image3 = font.render(qa['c'], True, grid, b3)
    msg_rect3 = msg_image3.get_rect()
    msg_rect3.center = rect_3.center
    screen.fill(b3, rect_3)
    screen.blit(msg_image3, msg_rect3)

    rect_4 = pygame.Rect(430, 250, 100, 50)
    msg_image4 = font.render(qa['d'], True, grid, b4)
    msg_rect4 = msg_image4.get_rect()
    msg_rect4.center = rect_4.center
    screen.fill(b4, rect_4)
    screen.blit(msg_image4, msg_rect4)

    rect_5 = pygame.Rect(350, 400, 200, 50)
    msg_image5 = font.render("Choose and Press me", True, grid, (0,153,0))
    msg_rect5 = msg_image5.get_rect()
    msg_rect5.center = rect_5.center
    screen.fill((0,153,0), rect_5)
    screen.blit(msg_image5, msg_rect5)

def riddle(code, time_amount):
    from gameScreen import countdown
    global clicked
    global winner
    global game_over
    global b1
    global b2
    global b3
    global b4
    global choice
    ## timer
    clock_time = pygame.time.Clock()
    timer_font = pygame.font.Font(None, 38)
    rect = screen.get_rect()
    position = rect.centerx, 20
    timer = countdown.DisplayCountDown(time_amount, timer_font, pygame.Color("Black"), position, "midtop")
    timer_group = Group(timer.text)

    ## random question
    rand_index = random.randint(0,len(q_and_a) - 1)

    run = True
    while run:
        draw_grid(q_and_a[rand_index])
        back_button.draw_button()

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
                
                if game_over == False:
                    if (250 <= cell_y and cell_y <= 300):
                        if (85 <= cell_x and cell_x <= 185):
                            choice = 'a'
                            b1 = (0, 154, 0)
                            b2, b3, b4 = babyblue, babyblue, babyblue
                        elif (200 <= cell_x and cell_x <= 300):
                            choice = 'b'
                            b2 = (0, 154, 0)
                            b1, b3, b4 = babyblue, babyblue, babyblue
                        elif (315 <= cell_x and cell_x <= 415):
                            choice = 'c'
                            b3 = (0, 154, 0)
                            b1, b2, b4 = babyblue, babyblue, babyblue
                        elif (430 <= cell_x and cell_x <= 530):
                            choice = 'd'
                            b4 = (0, 154, 0)
                            b1, b2, b3 = babyblue, babyblue, babyblue
                    
                    if (400 <= cell_y and cell_y <= 450):
                        if (350 <= cell_x and cell_x <= 550):
                            if(choice == q_and_a[rand_index]['answer']):
                                print("you won")
                                winner = 1
                                game_over = True
                            else:
                                rand_index = random.randint(0,len(q_and_a) - 1)
                                winner = -1


        if winner == 1:
            win_text = "You WON! Your Code is: " + code
            win_img = font.render(win_text, True, blue)
            screen.blit(win_img, (100, 350))
        elif winner == -1 or time_amount <= 0:
            win_text = "Wrong! Try another question." 
            win_img = font.render(win_text, True, red)
            screen.blit(win_img, (100, 350))

        pygame.display.update()
