import pygame as pg

pg.init()

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pg.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 300

pg.display.set_caption("Shooter Game")
screen = pg.display.set_mode((1280, 720))

background = pg.image.load('assets/bg.jpg')

player = Player()

running = True

while running:
    screen.blit(background, (0, -200))

    screen.blit(player.image, player.rect)

    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()