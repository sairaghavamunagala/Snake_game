import pygame

pygame.init()


class SnakeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def playstep(self):
        pass


if __name__ == "__main__":
    game = SnakeGame()

    while True:
        game.playstep()

        pygame.quit()
