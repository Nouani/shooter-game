import pygame as pg
from player import Player
from monster import Monster

class Game:
    def __init__(self):
        self.player = Player()
        self.allMonsters = pg.sprite.Group()
        self.pressed = {}
        self.spawnMonster()

    def spawnMonster(self):
        monster = Monster()
        self.allMonsters.add(monster)