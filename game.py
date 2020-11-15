import pygame as pg
from player import Player
from monster import Monster
from cometEvent import CometEvent

class Game:
    def __init__(self):
        self.isPlaying = False
        self.isPause = False
        self.allPlayers = pg.sprite.Group()
        self.player = Player(self)
        self.cometEvent = CometEvent(self)
        self.allPlayers.add(self.player)
        self.allMonsters = pg.sprite.Group()
        self.pressed = {}      

    def start(self):
        self.isPlaying = True
        self.spawnMonster()
        self.spawnMonster()

    def gameOver(self):
        self.player.allProjectiles = pg.sprite.Group()
        self.player.rect.x = 550
        self.player.rect.y = 500
        self.player.health = self.player.maxHealth

        self.player.allProjectiles = pg.sprite.Group()

        self.allMonsters = pg.sprite.Group()

        self.cometEvent.allComets = pg.sprite.Group()
        self.cometEvent.resetPercent()

        self.isPlaying = False

    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)

        self.player.updateHealthBar(screen)

        if not self.isPause:
            self.cometEvent.addPercent()
        self.cometEvent.updateBar(screen)

        if not self.isPause:
            for projectile in self.player.allProjectiles:
                projectile.move()

        for monster in self.allMonsters:
            if not self.isPause:
                monster.forward()
            monster.updateHealthBar(screen)

        for comet in self.cometEvent.allComets:
            if not self.isPause:
                comet.fall()

        self.player.allProjectiles.draw(screen)

        self.allMonsters.draw(screen)

        self.cometEvent.allComets.draw(screen)

        if not self.isPause:
            if self.pressed.get(pg.K_RIGHT) and self.player.rect.x + self.player.rect.width - 35 < screen.get_width():
                self.player.moveRight()
            elif self.pressed.get(pg.K_LEFT) and self.player.rect.x + 35 > 0:
                self.player.moveLeft()

    def checkCollision(self, sprite, group):
        return pg.sprite.spritecollide(sprite, group, False, pg.sprite.collide_mask)

    def spawnMonster(self):
        monster = Monster(self)
        self.allMonsters.add(monster)