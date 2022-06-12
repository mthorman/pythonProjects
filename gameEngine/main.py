import pygame, math, sys, gameEngine, random
from pygame import mixer
#Michael Thorman
#CSCI437/Fall 2021
#10/29/21
#The purpose of this assignment was to use a programming language of my choice to build a game engine. 
# The game engine should have included some sort of tool for managing the background and timing, support for sprites, 
# and motion, collision detection, and boundary detection.
pygame.init()
mixer.music.load('nightofthewerewolf.mp3')
mixer.music.play(-1)

class playerSprite(gameEngine.Sprite):
    def __init__(self, scene, x, y):
        self.scene = scene
        self._layer = 4
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



    def update(self):
        self.movement()
        self.collide_enemy()

        self.rect.x += self.x_change
        self.collide_blocks("x")
        self.rect.y += self.y_change
        self.collide_blocks("y")

        self.x_change = 0
        self.y_change = 0
    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.scene.enemies, False)
        if hits:
            self.kill()
            self.scene.playing = False
    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.scene.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.scene.all_sprites:
                        sprite.rect.x += 3
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.scene.all_sprites:
                        sprite.rect.x -= 3

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.scene.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.scene.all_sprites:
                        sprite.rect.y += 3
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.scene.all_sprites:
                        sprite.rect.y -= 3
    def movement(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            for sprite in self.scene.all_sprites:
                sprite.rect.x += 3
            self.x_change -= 3

        if keys[pygame.K_RIGHT]:
            for sprite in self.scene.all_sprites:
                sprite.rect.x -= 3
            self.x_change += 3

        if keys[pygame.K_UP]:
            for sprite in self.scene.all_sprites:
                sprite.rect.y += 3
            self.y_change -= 3

        if keys[pygame.K_DOWN]:
            for sprite in self.scene.all_sprites:
                sprite.rect.y -= 3
            self.y_change += 3
        if keys[pygame.K_SPACE]:
            self.scene.bullet.fire()


class Game(gameEngine.Scene):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640,480))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font("Another Danger.otf", 32)
        self.intro_background = pygame.image.load("creepyforest.jpg")
        self.go_background = pygame.image.load('gameover.jpg')


    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTileMap()
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.facing == 'up':
                        Attack(self, self.player.rect.x, self.player.rect.y - 32)
                    if self.player.facing == 'down':
                        Attack(self, self.player.rect.x, self.player.rect.y + 32)
                    if self.player.facing == 'left':
                        Attack(self, self.player.rect.x - 32, self.player.rect.y)
                    if self.player.facing == 'right':
                        Attack(self, self.player.rect.x + 32, self.player.rect.y)

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        self.clock.tick(60)
        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def game_over(self):
        text = self.font.render('Game Over', True, (255, 255, 255))
        text_rect = text.get_rect(center=(640 / 2, 480 / 2))
        restart_button = Button(10, 480 - 60, 120, 50, (255, 255, 255), (0, 0, 0), 'Restart', 32)
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

    def intro_screen(self):
        intro = True
        title = self.font.render("Lycan Escape", True, (255, 255, 255))
        title_rect = title.get_rect(x=10, y=10)
        play_button = Button(10, 50, 100, 50, (255, 255, 255), (0, 0, 0), "Play", 32)
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(60)
            pygame.display.update()
    def createTileMap(self):
        tilemap = [
            '11111111111111111111',
            '100E0000000000E00001',
            '10000111111111111111',
            '10000000000000000001',
            '11111111111111100001',
            '1000000000000E000001',
            '10001110000000000001',
            '100000000P0000000001',
            '10000000000001111001',
            '10000E00000000E00001',
            '10000011111111111111',
            '10000000000000000001',
            '11111111111111100001',
            '100000E0000000000001',
            '11111111111111111111',
        ]
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "1":
                    Block(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == "P":
                    self.player = playerSprite(self, j, i)
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
            self.max_travel = random.randint(7,30)

            image_to_load = pygame.image.load('werewolf.jpg')
            self.image = pygame.Surface([self.width, self.height])
            self.image.set_colorkey((0, 0, 0))
            self.image.blit(image_to_load, (0, 0))

            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

    def update(self):
            self.movement()

            self.rect.x += self.x_change
            self.rect.y += self.y_change
            self.x_change = 0
            self.y_change = 0

    def movement(self):
            if self.facing == 'left':
                self.x_change -= 2
                self.movement_loop -= 1
                if self.movement_loop <= -self.max_travel:
                    self.facing = 'right'
            if self.facing == 'right':
                self.x_change += 2
                self.movement_loop += 1
                if self.movement_loop >= self.max_travel:
                    self.facing = 'left'

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
