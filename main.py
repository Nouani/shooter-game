import pygame as pg
from game import Game

pg.init()

pg.display.set_caption("Shooter Game")
screen = pg.display.set_mode((1280, 720))

background = pg.image.load('assets/bg.jpg')

game = Game()

running = True

while running:
    screen.blit(background, (0, -200))

    screen.blit(game.player.image, game.player.rect)

    if game.pressed.get(pg.K_RIGHT) and game.player.rect.x + game.player.rect.width - 35 < screen.get_width():
        game.player.moveRight()
    elif game.pressed.get(pg.K_LEFT) and game.player.rect.x + 35 > 0:
        game.player.moveLeft()

    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
        elif event.type == pg.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pg.KEYUP:
            game.pressed[event.key] = False