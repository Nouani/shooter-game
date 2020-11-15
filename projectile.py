import pygame as pg

class Projectile(pg.sprite.Sprite):
    def __init__(self, player):
        # inicializa as variaveis
        super().__init__()
        self.velocity = 6
        self.player = player
        self.image = pg.image.load('assets/projectile.png')
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 125
        self.rect.y = player.rect.y + 85
        self.origin_image = self.image
        self.angle = 0

    # movimenta o projetil
    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        for monster in self.player.game.checkCollision(self, self.player.game.allMonsters): # percorre uma lista de todos os monstros que estão colidindo com o projetil
            self.remove()  # remove o projetil
            monster.damage(self.player.attack) # aplica dano no monstro

        if self.rect.x > 1280: # se passar da tela
            self.remove() # remove

    # remove o projetil
    def remove(self):
        self.player.allProjectiles.remove(self)

    # animação de rotação do projetil
    def rotate(self):
        self.angle += 16
        self.image = pg.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)