import pygame
import random
import math 
from engine import Creature

pygame.init()

# global variables
CELL_NUMBER = 10
SQ_SIZE = 50
FOV_HEIGHT = 3
FOV_WIDTH = 3
MAX_NUM_ROUNDS = 10
PENELTY_MISSING = 10
PENELTY_TOO_MANY = 5
PIXEL_OFFSET = 20

WIDTH, HEIGHT = SQ_SIZE * CELL_NUMBER, SQ_SIZE * CELL_NUMBER
WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
pygame.display.set_caption("Zombieland - Multiplayer Version")

# cursor
targeting_cursor = pygame.cursors.Cursor(pygame.cursors.broken_x)
default_cursor = pygame.cursors.Cursor(pygame.cursors.arrow)

# colours
GREY = (40, 50, 60)
BLACK = (0, 0, 0)
GREEN = (50, 200, 150)
YELLOW = (250, 250, 0)
WHITE = (255, 255, 255)
MONITOR_GREEN = (175, 225, 175)

# fonts
font40 = pygame.font.SysFont('agencyfb', 40, bold=True)
font25 = pygame.font.SysFont('agencyfb', 25, bold=True)

# flashlights
flashlight = pygame.image.load('flashlight.png')
flashlight = pygame.transform.scale(flashlight, (150, 150))
flashlight_small = pygame.transform.scale(flashlight, (100, 100))

# buttons
button_flashlight = flashlight.get_rect()
button_flashlight_small = flashlight_small.get_rect()
button_light_on_off = pygame.Rect(600, 425, 140, 60)


# draw grid
def draw_grid(left = 0, top = 0):
    for i in range(CELL_NUMBER*CELL_NUMBER):
        x = i % CELL_NUMBER * SQ_SIZE
        y = i // CELL_NUMBER * SQ_SIZE
        square = pygame.Rect(x, y, SQ_SIZE, SQ_SIZE)
        pygame.draw.rect(WIN, BLACK, square, width=3)
    return

# draw zombie onto grids
def draw_zombies(zombie, display_result):
    x = zombie.col * SQ_SIZE + (PIXEL_OFFSET/2)
    y = zombie.row * SQ_SIZE + (PIXEL_OFFSET/2)
    rectangle = pygame.Rect(x, y, SQ_SIZE-PIXEL_OFFSET, SQ_SIZE-PIXEL_OFFSET)
    if display_result:
        pygame.draw.rect(WIN, GREEN, rectangle)
    else:
        pygame.draw.rect(WIN, GREY, rectangle)

# draw human onto grids
def draw_humans(human, display_result):
    x = human.col * SQ_SIZE + (PIXEL_OFFSET/2)
    y = human.row * SQ_SIZE + (PIXEL_OFFSET/2)
    rectangle = pygame.Rect(x, y, SQ_SIZE-PIXEL_OFFSET, SQ_SIZE-PIXEL_OFFSET)
    if display_result:
        pygame.draw.rect(WIN, YELLOW, rectangle)
    else:
        pygame.draw.rect(WIN, GREY, rectangle)

def draw_light_button(alreadyPressed):
    if alreadyPressed:
        text = font25.render('Light on!', True, WHITE)
        pygame.draw.rect(WIN, (255, 168, 54), button_light_on_off)
        WIN.blit(text, (620, 440))
    else:
        text = font25.render('Light off!', True, WHITE)
        pygame.draw.rect(WIN, (136, 128, 123), button_light_on_off)
        WIN.blit(text, (620, 440))

def number_players_window():
    run = True
    
    while run:

        # track user interaction
        for event in pygame.event.get():

            # user closes the pygame window
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:   # left mouse click
                    if button_one_player.collidepoint(event.pos):
                        print('1')
                        return 1
                    elif button_two_player.collidepoint(event.pos):
                        print('2')
                        return 2
                    elif button_three_player.collidepoint(event.pos):
                        print('3')
                        return 3
                    elif button_four_player.collidepoint(event.pos):
                        print('4')
                        return 4

            # draw window
            WIN.fill(GREY) 
            text = font40.render('How many players? ', True, WHITE)
            WIN.blit(text, (270, 100))

            # draw player options
            button_one_player = pygame.Rect(250, 250, 50, 50)
            text__one = font40.render('1', True, BLACK)
            pygame.draw.rect(WIN, WHITE, button_one_player)
            WIN.blit(text__one, (270, 250))

            button_two_player = pygame.Rect(350, 250, 50, 50)
            text__two = font40.render('2', True, BLACK)
            pygame.draw.rect(WIN, WHITE, button_two_player)
            WIN.blit(text__two, (370, 250))

            button_three_player = pygame.Rect(450, 250, 50, 50)
            text__three = font40.render('3', True, BLACK)
            pygame.draw.rect(WIN, WHITE, button_three_player)
            WIN.blit(text__three, (470, 250))

            button_four_player = pygame.Rect(550, 250, 50, 50)
            text__four = font40.render('4', True, BLACK)
            pygame.draw.rect(WIN, WHITE, button_four_player)
            WIN.blit(text__four, (570, 250))

            pygame.display.flip()
            pygame.display.update()  

    pygame.quit()

