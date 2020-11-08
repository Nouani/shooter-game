import pygame as pg

class Monster(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pg.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540
        self.velocity = 0.8

    def forward(self):
        if not self.game.checkCollision(self, self.game.allPlayers):
            self.rect.x -= self.velocity