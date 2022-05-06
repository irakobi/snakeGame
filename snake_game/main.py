import pygame
from pygame.locals import *
import time


size = 17
class Snake:
    def __init__(self, surface, length):
        self.major_screen = surface
        self.length = length
        self.block = pygame.image.load("tools/body.png").convert()
        self.axis_x = [size]*length
        self.axis_y = [size]*length
        self.direction = 'right'


    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def draw(self):
        self.major_screen.fill((100, 110, 5))
        for i in range(self.length):
           self.major_screen.blit(self.block, (self.axis_x[i], self.axis_y[i]))
        pygame.display.flip()

    def walk(self):

        for i in range(self.length -1,0,-1):
            self.axis_x[i] = self.axis_x[i-1]
            self.axis_y[i] = self.axis_y[i-1]

        if self.direction == 'up':
            self.axis_y[0] -= size
        if self.direction == 'down':
            self.axis_y[0] += size
        if self.direction == 'left':
            self.axis_x[0] -= size
        if self.direction == 'right':
            self.axis_x[0] += size
        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.surface.fill((100, 110, 5))
        self.snake = Snake(self.surface, 3)
        self.snake.draw()

    def run(self):
        running = True

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

                elif event.type == QUIT:
                    running = False

            self.snake.walk()
            time.sleep(0.3)


if __name__ == "__main__":
    game = Game()
    game.run()