def select_flashlight_window(num_players):

    run = True
    players_flashlights = list()
    player_counter = 1
    while run:

        # track user interaction
        for event in pygame.event.get():

            # user closes the pygame window
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:   # left mouse click
                    if button_flashlight.collidepoint(event.pos):
                        players_flashlights.append('Large')
                        
                    elif button_flashlight_small.collidepoint(event.pos):
                        players_flashlights.append('Small')

                    player_counter = player_counter + 1
            # draw window
            WIN.fill(GREY) 
            text = font40.render('Select your flashlight ', True, WHITE)
            WIN.blit(text, (270, 100))

            # draw flashlights
            button_flashlight.x = 200
            button_flashlight.y = 200
            WIN.blit(flashlight, button_flashlight)

            button_flashlight_small.x = 380
            button_flashlight_small.y = 220
            WIN.blit(flashlight_small, button_flashlight_small)

            # print output
            for player in range(num_players):
                if player < len(players_flashlights):
                    selection = font25.render('Player ' + str(player+1) + ': ' + players_flashlights[player-1], True, WHITE)
                else:
                    selection = font25.render('Player ' + str(player+1) + ': ', True, WHITE)
                WIN.blit(selection, (550, 200 + player*50))

            pygame.display.flip()
            pygame.display.update()  

            if player_counter > num_players:
                return players_flashlights

    pygame.quit()
        
def main_game(flashlights):
    counter_rounds = 1
    run = True
    pausing = False
    light_off = True
    use_flashlight = list()
    place_fov = False
    make_fov_visible = False
    place_fov_small = False
    make_fov_visible_small = False
    loc_fov = []
    loc_fov_small = []
    num = 0
    registered_zombies = 0
    registered_humans = 0
    button_flashlights = list()
    use_flashlight = list()
    for i in range(len(flashlights)):
        use_flashlight.append(False)

    while run:
   
        # track user interaction
        for event in pygame.event.get():

            # user closes the pygame window
            if event.type == pygame.QUIT:
                run = False
                
            # draw background
            WIN.fill(GREY)   
        
            # draw grid
            draw_grid()

            draw_light_button(light_off)

            # draw flashlight
            for player in range(len(flashlights)):
                if player+1 < 3:
                    y_coord = 150
                else:
                    y_coord = 280
                if flashlights[player-1] == 'Large':
                    button = flashlight.get_rect()
                    button_flashlights.append(button)
                    button.x = 500 + (player%2) * 150
                    button.y = y_coord
                    WIN.blit(flashlight, button)
                elif flashlights[player-1] == 'Small':
                    button = flashlight_small.get_rect()
                    button_flashlights.append(button)
                    button.x = 500 + (player%2) * 150
                    button.y = y_coord
                    WIN.blit(flashlight_small, button)
                    
                # if player < len(players_flashlights):
                #     selection = font25.render('Player ' + str(player+1) + ': ' + players_flashlights[player-1], True, WHITE)
                # else:
                #     selection = font25.render('Player ' + str(player+1) + ': ', True, WHITE)
                # WIN.blit(selection, (550, 200 + player*50))

            pygame.display.flip()
            pygame.display.update()

    pygame.quit()

# execute game
def main():
    counter_rounds = 1
    pygame.mouse.set_cursor(default_cursor)

    # select number of players
    num_players = number_players_window()

    # select type of flashlight
    flashlights = list()
    flashlights = select_flashlight_window(num_players)

    # main game
    main_game(flashlights)


if __name__ == "__main__":
    main()                