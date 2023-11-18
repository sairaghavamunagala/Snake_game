import pygame
from enum import Enum
pygame.init()

class Direction(Enum):
    RIGHT=1
    LEFT=2
    UP=3
    DOWN=4

class SnakeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.display=pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Snake Game")
        self.clock=pygame.time.Clock()

    def playstep(self):
        pass


if __name__ == "__main__":
    game = SnakeGame()

    while True:
        game.playstep()

        pygame.quit()
