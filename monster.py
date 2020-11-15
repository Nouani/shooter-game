import pygame as pg
import random

class Monster(pg.sprite.Sprite):
    def __init__(self, game):
        # inicializa as variaveis
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

    # registra dano no monstro
    def damage(self, amount):
        self.health -= amount # diminui a vida
        self.damageSound() # aciona o som
        if self.health <= 0: # se chegou a zero
            # reinicia o monstro
            self.rect.x = 1000 + random.randint(0, 500)
            self.velocity = random.randint(2, 4)
            self.health = self.maxHealth
            self.game.updateScore() # atualiza a pontuação do player

            if self.game.cometEvent.isFullLoaded(): # se comecou a "chuva" de bolas de fogo
                # remove os monstros
                self.game.allMonsters.remove(self)
                self.game.cometEvent.attemptFall()

    # redesenha a barra de vida em tela
    def updateHealthBar(self, surface):
        pg.draw.rect(surface, (60, 63, 60), [self.rect.x + 13, self.rect.y - 10, self.maxHealth, 5])
        pg.draw.rect(surface, (111, 210, 46), [self.rect.x + 13, self.rect.y - 10, self.health, 5])

    # realiza a escolha de ações do monstro
    def forward(self):
        if not self.game.checkCollision(self, self.game.allPlayers): # se não estã colidindo com player
            self.rect.x -= self.velocity # se movimenta
        else: # se não
            self.game.player.damage(self.attack) # ataca o player

    # efeito sonoro de dano do monstro
    def damageSound(self):
        sfx = pg.mixer.Sound("assets/sounds/damageEnemy.wav")  
        sfx.set_volume(0.07)                       
        sfx.play()