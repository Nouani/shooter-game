import pygame as pg
import random

class Comet(pg.sprite.Sprite):
    def __init__(self, cometEvent):
        # inicialização das variaveis
        super().__init__()
        self.image = pg.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(2, 4)
        self.rect.x = random.randint(20, 1000)
        self.rect.y = random.randint(0, 80)
        self.cometEvent = cometEvent

    # remove uma bola de fogo
    def remove(self):
        self.cometEvent.allComets.remove(self)
        self.cometRemoveSound()

        if len(self.cometEvent.allComets) == 0: # se chegar a zero
            self.cometEvent.resetPercent() # reseta a barra de loading
            # coloca os monstros novamente
            self.cometEvent.game.spawnMonster()
            self.cometEvent.game.spawnMonster()

    # realiza o movimento da bola de fogo
    def fall(self):
        self.rect.y += self.velocity # movimenta

        if self.rect.y >= 500: # se chegou o passou do "chão"
            self.remove() # remove

            if len(self.cometEvent.allComets) == 0: # se todas as bolas de fogo foram removidas
                self.cometEvent.resetPercent() # reinicia o loading
                self.cometEvent.fallMode = False # desativa o modo de "chuvas" de bola de fogo
        
        if self.cometEvent.game.checkCollision(self, self.cometEvent.game.allPlayers): # se a bola de fogo colidiu com o player
            self.remove() # remove a bola
            self.cometEvent.game.player.damage(20) # diminui a vida
            self.cometEvent.game.reduceScore() # dimnui a pontuação

    # efeito sonoro das bolas de fogo
    def cometRemoveSound(self):
        sfx = pg.mixer.Sound("assets/sounds/fireExplode.wav")  
        sfx.set_volume(0.07)                       
        sfx.play()