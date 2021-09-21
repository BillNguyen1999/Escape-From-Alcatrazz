import pygame,sys
pygame.init()

win = pygame.display.set_mode((600,500))
clock = pygame.time.Clock()
textFont=pygame.font.Font(None,32)

red = (255,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                    
    # Fill the screen black after space is selected
    win.fill((0,0,0))

    #Create Heading
    heading = textFont.render('Game Over', True, red, white)

    #Display Heading
    win.blit(heading,(240, 200))

    pygame.display.flip()

    clock.tick(60)