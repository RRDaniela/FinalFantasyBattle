import pygame

pygame.init()

#Set frame rate to not use while(True) on the main loop
clock = pygame.time.Clock()
fps = 60

#Game window
bottom_panel = 150
screen_width=800
screen_height=400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')

#Load images
#Background images
#TODO: Refactor to a dictionary
background_image = pygame.image.load('img/Background/background.png').convert_alpha()
#Panel image
panel_image = pygame.image.load('img/Icons/panel.png').convert_alpha()

#TODO: Refactor to only 1 function for drawing
#Function for drawing background
def draw_bg():
    screen.blit(background_image, (0,0))

#Function for drawing panel
def draw_panel():
    screen.blit(panel_image, (0, screen_height - bottom_panel))

run = True
#Game loop
while run:
    #Fixed processing rate, while loop is running at 60fps
    clock.tick(fps)
    #Draw background
    draw_bg()
    draw_panel()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
