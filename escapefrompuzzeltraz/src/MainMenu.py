import pygame
import pygame_menu

pygame.init()

surface = pygame.display.set_mode((600,500))
DIFFICULTY = ['EASY']

def set_difficulty(value, difficulty):
    selected, index = value
    print('Selected difficulty: "{0}" ({1}) at index {2}'
          ''.format(selected, difficulty, index))
    DIFFICULTY[0] = difficulty

def start_the_game(difficulty):
    from gameScreen import gameController
    assert isinstance(difficulty, list)
    difficulty = difficulty[0]
    assert isinstance(difficulty, str)

    if difficulty == 'EASY':
        timer = 900
        gameController.main(difficulty, timer)
        print("Successfully setup EASY")
    elif difficulty == 'MEDIUM':
        timer = 600
        gameController.main(difficulty, timer)
        print("Successfully setup MEDIUM")
    elif difficulty == 'HARD':
        timer = 300
        gameController.main(difficulty, timer)
        print("Successfully setup HARD")
    else:
        raise Exception('unknown difficulty {0}'.format(difficulty))

menu = pygame_menu.Menu(300, 400, 'Welcome To:',
                       theme=pygame_menu.themes.THEME_DARK)

# menu.add.text_input('Name :', default='John Doe')
menu.add.label('Escape From Puzzletraz', font_color=(204,0,0))
menu.add.selector('Difficulty :', [('Easy', 'EASY'), ('Medium', 'MEDIUM'), ('Hard', 'HARD')], onchange=set_difficulty, selector_id='select_difficulty')
menu.add.button('Play', start_the_game, DIFFICULTY, font_color=(204,0,0))
menu.add.button('Quit', pygame_menu.events.EXIT, font_color=(204,0,0))
menu.mainloop(surface)