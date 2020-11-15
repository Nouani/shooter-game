import pygame as pg
from comet import Comet
import random

class CometEvent:
    def __init__(self, game):
        self.percent = 0
        self.percentSpeed = 35
        self.fallMode = False
        self.game = game
        self.allComets = pg.sprite.Group()

    def addPercent(self):
        self.percent += self.percentSpeed / 100

    def isFullLoaded(self):
        return self.percent >= 100

    def resetPercent(self):
        self.percent = 0

    def meteorFall(self):
        for i in range(0, random.randint(10, 23)):
            self.allComets.add(Comet(self))

    def attemptFall(self):
        if self.isFullLoaded() and len(self.game.allMonsters) == 0:
            self.meteorFall()
            self.fallMode = True

    def updateBar(self, surface):
        pg.draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 10])
        pg.draw.rect(surface, (187, 11, 11), [0, surface.get_height() - 20, (surface.get_width() / 100) * self.percent, 10])