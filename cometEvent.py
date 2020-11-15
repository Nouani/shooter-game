import pygame as pg
from comet import Comet
import random

class CometEvent:
    def __init__(self, game):
        # inicializa as variaveis
        self.percent = 0
        self.percentSpeed = 35
        self.fallMode = False
        self.game = game
        self.allComets = pg.sprite.Group()

    # aumenta a porcentagem da barra de loading
    def addPercent(self):
        self.percent += self.percentSpeed / 100

    # retorna se chegou no fim do loading
    def isFullLoaded(self):
        return self.percent >= 100

    # reseta a porcentagem da barra de loading
    def resetPercent(self):
        self.percent = 0

    # inicializa as bolas de fogo randomizando entre 10 a 23 bolas
    def meteorFall(self):
        for i in range(0, random.randint(10, 23)):
            self.allComets.add(Comet(self))

    # inicia a exibição das bolas de fogo
    def attemptFall(self):
        if self.isFullLoaded() and len(self.game.allMonsters) == 0:
            self.meteoriteSound()
            self.meteorFall()
            self.fallMode = True

    # atualiza a barra de loading em tela
    def updateBar(self, surface):
        pg.draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 10])
        pg.draw.rect(surface, (187, 11, 11), [0, surface.get_height() - 20, (surface.get_width() / 100) * self.percent, 10])

    # efeito sonoro ao iniciar a queda das bolas de fogo
    def meteoriteSound(self):
        sfx = pg.mixer.Sound("assets/sounds/meteorite.ogg")
        sfx.set_volume(0.07)                       
        sfx.play()