import pygame as pg
import random

class Monster(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.maxHealth = 100
        self.attack = 1
        self.image = pg.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 500)
        self.rect.y = 540
        self.velocity = random.randint(1,4)

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 500)
            self.velocity = random.randint(2, 4)
            self.health = self.maxHealth

            if self.game.cometEvent.isFullLoaded():
                self.game.allMonsters.remove(self)
                self.game.cometEvent.attemptFall()

    def updateHealthBar(self, surface):
        pg.draw.rect(surface, (60, 63, 60), [self.rect.x + 13, self.rect.y - 10, self.maxHealth, 5])
        pg.draw.rect(surface, (111, 210, 46), [self.rect.x + 13, self.rect.y - 10, self.health, 5])

    def forward(self):
        if not self.game.checkCollision(self, self.game.allPlayers):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)