
# Import libraries
import pygame 

# Initialize pygame
pygame.init()

# game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ćastle Game')

# game loop
run = True
while run:



    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit


