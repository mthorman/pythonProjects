#Michael Thorman
#CSCI437/Fall 2021
#10/29/21
#The purpose of this assignment was to use a programming language of my choice to build a game engine. 
# The game engine should have included some sort of tool for managing the background and timing, support for sprites, 
# and motion, collision detection, and boundary detection.
import pygame, math, sys, random


class Sprite(pygame.sprite.Sprite):
    def __init__(self, scene, x, y):
        pygame.sprite.Sprite.__init__(self, self.groups)
    def update(self):
        pass
    def movement(self):
        pass
    def animate(self):
        pass
    def collide_enemy(self):
        pass
    def collide_blocks(self):
        pass

class Scene:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640,480))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font("Another Danger.otf", 32)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

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
        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        pass
    def createTileMap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "1":
                    Block(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == "P":
                    self.player = Player(self, j, i)
class Button:
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


