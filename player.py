import pygame as pg
from projectile import Projectile

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.allProjectiles = pg.sprite.Group()
        self.image = pg.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 500
    
    def moveRight(self):
        self.rect.x += self.velocity
    
    def moveLeft(self):
        self.rect.x -= self.velocity

    def launchProjectile(self):
        self.allProjectiles.add(Projectile(self))