
# Import libraries
import pygame 

# Initialize pygame
pygame.init()

# game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
clock = pygame.time.Clock()
FPS = 60

# create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ćastle Game')

# load images - background
bg = pygame.image.load('img/bg.png').convert_alpha()
# load images - castle
castle_img_100 = pygame.image.load('img/castle/castle_100.png').convert_alpha()


# game loop
run = True
while run:

    clock.tick(FPS)

    screen.blit(bg, (0, 0))
    screen.blit(castle_img_100, (0, 0))


    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display window
    pygame.display.update()

pygame.quit


