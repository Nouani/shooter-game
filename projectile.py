import pygame as pg

class Projectile(pg.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 2
        self.image = pg.image.load('assets/projectile.png')
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 125
        self.rect.y = player.rect.y + 85