import pygame as pg
from player import Player
from monster import Monster
from cometEvent import CometEvent

class Game:
    def __init__(self):
        # inicializa variaveis
        self.isPlaying = False
        self.needsHelp = False
        self.allPlayers = pg.sprite.Group()
        self.player = Player(self)
        self.cometEvent = CometEvent(self)
        self.allPlayers.add(self.player)
        self.allMonsters = pg.sprite.Group()
        self.pressed = {}
        self.score = 0
        self.font = pg.font.Font('assets/FreeSansBold.ttf', 32)

    # função para iniciar o game ja com dois monstros
    def start(self): 
        self.isPlaying = True
        self.spawnMonster()
        self.spawnMonster()

    # reinicializa as variaveis para caso o player queira jogar novamente
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

    # atualiza o game
    def update(self, screen):
        screen.blit(self.player.image, self.player.rect) # redesenha o player

        self.player.updateHealthBar(screen) # atualiza a barra de vida do player

        # atualizam o loading para começar a "chuva" de bolas de fogo
        self.cometEvent.addPercent()
        self.cometEvent.updateBar(screen)


        for projectile in self.player.allProjectiles: # atualiza todos os projeteis em tela
            projectile.move()

        for monster in self.allMonsters: # atualiza todos os monstros em tela
            monster.forward()
            monster.updateHealthBar(screen)

        for comet in self.cometEvent.allComets: # atualiza todas as bolas de fogo em tela
            comet.fall()

        self.player.allProjectiles.draw(screen) # redesenha todos os projeteis

        self.allMonsters.draw(screen) # redesenha todos os monstros

        self.cometEvent.allComets.draw(screen) # redesenha as bolas de fogo

        self.showScore(screen) # redesnha a pontuação

        # verifica se o player pressionou a seta para direta/esquerda e não está no limite da tela
        if self.pressed.get(pg.K_RIGHT) and self.player.rect.x + self.player.rect.width - 35 < screen.get_width():
            self.player.moveRight()
        elif self.pressed.get(pg.K_LEFT) and self.player.rect.x + 35 > 0:
            self.player.moveLeft()

    # verifica colisão entre duas entidades
    def checkCollision(self, sprite, group):
        return pg.sprite.spritecollide(sprite, group, False, pg.sprite.collide_mask)

    # exibi um novo monstro
    def spawnMonster(self):
        monster = Monster(self)
        self.allMonsters.add(monster)

    # efeito sonoro de click
    def clickSound(self):
        sfx = pg.mixer.Sound("assets/sounds/click.ogg")  
        sfx.set_volume(0.07)                       
        sfx.play()

    # efeito sonoro ao lançar o projetil
    def tileSound(self):
        sfx = pg.mixer.Sound("assets/sounds/tir.ogg")  
        sfx.set_volume(0.07)
        sfx.play()

    # aumenta a pontuação
    def updateScore(self):
        self.score += 5
        self.player.updateHealth()

    # diminui a pontuação
    def reduceScore(self):
        self.score -= 3

    # exibi a pontuação
    def showScore(self, screen):
        scoreScreen = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        screen.blit(scoreScreen, (1120, 20))