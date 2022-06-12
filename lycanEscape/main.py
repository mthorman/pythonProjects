import pygame, math, sys, gameEngine, random, pyautogui
from pygame import mixer
#Michael Thorman
#CSCI437/Fall 2021
#10/29/21
# The purpose of this assignment was to use a programming language of my choice to build a game engine.
# The game engine should have included some sort of tool for managing the background and timing, support for sprites, 
# and motion, collision detection, and boundary detection.
pygame.init()
mixer.music.load('nightofthewerewolf.mp3')
mixer.music.play(-1)
silver = 0
inventory = []
HP = 1000
wolfsbane = 0
silverbullet = 0
lycankilled = 0



class playerSprite(gameEngine.Sprite):
    def __init__(self, scene, x, y):
        self.scene = scene
        self._layer = 8
        self.groups = self.scene.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * 32
        self.y = y * 32
        self.width = 32
        self.height = 32




        image_to_load = pygame.image.load('pixelcharacter.png')
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey((0, 0, 0))
        self.image.blit(image_to_load, (0, 0))

        self.rect = self.image.get_rect()
        self.x_change = 0
        self.y_change = 0
        self.rect.x = self.x
        self.rect.y = self.y
        self.facing = 'down'
    def hit(self):
        print('hit')

    def update(self):
        self.movement()
        self.collide_enemy()
        self.collide_town()
        self.collide_silver()
        self.collide_potion()
        self.collide_wolfsbane()

        self.rect.x += self.x_change
        self.collide_blocks("x")
        self.rect.y += self.y_change
        self.collide_blocks("y")

        self.x_change = 0
        self.y_change = 0
    def collide_enemy(self):
        global silver
        global HP
        global wolfsbane
        global silverbullet
        global lycankilled
        hits = pygame.sprite.spritecollide(self, self.scene.enemies, False)
        if hits:
            HP -=5
            if HP <= 0:
                self.kill()
                silver = 0
                wolfsbane = 0
                silverbullet = 0
                HP = 1000
                pygame.display.set_caption(str(silver))
                pygame.display.set_caption(str(HP))
                pygame.display.set_caption(str(wolfsbane))
                pygame.display.set_caption(str(silverbullet))
                self.scene.game_over()
                self.scene.playing = False
            if wolfsbane >=3:
                HP+=100
                wolfsbane -=3
            if silverbullet >=1:
                hits = pygame.sprite.spritecollide(self,self.scene.enemies, True)
                lycankilled +=1
                silverbullet -=1

    def collide_town(self):
        hits = pygame.sprite.spritecollide(self, self.scene.town, False)
        if hits:
            self.kill()
            self.scene.win_screen()
            self.scene.playing = False
    def collide_silver(self):
        global silver
        global silverbullet
        hits = pygame.sprite.spritecollide(self, self.scene.silver, True)
        if hits:
             silver += 1
             pygame.display.set_caption(str(silver))
             if silver >=2:
                 silver -=2
                 silverbullet +=1
                 pygame.display.set_caption(str(silver))
                 pygame.display.set_caption(str(silverbullet))

    def collide_wolfsbane(self):
        global wolfsbane
        hits = pygame.sprite.spritecollide(self, self.scene.wolfsbane, True)
        if hits:
             wolfsbane += 1
             pygame.display.set_caption(str(wolfsbane))
    def collide_potion(self):
        global HP
        hits = pygame.sprite.spritecollide(self, self.scene.potion, True)
        if hits:
            HP +=250
            if HP >=1000:
                HP = 1000
            pygame.display.set_caption(str(HP))

    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.scene.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right


        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.scene.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

    def movement(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            # for sprite in self.scene.all_sprites:
            #     sprite.rect.x += 3
            self.x_change -= 3
            self.facing = 'left'

        if keys[pygame.K_RIGHT]:
            # for sprite in self.scene.all_sprites:
            #     sprite.rect.x -= 3
            self.x_change += 3
            self.facing = 'right'

        if keys[pygame.K_UP]:
            # for sprite in self.scene.all_sprites:
            #     sprite.rect.y += 3
            self.y_change -= 3
            self.facing = 'up'

        if keys[pygame.K_DOWN]:
            # for sprite in self.scene.all_sprites:
            #     sprite.rect.y -= 3
            self.y_change += 3
            self.facing = 'down'


class Game(gameEngine.Scene):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((540, 960))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font("Another Danger.otf", 65)
        self.font2 = pygame.font.SysFont("Another Danger.otf", 22)
        self.intro_background = pygame.image.load("creepyforest.jpg")
        self.intro_background2 = pygame.image.load("creepyforest2.png")
        self.go_background = pygame.image.load('gameover.jpg')
        self.go_background2=pygame.image.load("winscreen.jpg")




    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.town = pygame.sprite.LayeredUpdates()
        self.silver = pygame.sprite.LayeredUpdates()
        self.potion = pygame.sprite.LayeredUpdates()
        self.wolfsbane = pygame.sprite.LayeredUpdates()

        self.createTileMap()
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False




    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        self.clock.tick(60)
        text = self.font2.render('Silver: '+str(silver), 1, (255,255,255))
        self.screen.blit(text, (220, 935))
        text2 = self.font2.render('HP: '+str(HP),1,(255,255,255))
        self.screen.blit(text2,(10,935))
        text2 = self.font2.render('Wolfsbane: ' + str(wolfsbane), 1, (255, 255, 255))
        self.screen.blit(text2, (100, 935))
        text2 = self.font2.render('Silver Bullet: ' + str(silverbullet), 1, (255, 255, 255))
        self.screen.blit(text2, (300, 935))
        text2 = self.font2.render('Lycan Killed: ' + str(lycankilled), 1, (255, 255, 255))
        self.screen.blit(text2, (420, 935))
        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def game_over(self):
        text = self.font.render('You were killed!', True, (255, 255, 255))
        text_rect = text.get_rect(center=(540/2, 265/2))

        restart_button = Button(320, 165, 170, 50, (255, 255, 255), (0, 0, 0), "Play Again",32 )
        for sprite in self.all_sprites:
            sprite.kill()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()
            self.screen.blit(self.go_background, (0, 0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.clock.tick(60)
            pygame.display.update()
    def win_screen(self):
        text = self.font.render('You escaped!', True, (255, 255, 255))
        text_rect = text.get_rect(center=(540/2, 265/2))

        restart_button = Button(320, 165, 170, 50, (255, 255, 255), (0, 0, 0), "Play Again",32 )
        for sprite in self.all_sprites:
            sprite.kill()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()
            self.screen.blit(self.go_background2, (0, 0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.clock.tick(60)
            pygame.display.update()


    def intro_screen(self):
        intro = True
        title = self.font.render("Lycan Escape", True, (255, 255, 255))
        title_rect = title.get_rect(x=80, y=695)
        play_button = Button(280, 790, 170, 50, (255, 255, 255), (0, 0, 0), "Start Game",32 )
        story_button = Button(280, 845, 170, 50, (255, 255, 255), (0, 0, 0), "Story", 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if play_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()
                intro = False
            if story_button.is_pressed(mouse_pos, mouse_pressed):
                self.story_screen()
                intro = False
            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.screen.blit(story_button.image, story_button.rect)
            self.clock.tick(60)
            pygame.display.update()
    def story_screen(self):
        story = True
        intro_button =  Button(320, 165, 170, 50, (255, 255, 255), (0, 0, 0), "Main Menu",32 )
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    story = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if intro_button.is_pressed(mouse_pos, mouse_pressed):
                self.intro_screen()
            self.screen.blit(self.intro_background2, (0, 0))
            self.screen.blit(intro_button.image, intro_button.rect)
            self.clock.tick(60)
            pygame.display.update()

    def createTileMap(self):
        tilemap1 = [
            '11111111111111111',
            '1P011110000011111',
            '100W00000E0000S11',
            '11111110000100001',
            '1S0E0000011111111',
            '100W000011E0000S1',
            '1011100H1000000W1',
            '1001111110000E001',
            '1001S000001110001',
            '10011111000E00001',
            '11000001000110111',
            '111100E0000000111',
            '1111100100E000011',
            '10010W000010000H1',
            '10110001111000001',
            '100E0011111111001',
            '100110001100S0001',
            '1000100001S000111',
            '11000001010000011',
            '1111000000E000011',
            '10000H00E00101111',
            '1S11100W00010W001',
            '10000E0010W001101',
            '11100011100E00101',
            '100WT01000H000101',
            '100111101E0000001',
            '10110E00000000111',
            '100W00010011100S1',
            '11111111111111111',
        ]
        tilemap2 = [
            '11111111111111111',
            '100W0000E00000111',
            '1H011100001110011',
            '1111001111S010001',
            '1S00000000E001001',
            '101W00P0100001001',
            '110000011000100H1',
            '110000E1000100111',
            '111W0010000E00W11',
            '11110011110001001',
            '100S00000010000S1',
            '10E01111111111111',
            '100W1000000W00001',
            '10001011111111101',
            '1001S01000E000001',
            '10010010100011111',
            '10E01010101100011',
            '100010101011110W1',
            '11001000101T000W1',
            '100010101011110W1',
            '10E010101000W0001',
            '10001010000111101',
            '10S1101S0E0000001',
            '10111011111111111',
            '10001H00W000E0001',
            '10E01111110000101',
            '100000E00001110S1',
            '1H01100001000W011',
            '11111111111111111',
        ]
        tilemap3 = [
            '11111111111111111',
            '11110E0000E0000S1',
            '111W0000111000101',
            '11110001000W00001',
            '1100S001001100011',
            '10E0001000E000W01',
            '1011110W0000000H1',
            '1H000010000001111',
            '1111000000W000011',
            '110S0000100E00001',
            '1000E001100001111',
            '10000011110000001',
            '10011111111111001',
            '10000111TW00E00W1',
            '101000011111000H1',
            '10000E000001S0011',
            '100E00W000S111111',
            '10011111111111111',
            '100000E0000001111',
            '1001100000E000111',
            '101111100000W0001',
            '10001111010010001',
            '11100S01000010001',
            '11110000100E110S1',
            '11111000011111111',
            '1W0000E000001H011',
            '100E000111100W001',
            '1S0000011111W0P01',
            '11111111111111111',
        ]

        tileMapArray =[tilemap1, tilemap2, tilemap3]
        tilemap = random.choice(tileMapArray)
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "1":
                    Block(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == "P":
                    self.player = playerSprite(self, j, i)
                if column == "T":
                    Town(self, j, i)
                if column == "S":
                    Silver(self,j, i)
                if column == "H":
                    Potion(self, j, i)
                if column == "W":
                    Wolfsbane(self, j, i)

class Block(gameEngine.Sprite):
    def __init__(self, scene, x, y):
        self.scene = scene
        self._layer = 2
        self.groups = self.scene.all_sprites, self.scene.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*32
        self.y = y*32
        self.width = 32
        self.height = 32

        image_to_load = pygame.image.load('terrain.png')
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey((0,0,0))
        self.image.blit(image_to_load, (0,0))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
class Ground(gameEngine.Sprite):
    def __init__(self, scene, x, y):
        self.scene = scene
        self._layer = 1
        self.groups = self.scene.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x*32
        self.y = y*32
        self.width = 32
        self.height = 32

        image_to_load = pygame.image.load('ground.png')
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey((0,0,0))
        self.image.blit(image_to_load, (0,0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Enemy(gameEngine.Sprite):
    def __init__(self, scene, x, y):
            self.scene = scene
            self._layer = 3

            self.groups = self.scene.all_sprites, self.scene.enemies
            pygame.sprite.Sprite.__init__(self, self.groups)

            self.x = x*32
            self.y = y*32
            self.width = 32
            self.height = 32

            self.x_change = 0
            self.y_change = 0

            self.facing = random.choice(['left', 'right'])
            self.animation_loop = 1
            self.movement_loop = 0
            self.max_travel = random.randint(7,50)

            image_to_load = pygame.image.load('werewolf.png')
            self.image = pygame.Surface([self.width, self.height])
            self.image.set_colorkey((0, 0, 0))
            self.image.blit(image_to_load, (0, 0))

            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

    def update(self):
            self.movement()
            self.rect.x += self.x_change
            self.collide_blocks("x")
            self.rect.y += self.y_change
            self.collide_blocks("y")
            self.x_change = 0
            self.y_change = 0


    def movement(self):
             if self.facing == 'left':
                 self.direction = 1
                 self.x_change -= 3
                 self.movement_loop -= .4
                 if self.movement_loop <= -self.max_travel:
                     self.facing = 'right'

             if self.facing == 'right':
                 self.direction = 1
                 self.x_change += 3
                 self.movement_loop += .4
                 if self.movement_loop >= self.max_travel:
                     self.facing = 'left'


    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.scene.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.scene.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom


class Town(gameEngine.Sprite):
    def __init__(self, scene, x, y):
            self.scene = scene
            self._layer = 4

            self.groups = self.scene.all_sprites, self.scene.town
            pygame.sprite.Sprite.__init__(self, self.groups)

            self.x = x*32
            self.y = y*32
            self.width = 32
            self.height = 32

            self.x_change = 0
            self.y_change = 0

            self.facing = random.choice(['left', 'right'])
            self.animation_loop = 1
            self.movement_loop = 0
            self.max_travel = random.randint(7,30)

            image_to_load = pygame.image.load('village1.png')
            self.image = pygame.Surface([self.width, self.height])
            self.image.set_colorkey((0, 0, 0))
            self.image.blit(image_to_load, (0, 0))

            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

    def update(self):
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        self.x_change = 0
        self.y_change = 0

class Silver(gameEngine.Sprite):
    def __init__(self, scene, x, y):
            self.scene = scene
            self._layer = 5

            self.groups = self.scene.all_sprites, self.scene.silver
            pygame.sprite.Sprite.__init__(self, self.groups)

            self.x = x*32
            self.y = y*32
            self.width = 32
            self.height = 32

            self.x_change = 0
            self.y_change = 0

            self.facing = random.choice(['left', 'right'])
            self.animation_loop = 1
            self.movement_loop = 0

            image_to_load = pygame.image.load('silver.png')
            self.image = pygame.Surface([self.width, self.height])
            self.image.set_colorkey((0, 0, 0))
            self.image.blit(image_to_load, (0, 0))

            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

    def update(self):
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        self.x_change = 0
        self.y_change = 0
class Wolfsbane(gameEngine.Sprite):
    def __init__(self, scene, x, y):
            self.scene = scene
            self._layer = 7

            self.groups = self.scene.all_sprites, self.scene.wolfsbane
            pygame.sprite.Sprite.__init__(self, self.groups)

            self.x = x*32
            self.y = y*32
            self.width = 32
            self.height = 32

            self.x_change = 0
            self.y_change = 0

            self.facing = random.choice(['left', 'right'])
            self.animation_loop = 1
            self.movement_loop = 0

            image_to_load = pygame.image.load('wolfsbane.png')
            self.image = pygame.Surface([self.width, self.height])
            self.image.set_colorkey((0, 0, 0))
            self.image.blit(image_to_load, (0, 0))

            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

    def update(self):
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        self.x_change = 0
        self.y_change = 0

class Potion(gameEngine.Sprite):
    def __init__(self, scene, x, y):
            self.scene = scene
            self._layer = 6

            self.groups = self.scene.all_sprites, self.scene.potion
            pygame.sprite.Sprite.__init__(self, self.groups)

            self.x = x*32
            self.y = y*32
            self.width = 32
            self.height = 32

            self.x_change = 0
            self.y_change = 0

            self.facing = random.choice(['left', 'right'])
            self.animation_loop = 1
            self.movement_loop = 0

            image_to_load = pygame.image.load('potion.png')
            self.image = pygame.Surface([self.width, self.height])
            self.image.set_colorkey((0, 0, 0))
            self.image.blit(image_to_load, (0, 0))

            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

    def update(self):
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        self.x_change = 0
        self.y_change = 0

class Button(gameEngine.Button):
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font('Another Danger.otf', fontsize)
        self.content = content
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fg = fg
        self.bg = bg
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center =(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)
    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False



def main():
    game = Game()
    game.intro_screen()
    game.new()
    while game.running:
        game.main()
        game.game_over()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
