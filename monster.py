import pygame as pg

class Monster(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pg.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()