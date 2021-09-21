import pygame.font
 
window_width = 600
window_height = 500

class Button():
    def __init__(self, window, msg):
        self.window = window
        self.window_rect = self.window.get_rect()
        self.width = 100
        if msg == "Play Again":
            self.width = 200
        self.height = 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        if msg == "Play Again":
            self.rect = pygame.Rect(400, 0, self.width, self.height)
        if msg == "RETURN":
            self.rect.center = (window_width/2, window_height - 400)
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.rect.center
        
    def draw_button(self):
        self.window.fill(self.button_color, self.rect)
        self.window.blit(self.msg_image, self.msg_rect)