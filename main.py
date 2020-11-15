import pygame as pg
from game import Game

pg.init()

pg.display.set_caption("Shooter Game")
screen = pg.display.set_mode((1280, 720))

background = pg.image.load('assets/bg.jpg')

banner = pg.image.load('assets/logo.png')
bannerRect = banner.get_rect()
bannerRect.x = (screen.get_width() / 2) - (banner.get_width() / 2)
bannerRect.y = 60

buttonPlay = pg.image.load('assets/buttonPlay.png')
buttonPlayRect = buttonPlay.get_rect()
buttonPlayRect.x = (screen.get_width() / 2) - (buttonPlay.get_width() / 2)
buttonPlayRect.y = bannerRect.y + banner.get_height()

buttonHelp = pg.image.load('assets/buttonHelp.png')
buttonHelpRect = buttonHelp.get_rect()
buttonHelpRect.x = (screen.get_width() / 2) - (buttonHelp.get_width() / 2)
buttonHelpRect.y = buttonPlayRect.y + buttonPlay.get_height() - 5

buttonQuit = pg.image.load('assets/buttonQuit.png')
buttonQuitRect = buttonQuit.get_rect()
buttonQuitRect.x = (screen.get_width() / 2) - (buttonQuit.get_width() / 2)
buttonQuitRect.y = buttonHelpRect.y + buttonHelp.get_height() - 5

helpBoard = pg.image.load('assets/teste.png')
helpBoardRect = helpBoard.get_rect()
helpBoardRect.x = (screen.get_width() / 2) - (helpBoard.get_width() / 2)
helpBoardRect.y = (screen.get_height() / 2) - (helpBoard.get_height() / 2)

buttonClose = pg.image.load('assets/closeButton.png')
buttonCloseRect = buttonClose.get_rect()
buttonCloseRect.x = helpBoard.get_width() + 90
buttonCloseRect.y = (buttonClose.get_height() / 2) + 80

mask = pg.Surface((1280,720))  
mask.set_alpha(128)            
mask.fill((0.2,0.2,0.2))

game = Game()

clock = pg.time.Clock()
running = True

while running:
    screen.blit(background, (0, -200))
        
    if game.isPlaying:
        game.update(screen)
    else:
        screen.blit(mask, (0,0))
        screen.blit(banner, bannerRect)
        screen.blit(buttonPlay, buttonPlayRect)
        screen.blit(buttonHelp, buttonHelpRect)
        screen.blit(buttonQuit, buttonQuitRect)

    if game.needsHelp:
        screen.blit(helpBoard, helpBoardRect)
        screen.blit(buttonClose, buttonCloseRect)

    pg.display.flip()

    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
        elif event.type == pg.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pg.K_SPACE:
                game.tileSound()
                game.player.launchProjectile()
        elif event.type == pg.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pg.MOUSEBUTTONDOWN and not game.isPlaying:
            if buttonPlayRect.collidepoint(event.pos):
                game.clickSound()
                game.start()
            elif buttonHelpRect.collidepoint(event.pos):
                game.clickSound()
                game.needsHelp = True
            elif buttonQuitRect.collidepoint(event.pos):
                game.clickSound()
                running = False
                pg.quit()
            elif buttonCloseRect.collidepoint(event.pos):
                game.clickSound()
                game.needsHelp = False
