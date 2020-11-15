import pygame as pg
from game import Game

pg.init()

pg.display.set_caption("Shooter Game")
screen = pg.display.set_mode((1280, 720))

background = pg.image.load('assets/bg.jpg')

banner = pg.image.load('assets/banner.png')
banner = pg.transform.scale(banner, (700, 700))
bannerRect = banner.get_rect()
bannerRect.x = (screen.get_width() / 2) - (banner.get_width() / 2)
bannerRect.y = -60

buttonPlay = pg.image.load('assets/button.png')
buttonPlay = pg.transform.scale(buttonPlay, (300, 100))
buttonPlayRect = buttonPlay.get_rect()
buttonPlayRect.x = (screen.get_width() / 2) - (buttonPlay.get_width() / 2)
buttonPlayRect.y = bannerRect.y + banner.get_height() - buttonPlay.get_height() - 30

game = Game()

clock = pg.time.Clock()
running = True

while running:
    screen.blit(background, (0, -200))

    if game.isPlaying:
        game.update(screen)
    else:
        screen.blit(banner, bannerRect)
        screen.blit(buttonPlay, buttonPlayRect)

    pg.display.flip()

    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
        elif event.type == pg.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pg.K_SPACE and not game.isPause:
                game.player.launchProjectile()
            elif event.key == pg.K_ESCAPE and game.isPlaying:
                game.isPause = not game.isPause
        elif event.type == pg.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if buttonPlayRect.collidepoint(event.pos):
                game.start()
    
    