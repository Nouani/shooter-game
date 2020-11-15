import pygame as pg
import random

class Comet(pg.sprite.Sprite):
    def __init__(self, cometEvent):
        super().__init__()
        self.image = pg.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(2, 4)
        self.rect.x = random.randint(20, 1000)
        self.rect.y = random.randint(0, 80)
        self.cometEvent = cometEvent

    def remove(self):
        self.cometEvent.allComets.remove(self)

        if len(self.cometEvent.allComets) == 0:
            self.cometEvent.resetPercent()
            self.cometEvent.game.spawnMonster()
            self.cometEvent.game.spawnMonster()

    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y >= 500:
            self.remove()

            if len(self.cometEvent.allComets) == 0:
                self.cometEvent.resetPercent()
                self.cometEvent.fallMode = False
        
        if self.cometEvent.game.checkCollision(self, self.cometEvent.game.allPlayers):
            self.remove()
            self.cometEvent.game.player.damage(20)