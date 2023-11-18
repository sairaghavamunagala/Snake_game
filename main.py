import pygame
from enum import Enum
from collections import namedtuple
import random

pygame.init()


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


Point = namedtuple("Point", 'x, y')
BLOCK_SIZE = 20


class SnakeGame:
    def __init__(self, width=640, height=480):

        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        self.direction = Direction.RIGHT
        self.head = Point(self.width / 2, self.height / 2)
        self.snake = [
            self.head,
            Point(self.head.x - BLOCK_SIZE, self.head.y),
            Point(self.head.x - (2 * BLOCK_SIZE), self.head.y),
        ]

        self.score = 0
        self.food = None
        self._place_food()

    def _place_food(self):
        """
        This method is useful for putting the food in the game.
        """
        x = random.randint(0, (self.width - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.height - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

    def playstep(self):
        """
        This method handles gameover
        """
        gameover=False
        return gameover,self.score


if __name__ == "__main__":
    game = SnakeGame()

    while True:
        gameover,score=game.playstep()
        if gameover==True:
            break
        print("Final Score:",score)
        pygame.quit()
