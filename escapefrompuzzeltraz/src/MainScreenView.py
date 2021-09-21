import pygame

WIDTH,HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape From PuzzleTraz")
pygame.init()

BLUE = (0,0,255)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(BLUE)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()

        
