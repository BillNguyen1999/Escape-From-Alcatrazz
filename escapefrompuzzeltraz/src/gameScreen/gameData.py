import pygame
pygame.init()

from pygame.sprite import Sprite, Group



# This class handles sprite sheets
# This was taken from www.scriptefun.com/transcript-2-using
# sprite-sheets-and-drawing-the-background
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)
class spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error:
            print ('Unable to load spritesheet image:', filename)
            raise SystemExit
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image





moveRight = [pygame.image.load('image/R1.png'), pygame.image.load('image/R2.png'), pygame.image.load('image/R3.png'), pygame.image.load('image/R4.png'), pygame.image.load('image/R5.png'), pygame.image.load('image/R6.png'), pygame.image.load('image/R7.png'), pygame.image.load('image/R8.png'), pygame.image.load('image/R9.png')]
moveLeft = [pygame.image.load('image/L1.png'), pygame.image.load('image/L2.png'), pygame.image.load('image/L3.png'), pygame.image.load('image/L4.png'), pygame.image.load('image/L5.png'), pygame.image.load('image/L6.png'), pygame.image.load('image/L7.png'), pygame.image.load('image/L8.png'), pygame.image.load('image/L9.png')]
background = pygame.image.load('image/bg.jpg')
standing = pygame.image.load('image/standing.png')
ss = spritesheet('image/tiles_spritesheet.png')
image = ss.image_at((792, 850, 45, 80))
escapeDoor = ss.image_at((650, 410, 65, 80))
info1="Press spacebar to enter challenge/escape door"
info2="Win each challenege to get escape key"
info3="Enter escape key in order to escape room"