import pygame

WIDTH = 800
HEIGHT = 600
FPS = 60

BLUE = (60, 60, 120)
GREEN = (0, 255, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 80))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT
        self.canJump = True
        self.speedx = 0
        self.speedy = 0

    def update(self):
        Player.acceleratex(self)
        Player.acceleratey(self)

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.speedy = 0
            self.canJump = True
        if self.rect.top < 0:
            self.rect.top = 0

    def acceleratex(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx += -1
            if self.speedx < -10:
                self.speedx = -10
        if keystate[pygame.K_d]:
            self.speedx += 1
            if self.speedx > 10:
                self.speedx = 10
        if (not keystate[pygame.K_a] and not keystate[pygame.K_d]) or (keystate[pygame.K_a] and keystate[pygame.K_d]):
            self.speedx -= 2
            if self.speedx < 0:
                self.speedx = 0

    def acceleratey(self):
        keystate = pygame.key.get_pressed()
        if self.canJump:
            self.speedy = 0
        if keystate[pygame.K_SPACE] and self.canJump:
            self.speedy = -11
            self.canJump = False
        self.speedy += .4
        if self.speedy > 25:
            self.speedy = 25