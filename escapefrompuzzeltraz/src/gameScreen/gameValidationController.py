import pygame,sys
from gameScreen import gameValidationData
pygame.init()



# gamevalidation controller

win = pygame.display.set_mode((600,500))
clock = pygame.time.Clock()
textFont=pygame.font.Font(None,32)
textFont2=pygame.font.Font(None,42)

userText=''

# text box
textBox = pygame.Rect(260,250,140,32)
color = (255,0,0)
red = (255,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


def finalMessage(win,key):
    gameLost="YOU LOST !!"
    gameWin = "YOU WIN !!"
    if (key==gameValidationData.getWinningKey()):
        message = textFont.render(gameWin, True, green, blue) 
    else:
        message = textFont.render(gameLost, True, red, blue)

    win.blit(message,(240, 350))

running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and len(userText)<5:
                userText = userText[:-1]
            else:
                if(len(userText)<5):
                    userText += event.unicode
                    
  

    # Fill the screen black after space is selected
    win.fill((0,0,0))

    # Create text box
    pygame.draw.rect(win,color,textBox,2)

    heading = textFont.render('Enter Key To Escape', True, green, blue)
    textScreen = textFont.render(userText,True,(255,255,255))
    
    # show text on screen
    win.blit(heading,(190, 200))
    win.blit(textScreen,(textBox.x + 5, textBox.y + 5))

    textBox.w = max(80,textScreen.get_width() +10)

    if(len(userText)==5):
        finalMessage(win,userText)


    pygame.display.flip()

    clock.tick(60)