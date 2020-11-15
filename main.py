import pygame as pg
from game import Game

pg.init()

pg.display.set_caption("Shooter Game")
screen = pg.display.set_mode((1280, 720))

# load das imagens
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

helpBoard = pg.image.load('assets/helpBoard.png')
helpBoardRect = helpBoard.get_rect()
helpBoardRect.x = (screen.get_width() / 2) - (helpBoard.get_width() / 2)
helpBoardRect.y = (screen.get_height() / 2) - (helpBoard.get_height() / 2)

buttonClose = pg.image.load('assets/closeButton.png')
buttonCloseRect = buttonClose.get_rect()
buttonCloseRect.x = helpBoard.get_width() + 90
buttonCloseRect.y = (buttonClose.get_height() / 2) + 80

# mascara escura para o menu
mask = pg.Surface((1280,720))  
mask.set_alpha(128)            
mask.fill((0.2,0.2,0.2))

game = Game()

clock = pg.time.Clock()
running = True

while running:
    screen.blit(background, (0, -200)) # desenhando o background
        
    if game.isPlaying: # se jogo comecou
        game.update(screen) # atualiza o jogo
    else: # se não
        # desenha o menu
        screen.blit(mask, (0,0))
        screen.blit(banner, bannerRect)
        screen.blit(buttonPlay, buttonPlayRect)
        screen.blit(buttonHelp, buttonHelpRect)
        screen.blit(buttonQuit, buttonQuitRect)

    if game.needsHelp: # se clicou no botao help
        screen.blit(helpBoard, helpBoardRect)
        screen.blit(buttonClose, buttonCloseRect)

    pg.display.flip()

    clock.tick(60) 

    for event in pg.event.get(): # controle de eventos
        if event.type == pg.QUIT:
            running = False
            pg.quit()
        elif event.type == pg.KEYDOWN: # se pressionou qualquer tecla
            game.pressed[event.key] = True # seta no array pela key da tecla como true

            if event.key == pg.K_SPACE: # se apertou space
                game.tileSound() # ativa o som de projeteis
                game.player.launchProjectile() # movimenta o projetil
        elif event.type == pg.KEYUP: # se soltou qualquer tecla
            game.pressed[event.key] = False # seta no array pela key da tecla como false
        elif event.type == pg.MOUSEBUTTONDOWN and not game.isPlaying: # se pressionou qualquer botao do mouse e não esta no jogo
            # verifica se o ponto do click possui algum dos botões do menu
            if buttonPlayRect.collidepoint(event.pos): # se clicou no botao play
                game.clickSound()
                game.start() # inicia o jogo
            elif buttonHelpRect.collidepoint(event.pos): # se clicou no botao help
                game.clickSound()
                game.needsHelp = True # seta variavel para posterimente exibir os dados
            elif buttonQuitRect.collidepoint(event.pos): # se clicou no botao quit
                game.clickSound()
                running = False
                pg.quit() # fecha o jogo
            elif buttonCloseRect.collidepoint(event.pos): # se clicou no botao de fechar da tela de help
                game.clickSound()
                game.needsHelp = False # seta variavel para posteriomente não exibir mais os dados de help
