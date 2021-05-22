# Santosh Khadka
# PyGame - Snake Game

import pygame
from pygame.locals import *
import time

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen 
        self.apple = pygame.image.load("resources/apple.png").convert()
        self.apple_x = 100
        self.apple_y = 100
    
    def draw(self): 
        self.surface.fill((91, 25, 84))  # without this the previous screen will stay - images on top of each other
        self.parent_screen.blit(self.apple, (self.apple_x, self.apple_y))
        pygame.display.flip()
    
    def move_up(self):
        self.apple_y += 20
        self.draw()
    def move_down(self):
        self.apple_y -= 20
        self.draw()
    def move_left(self):
        self.apple_x -= 20 
        self.draw()
    def move_right(self):
        self.apple_x += 20
        self.draw()

class Game:
    def __init__(self): # whats happening on inital load 
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500)) # size of the window: (Width,Height)
        self.surface.fill((255, 255, 255))    # background colors - rgb values 
        self.snake = Snake(self.surface)
        self.snake.draw()
    
    def run(self):
        running = True
        # Event loop - fundamental to any UI programming where it waits for changes to occur
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:    # when you want the programming to quit. Running until running is false
                    running = False

if __name__ == "__main__":
    game = Game()
    game.run()

    pygame.display.flip()   # loads display - otherwise black

    # 30:00

