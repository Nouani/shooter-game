import pygame as pg

class Projectile(pg.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 1.6
        self.player = player
        self.image = pg.image.load('assets/projectile.png')
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 125
        self.rect.y = player.rect.y + 85
        self.origin_image = self.image
        self.angle = 0

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        if self.player.game.checkCollision(self, self.player.game.allMonsters):
            self.remove()

        if self.rect.x > 1280:
            self.remove()

    def remove(self):
        self.player.allProjectiles.remove(self)

    def rotate(self):
        self.angle += 6
        self.image = pg.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)