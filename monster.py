import pygame as pg

class Monster(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.maxHealth = 100
        self.attack = 5
        self.image = pg.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540
        self.velocity = 1

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 1000
            self.health = self.maxHealth

    def updateHealthBar(self, surface):
        barColor = (111, 210, 46)
        backBarColor = (60, 63, 60)

        backBarPosition = [self.rect.x + 13, self.rect.y - 10, self.maxHealth, 5]
        barPosition = [self.rect.x + 13, self.rect.y - 10, self.health, 5]

        pg.draw.rect(surface, backBarColor, backBarPosition)
        pg.draw.rect(surface, barColor, barPosition)

    def forward(self):
        if not self.game.checkCollision(self, self.game.allPlayers):
            self.rect.x -= self.velocity