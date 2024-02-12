import pygame as pg
from random import randrange

vec2 = pg.math.Vector2


class Snake:
    def __init__(self, game):
        self.game = game
        self.size = game.TITLE_SIZE
        self.rect = pg.rect.Rect([0, 0, game.TITLE_SIZE - 2, game.TITLE_SIZE - 2])
        self.rect.center = self.get_random_position()
        self.direction = vec2(self.size, 0)
        self.step_delay = 100  # this is in milliseconds

    def get_random_position(self):
        return [randrange(self.size // 2, self.game.WINDOW_SIZE - self.size // 2, self.size)] * 2

    def move(self):
        self.rect.move_ip(self.direction)

    def update(self):
        self.move()

    def draw(self):
        pg.draw.rect(self.game.screen, 'green', self.rect)

class Food:
    def __init__(self, game):
        pass

    def draw(self):
        pass