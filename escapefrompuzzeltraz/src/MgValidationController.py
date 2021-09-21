from MgValidationView import *
from MgValidationData import *
import sys
class MgValidationController:
    def __init__(self, mgd):
        self.mgvv = MgValidationView()
        self.mgvd = MgValidationData(mgd.key)
    
    
    def setStatus(self, status):
        self.mgvd.won = (status == "winning")


    def main(self, controller):
        running = True

        while(running):
            keys = pygame.key.get_pressed()  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                if keys[pygame.K_e]:
                    running = False
                    controller.exit()
                    # print("here")
                if(keys[pygame.K_r] and not(self.mgvd.won)):
                    running = False
                    controller.restart()
            self.mgvv.drawScreen(self.mgvd.won, self.mgvd.key)
            self.mgvv.updatePygame()
        

        
