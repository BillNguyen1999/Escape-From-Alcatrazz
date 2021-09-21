import pygame
from MinigameView import Colour

win = pygame.display.set_mode((600,500))
textFont=pygame.font.Font(None,30)


class MgValidationView:
    def __init__(self):
        win.fill(Colour.black)

    def drawScreen(self, won, key):
        win.fill(Colour.black)
        if(won):
            self.drawWin(key)
        else:
            self.drawLoss()
        
        press_e = "Press E to exit"
        display = textFont.render(press_e, True, Colour.red)
        win.blit(display,(200,300))
    
    def drawWin(self, key):
        message = "Congratulations, You won the minigame. Your letter is: " + key
        display = textFont.render(message, True, Colour.green)
        win.blit(display,(25,200))

    
    def drawLoss(self):
        message = "Minigame Failed"
        display = textFont.render(message, True, Colour.red)
        win.blit(display,(200,200))

        press_r = "Press R to restart"
        display = textFont.render(press_r, True, Colour.red)
        win.blit(display,(200,400))
    def updatePygame(self):
        
        pygame.display.update()


        

        