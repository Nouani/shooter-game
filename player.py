import pygame as pg
from projectile import Projectile

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.maxHealth = 100
        self.attack = 7
        self.velocity = 10
        self.allProjectiles = pg.sprite.Group()
        self.image = pg.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 500
    
    def moveRight(self):
        if not self.game.checkCollision(self, self.game.allMonsters):
            self.rect.x += self.velocity
    
    def moveLeft(self):
        self.rect.x -= self.velocity

    def launchProjectile(self):
        self.allProjectiles.add(Projectile(self))

    def updateHealthBar(self, surface):
        pg.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 10, self.maxHealth, 5])
        pg.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 10, self.health, 5])

    def updateHealth(self):
        if self.health + 10 > self.maxHealth:
            self.health = self.maxHealth
        else:
            self.health += 10

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
            self.damageSound()
        else:
            self.game.gameOver()
    
    def damageSound(self):
        sfx = pg.mixer.Sound("assets/sounds/damage.wav")  
        sfx.set_volume(0.07)                       
        sfx.play()