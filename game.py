import pygame as pg
from player import Player
from monster import Monster

class Game:
    def __init__(self):
        self.allPlayers = pg.sprite.Group()
        self.player = Player(self)
        self.allPlayers.add(self.player)
        self.allMonsters = pg.sprite.Group()
        self.pressed = {}
        self.spawnMonster()

    def checkCollision(self, sprite, group):
        return pg.sprite.spritecollide(sprite, group, False, pg.sprite.collide_mask)

    def spawnMonster(self):
        monster = Monster(self)
        self.allMonsters.add(monster)