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

#TODO: Move to a separate file (Fighter)
#Fighter class
class Fighter():
    '''Class fighter used for all characters (Knight/Bandit)'''
    def __init__(self, x, y, name, max_health, strength, potions):
        self.name = name
        self.max_health = max_health
        self.hp = max_health
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        #Defining image for each Fighter whether it's a Knight or Enemy
        #Scaling image to be bigger
        img = pygame.image.load(f'img/{self.name}/Idle/0.png')
        self.image = pygame.transform.scale(img, (img.get_width() * 3, img.get_height()*3))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    #Function for drawing a Fighter
    def draw(self):
        screen.blit(self.image, self.rect)

#Instance of the fighter class
knight = Fighter(200, 260, 'Knight', 30, 10, 3)
bandit_1 = Fighter(550, 270, 'Bandit', 20,10,3)
bandit_2 = Fighter(700, 270, 'Bandit', 20,10,3)

#Adding bandits to a list
bandit_list = []
bandit_list.append(bandit_1)
bandit_list.append(bandit_2)

run = True
#Game loop
while run:
    #Fixed processing rate, while loop is running at 60fps
    clock.tick(fps)
    #Draw background
    draw_bg()
    #Draw panel
    draw_panel()
    #Draw fighters
    knight.draw()

    #Draw bandits
    for bandit in bandit_list:
        bandit.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
