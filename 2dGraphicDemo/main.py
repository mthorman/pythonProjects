""" graphic.py
    Michael Thorman
    CSCI437
    9/27/21
    Build a basic image using 2D graphics primitives
    """

import pygame, sys
from pygame.locals import*

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('tile000.png'))
        self.sprites.append(pygame.image.load('tile001.png'))
        self.sprites.append(pygame.image.load('tile002.png'))
        self.sprites.append(pygame.image.load('tile003.png'))
        self.sprites.append(pygame.image.load('tile004.png'))
        self.sprites.append(pygame.image.load('tile005.png'))
        self.sprites.append(pygame.image.load('tile006.png'))
        self.sprites.append(pygame.image.load('tile007.png'))
        self.sprites.append(pygame.image.load('tile008.png'))
        self.sprites.append(pygame.image.load('tile009.png'))
        self.sprites.append(pygame.image.load('tile010.png'))
        self.sprites.append(pygame.image.load('tile011.png'))
        self.current_sprite=0
        self.image=self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = [pos_x, pos_y]
    def update(self):
        self.current_sprite +=0.2
        if self.current_sprite >=len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

#Import and initialize
pygame.init()


    #Display configuration
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Graphic.py")

    #Entities
    #background = pygame.Surface(screen.get_size())
    #background = background.convert()
    #background.fill((255, 255, 255))

tile_size=100

bg_img = pygame.image.load('forest full moon.jpg')
potion_img = pygame.image.load('potion.png')
gun_img = pygame.image.load('gun.png')
werewolf_img = pygame.image.load('werewolf.gif')
werewolf_img2 =pygame.image.load('werewolf.gif')
class World():
    def __init__(self, data):
        self.tile_list =[]
        rock_img = pygame.image.load('rock.png')
        row_count =0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(rock_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count*tile_size
                    img_rect.y = row_count*tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])



world_data = [
[0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0],
[1,1,1,0,0,0,0,0,0,0],
[0,0,0,0,1,1,0,0,0,0],
[0,0,0,0,0,0,0,1,0,1],
[1,0,1,1,0,0,1,0,0,0],
[0,0,0,0,0,1,1,0,0,0],
[0,0,0,0,1,0,1,1,1,0],
[1,0,0,1,0,0,0,0,0,0],
[1,1,1,1,0,1,1,1,1,1],
]

world = World(world_data)
myFont = pygame.font.SysFont("Georgia", 40)
label = myFont.render("Night       Train", 1, (255, 255,255))


    #Action
        #Assign values to key variables
clock=pygame.time.Clock()
keepGoing = True
        #Set up main loop

moving_sprites=pygame.sprite.Group()
player = Player(120,915)
moving_sprites.add(player)
while keepGoing:

        screen.blit(bg_img, (-150, 0))
        screen.blit(potion_img, (30, 455))
        screen.blit(gun_img, (500,850))
        screen.blit(werewolf_img, (390, 50))
        screen.blit(werewolf_img2, (700,450))
        screen.blit(label, (610, 230))

        moving_sprites.draw(screen)
        moving_sprites.update()

            #timer to set frame rate
        clock.tick(30)
        world.draw()
            #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 keepGoing = False
            #refresh display

            #screen.blit(background, (0, 0))
        pygame.display.update()
pygame.quit()
