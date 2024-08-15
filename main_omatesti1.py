
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




# Määritetään muuttuja, jota käytetään avuksi linnakkeen skaalaamisessa
new_width = 200

# Määritellaan variablet, jolla sailytetaan oikea kuvasuhde kun linnakuvaa skaalataan
aspect_ratio = castle_img_100.get_height() / castle_img_100.get_width()
new_height = int(new_width * aspect_ratio)

# Skaalaa kuva uuteen kokoon ja luodaan siita variable
castle_img_100_scaled = pygame.transform.scale(castle_img_100, (new_width, new_height))



# game loop
run = True
while run:

    clock.tick(FPS)

    screen.blit(bg, (0, 0))

    # Piirrä skaalattu kuva ruudulle (määritelty muuttujaksi ylla)
    screen.blit(castle_img_100_scaled, (0, 0))

    # Alla oleva linnakkeen piirto on oma kokeilu ilman videota
    # screen.blit(castle_img_100, (0, 0))


    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display window
    pygame.display.update()

pygame.quit


