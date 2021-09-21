import pygame,sys
from button_2 import Button
pygame.init()


from gameScreen import gameData

win = pygame.display.set_mode((600,500))
back_button=Button(win,"BACK")
info_button=Button(win,"Info")

def showInfo():
    
    textFont=pygame.font.Font(None,32)
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((600,500))
    red = (255,0,0)
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                back = back_button.rect.collidepoint(mouse_x, mouse_y)
                info = info_button.rect.collidepoint(mouse_x, mouse_y)
                if back:
                    running = False
      
        win.fill((0,0,0))
        info1 = textFont.render(gameData.info1, True, green, blue)
        info2 = textFont.render(gameData.info2, True, green, blue)
        info3 = textFont.render(gameData.info3, True, green, blue)
        

        # show text on screen
        win.blit(info1,(50, 200))
        win.blit(info2,(50, 240))
        win.blit(info3,(50, 280))

        # draw back button
        back_button.draw_button()

        pygame.display.flip()

        clock.tick(60)


def drawChallenege(win):
    image = gameData.image
    win.blit(image,(100,400,40,60))
    win.blit(image,(175,400,40,60))
    win.blit(image,(250,400,40,60))
    win.blit(image,(325,400,40,60))
    win.blit(image,(400,400,40,60)) 

def redrawGameWindow(player,win):
    # Add background the window
    win.blit(gameData.background, (0,0)) 
    drawChallenege(win)
    # draw escape door
    win.blit(gameData.escapeDoor,(520,400,40,60)) 
    #Draw player
    player.draw(win)

    # draw back button
    back_button.draw_button()

    # draw back button
    info_button.draw_button()

    pygame.display.update() 