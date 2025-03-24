import random


import pygame as pg
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Meteorite(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("output/meteorite.png")
        size = random.randint(70, 130)

        self.image = pg.transform.scale(self.image, (size, size))

        self.rect = self.image.get_rect()
        self.rect.topleft = (800, random.randint(0, 600 - size))

        self.speedx = random.randint(1, 3)
        self.speedy = random.randint(-1, 1)

    def update(self):
        self.rect.x -= self.speedx
        self.rect.y += self.speedy


class Mouse_starship(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("starships/Mouse_starship.png")
        size = random.randint(55, 150)

        self.image = pg.transform.scale(self.image, (size, size))
        self.image = pg.transform.flip(self.image, False, True)

        self.rect = self.image.get_rect()
        self.rect.midbottom = (random.randint(0, 600 - size), 0)

        self.speedx = random.randint(-1, +1)
        self.speedy = random.randint(1, 2)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy


class Laser(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("output/laser.png")

        self.image = pg.transform.scale(self.image, (30, 30))

        self.rect = self.image.get_rect(midbottom=pos)

        self.speed = 2

    def update(self):
        self.rect.y -= self.speed


class Starship(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("starships/cat_starship_horizontal.png")
        self.image = pg.transform.scale(self.image, (100, 100))
        self.image = pg.transform.flip(self.image, False, True)

        self.rect = self.image.get_rect()
        self.rect.midleft = (0, 300)

        self.mode = "vertical"

    def update(self):
        keys = pg.key.get_pressed()
        if self.mode == "horizontal":
            if self.rect.left > 0:
                if keys[pg.K_a]:
                    self.rect.x -= 2
            if self.rect.right < SCREEN_WIDTH:
                if keys[pg.K_d]:
                    self.rect.x += 2
            if self.rect.top > 0:
                if keys[pg.K_w]:
                    self.rect.y -= 2
            if self.rect.bottom < SCREEN_HEIGHT:
                if keys[pg.K_s]:
                    self.rect.y += 2

        if self.mode == "vertical":
            if self.rect.top > 0:
                if keys[pg.K_w]:
                    self.rect.y -= 2
            if self.rect.bottom < SCREEN_HEIGHT:
                if keys[pg.K_s]:
                    self.rect.y += 2
            if self.rect.right < SCREEN_WIDTH:
                if keys[pg.K_d]:
                    self.rect.x += 2
            if self.rect.left > 0:
                if keys[pg.K_a]:
                    self.rect.x -= 2

    def switch_mode(self):
        self.image = pg.image.load("starships/cat_starship.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.midbottom = (400, 580)

        self.mode = "horizontal"


class Captain(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("animals/captain.png")
        self.image = pg.transform.scale(self.image, (350, 350))

        self.rect = self.image.get_rect()
        self.rect.topleft = (-30, 600)

        self.mode = "up"

    def update(self):
        if self.mode == "up":
            self.rect.y -= 3
            if self.rect.y <= 300:
                self.mode = "stay"


class Alien(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("animals/alien_cat.png")
        self.image = pg.transform.scale(self.image, (400, 400))

        self.rect = self.image.get_rect()
        self.rect.topleft = (-30, 600)

        self.mode = "up"

    def update(self):
        if self.mode == "up":
            self.rect.y -= 3
            if self.rect.y <= 300:
                self.mode = "stay"
