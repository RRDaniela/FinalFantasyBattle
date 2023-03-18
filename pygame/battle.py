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

#define game variables
current_fighter=1
total_fighters=3
action_cooldown = 0
action_wait_time = 90

#define fonts
font = pygame.font.SysFont('Times New Roman', 26)

#define colors
red = (255, 0, 0)
green = (0,255,0)

#Load images
#Background images
#TODO: Refactor to a dictionary
background_image = pygame.image.load('img/Background/background.png').convert_alpha()
#Panel image
panel_image = pygame.image.load('img/Icons/panel.png').convert_alpha()

#Create function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#TODO: Refactor to only 1 function for drawing
#Function for drawing background
def draw_bg():
    screen.blit(background_image, (0,0))

#Function for drawing panel
def draw_panel():
    #Draw panel rectangle
    screen.blit(panel_image, (0, screen_height - bottom_panel))
    #Show knight stats
    draw_text(f'{knight.name} HP: {knight.max_health}', font, red, 100, screen_height-bottom_panel + 10)
    for count, i in enumerate(bandit_list):
        draw_text(f'{i.name} HP: {i.max_health}', font, red, 550, (screen_height-bottom_panel + 10) + count*60)


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
        self.animation_list = []
        self.frame_index = 0
        #Control if it's idle or fighting {0:idle, 1:attack, 2:hurt, 3:dead}
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        #load images
        temp_list = []

        #Defining image for each Fighter whether it's a Knight or Enemy
        #Scaling image to be bigger
        for image in range(8):
            img = pygame.image.load(f'img/{self.name}/Idle/{image}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height()*3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    
    def draw(self):
        '''Function for drawing a Fighter'''
        screen.blit(self.image, self.rect)

    def animate(self):
        '''Animate the character based off the animation_list'''
        animation_cooldwon=100
        #Handle animation
        #Update image
        self.image = self.animation_list[self.action][self.frame_index]
        #Take the current time, substract when it was last update. if greater ? update : don't update
        if pygame.time.get_ticks() - self.update_time > animation_cooldwon:
                self.update_time = pygame.time.get_ticks()
                self.frame_index +=1
        #If the animation has run out then reset back to 0
        self.frame_index = 0 if self.frame_index >= len(self.animation_list[self.action]) else self.frame_index

class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y=y
        self.hp=hp
        self.max_hp=max_hp

    def draw(self, hp):
        #Update with new health
        self.hp = hp
        #Calculate health ratio
        ratio = self.hp /self.max_hp
        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, green, (self.x, self.y, 150*ratio, 20))


    

#Instance of the fighter class
knight = Fighter(200, 260, 'Knight', 30, 10, 3)
bandit_1 = Fighter(550, 270, 'Bandit', 20,10,3)
bandit_2 = Fighter(700, 270, 'Bandit', 20,10,3)

#Instance of the Health bar
knight_healthbar = HealthBar(100, screen_height-bottom_panel+40, knight.hp, knight.max_health)
bandit1_healthbar = HealthBar(550, screen_height-bottom_panel+40, bandit_1.hp, bandit_1.max_health)
bandit2_healthbar = HealthBar(550, screen_height-bottom_panel+100, bandit_2.hp, bandit_2.max_health)

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
    knight_healthbar.draw(knight.hp)
    bandit1_healthbar.draw(bandit_1.hp)
    bandit2_healthbar.draw(bandit_2.hp)
    #Update animation
    knight.animate()
    #Draw fighters
    knight.draw()

    #Draw bandits
    for bandit in bandit_list:
        bandit.animate()
        bandit.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
